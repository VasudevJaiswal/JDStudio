import requests


def member(username):
    try:
        details = requests.get(
            f"https://raw.githubusercontent.com/jaidevstudio/LinkFree/main/public/data/{username}.json"
        ).json()
    except:
        details = {}
    if details == {}:
        orgs = requests.get(f"https://api.github.com/users/{username}/orgs").json()
        joined = False
        for org in orgs:
            if "Jaidevstudio" in org["login"]:
                joined = True
        if not joined:
            error = "User not join Jaidevstudio. Please join on https://github.com/jaidevstudio " \
            "if already joined change visibility to public."
        else:
            error = "User not found, Add data in https://github.com/jaidevstudio/Member.json"
        details = {
            "error": error
        }
    return details


def members():
    results = requests.get(
        "https://api.github.com/orgs/jaidevstudio/Member.json"
    ).json()
    return results
