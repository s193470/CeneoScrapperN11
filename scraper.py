import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.ceneo.pl/71299209#tab=reviews")


page_dom = BeautifulSoup(response.text, 'html.parser') 

#print(page_dom.prettify())

revievs = page_dom.select("div.js_product-review")
print(type(reviews))
review = reviews.pop(0)
print(type(review))
review = page_dom.select_one("div.js_product-review")
print(type(review))

review_id = review["data-entry-id"]
author = review.select_one("span.user-post__author-name")