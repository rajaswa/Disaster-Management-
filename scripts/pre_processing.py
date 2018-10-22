import re

#Preprocessing function

def preprocess(corpus):
	corpus = corpus.apply(lambda z: re.sub(u'http\S+', u'', z)) 
	corpus = corpus.apply(lambda z: re.sub(u'(\s)@\w+', u'', z))
	corpus = corpus.apply(lambda z: re.sub(u'#', u'', z))
	corpus = corpus.apply(lambda z: re.sub(u'RT', u'', z))
	
	return corpus