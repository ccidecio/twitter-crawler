#!/usr/bin/env python
# coding: utf-8

# In[19]:


import tweepy as tw
import os

# These API keys belongs to a twitter crawler app created under the
# twitter user <developer_name>. Keys are hidden for privacy and security reasons.
CONSUMER_KEY=""    # hidden 
CONSUMER_KEY_SEC=""    # hidden
ACCESS_TOKEN = ""    # hidden
ACCESS_TOKEN_SECRET = ""    # hidden

DATE_UNTIL="2020-05-30"	 # "YYYY-MM-DD"
LANG = "tr" # Language of the tweet(ISO 639-1 code)
TWEET_LIMIT = 2000

def dump_tweets(tweets, searchQuery):
    if(LANG == ""):
        outFileName = "tweets_" + searchQuery[1:]
    else:
        outFileName = "tweets_" + searchQuery[1:] + "_" + LANG
    f = open(outFileName,"w+")
    for count,tweet in enumerate(tweets):
        f.write(tweet.text + "\n")
    print("(" + searchQuery + ")" + "Tweets crawled: " + str(count))
    f.close()
    os.rename(outFileName, outFileName + "_" + str(count) + ".txt")

def auth():
	auth = tw.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SEC)
	auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
	api = tw.API(auth, wait_on_rate_limit=True)
	return api

def crawl(api, searchQuery):
    tweets = tw.Cursor(api.search, 
                        q=searchQuery, 
                        until=DATE_UNTIL,
                        lang=LANG).items(TWEET_LIMIT)    
    dump_tweets(tweets, searchQuery)
    return tweets

def main():
    api = auth()
    searchQuery = "#coronavirus"    
    tweets = crawl(api, searchQuery)
    return 0

