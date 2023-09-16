# !usr/bin/env python3

from src.logger import logger

from src.settings import TEAM_TOKEN
from src.scripts.logic import main_cycle_logic


if __name__ == '__main__':
    main_cycle_logic()
