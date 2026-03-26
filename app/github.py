import requests
from app.config import GITHUB_TOKEN, GITHUB_API_URL

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}


def get_repos(username):
    url = f"{GITHUB_API_URL}/users/{username}/repos"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": response.json()}

    return response.json()



def create_issue(owner, repo, title, body):
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/issues"

    data = {
        "title": title,
        "body": body
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code != 201:
        return {"error": response.json()}

    return response.json()


def list_issues(owner, repo):
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/issues"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": response.json()}

    return response.json()