from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time

# =========================
# CONFIG
# =========================
cities = [
    
    # Alabama
    "Birmingham, AL", "Montgomery, AL", "Mobile, AL",

    # Alaska
    "Anchorage, AK", "Fairbanks, AK",

    # Arizona
    "Phoenix, AZ", "Tucson, AZ", "Mesa, AZ",

    # Arkansas
    "Little Rock, AR", "Fayetteville, AR",

    # California
    "Los Angeles, CA", "San Diego, CA", "San Jose, CA", "San Francisco, CA",

    # Colorado
    "Denver, CO", "Colorado Springs, CO",

    # Connecticut
    "Bridgeport, CT", "New Haven, CT",

    # Delaware
    "Wilmington, DE", "Dover, DE",

    # Florida
    "Miami, FL", "Orlando, FL", "Tampa, FL", "Jacksonville, FL",

    # Georgia
    "Atlanta, GA", "Savannah, GA",

    # Hawaii
    "Honolulu, HI",

    # Idaho
    "Boise, ID",

    # Illinois
    "Chicago, IL", "Springfield, IL",

    # Indiana
    "Indianapolis, IN", "Fort Wayne, IN",

    # Iowa
    "Des Moines, IA",

    # Kansas
    "Wichita, KS", "Kansas City, KS",

    # Kentucky
    "Louisville, KY", "Lexington, KY",

    # Louisiana
    "New Orleans, LA", "Baton Rouge, LA",

    # Maine
    "Portland, ME",

    # Maryland
    "Baltimore, MD",

    # Massachusetts
    "Boston, MA",

    # Michigan
    "Detroit, MI", "Grand Rapids, MI",

    # Minnesota
    "Minneapolis, MN",

    # Mississippi
    "Jackson, MS",

    # Missouri
    "St. Louis, MO", "Kansas City, MO",

    # Montana
    "Billings, MT",

    # Nebraska
    "Omaha, NE",

    # Nevada
    "Las Vegas, NV", "Reno, NV",

    # New Hampshire
    "Manchester, NH",

    # New Jersey
    "Newark, NJ", "Jersey City, NJ",

    # New Mexico
    "Albuquerque, NM",

    # New York
    "New York, NY", "Buffalo, NY", "Rochester, NY",

    # North Carolina
    "Charlotte, NC", "Raleigh, NC",

    # North Dakota
    "Fargo, ND",

    # Ohio
    "Columbus, OH", "Cleveland, OH", "Cincinnati, OH",

    # Oklahoma
    "Oklahoma City, OK", "Tulsa, OK",

    # Oregon
    "Portland, OR",

    # Pennsylvania
    "Philadelphia, PA", "Pittsburgh, PA",

    # Rhode Island
    "Providence, RI",

    # South Carolina
    "Charleston, SC", "Columbia, SC",

    # South Dakota
    "Sioux Falls, SD",

    # Tennessee
    "Nashville, TN", "Memphis, TN",

    # Texas
    "Houston, TX", "Dallas, TX", "Austin, TX", "San Antonio, TX",

    # Utah
    "Salt Lake City, UT",

    # Vermont
    "Burlington, VT",

    # Virginia
    "Virginia Beach, VA", "Richmond, VA",

    # Washington
    "Seattle, WA", "Spokane, WA",

    # District of Columbia
    "Washington, DC",

    # West Virginia
    "Charleston, WV",

    # Wisconsin
    "Milwaukee, WI", "Madison, WI",

    # Wyoming
    "Cheyenne, WY"

]

BASE_URL = "https://www.mcdonalds.com/us/en-us/restaurant-locator.html"


def scrape_city(page, city):
    print(f"\n🔍 Scraping city: {city}")

    page.goto("https://www.mcdonalds.com/us/en-us/restaurant-locator.html", timeout=60000)

    # ✅ Use ID instead of placeholder
    search_box = page.locator("#form-text-1673594539")
    search_box.wait_for(state="visible", timeout=20000)

    # Clear + type
    search_box.fill("")
    search_box.type(city, delay=100)

    # Press Enter
    search_box.press("Enter")

    page.wait_for_timeout(5000)

    # OPTIONAL: Select 50 miles (if exists)
    try:
        radius_dropdown = page.locator("select")
        radius_dropdown.select_option("50")
        page.wait_for_timeout(3000)
    except:
        print("⚠️ Radius option not found")

    # =========================
    # LOAD ALL RESULTS
    # =========================
    while True:
        try:
            show_more = page.locator("#button-93a5672f17")
            if show_more.is_visible():
                show_more.click()
                print("➡️ Loading more...")
                page.wait_for_timeout(3000)
            else:
                print ("Show more is not working")
                break
        except:
            print("Show more not working")
            break

    # =========================
    # GET HTML
    # =========================
    html = page.content()
    soup = BeautifulSoup(html, "html.parser")

    links = []

    # Inspect website to adjust selector if needed
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "/us/en-us/location/" in href:
            full_link = "https://www.mcdonalds.com" + href
            links.append(full_link)

    # Remove duplicates
    links = list(set(links))

    print(f"✅ Found {len(links)} stores")
    return links


def main():
    all_links = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        for city in cities:
            links = scrape_city(page, city)
            all_links.extend(links)

        browser.close()

    # Remove duplicates globally
    all_links = list(set(all_links))

    print("\n======================")
    print(f"TOTAL STORES: {len(all_links)}")

    # Save to file
    with open("mcdonalds_links.txt", "w") as f:
        for link in all_links:
            f.write(link + "\n")

    print("📁 Saved to mcdonalds_links.txt")

if __name__ == "__main__":
    main()