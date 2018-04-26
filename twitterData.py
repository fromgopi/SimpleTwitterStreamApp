import tweepy
import _pickle as pickle
from credentials import *


def tweet_config():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    return api


def extract_tweets(screen_name):
    extractor = tweet_config()
    tweets = extractor.user_timeline(screen_name=screen_name, count=1000, tweet_mode="extended")
    new_tweet = [[tweet.full_text] for tweet in tweets]
    #print(new_tweet)
    return new_tweet


def writeToFile():
    tweets = extract_tweets("realDonaldTrump")

    with open("tweets.txt", "wb") as line:
        for items in tweets:
            for item in items:
                line.write(u''.join(item + "\n").encode('utf-8').strip())


if __name__ == '__main__':
    writeToFile()
