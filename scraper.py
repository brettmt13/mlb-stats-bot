import requests
import urllib.parse
from bs4 import BeautifulSoup
import pandas as pd

'''
Returns the scraped search results

Params:
query_params: params for search query
top_k: top k players of result

Returns:
dataframe of top k player stats of query
'''
def get_data(query_params, top_k=5): 
    res = requests.get("https://baseballsavant.mlb.com/statcast_search", query_params)
    soup = BeautifulSoup(res.text, 'lxml')

    search_results_table = soup.find('table', id='search_results')

    columns = search_results_table.find_all('th')
    headers=[]

    col_ind = 0
    for col in columns:
        # indicate this is an image
        if col_ind == 1:
            headers.append("Player Image URL")
        else:
            headers.append(col.text.strip())
        col_ind+=1

    results = pd.DataFrame(columns = headers[:-1])
    
    rows = search_results_table.find_all('tr', {"data-group-by": "name"})
    for row in rows:
        row_items = row.find_all('td')
        player_img_url = row.find_all('img', {"class": "player-mug"})[0]['src']
        player_data = [item.text.strip() for item in row_items][:-1]
        player_data[1] = player_img_url
        results.loc[len(results)] = player_data

    return results.sort_values("BIP", 0, ascending=False)[0:top_k]