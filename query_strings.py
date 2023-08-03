import urllib.parse
from datetime import date

game_dt = str(date.today())
game_dt = '2023-07-31'

PARAMS_BBE = {'hfSea': urllib.parse.unquote('2023%7C'), 'hfGT': urllib.parse.unquote('R%7C'), 'chk_game_date_gt': 'on', 'chk_stats_bip': "on", 'game_date_gt': game_dt, 'game_date_lt': game_dt, 'sort_by': 'desc'}
PARAMS_BBDIST = {'hfSea': urllib.parse.unquote('2023%7C'), 'hfGT': urllib.parse.unquote('R%7C'), 'chk_game_date_gt': 'on', 'chk_stats_bbdist': "on", 'game_date_gt': game_dt, 'game_date_lt': game_dt, 'sort_by': 'desc'}

query_strings = [PARAMS_BBE,
                 PARAMS_BBDIST]