import tweepy

access_token = "1686518036314898432-jUwmpVkqLiQOjFdIYEdcpN5mtW2cVr"
access_token_secret = "rS3EX7fbwsVtcATPcS9ckpGAi29m47TuyFdzw9QbAsiih"
consumer_key = "Ty4a1OkGA9sx9Lgl4NKjfMnuq"
consumer_secret = "oKcNI8lLqqrWfDYLYQRiqxJc7uOhVlOARbiPq8gxXsMsekEaKq"
client_id = "SUJXc0xjZWI3Wm9WVkJJM1BYTmE6MTpjaQ"
client_secret = "i_a9Ncrt3AsTCy64mJjtG3NzsTOnaeJwCEvIUbeIKk8qawRns8"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAHCjpAEAAAAA6xjUYTGu%2F0RRPYaSUk3S%2B9OB3mU%3DnBMIqSzfSeqDy1x1OFfZJUaSJ8mKlGCVFrkClL2vJmZwavFIlO"
bearer_token = bytes(bearer_token, "utf-8").decode("unicode-escape")

# authorize app to bot
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# for media
api_v1 = tweepy.API(auth)
media_upload = api_v1.media_upload(filename="./image.jpg")

# for text
api_v2 = tweepy.Client(bearer_token=bearer_token,
                    access_token=access_token,
                    access_token_secret=access_token_secret,
                    consumer_key=consumer_key,
                    consumer_secret=consumer_secret)

api_v2.create_tweet(text='Hi', media_ids=[media_upload.media_id])