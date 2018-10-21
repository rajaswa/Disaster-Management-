#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "2942900654-SXdsN5ziOiW8pogcSP0DXGWsL5RIkHV5uLwbzGa"
access_token_secret = "04BIhJAYxUVyOxgzjlXpxd5p6meihPZM48I3iMDifD7Hd"
consumer_key = "nHrP4zQdr9W6qDuw6dtmzmcas"
consumer_secret = "kelpyn6orbvgP6RvUdhNnWpHWooUdBKb49GiI262Tr2RQ8Kisj"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)
		
		
if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'Indonesia'
    stream.filter(track=['Indonesia', 'earthquake'])
	