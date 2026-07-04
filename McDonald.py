from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
import gc
import json
from urllib.parse import urlparse
import os

# =========================
# CONFIG - US Cities (Reduced for testing)
# =========================
cities = [
     "New York, NY", "Los Angeles, CA" 
    
]

# Full list - uncomment when testing is complete
# cities = [
#     "Birmingham, AL", "Montgomery, AL", "Mobile, AL",
#     "Anchorage, AK", "Fairbanks, AK",
#     "Phoenix, AZ", "Tucson, AZ", "Mesa, AZ",
#     "Little Rock, AR", "Fayetteville, AR",
#     "Los Angeles, CA", "San Diego, CA", "San Jose, CA", "San Francisco, CA",
#     "Denver, CO", "Colorado Springs, CO",
#     "Bridgeport, CT", "New Haven, CT",
#     "Wilmington, DE", "Dover, DE",
#     "Miami, FL", "Orlando, FL", "Tampa, FL", "Jacksonville, FL",
#     "Atlanta, GA", "Savannah, GA",
#     "Honolulu, HI",
#     "Boise, ID",
#     "Chicago, IL", "Springfield, IL",
#     "Indianapolis, IN", "Fort Wayne, IN",
#     "Des Moines, IA",
#     "Wichita, KS", "Kansas City, KS",
#     "Louisville, KY", "Lexington, KY",
#     "New Orleans, LA", "Baton Rouge, LA",
#     "Portland, ME",
#     "Baltimore, MD",
#     "Boston, MA",
#     "Detroit, MI", "Grand Rapids, MI",
#     "Minneapolis, MN",
#     "Jackson, MS",
#     "St. Louis, MO", "Kansas City, MO",
#     "Billings, MT",
#     "Omaha, NE",
#     "Las Vegas, NV", "Reno, NV",
#     "Manchester, NH",
#     "Newark, NJ", "Jersey City, NJ",
#     "Albuquerque, NM",
#     "New York, NY", "Buffalo, NY", "Rochester, NY",
#     "Charlotte, NC", "Raleigh, NC",
#     "Fargo, ND",
#     "Columbus, OH", "Cleveland, OH", "Cincinnati, OH",
#     "Oklahoma City, OK", "Tulsa, OK",
#     "Portland, OR",
#     "Philadelphia, PA", "Pittsburgh, PA",
#     "Providence, RI",
#     "Charleston, SC", "Columbia, SC",
#     "Sioux Falls, SD",
#     "Nashville, TN", "Memphis, TN",
#     "Houston, TX", "Dallas, TX", "Austin, TX", "San Antonio, TX",
#     "Salt Lake City, UT",
#     "Burlington, VT",
#     "Virginia Beach, VA", "Richmond, VA",
#     "Seattle, WA", "Spokane, WA",
#     "Washington, DC",
#     "Charleston, WV",
#     "Milwaukee, WI", "Madison, WI",
#     "Cheyenne, WY"
# ]

BASE_URL = "https://www.mcdonalds.com/us/en-us/restaurant-locator.html"

def create_browser():
    """Create a browser instance with memory optimization"""
    p = sync_playwright().start()
    browser = p.chromium.launch(
        headless=False,
        args=[
            '--disable-dev-shm-usage',
            '--disable-gpu',
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-accelerated-2d-canvas',
            '--disable-accelerated-jpeg-decoding',
            '--disable-accelerated-mjpeg-decode',
            '--disable-accelerated-video-decode',
            '--disable-background-timer-throttling',
            '--disable-backgrounding-occluded-windows',
            '--disable-breakpad',
            '--disable-component-extensions-with-background-pages',
            '--disable-features=TranslateUI,BlinkGenPropertyTrees',
            '--disable-ipc-flooding-protection',
            '--disable-renderer-backgrounding',
            '--disable-extensions',
            '--disable-plugins',
            '--disable-images',  # Disable images to save memory
            '--disable-javascript',  # Actually, we need JS, so don't use this
            '--max_old_space_size=512',  # Limit memory
            '--memory-pressure-off'
        ]
    )
    page = browser.new_page()
    page.set_default_timeout(20000)
    
    # Block images and unnecessary resources
    page.route("**/*", lambda route: route.abort() if route.request.resource_type in ["image", "media", "font", "stylesheet"] else route.continue_())
    
    return p, browser, page

