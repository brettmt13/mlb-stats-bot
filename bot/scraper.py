import requests
from bs4 import BeautifulSoup
import pandas as pd
import query_strings

'''
Returns the scraped search results

Params:
query_params: params for search query
top_k: top k players of result

Returns:
dataframe of top k player stats of query
'''
def get_data_image(query_params, top_k=5):
    print("in func")
    res = requests.get("https://baseballsavant.mlb.com/statcast_search", query_params)
    print("Request URL: ", res.url, "\nStatus: ", res.status_code)
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
        
    if query_params['player_type'] == 'pitcher' and query_params.get('min_pitches') == None: # pitcher columns behave differently
        results = results[results['Total'] != '']
        results['Total'] = results['Total'].astype(float)
        results = results.sort_values('Total', 0, ascending=False)[0:top_k]
        stat = results['Total'].values
    else:  
        results = results[results[results.columns[-1]] != '']
        results[results.columns[-1]] = results[results.columns[-1]].astype(float)
        results = results.sort_values(results.columns[-1], 0, ascending=False)[0:top_k]
        stat = results[results.columns[-1]].values
    image_data = results.loc[:,["Player", "Player Image URL"]]
    
    
    print("finished grabbing stat data...:\n")
    print(stat)
    
    return image_data, stat



'''
Returns the scraped search results

Params:
query_params: params for search query
top_k: top k players of result

Returns:
dataframe of top k player stats of query
'''
def get_data_string(query_params, top_k=5):
    res = requests.get("https://baseballsavant.mlb.com/statcast_search", query_params)
    print("Request URL: ", res.url, "\nStatus: ", res.status_code)
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
        
    if query_params['player_type'] == 'pitcher' and query_params.get('min_pitches') == None: # pitcher columns behave differently
        results = results[results['Total'] != '']
        results['Total'] = results['Total'].astype(float)
        results = results.sort_values('Total', 0, ascending=False)[0:top_k]
    else:  
        results = results[results[results.columns[-1]] != '']
        results[results.columns[-1]] = results[results.columns[-1]].astype(float)
        results = results.sort_values(results.columns[-1], 0, ascending=False)[0:top_k]
        
        if query_params['player_type'] == 'pitcher' and query_params.get('min_pitches') == None:
            tweet_string = results.to_string(columns=["Player", "Total"], index=False, header=False)
        else:  
            tweet_string = results.to_string(columns=["Player", results.columns[-1]], index=False, header=False)
    
    return tweet_string