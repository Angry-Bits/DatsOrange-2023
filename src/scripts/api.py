import httpx

from src.settings import TEAM_TOKEN

def get_sell_stock():
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
    news = r.json()
    # print(r.json())
    return news

# info-controller

def info():
    url = "https://datsorange.devteam.games/info"
    header = {"token": TEAM_TOKEN}

    r = httpx.get(url, headers=header)

def cancel_bid(bid_id: int):
    """
    Отменить заявку по заданному ID
    """
    url = "https://datsorange.devteam.games/RemoveBid"
    header = {"token": TEAM_TOKEN}
    payload = {"bidId": bid_id}

    r = httpx.post(url, headers=header, json=payload)
    return r.json()


def place_buy_order(symbol_id: int, price: int, quantity: int):
    """
    Размещает заявку на покупку по цене не более установленной
    """
    url = "https://datsorange.devteam.games/LimitPriceBuy"
    header = {"token": TEAM_TOKEN}
    payload = {
        "symbolId": symbol_id,
        "price": price,
        "quantity": quantity
    }

    r = httpx.post(url, headers=header, json=payload)
    return r.json()


def sell_at_best_price(symbol_id: int, quantity: int):
    """
    Разместить заявку на продажу актива по лучшей доступной цене.
    """
    url = "https://datsorange.devteam.games/BestPriceSell"
    headers = {"token": TEAM_TOKEN}
    payload = {
        "symbolId": symbol_id,
        "quantity": quantity
    }

    r = httpx.post(url, headers=headers, json=payload)
    return r.json()


def buy_at_best_price(symbol_id: int, quantity: int):
    """
    Разместить заявку на покупку актива по лучшей доступной цене.
    """
    url = "https://datsorange.devteam.games/BestPriceBuy"
    headers = {"token": TEAM_TOKEN}
    payload = {
        "symbolId": symbol_id,
        "quantity": quantity
    }

    r = httpx.post(url, headers=headers, json=payload)
    return r.json()
