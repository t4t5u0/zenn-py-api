import json

import requests

from bs4 import BeautifulSoup

with open('./secrets.json') as f:
    load_json = json.load(f)
    AUTHOR = load_json['author']

ARTICLES = f"http://zenn.dev/{AUTHOR}"

BOOKS = ARTICLES + '?tab=books'


r_article = requests.get(ARTICLES)

soup = BeautifulSoup(r_article.text, 'lxml')
title_text = soup.find('title').get_text()
print(title_text)