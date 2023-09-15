import httpx

from src.settings import TEAM_TOKEN


# stock-info

def sell_stock():
    url = "https://datsorange.devteam.games/sellStock"
    header = {"token": TEAM_TOKEN}

    r = httpx.get(url, headers=header)
    return r.json()


def get_symbols():
    url = "https://datsorange.devteam.games/getSymbols"
    header = {"token": TEAM_TOKEN}

    r = httpx.get(url, headers=header)
    return r.json()


def buy_Stock():
    url = "https://datsorange.devteam.games/buyStock"
    header = {"token": TEAM_TOKEN}

    r = httpx.get(url, headers=header)
    return r.json()


# news-controller

def latest_news():
    url = "https://datsorange.devteam.games/news/LatestNews"
    header = {"token": TEAM_TOKEN}

    r = httpx.get(url, headers=header)
    return r.json()


def latest_news_5_minutes():
    url = "https://datsorange.devteam.games/news/LatestNews5Minutes"
    header = {"token": TEAM_TOKEN}

    r = httpx.get(url, headers=header)
    return r.json()


def latest_news_1_minutes():
    url = "https://datsorange.devteam.games/news/LatestNews1Minute"
    header = {"token": TEAM_TOKEN}

    r = httpx.get(url, headers=header)
    return r.json()


# info-controller

def info():
    url = "https://datsorange.devteam.games/info"
    header = {"token": TEAM_TOKEN}

    r = httpx.get(url, headers=header)
    return r.json()
