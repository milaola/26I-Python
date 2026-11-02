import requests 

from bs4 import BeautifulSoup

import pandas as pd

url ="https://books.toscrape.com/"

response= requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

print("Number of books found:" , len(books))

products = []

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").get_text(strip=True)

    clean_price = float(price.replace("£", "") .replace("Â", ""))

    products.append({
        "title":title,
        "price_gbp": clean_price
    })

print(products)

print("Status code:", response.status_code)
print("Website response:",response.reason)
print (type(products[0]["price_gbp"]))




                     
