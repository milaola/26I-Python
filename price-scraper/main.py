import requests 

from bs4 import BeautifulSoup

import pandas as pd

url ="https://books.toscrape.com/"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    
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

except requests.exceptions.RequestException as e:
    print("Website connection failed:", e)
    exit()







api_url ="https://open.er-api.com/v6/latest/GBP"

try:
    api_response = requests.get(api_url)
    api_response.raise_for_status()
    
    print("API status code:", api_response.status_code)
    
    exchange_data = api_response.json()
    
    exchange_rate = exchange_data["rates"]["KES"]
    
    print("GBP to KES exchange rate:", exchange_rate)
    
    print (type(products[0]["price_gbp"]))

except (ValueError, KeyError) as e:
    print("Currency API returned unexpected data:", e)
    exit()



for product in products:
    product["price_kes"] = round (
        product["price_gbp"] * exchange_rate, 2
    )


df = pd.DataFrame(products)

df.to_csv("book_prices_kes.csv", index=False)

print("Data successfully saved to CSV!")

print("\nBook price")
print(df.to_string(index=False))


                     
