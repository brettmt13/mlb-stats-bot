import tweepy
import tweet_strings
import query_strings
import scraper
import random
import yaml
import os
import image_gen
import numpy
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


def gen_tweet_with_text():
    for i in range(1):
        try:
            player_images_data = scraper.get_data_image(query_strings_[choice_inds[i]])
        except AttributeError:
            print("Data not yet available for parsing. Try again soon.")
            exit(1)
        data_string = data_string.rstrip()
        data_string = data_string.lstrip()
        player_images_URL = player_images_data["Player Image URL"]
        player_names = player_images_data["Player"]
        # print(data_string)
        tweet_text = str(query_strings.game_dt + "\n\n" + tweet_strings_[choice_inds[i]] + "\n\n" + data_string)
        # print(tweet_text)
        # api_v2.create_tweet(text=tweet_text)
        print()
        
def gen_tweet_only_image():
    for i in range(1):
        try:
            player_images_data = scraper.get_data_image(query_strings_[choice_inds[i]])
        except AttributeError:
            print("Data not yet available for parsing. Try again soon.")
            exit(1)
        player_images_URL = player_images_data["Player Image URL"].to_numpy()
        player_names = player_images_data["Player"].to_numpy()
        print("Checking player names and URL separate...:\n")
        print(player_images_URL)
        print(player_names)
        tweet_text = str(query_strings.game_dt + "\n\n" + tweet_strings_[choice_inds[i]] + "\n\n")
        image_gen.generate_image(player_images_URL, player_names)
        media_upload = api_v1.media_upload(filename="twit_img.jpg")
        api_v2.create_tweet(text=tweet_text, media_ids=[media_upload.media_id])

    # clear images
    for i in range(5):
        os.remove(f'player_image{i}.png')
    os.remove('twit_img.jpg')
        
if __name__ == "__main__":
    gen_tweet_only_image()