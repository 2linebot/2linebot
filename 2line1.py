<<<<<<< HEAD
import tweepy
import time
import os
from os import environ

ckey=environ['ckey']
csecret=environ['csecret']
atoken=environ['atoken']
asecret=environ['asecret']

auth=tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api=tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user=api.me()

search='Line 2 Bloor-Danforth from:TTCnotices'
nrTweets=5

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Alert RTd')
        print(tweet.text)
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break





=======
import tweepy
import time
import os

ckey=os.environ['ckey']
csecret=os.environ['csecret']
atoken=os.environ['atoken']
asecret=os.environ['asecret']

auth=tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api=tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user=api.me()

search='Line 2 Bloor-Danforth from:TTCnotices'
nrTweets=5

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Alert RTd')
        print(tweet.text)
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break





>>>>>>> d9e36d846ab2f51d83f8759dcf229fd1ac2d2516
