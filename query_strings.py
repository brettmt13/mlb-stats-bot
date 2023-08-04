import urllib.parse
from datetime import date
from datetime import timedelta

today = date.today()

# yesterday
game_dt = str(today - timedelta(days = 1))

PARAMS_BBE = {'hfSea': urllib.parse.unquote('2023%7C'), 'hfGT': urllib.parse.unquote('R%7C'), 'chk_game_date_gt': 'on', 'chk_stats_bip': "on", 'game_date_gt': game_dt, 'game_date_lt': game_dt, 'sort_by': 'desc', 'player_type': 'batter'}
PARAMS_BBDIST = {'hfSea': urllib.parse.unquote('2023%7C'), 'hfGT': urllib.parse.unquote('R%7C'), 'chk_game_date_gt': 'on', 'chk_stats_bbdist': "on", 'game_date_gt': game_dt, 'game_date_lt': game_dt, 'sort_by': 'desc', 'player_type': 'batter'}
PARAMS_STRIKES = {'hfSea': urllib.parse.unquote('2023%7C'), 'hfGT': urllib.parse.unquote('R%7C'), 'chk_game_date_gt': 'on', 'chk_game_date_lt': 'on', 'chk_pitch_result': "on", 'game_date_gt': game_dt, 'game_date_lt': game_dt, 'sort_by': 'desc', 'player_type': 'pitcher', 'hfPR': urllib.parse.unquote('called%5C.%5C.strike%7Cswinging%5C.%5C.pitchout%7Cswinging%5C.%5C.strike%7Cswinging%5C.%5C.strike%5C.%5C.blocked%7C')}
PARAMS_OBP = {'hfSea': urllib.parse.unquote('2023%7C'), 'hfGT': urllib.parse.unquote('R%7C'), 'chk_game_date_gt': 'on', 'chk_stats_obp': "on", 'game_date_gt': game_dt, 'game_date_lt': game_dt, 'sort_by': 'desc', 'player_type': 'batter'}
PARAMS_SLG = {'hfSea': urllib.parse.unquote('2023%7C'), 'hfGT': urllib.parse.unquote('R%7C'), 'chk_game_date_gt': 'on', 'chk_stats_slg': "on", 'game_date_gt': game_dt, 'game_date_lt': game_dt, 'sort_by': 'desc', 'player_type': 'batter'}
PARAMS_EV = {'hfSea': urllib.parse.unquote('2023%7C'), 'hfGT': urllib.parse.unquote('R%7C'), 'chk_game_date_gt': 'on', 'chk_stats_launch_speed': "on", 'game_date_gt': game_dt, 'game_date_lt': game_dt, 'sort_by': 'desc', 'player_type': 'batter'}

# chk_stats_obp=on
query_strings = [PARAMS_BBE,
                 PARAMS_BBDIST,
                 PARAMS_STRIKES,
                 PARAMS_OBP,
                 PARAMS_SLG,
                 PARAMS_EV]