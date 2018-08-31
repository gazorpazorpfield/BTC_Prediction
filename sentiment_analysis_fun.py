import tweepy
from textblob import TextBlob
#To run this will need an API Key
#You can get a free API key at Twitter API. Once you have your API key copy and paste it into the below cell. https://developer.twitter.com/en/account/get-started
consumer_key = 'XXXXXX'
consumer_secret = 'XXXXXXX'

access_token = 'XXXX'
access_secret = 'XXXXXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

public_tweets = api.search('Bitcoin')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
