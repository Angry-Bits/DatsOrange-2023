import httpx

from src.settings import TEAM_TOKEN


# place-bid-controller

def remove_bid(bid_id: int):
    """
    Отменяет заявку.
    """
    url = "https://datsorange.devteam.games/RemoveBid"
    header = {"token": TEAM_TOKEN}
    payload = {"bidId": bid_id}

    r = httpx.post(url, headers=header, json=payload)
    return r.json()


def limit_price_sell(bid_id: int):
    """
    Размещает заявку на продажу по цене не менее установленной.
    """
    url = "https://datsorange.devteam.games/LimitPriceSell"
    header = {"token": TEAM_TOKEN}
    payload = {"bidId": bid_id}

    r = httpx.post(url, headers=header, json=payload)
    return r.json()


def place_buy_order(symbol_id: int, price: int, quantity: int):
    """
    Размещает заявку на покупку по цене не более установленной.
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


def best_price_sell(symbol_id: int, quantity: int):
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


def best_price_buy(symbol_id: int, quantity: int):
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


# stock-info

def sell_stock():
    """
    Заявки на продажу.
    """
    url = "https://datsorange.devteam.games/sellStock"
    header = {"token": TEAM_TOKEN}

    r = httpx.get(url, headers=header)
    return r.json()

def get_symbols():
    """
    Список всех активов.
    """
    url = "https://datsorange.devteam.games/getSymbols"
    header = {"token": TEAM_TOKEN}

    r = httpx.get(url, headers=header)
    return r.json()


def buy_stock():
    """
    Заявки на покупку.
    """
    url = "https://datsorange.devteam.games/buyStock"
    header = {"token": TEAM_TOKEN}

    r = httpx.get(url, headers=header)
    return r.json()


# news-controller

def latest_news():
    """
    Возвращает последнюю новость.
    """
    url = "https://datsorange.devteam.games/news/LatestNews"
    header = {"token": TEAM_TOKEN}

    r = httpx.get(url, headers=header)
    return r.json()


def latest_news_5_minutes():
    """
    Возвращает новости за последние 5 минут.
    """
    url = "https://datsorange.devteam.games/news/LatestNews5Minutes"
    header = {"token": TEAM_TOKEN}

    r = httpx.get(url, headers=header)
    return r.json()


def latest_news_1_minutes():
    """
    Возвращает новости за последнюю минуту.
    """
    url = "https://datsorange.devteam.games/news/LatestNews1Minute"
    header = {"token": TEAM_TOKEN}

    r = httpx.get(url, headers=header)
    return r.json()


# info-controller

def info():
    """
    Информация о счете.
    """
    url = "https://datsorange.devteam.games/info"
    header = {"token": TEAM_TOKEN}

    r = httpx.get(url, headers=header)
    return r.json()
