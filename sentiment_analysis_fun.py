import tweepy
from textblob import TextBlob

consumer_key = 'bqkEuU6QRRWfxUlLwZTRy6wyC'
consumer_secret = '0g6V6NrmR24i14xhkcoPh5Y98syxSqHVEoGOHtmC8gTwOXVLQl'

access_token = '1141728997-chhaQ1h3m5kkweFqjxScUHTg1JVCmlZpjfR68Di'
access_secret = 'wKp3lbZ6cYGM40Zl4dFWGaJFssts7LLH5leCzV9xDnkZ7'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

public_tweets = api.search('Bitcoin')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)