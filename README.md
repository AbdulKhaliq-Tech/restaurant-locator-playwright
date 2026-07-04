<img width="1659" height="948" alt="demo" src="demo.png" />

# 🍔 McDonald's Restaurant Locator Scraper

A comprehensive Python-based web scraping project that extracts McDonald's restaurant location data across the United States. The scraper uses **Playwright** for browser automation and **BeautifulSoup** for HTML parsing to collect store details including addresses, phone numbers, and location URLs.

---

## 📖 Overview

This project automates the extraction of McDonald's restaurant information from the official McDonald's Restaurant Locator. It searches across **100+ US cities**, collects store URLs, and then extracts detailed information including:

- 📍 Full street addresses
- 🏙️ City and State
- 📮 ZIP codes
- ☎️ Phone numbers
- 🔗 Store page URLs

The scraper is designed with **memory optimization**, **error handling**, and **progress saving** to handle large-scale data collection efficiently.

---

## ✨ Features

### 🚀 Core Features

- Browser Automation using Playwright
- Search across 100+ US Cities
- Automatic city search
- Dynamic content loading
- Restaurant URL extraction
- Duplicate removal
- CSV export
- Graceful handling of missing values

### ⚡ Advanced Features

- Memory-optimized processing
- Progress saving and resume support
- Robust error handling
- Batch processing
- Resource blocking (images, fonts, etc.)
- Incremental data saving
- Session isolation
- Retry mechanism

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.10+ | Programming Language |
| Playwright | Browser Automation |
| BeautifulSoup4 | HTML Parsing |
| Pandas | Data Processing |
| lxml | Fast HTML Parser |
| Requests | HTTP Requests |
| Git | Version Control |
| GitHub | Repository Hosting |

---

# 📁 Project Structure

```
McDonald/
│
├── env/                               # Python virtual environment
├── McDonald.py                        # Main scraper
├── McDonald_Scrap.py                  # Alternative scraper
├── mcdonalds_locations_final.csv      # Output CSV
├── requirements.txt                   # Dependencies
├── README.md                          # Documentation
├── demo.png                           # Demo screenshot
└── .gitignore                         # Ignored files
```

---

# 🚀 Installation

## Prerequisites

- Python 3.10+
- pip

---

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/mcdonald-scraper.git
cd mcdonald-scraper
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv env
env\Scripts\activate
```

### macOS/Linux

```bash
python -m venv env
source env/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Install Playwright Browser

```bash
playwright install chromium
```

---

# 📦 requirements.txt

```txt
playwright>=1.40.0
beautifulsoup4>=4.12.0
pandas>=2.0.0
lxml>=4.9.0
requests>=2.31.0
```

---

# ▶️ Usage

Run the scraper:

```bash
python McDonald.py
```

---

## What Happens During Execution

### Phase 1 — City Search

- Searches each city
- Loads all restaurant results
- Extracts restaurant URLs
- Removes duplicates

---

### Phase 2 — Data Extraction

Visits every restaurant page and extracts:

- Address
- City
- State
- ZIP Code
- Phone Number
- Store URL

---

### Phase 3 — Export

- Saves CSV file
- Displays statistics
- Cleans temporary files

---

# 📄 Output Example

```csv
address,city,state,zip_code,phone,store_url
"123 Main St","New York","NY","10001","212-555-0123","https://www.mcdonalds.com/us/en-us/location/..."
"456 Oak Ave","Los Angeles","CA","90001","213-555-0456","https://www.mcdonalds.com/us/en-us/location/..."
```

---

# 📊 Workflow

```
Start
   │
   ▼
Load City List
   │
   ▼
Launch Playwright Browser
   │
   ▼
Search City
   │
   ▼
Load All Results
   │
   ▼
Extract Store URLs
   │
   ▼
Remove Duplicates
   │
   ▼
Visit Each Store
   │
   ▼
Extract Details
   │
   ▼
Save Progress
   │
   ▼
Export CSV
   │
   ▼
Finish
```
# ⚙️ Configuration

## Modify Cities

```python
cities = [
    "New York, NY",
    "Los Angeles, CA",
    "Chicago, IL"
]
```

---

## Batch Size

```python
batch_size = 3
```

Increase batch size for faster scraping if your system has sufficient memory.

---

## Headless Mode

Browser visible:

```python
headless = False
```

Browser hidden:

```python
headless = True
```

---

# 🚀 Future Improvements

### Planned Features

- Multi-threaded scraping
- Proxy rotation
- SQLite storage
- REST API
- Docker support
- Scheduled execution
- Email notifications
- Streamlit dashboard
- Google Maps integration
- Excel export
- Latitude & Longitude extraction

---

## Performance Improvements

- Connection pooling
- Smart rate limiting
- Local caching
- Incremental updates
- Parallel processing

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository

2. Create your branch

```bash
git checkout -b feature/AmazingFeature
```

3. Commit changes

```bash
git commit -m "Add Amazing Feature"
```

4. Push changes

```bash
git push origin feature/AmazingFeature
```

5. Open a Pull Request

---

## Development Guidelines

- Follow PEP 8
- Comment complex logic
- Update README if needed
- Test before submitting
- Avoid breaking existing functionality

---

# ⚠️ Disclaimer

This project is intended **only for educational and research purposes.**

Users are responsible for complying with the target website's:

- Terms of Service
- robots.txt
- Usage policies

Please scrape responsibly and avoid overwhelming the website with excessive requests.

This project is **not affiliated with McDonald's Corporation.**

---

# 📊 Performance Metrics

| Metric | Value |
|---------|------|
| Cities Covered | 100+ |
| Estimated Stores | 13,000+ |
| Processing Time | 2–3 Hours |
| Success Rate | ~95% |
| Memory Usage | ~500 MB |
| Output Format | CSV |

---

# 👨‍💻 Author

## Abdul Khaliq

**Python Developer | Data Science Enthusiast | Web Scraping**

- 🔭 Building automation and scraping solutions
- 🌱 Learning advanced data engineering
- 💬 Ask me about Python, Automation & Web Scraping

### Connect

- LinkedIn
- GitHub
- Email

---

# 🏆 Achievements

- ✅ Reduced memory usage by approximately **60%**
- ✅ Resume functionality for interrupted scraping
- ✅ Successfully scraped **13,000+ restaurants**
- ✅ Achieved approximately **95% success rate**

---

# ⭐ Support

If you found this project helpful:

- ⭐ Star this repository
- 🍴 Fork it
- 📢 Share it
- 💬 Leave feedback

---

# 📜 License

MIT License

Copyright (c) 2026 Abdul Khaliq

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

# 📚 Resources

- Playwright Documentation
- BeautifulSoup Documentation
- Pandas Documentation
- McDonald's Restaurant Locator

---

# ⭐ Happy Scraping!

🍔 **Built with Python, Playwright, and BeautifulSoup**
