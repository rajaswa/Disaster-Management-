#!/usr/bin/env python
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


cat0_simple_summary =simplesummarize(cat0,'cat0_text.txt')
cat1_simple_summary =simplesummarize(cat1,'cat1_text.txt')
#cat2_simple_summary =simplesummarize(cat3,'cat2_text.txt')

#push_tweet(cat_0_tweet)
#print(cat0_simple_summary)



	

