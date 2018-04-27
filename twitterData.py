import tweepy
import codecs
from credentials import *


def tweet_config():
    try:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        api = tweepy.API(auth)

        return api
    except:
        pass


def extract_tweets(screen_name):

    try:
        extractor = tweet_config()
        tweets = extractor.user_timeline(screen_name=screen_name, count=100, tweet_mode="extended")
        with codecs.open('tweets/%s_tweets.csv' % screen_name, "w", "utf-8") as fp:
            for items in tweets:
                fp.write("\n")
                fp.write(items.full_text)
    except:
        pass



if __name__ == '__main__':
    extract_tweets("realDonaldTrump")
