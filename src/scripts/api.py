import httpx
import json
from pathlib import Path

from ..settings import TEAM_TOKEN, BASE_DIR


PRINTS = Path(BASE_DIR).joinpath('prints')


def write(result, file: Path):
    with open(file):
        file.write_text(json.dumps(result, indent=4))


# place-bid-controller

def remove_bid(bid_id: int):
    """
    Отменяет заявку.
    """
    FILE = PRINTS.joinpath('remove_bid.txt')

    url = "https://datsorange.devteam.games/RemoveBid"
    header = {"token": TEAM_TOKEN}
    payload = {"bidId": bid_id}

    r = httpx.post(url, headers=header, json=payload)
    result = r.json()

    write(result, FILE)

    return result


def limit_price_sell(bid_id: int):
    """
    Размещает заявку на продажу по цене не менее установленной.
    """
    FILE = PRINTS.joinpath('limit_price_sell.txt')

    url = "https://datsorange.devteam.games/LimitPriceSell"
    header = {"token": TEAM_TOKEN}
    payload = {"bidId": bid_id}

    r = httpx.post(url, headers=header, json=payload)
    result = r.json()

    # write(result, FILE)

    return result


def place_buy_order(symbol_id: int, price: int, quantity: int):
    """
    Размещает заявку на покупку по цене не более установленной.
    """
    FILE = PRINTS.joinpath('place_buy_order.txt')

    url = "https://datsorange.devteam.games/LimitPriceBuy"
    header = {"token": TEAM_TOKEN}
    payload = {
        "symbolId": symbol_id,
        "price": price,
        "quantity": quantity
    }

    r = httpx.post(url, headers=header, json=payload)
    result = r.json()

    write(result, FILE)

    return result


def best_price_sell(symbol_id: int, quantity: int):
    """
    Разместить заявку на продажу актива по лучшей доступной цене.
    """
    FILE = PRINTS.joinpath('best_price_sell.txt')

    url = "https://datsorange.devteam.games/BestPriceSell"
    headers = {"token": TEAM_TOKEN}
    payload = {
        "symbolId": symbol_id,
        "quantity": quantity
    }

    r = httpx.post(url, headers=headers, json=payload)
    result = r.json()

    write(result, FILE)

    return result


def best_price_buy(symbol_id: int, quantity: int):
    """
    Разместить заявку на покупку актива по лучшей доступной цене.
    """
    FILE = PRINTS.joinpath('best_price_buy.txt')

    url = "https://datsorange.devteam.games/BestPriceBuy"
    headers = {"token": TEAM_TOKEN}
    payload = {
        "symbolId": symbol_id,
        "quantity": quantity
    }

    r = httpx.post(url, headers=headers, json=payload)
    result = r.json()

    # write(result, FILE)

    return result


# stock-info

def sell_stock():
    """
    Заявки на продажу.
    """
    FILE = PRINTS.joinpath('sell_stock.txt')

    url = "https://datsorange.devteam.games/sellStock"
    header = {"token": TEAM_TOKEN}

    r = httpx.get(url, headers=header)
    result = r.json()

    write(result, FILE)

    return result


def get_symbols():
    """
    Список всех активов.
    """
    FILE = PRINTS.joinpath('get_symbols.txt')

    url = "https://datsorange.devteam.games/getSymbols"
    header = {"token": TEAM_TOKEN}

    r = httpx.get(url, headers=header)
    result = r.json()

    write(result, FILE)

    return result


def buy_stock():
    """
    Заявки на покупку.
    """
    FILE = PRINTS.joinpath('buy_stock.txt')

    url = "https://datsorange.devteam.games/buyStock"
    header = {"token": TEAM_TOKEN}

    r = httpx.get(url, headers=header)
    result = r.json()

    write(result, FILE)

    return result


# news-controller

def latest_news():
    """
    Возвращает последнюю новость.
    """
    FILE = PRINTS.joinpath('latest_news.txt')

    url = "https://datsorange.devteam.games/news/LatestNews"
    header = {"token": TEAM_TOKEN}

    r = httpx.get(url, headers=header)
    result = r.json()

    write(result, FILE)

    return result


def latest_news_5_minutes():
    """
    Возвращает новости за последние 5 минут.
    """
    FILE = PRINTS.joinpath('latest_news_5_minutes.txt')

    url = "https://datsorange.devteam.games/news/LatestNews5Minutes"
    header = {"token": TEAM_TOKEN}

    r = httpx.get(url, headers=header)
    result = r.json()

    write(result, FILE)

    return result


def latest_news_1_minutes():
    """
    Возвращает новости за последнюю минуту.
    """
    FILE = PRINTS.joinpath('latest_news_1_minutes.txt')

    url = "https://datsorange.devteam.games/news/LatestNews1Minute"
    header = {"token": TEAM_TOKEN}

    r = httpx.get(url, headers=header)
    result = r.json()

    write(result, FILE)

    return result


# info-controller

def info():
    """
    Информация о счете.
    """
    FILE = PRINTS.joinpath('info.txt')

    url = "https://datsorange.devteam.games/info"
    header = {"token": TEAM_TOKEN}

    r = httpx.get(url, headers=header)
    result = r.json()

    write(result, FILE)

    return result


if __name__ == "__main__":
    info()
