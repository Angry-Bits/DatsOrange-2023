import httpx

from src.settings import TEAM_TOKEN
def get_sell_stock():
    """

    """
    url = "https://datsorange.devteam.games/sellStock"
    header = {"token": TEAM_TOKEN}

    r = httpx.get(url, headers=header)
    print(r.json())



def get_news():
    """
    Получить последние новости за 1 минуту
    """
    url = "https://datsorange.devteam.games/news/LatestNews1Minute"
    header = {"token": TEAM_TOKEN}

    r = httpx.get(url, headers=header)
    news = r.json()
    # print(r.json())
    return news
