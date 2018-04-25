import tweepy
import pandas as pd
from IPython.display import display
from credentials import *


def tweet_config():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    return api


def extract_tweets(screen_name):
    extractor = tweet_config()
    tweets = extractor.user_timeline(screen_name=screen_name, count=2, tweet_mode="extended")
    new_tweet = [[tweet.full_text] for tweet in tweets]
    print(new_tweet)

if __name__ == '__main__':
    extract_tweets("PawanKalyan")