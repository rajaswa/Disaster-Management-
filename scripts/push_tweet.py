import tweepy

#tokens and keys
consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

#authorization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#posting

def push_tweet(string):
	api.update_status(string)
	