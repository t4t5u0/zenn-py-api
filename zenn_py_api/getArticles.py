from bs4 import BeautifulSoup
from pydantic import BaseModel

import requests


class Article(BaseModel):
    title: str
    tags: list[dict[str, str]]
    url: str
    likes_count: int
    created_at: str


def getArticles(user_id: str) -> list:

    ARTICLES = f"https://zenn.dev/{user_id}"

    # TODO: ページネーションに対応する
    # TODO: Bookに対応する
    # BOOKS = ARTICLES + "?tab=books"

    r_article = requests.get(ARTICLES)
    soup = BeautifulSoup(r_article.text, "lxml")

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
