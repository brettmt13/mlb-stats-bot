import scraper
import query_strings

data, image_data = scraper.get_data(query_params=query_strings.PARAMS_SWING_AND_MISS)
print(image_data)