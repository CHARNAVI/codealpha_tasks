import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://books.toscrape.com/"
response = requests.get(url)
if response.status_code == 200:
    print("Website accessed successfully!")
else:
    print("Failed to access website")
soup = BeautifulSoup(response.text, "lxml")
books = soup.find_all("article", class_="product_pod")
book_data = []
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    book_data.append({
        "Book Title": title,
        "Price": price
    })
df = pd.DataFrame(book_data)
print("\nCollected Data:\n")
print(df)
df.to_csv("books_dataset.csv", index=False)
print("\nDataset saved as books_dataset.csv")