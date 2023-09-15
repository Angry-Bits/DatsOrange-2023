import time
from datetime import datetime as dt
from src.scripts.api import *
import json, os

# start_price = 100



def main_cycle_logic():
    with open("../../data/prices_company.json", "r", encoding="utf-8") as f:
        companies_prices = json.load(f)
    with open("../../data/last_time_update.txt", "r", encoding="utf-8") as f:
        last_time_news = dt.strptime(f.read(), "%Y-%m-%dT%H:%M:%SZ") # json.load(f)
    # last_time_news = # dt.strptime("2023-09-15T14:30:15Z", "%Y-%m-%dT%H:%M:%SZ")

    while 1:
        # print()
        # чекам новости
        news = get_news()
        if news:

            for _new in news:
                time_news = dt.strptime(_new["date"], "%Y-%m-%dT%H:%M:%SZ")
                if time_news > last_time_news:
                    print("НОВОСТЬ ПРИШЛА", news)
                    last_time_news = time_news
                    # теперь в этой новости берем компанию каждую и для неё меняем цены
                    for company in _new["companiesAffected"]:
                        company_price = companies_prices.get(company, 100)
                        # МЕНЯЕМ СУММУ НА ПРОЦЕНТ ИЗ НОВОСТИ
                        company_price = company_price*(1+_new["rate"]/100)
                        companies_prices[company] = company_price

                    # сохранить в json на всякий
                    # print(os.path.dirname(os.path.realpath(__file__)))
                    with open("../../data/prices_company.json", "w", encoding="utf-8") as f:
                        json.dump(companies_prices, f, ensure_ascii=False)
                    with open("../../data/last_time_update.txt", "w", encoding="utf-8") as f:
                        f.write(_new["date"])
                    print("ПОСЛЕ НОВОСТИ", companies_prices)

        time.sleep(1)


