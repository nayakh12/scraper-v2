# 🛒 Ecommerce Product Scraper (Python Web Scraping Project)

## 📌 Overview
This project is a Python web scraper that extracts product data from an ecommerce website, including laptops and computers.  
It collects structured product information and saves it in a usable format for analysis or research.

---

## ⚙️ Features
- Scrapes product category (e.g., laptops, computers)
- Extracts product title/name
- Extracts price information
- Extracts product description
- Handles multiple product listings
- Stores data in CSV format

---

## 🧠 Technologies Used
- Python
- Requests
- BeautifulSoup
- Pandas (for data storage)

---

## 🚀 How It Works
1. Sends a request to the ecommerce website
2. Parses HTML content using BeautifulSoup
3. Locates product containers
4. Extracts:
   - Category
   - Title
   - Price
   - Description
5. Saves cleaned data into a CSV file

---

## 📂 Output Example

| Category | Title | Price | Description |
|----------|------|-------|-------------|
| Laptop | Dell Inspiron 15 | $650 | 15-inch laptop, 8GB RAM |
| Computer | HP Desktop | $500 | Intel i5, 8GB RAM |

---

## ▶️ How to Run
```bash
python scraper.py
