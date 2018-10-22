import tweepy

#tokens and keys
consumer_key = "nHrP4zQdr9W6qDuw6dtmzmcas"
consumer_secret = "kelpyn6orbvgP6RvUdhNnWpHWooUdBKb49GiI262Tr2RQ8Kisj"

access_token = "2942900654-SXdsN5ziOiW8pogcSP0DXGWsL5RIkHV5uLwbzGa"
access_token_secret = "04BIhJAYxUVyOxgzjlXpxd5p6meihPZM48I3iMDifD7Hd"

#authorization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#posting

def push_tweet(string):
	api.update_status(string)
	