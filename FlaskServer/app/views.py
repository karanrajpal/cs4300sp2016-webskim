from app import app
from flask import request
from flask.ext.cors import CORS, cross_origin
from sklearn.feature_extraction.text import CountVectorizer
import cPickle as pickle
import os
import sys
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/fetchCategory', methods=['GET'])
@cross_origin()
def login():
    keywords = request.args.get('keywords')
    if not os.path.exists('classifier.pickle'):
        print("Please put the output of the first assignment here!")
    else :
        with open('labeldata.pickle','rb') as f:
            labeldata = pickle.load(f)
    count_vect = CountVectorizer()
    X_train_counts = count_vect.fit_transform(labeldata.data)
    clf = MultinomialNB().fit(X_train_counts, labeldata.target)
    # if not os.path.exists('classifier.pickle'):
    #     print("Please put the output of the first assignment here!")
    # else :
    #     with open('classifier.pickle','rb') as f:
    #         clf = pickle.load(f)
    #     with open('classifier.pickle','rb') as f:
    #         categories = pickle.load(f)
    #     count_vect = CountVectorizer()
    X_new_counts = count_vect.transform([keywords])
    predicted = clf.predict(X_new_counts)
    print(keywords)
    return labeldata.target_names[predicted[0]]
    # return keywords

