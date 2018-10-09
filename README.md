
# Disaster Management using Text Mining from Twitter

## Overview

This projects aims at extracting vital information from Twitter related to natural disasters in real-time. This can be achieved by following the given pipeline :
* Collecting the tweets using Twitter’s Developer API.
* Pre-processing the data. (spelling corrections, splitting joint hashtags, emoticons)
* Feature extraction and selection (named entities- location, organization, money, temporal expressions using NLTK and additional concepts- earthquake, richter scale or magnitude using tf-idf)
* Training the model using neural network and classifying disaster related tweets. 
* Developing a multi-class classifier to identify and remove less informative tweets such as prayers and sentiments (using NLTK or SpaCy).
* Developing a real-time text summarization model on the situational tweets to have brief useful information related to the ongoing disaster crisis.

## Goals

* During any natural disaster, people related to it directly or indirectly generate tremendous information via tweets. But due to the high velocity and massive amount of data on Twitter, it is overwhelming for a rescue operation to comb through.  So we create a concise summary from real-time tweets related to any natural disaster.
* Our aim is to generate summary that accurately represents the situation regarding the area affected by disaster and will include information related to relief, loss of life, injured lives, helpline contact numbers, volunteers, charity organisations etc.
* Our aim also includes to develop an application for civilians to provide services like notifications (live updates), sos features, real-time status of a relatives or friends etc.

## Specifications

* **DEPENDENCIES** : Twython, numpy, pandas, tqdm, NLTK, SpaCY, textacy.
* **DATASETS**           : SOURCE -  [http://crisisnlp.qcri.org/]

Since Twitter API and AZURE’s cloud support allow only limited number of tweets, we plan to use open source datasets available on CRISIS NLP. The available datasets are already annotated and  have classified tweets (disaster and others). We expect to get output summary using this data in batches to try and simulate a real time tweet stream. 