def close_browser(p, browser):
    """Safely close browser and cleanup"""
    try:
        browser.close()
    except:
        pass
    try:
        p.stop()
    except:
        pass
    gc.collect()
    time.sleep(1)

def scrape_city_links(city):
    """Scrape all store links for a single city with its own browser instance"""
    print(f"\n🔍 Scraping city: {city}")
    
    p = None
    browser = None
    page = None
    
    try:
        p, browser, page = create_browser()
        
        page.goto(BASE_URL, timeout=30000, wait_until='domcontentloaded')
        page.wait_for_timeout(2000)
        
        # Use ID for search box
        search_box = page.locator("#form-text-1673594539")
        search_box.wait_for(state="visible", timeout=10000)
        
        # Clear and type city
        search_box.fill("")
        search_box.type(city, delay=50)
        search_box.press("Enter")
        
        page.wait_for_timeout(3000)
        
        # Select 50 miles radius if available
        try:
            radius_dropdown = page.locator("select")
            if radius_dropdown.count() > 0:
                radius_dropdown.select_option("50")
                page.wait_for_timeout(2000)
        except:
            pass
        
        # Load all results with limit
        click_count = 0
        max_clicks = 15
        
        while click_count < max_clicks:
            try:
                show_more = page.locator("#button-93a5672f17")
                if show_more.is_visible():
                    show_more.click()
                    print(f"➡️ Loading more... (click {click_count + 1})")
                    page.wait_for_timeout(2000)
                    click_count += 1
                else:
                    break
            except:
                break
        
        # Get HTML and extract links
        html = page.content()
        soup = BeautifulSoup(html, "html.parser")
        
        links = []
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if "/us/en-us/location/" in href and href not in links:
                full_link = "https://www.mcdonalds.com" + href
                links.append(full_link)
        
        print(f"✅ Found {len(links)} stores for {city}")
        return links
        
    except Exception as e:
        print(f"❌ Error scraping {city}: {str(e)[:100]}")
        return []
    
    finally:
        if browser:
            close_browser(p, browser)

def extract_store_details(url):
    """Extract store details from a single URL with its own browser instance"""
    p = None
    browser = None
    page = None
    
    try:
        p, browser, page = create_browser()
        
        page.goto(url, timeout=15000, wait_until='domcontentloaded')
        page.wait_for_timeout(1000)
        
        soup = BeautifulSoup(page.content(), "html.parser")
        
        # Extract address
        address_tag = soup.find("h1", class_="cmp-restaurant-detail__details-meta-title")
        address = address_tag.text.strip() if address_tag else None
        
        # Extract location details (city, state, zip)
        text_tag = soup.find("span", class_="cmp-restaurant-detail__details-meta-address")
        
        city = None
        state = None
        zip_code = None
        
        if text_tag:
            text = text_tag.text
            parts = text.split(",")
            if len(parts) >= 2:
                city = parts[0].strip()
                parts_2 = parts[1].strip().split()
                if len(parts_2) >= 2:
                    state = parts_2[0]
                    zip_code = parts_2[1]
        
        # Extract phone
        phone_tag = soup.find("a", href=re.compile("tel:"))
        phone = phone_tag.text.strip() if phone_tag else None
        
        return {
            'address': address,
            'city': city,
            'state': state,
            'zip_code': zip_code,
            'phone': phone,
            'store_url': url
        }
        
    except Exception as e:
        print(f"   ❌ Error: {str(e)[:80]}")
        return None
    
    finally:
        if browser:
            close_browser(p, browser)

def load_progress(filename="progress.json"):
    """Load progress from file"""
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except:
            return {'processed_cities': [], 'processed_urls': [], 'store_details': []}
    return {'processed_cities': [], 'processed_urls': [], 'store_details': []}

def save_progress(progress, filename="progress.json"):
    """Save progress to file"""
    try:
        with open(filename, 'w') as f:
            json.dump(progress, f, indent=2)
    except:
        pass

