# -*- coding: utf-8 -*-

import requests
from flask import Flask

app = Flask(__name__)


# https://flask.palletsprojects.com/en/2.0.x/
@app.get("/api/statistics/repository/<owner>/<repository>")
def repository_statistics(owner, repository):
    # See: https://docs.github.com/en/rest/reference/repos#get-a-repository
    repo = requests.get("https://api.github.com/repos/" + owner + "/" + repository).json()
    contributors = requests.get(
        "https://api.github.com/repos/" + owner + "/" + repository + "/contributors?per_page=10").json()
    issues = requests.get(
        "https://api.github.com/repos/" + owner + "/" + repository + "/issues?sort=comments&per_page=10").json()

    # Adapt contributors data
    top_10_contributors = []
    for contrib in contributors:
        top_10_contributors.append(
            {'contributions': contrib['contributions'], "login": contrib['login']})

    # Adapt issues data
    top_10_issues = []
    for issue in issues:
        top_10_issues.append(
            {"comments": issue['comments'], "title": issue['title']})

    return {
        'owner': owner,
        'repository': repository,
        'forks': repo['forks_count'],
        'stars': repo['stargazers_count'],
        'watchings': repo['subscribers_count'],
        'statistics': {
            "contributors": {
                "top10": top_10_contributors,
            }
        },
        'issues': {
            "totalOpen": repo['open_issues_count'],
            "top 10 of  issues": [top_10_issues]
        }
    }
