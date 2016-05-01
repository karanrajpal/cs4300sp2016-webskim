from app import app
from flask import request

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/fetchCategory', methods=['GET'])
def login():
    keywords = request.args.get('keywords')
    if not os.path.exists('classifier.pickle'):
    	print("Please put the output of the first assignment here!",
          file=sys.stderr)
	else:
    	with open('classifier.pickle','rb') as f:
        	clf = pickle.load(f)
    return keywords

