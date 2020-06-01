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





