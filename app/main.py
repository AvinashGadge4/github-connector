from fastapi import FastAPI
from app.github import get_repos, create_issue, list_issues

app = FastAPI()

@app.get("/")
def home():
    return {"message": "GitHub Connector Running "}


@app.get("/repos/{username}")
def fetch_repos(username: str):
    return get_repos(username)


@app.post("/create-issue/")
def create_issue_api(owner: str, repo: str, title: str, body: str):
    return create_issue(owner, repo, title, body)


@app.get("/list-issues/")
def list_issues_api(owner: str, repo: str):
    return list_issues(owner, repo)