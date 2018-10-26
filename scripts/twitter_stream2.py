import json
import pandas as pd

tweets_data_path = './twitter_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
		
		
tweets = pd.DataFrame()

tweet_text = []

for i in range(len(tweets_data)):
    try:
        string = tweets_data[i]['text']
        tweet_text.append(string)
    except:
        continue
		
tweets['tweet_text'] = tweet_text

tweets.to_csv('./data/tweets_indonesia_unseen.csv', encoding = 'utf-8')