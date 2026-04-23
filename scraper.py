import requests, pandas as pd
from bs4 import BeautifulSoup

categories = [
    "computers/laptops",
    "computers/tablets"
]

base_url = "https://webscraper.io/test-sites/e-commerce/static/"

data=[]

for category in categories:
    url = base_url + category
    print(url)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.find_all("div", class_="caption")

    for item in items:
        title = item.find("a", class_="title").text.strip()
        price = item.find("h4", class_="price").text.strip()
        description = item.find("p", class_="description").text.strip()

    data.append([category, title, price, description])

df = pd.DataFrame(data, columns=["Category", "Title", "Price", "Description"])

df.to_csv("products.csv", index=False)