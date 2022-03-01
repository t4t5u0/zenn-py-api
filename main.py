import uvicorn
from fastapi import FastAPI


from zenn_py_api.getArticles import getArticles, Article


app = FastAPI()


@app.get("/v1/qiita/{user_id}")
async def get_articles(user_id: str) -> list[Article]:
    return getArticles(user_id)


def main():
    uvicorn.run("main:app", host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
