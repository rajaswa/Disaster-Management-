import tweepy

#tokens and keys
consumer_key = "FR3xuN0UYgdMpngpaj8gtnAvU"
consumer_secret = "JeGf8tWdPROcWAbrEELtvSk86wYzGi9mv0kOsIQdJUQevK1oVD"

access_token = "2942900654-SXdsN5ziOiW8pogcSP0DXGWsL5RIkHV5uLwbzGa"
access_token_secret = "04BIhJAYxUVyOxgzjlXpxd5p6meihPZM48I3iMDifD7Hd"

#authorization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#posting

def push_tweet(string):
	api.update_status(string)
	