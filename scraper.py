import requests
from bs4 import BeautifulSoup
import json 


def extract_element(dom_tree, selector,attribute=None,return_list=None):
    try:
        if isinstance (attribute, str): 
            return dom_tree.select_one(selector)[attribute].text.strip()
        if isinstance (attribute, list):
            return [e.text.strip() for e in dom_tree.select(selector)]
        return dom_tree.select_one(selector).text.strip()
    except AttributeError:
        return None

all_reviews = []
service_url = "https://www.ceneo.pl"
next_page = "/71299209#tab=reviews"

while next_page:

    response = requests.get(service_url,next_page)
    page_dom = BeautifulSoup(response.text, 'html.parser')
    reviews = page_dom.select("div.js_product-review")
    for review in reviews:
        single_review = {
            "review_id": review["data-entry-id"],
            "author" : extract_element(review, "span.user-post__author-name"),
            "recommendation" : extract_element(review,"span.user-post__author-recomendation"),
            "stars" : extract_element(review,"span.user-post__score-count"),
            "content" : extract_element(review,"div.user-post__text"),
            "pros" : extract_element(review,"div.review-feature__title--positives ~ div.review-feature__item",[]),
            "cons" : extract_element(review,"div.review-feature__title--negatives ~ div.review-feature__item",[]),
            "useful" : extract_element(review,"button.vote-yes"),
            "useless" : extract_element(review,"button.vote-no"),
            "purchased" : extract_element(review,"div.review-pz"),
            "review_date" : extract_element(review,"span.user-post__published > time:nth-child(1)","datetime"),
            "purchase_date" : extract_element(review,"span.user-post__published > time:nth-child(1)","datetime"),
        }
        all_reviews.append(single_review)
    next_page = extract_element(page_dom,"a.pagination_next", "href")

with open("opinions/71299209.json","w",encoding="UTF-8") as jf:
    json.dump(all_reviews, jf, ensure_ascii=False, indent=4)

#print(json.dumps(single_review, ensure_ascii=False, indent=4))




