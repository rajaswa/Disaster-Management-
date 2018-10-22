import pandas as pd

from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Flatten
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.models import load_model

import re
from sklearn.feature_extraction.text import TfidfVectorizer

from pre_processing import *

def binary_classification(path):
	
	#Unseen data
	unseen_data = pd.read_csv(path)
	
	unseen_data.columns = unseen_data.columns.str.strip()
	x_unseen = unseen_data['tweet_text']
	
	#Tfidf fit training data
	tweets_binary_df = pd.read_csv('./data/tweets_binary_df.csv')
	x_binary = tweets_binary_df['tweet_text']
	
	#Preprocessing
	x_binary = preprocess(x_binary)
	x_unseen = preprocess(x_unseen)
	
	#TFIDIF
	tvec1 = TfidfVectorizer(max_features=10000,ngram_range=(1, 3))
	tvec1.fit(x_binary)
	
	x_unseen_tfidf = tvec1.transform(x_unseen)
	
	#Model prediction
	model_binary = load_model('binary_classification.h5')
	y_unseen = model_binary.predict(x_unseen_tfidf, batch_size=256, verbose=0, steps=None)
	
	#Separating out disaster related tweets
	y_unseen_binary = []
	
	for i in range(len(y_unseen)):
		if (y_unseen[i] <= 0.5):
			y_unseen_binary.append(0)
		else:
			y_unseen_binary.append(1)
		
	x_unseen_disaster = []

	for i in range(len(x_unseen)):
		if (y_unseen_binary[i] == 1):
			x_unseen_disaster.append(x_unseen[i])
			
	return x_unseen_disaster
	
	
def multi_classification(x_unseen_disaster):
	
	#Tfidf fit training data
	label_data = pd.read_csv('./data/label_data.csv')
	x = label_data['tweet_text']
	
	#Preprocessing
	x = preprocess(x)
	
	#TFIDIF
	tvec2 = TfidfVectorizer(max_features=1000,ngram_range=(1, 3),analyzer='word',norm='l2',stop_words='english')
	tvec2.fit(x)
	
	x_unseen_disaster_tfidf = tvec2.transform(x_unseen_disaster)
	
	#Model prediction
	model_multi = load_model('multi_classification.h5')
	y_unseen_multi_one_hot = model_multi.predict(x_unseen_disaster_tfidf, batch_size=256, verbose=0, steps=None)
	y_unseen_multi = np.argmax(y_unseen_multi_one_hot , axis=1)
	
	#Converting predicted classes back into pandas dataframe:
	columns=['tweet_text']

	y_unseen_multi_transpose = y_unseen_multi.reshape(-1)

	unseen_data = pd.DataFrame(data = x_unseen_disaster, columns=columns)

	unseen_data['label_n'] = y_unseen_multi_transpose
	
	return unseen_data


	
	
	


