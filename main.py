import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from zenn_py_api.getArticles import getArticles, Article


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)

@app.get("/v1/qiita/{user_id}")
async def get_articles(user_id: str) -> list[Article]:
    return getArticles(user_id)


def main():
    uvicorn.run("main:app", host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
