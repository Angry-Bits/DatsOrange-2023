# !usr/bin/env python3

import requests

from src.logger import logger

from src.settings import TEAM_TOKEN
from src.scripts.api import *
#from src.scripts.api import *
from src.scripts.logic import main_cycle_logic

def main2(url: str = 'https://www.google.ru/') -> None:
    """Request checking script."""
    page = requests.get(url)
    logger.info(f'Выполнен запрос на {url}')
    team_token = TEAM_TOKEN if all((
        len(TEAM_TOKEN) == 26,
        TEAM_TOKEN.startswith('64ed'),
        TEAM_TOKEN.endswith('fccf')
    )) else ''
    if team_token:
        logger.info('Введен секретный токен.')
    else:
        logger.info(('Вы не ввели секретный токен! '
                    'Заполните его и повторите попытку.'))
    if page.status_code:
        logger.info('К хакатону готовы!')
    else:
        logger.info(('Ответ на запрос не получен. '
                    'Убедитесь в корректности адреcа запрашиваемого ресурса.'))



def main():
    # main_cycle_logic()
    print(buy_Stock())



if __name__ == '__main__':
    main()
