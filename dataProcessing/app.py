import bs4
import sys
import os
import fnmatch
import unicodedata
import cPickle as pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.stem.porter import PorterStemmer
import math
import numpy as np
import json
final_content = []
token_dict = {}
def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = []
    for item in tokens:
        stems.append(PorterStemmer().stem(item))
    return stems

def makeTfIdf(raw_html,index):
	# raw_html = raw_html.encode('utf-8').decode('ascii', 'ignore')
	bsoup = bs4.BeautifulSoup(raw_html)
	content_for_this_article = ""
	for hit in bsoup.findAll(attrs={'class' : 'story-body-text story-content'}):
		content_for_this_article += tokenize(hit.text.rstrip())
	final_content.append(content_for_this_article.encode('ascii', 'ignore'))

for folder, subs, files in os.walk("business"):
	for index, transcript_filename in enumerate(fnmatch.filter(files, '*.html')):
		with open(os.path.join(folder, transcript_filename)) as f:
			makeTfIdf(f.read(),index)

# with open('businessContent.pickle', 'wb') as f:
#     pickle.dump(final_content, f)

corpus = final_content
# tf = TfidfVectorizer(input='content', analyzer='word', min_df=1,max_features=5000, sublinear_tf=True,stop_words = 'english', norm = 'l2')
# response =  tf.fit_transform(corpus)
# feature_names = tf.get_feature_names()
result = {}


tfidf_vectorizer = TfidfVectorizer(
    min_df=1,  # min count for relevant vocabulary
    max_features=4000,  # maximum number of features
    stop_words = 'english',
    strip_accents='unicode',  # replace all accented unicode char
    # by their corresponding  ASCII char
    analyzer='word',  # features made of words
    token_pattern=r'\w{4,}',  # tokenize only words of 4+ chars
    ngram_range=(1, 1),  # features made of a single tokens
    use_idf=True,  # enable inverse-document-frequency reweighting
    smooth_idf=True,  # prevents zero division for unseen words
    sublinear_tf=False)

# vectorize and re-weight
print(corpus)
desc_vect = tfidf_vectorizer.fit_transform(corpus)
d = dict(zip(tfidf_vectorizer.get_feature_names(), desc_vect.data))
f = open('business.json', 'w')
json.dump(d, f)
f.close()


# # print(feature_names)
# # idf = tf.idf_
# # print dict(zip(tf.get_feature_names(), idf))
# indices = np.argsort(tf.idf_)[::-1]
# top_n = 50
# # top_features = [feature_names[i] for i in indices[:top_n]]
# # print top_features
# for col in sorted(response.nonzero()[1],reverse=True):
# 	if(response[0,col]!=0.0):
# 		result[feature_names[col]] = response[0,col]
# print result


		