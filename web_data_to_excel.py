import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titles = []
prices = []

for book in soup.select(".product_pod"):
    title = book.h3.a["title"]
    price = book.select_one(".price_color").text

    titles.append(title)
    prices.append(price)

data = pd.DataFrame({
    "Title": titles,
    "Price": prices
})

data.to_excel("books.xlsx", index=False)

print("Excel file created successfully!")
