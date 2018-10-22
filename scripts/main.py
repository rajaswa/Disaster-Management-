from pre_processing import *
from classification import *
from summary import *
from push_tweet import *

#Binary classification
x_unseen_disaster = binary_classification('./data/tweets_indonesia_unseen.csv') 

#Multi classification
unseen_data = multi_classification(x_unseen_disaster)

cat0 = [] #missing, dead or injured
cat1 = [] #Infrastructure damage
cat2 = [] #Other useful or volunteer and donation
cat3 = [] #irrelevant

for i in range(len(unseen_data)):
  
  if (unseen_data['label_n'][i] == 0):
    cat0.append(unseen_data['tweet_text'][i])
    
  if (unseen_data['label_n'][i] == 1):
    cat1.append(unseen_data['tweet_text'][i])
    
  if (unseen_data['label_n'][i] == 2):
    cat2.append(unseen_data['tweet_text'][i])
    
  if (unseen_data['label_n'][i] == 3):
    cat3.append(unseen_data['tweet_text'][i])
	
'''
#Getting Summaries
cat_0_summary = summarize(cat0)
cat_1_summary = summarize(cat1)
cat_2_summary = summarize(cat2)

cat_0_tweet = []
cat_1_tweet = []
cat_2_tweet = []

for i in cat_0_summary[0]:
    cat_0_tweet.append('--------------')
    cat_0_tweet.append(spacy_tweets[i])

push_tweet(cat_0_tweet)	
'''
cat_0_tweet = summarize(cat0)
#push_tweet(cat_0_tweet)

print(cat_0_tweet)


