import requests


def JDStudio():
    details = requests.get(
        "https://api.github.com/orgs/jaidevstudio"
    ).json()
    return details