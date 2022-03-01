# zenn-py-api

get article specify user

```sh
poerty install
poetry run start
```

```sh
curl -X 'GET' \
  'http://127.0.0.1:8000/v1/qiita/t4t5u0' \
  -H 'accept: application/json'
```

result

```json
[
  {
    "title": "[初心者向け] LaTeX文書をいい感じに運用する方法",
    "url": "https://zenn.dev/t4t5u0/t4t5u0/articles/latexoperation",
    "tags": [
      {
        "name": "GitHub Actions"
      },
      {
        "name": "textlint"
      },
      {
        "name": "Docker"
      },
      {
        "name": "LaTeX"
      },
      {
        "name": "初心者向け"
      }
    ],
    "likes_count ": 11,
    "created_at": "2021-12-28T22:14:03+00:00"
  },
  {
    "title": "Python3.10 時代のモダン Python",
    "url": "https://zenn.dev/t4t5u0/t4t5u0/articles/howtowritepython310",
    "tags": [
      {
        "name": "初心者"
      },
      {
        "name": "Python"
      }
    ],
    "likes_count ": 66,
    "created_at": "2021-12-08T02:32:45+00:00"
  },
  {
    "title": "GitHub Projects Beta (Table View) を用いたタスク管理",
    "url": "https://zenn.dev/t4t5u0/t4t5u0/articles/githubprojectsbeta",
    "tags": [
      {
        "name": "GitHub"
      }
    ],
    "likes_count ": 56,
    "created_at": "2021-11-01T03:35:56+00:00"
  }
]
```
