import scraper
import query_strings

data = scraper.get_data(query_params=query_strings.PARAMS_STRIKES)
print(data)