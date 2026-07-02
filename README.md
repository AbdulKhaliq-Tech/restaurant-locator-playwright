# 🍔 McDonald's Restaurant Locator Scraper

A Python-based web scraping project that automates the extraction of McDonald's restaurant location URLs across multiple cities in the United States using **Playwright** and **BeautifulSoup**.

---

## 📖 Overview

This project demonstrates how to automate interactions with a modern JavaScript-powered website using Playwright. It searches a list of US cities on the McDonald's Restaurant Locator, loads all available search results, extracts individual restaurant page URLs, removes duplicates, and saves the results into a text file.

The project is intended for **educational, research, and learning purposes** to showcase browser automation and web scraping techniques.

---

## ✨ Features

* 🚀 Browser automation using Playwright
* 🌎 Searches dozens of US cities automatically
* 🔍 Searches city by city without manual interaction
* 📄 Automatically loads additional results
* 🔗 Extracts restaurant location URLs
* 🧹 Removes duplicate links
* 💾 Saves all unique links into a text file
* 🧩 Clean and easy-to-understand Python code
* ⚡ Beginner-friendly project structure

---

## 🛠 Technologies Used

| Technology     | Purpose              |
| -------------- | -------------------- |
| Python 3       | Programming Language |
| Playwright     | Browser Automation   |
| BeautifulSoup4 | HTML Parsing         |
| lxml           | HTML Parser          |
| Git            | Version Control      |
| GitHub         | Source Code Hosting  |

---

## 📁 Project Structure

```text
mcdonalds-playwright-scraper/
│
├── scraper.py
├── requirements.txt
├── README.md
├── screenshots/
│   ├── banner.png
│   └── demo.png
└── sample_output.txt
```


## ▶ Usage

Run the scraper using:

```bash
python scraper.py
```

The script will:

1. Open Chromium
2. Search each configured city
3. Load all available restaurant results
4. Extract restaurant URLs
5. Remove duplicates
6. Save results into:

```text
mcdonalds_links.txt
```

---

## 📄 Example Output

```text
https://www.mcdonalds.com/us/en-us/location/ca/los-angeles/restaurant123.html

https://www.mcdonalds.com/us/en-us/location/tx/dallas/restaurant456.html

https://www.mcdonalds.com/us/en-us/location/fl/orlando/restaurant789.html
```

---

## 📊 Workflow

```text
Start
   │
   ▼
Launch Browser
   │
   ▼
Open Restaurant Locator
   │
   ▼
Search City
   │
   ▼
Load More Results
   │
   ▼
Extract URLs
   │
   ▼
Remove Duplicates
   │
   ▼
Save Links
   │
   ▼
Finish
```

---

## 📌 Requirements

* Python 3.10+
* Playwright
* BeautifulSoup4
* lxml

---

## 📦 requirements.txt

```text
playwright
beautifulsoup4
lxml
```

---

## 📷 Screenshots

### Search Process

<img width="1659" height="948" alt="demo" src="https://github.com/user-attachments/assets/7240059f-8062-411e-8939-eb36aa4a906c" />

```
screenshots/demo.png
```

---

## 🚀 Future Improvements

* Export results to CSV
* Export results to Excel
* Store results in SQLite/MySQL
* Multi-threaded scraping
* Retry mechanism
* Logging system
* Proxy support
* CAPTCHA handling
* Headless execution mode
* Command-line arguments
* Docker support
* GitHub Actions automation

---

## 🤝 Contributing

Contributions are welcome.

If you'd like to improve this project:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

## ⚠ Disclaimer

This repository is provided for educational and research purposes only.

Users are responsible for ensuring their use complies with the target website's Terms of Service, robots.txt policies where applicable, and all relevant laws and regulations.

This project is **not affiliated with, endorsed by, or sponsored by McDonald's Corporation**.

---

## 👨‍💻 Author

**Abdul Khaliq**

Python Developer | Data Science Enthusiast | Web Scraping | Automation | AI

GitHub: https://github.com/YourUsername

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork it

📢 Share it with others

---

## 📜 License

This project is licensed under the MIT License.