def main():
    print("=" * 60)
    print("🍔 MCDONALD'S LOCATION SCRAPER (Memory Optimized)")
    print("=" * 60)
    
    # Load progress
    progress = load_progress()
    all_store_urls = []
    store_details = progress.get('store_details', [])
    processed_cities = set(progress.get('processed_cities', []))
    processed_urls = set(progress.get('processed_urls', []))
    
    # Phase 1: Get store URLs
    print(f"\n📋 Processing {len(cities)} cities")
    print(f"   Already processed: {len(processed_cities)} cities")
    
    # Filter out already processed cities
    cities_to_process = [c for c in cities if c not in processed_cities]
    
    if cities_to_process:
        print(f"   Remaining: {len(cities_to_process)} cities")
        
        # Process each city individually to avoid memory issues
        for idx, city in enumerate(cities_to_process, 1):
            print(f"\n{'='*50}")
            print(f"City {idx}/{len(cities_to_process)}")
            
            links = scrape_city_links(city)
            if links:
                all_store_urls.extend(links)
                progress['processed_cities'].append(city)
                # Save progress after each city
                save_progress(progress)
            
            # Force garbage collection
            gc.collect()
            time.sleep(1)
    
    # Remove duplicates and already processed URLs
    all_store_urls = list(set(all_store_urls) - processed_urls)
    print(f"\n📊 New unique stores found: {len(all_store_urls)}")
    
    if len(all_store_urls) == 0:
        print("❌ No new stores found. Exiting.")
        print(f"Total stores in database: {len(store_details)}")
        if store_details:
            save_to_csv(store_details)
        return
    
    # Phase 2: Extract store details
    print("\n" + "=" * 50)
    print("PHASE 2: Extracting store details")
    print("=" * 50)
    
    # Process each URL individually to avoid memory issues
    for idx, url in enumerate(all_store_urls, 1):
        print(f"\n📍 Store {idx}/{len(all_store_urls)}")
        
        details = extract_store_details(url)
        if details:
            store_details.append(details)
            progress['processed_urls'].append(url)
            progress['store_details'] = store_details
            print(f"   ✅ {details['city']}, {details['state']} - {details['address']}")
        else:
            print(f"   ⚠️ No details extracted")
        
        # Save progress every 5 stores
        if idx % 5 == 0:
            save_progress(progress)
            
        # Force garbage collection
        if idx % 10 == 0:
            gc.collect()
            time.sleep(1)
    
    # Final save
    save_progress(progress)
    save_to_csv(store_details)

def save_to_csv(store_details):
    """Save store details to CSV"""
    if not store_details:
        print("❌ No store details to save")
        return
    
    print("\n" + "=" * 50)
    print("Saving data to CSV")
    print("=" * 50)
    
    try:
        df = pd.DataFrame(store_details)
        # Reorder columns for better readability
        df = df[['address', 'city', 'state', 'zip_code', 'phone', 'store_url']]
        df.to_csv("mcdonalds_locations_final.csv", index=False)
        
        print(f"✅ FINAL: Saved {len(df)} stores to mcdonalds_locations_final.csv")
        print("\n📊 Data Preview:")
        print(df.head(10))
        print(f"\n📊 Data Summary:")
        print(f"   Total stores: {len(df)}")
        print(f"   Unique cities: {df['city'].nunique()}")
        print(f"   Unique states: {df['state'].nunique()}")
        
        # Clean up progress file after successful save
        if os.path.exists("progress.json"):
            os.remove("progress.json")
            print("   ✅ Progress file cleaned up")
            
    except Exception as e:
        print(f"❌ Error saving to CSV: {e}")
        # Save as backup using json
        try:
            with open("mcdonalds_backup.json", 'w') as f:
                json.dump(store_details, f, indent=2)
            print("   💾 Saved backup as JSON")
        except:
            pass

if __name__ == "__main__":
    # Disable OpenBLAS threading to avoid memory issues
    os.environ['OPENBLAS_NUM_THREADS'] = '1'
    os.environ['MKL_NUM_THREADS'] = '1'
    os.environ['NUMEXPR_NUM_THREADS'] = '1'
    os.environ['OMP_NUM_THREADS'] = '1'
    
    main()