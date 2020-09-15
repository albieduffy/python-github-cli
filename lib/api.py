import requests
from .repo import Repo

def fetch_repos(username):
    req = requests.get(f'https://api.github.com/users/{username}/repos')

    for data in req.json():
        Repo(data)
