import tweepy
import tweet_strings
import query_strings
import scraper
import random
import yaml
import os
# import image_gen

def pick_three():
    random.shuffle(all_inds)
    choice_inds = all_inds[:3]
    return choice_inds

with open('../config.yml', 'r') as config_file:
    config = yaml.safe_load(config_file)

consumer_key = config['twitter']['consumer_key']
consumer_secret = config['twitter']['consumer_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']
bearer_token = config['twitter']['bearer_token']

# authorize app to bot
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# for media (future release)
api_v1 = tweepy.API(auth)
# media_upload = api_v1.media_upload(filename="./image.jpg")

# for text
api_v2 = tweepy.Client(bearer_token=bearer_token,
                    access_token=access_token,
                    access_token_secret=access_token_secret,
                    consumer_key=consumer_key,
                    consumer_secret=consumer_secret)

query_strings_ = query_strings.query_strings
tweet_strings_ = tweet_strings.tweet_strings
all_inds = list(range(len(query_strings_)))
choice_inds = pick_three()

for i in range(3):
    data_string = scraper.get_data(query_strings_[choice_inds[i]])
    data_string = data_string.rstrip()
    print(data_string)
    tweet_text = str(query_strings.game_dt + "\n\n" + tweet_strings_[choice_inds[i]] + "\n\n" + data_string)
    print(tweet_text)
    api_v2.create_tweet(text=tweet_text)