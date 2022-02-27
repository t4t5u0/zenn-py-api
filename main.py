import json

import requests

from bs4 import BeautifulSoup


def main() -> dict:

    with open("./secrets.json") as f:
        load_json = json.load(f)
        AUTHOR = load_json["author"]

    ARTICLES = f"https://zenn.dev/{AUTHOR}"

    BOOKS = ARTICLES + "?tab=books"

    r_article = requests.get(ARTICLES)

    soup = BeautifulSoup(r_article.text, "lxml")
    title_text = soup.find("title").get_text()
    print(title_text)
    print("-" * len(title_text))

    article_card = soup.select("article.ArticleCard_container__3qUYt")

    return [
        {
            "title": article.select_one("h3.ArticleCard_title__UnBHE").get_text(),
            "url": ARTICLES
            + article.select_one("a.ArticleCard_mainLink__X2TOE").get("href"),
            "tags": [
                {"name": tag.get_text()}
                for tag in article.select("a.ArticleCard_topicLink__NfdwJ")
            ],
            "likes_count ": int(
                article.select_one("span.ArticleCard_like__lvRrs").get_text()
            ),
            "created_at": article.select_one("time").get("datetime"),
        }
        for article in article_card
    ]


if __name__ == "__main__":
    main()
