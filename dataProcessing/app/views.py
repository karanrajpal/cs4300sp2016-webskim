from app import app
from flask import request
from sklearn.feature_extraction.text import CountVectorizer
import cPickle as pickle
import os
import sys

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/fetchCategory', methods=['GET'])
def login():
    keywords = request.args.get('keywords')
    if not os.path.exists('classifier.pickle'):
        print("Please put the output of the first assignment here!")
    else :
        with open('classifier.pickle','rb') as f:
            clf = pickle.load(f)
        with open('classifier.pickle','rb') as f:
            categories = pickle.load(f)
        count_vect = CountVectorizer()
        predicted = clf.predict(count_vect.transform(keywords))
    return categories[predicted[0]]

