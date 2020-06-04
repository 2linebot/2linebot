import tweepy
import time
import os
from os import environ
from apscheduler.schedulers.blocking import BlockingScheduler

sched=BlockingScheduler()

@sched.scheduled_job('interval', minutes=2)
def job():
   
   ckey=environ['ckey']
   csecret=environ['csecret']
   atoken=environ['atoken']
   asecret=environ['asecret']

   auth=tweepy.OAuthHandler(ckey, csecret)
   auth.set_access_token(atoken, asecret)

   api=tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

   user=api.me()
   search='"Line 2" from:TTCnotices'
   nrTweets=5

   for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
       try:
           print('Alert RTed')
           print(tweet.text)
           tweet.retweet()
           time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

sched.start()
