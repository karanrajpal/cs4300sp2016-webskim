import re 
import matplotlib.pyplot as plt

# politics = []
# for i in range(0,1001):
# 	text = open("politics/politics{}.html".format(i)).read()
# 	text = re.sub('[^w&^d]', ' ', text)
# 	text = text.lower()
# 	text = text.split()
# 	politics.append(len(text))
# plt.plot(politics)
# plt.ylabel('Politics article word count')
# plt.xlabel('File')
# plt.show()
from bs4 import BeautifulSoup
sports = []
politics = []
sportsAverage = 0
politicsAverage = 0
noOfWords = 0
for i in range(0,1001):
	text = open("politics/politics{}.html".format(i)).read()
	# text = re.sub(r'(<[^>]*>)',' ',text)
	# text = re.sub('\n',' ',text)
	# text = re.findall(r'\w+', text)
	# text = text.lower()
	# text = text.split()
	soup = BeautifulSoup(text)
	matches = soup.findAll("p", { "class" : "story-body-text" })
	matches_new = []
	# print(matches[0].contents)
	for index,match in enumerate(matches):
		matches_new.append(matches[index].contents)
	matchesText = ''.join(map(str, matches_new))
	text  = matchesText.split()
	noOfWords+= len(text)
	# print(len(text))
	# print("sum is: {}".format(sum(len(word) for word in text)))
	if(len(text)!=0):
		average = sum(len(word) for word in text)/len(text)
	# print("average in artocle 0 for sports is : {} ".format(average))
	sports.append(len(text))
	sportsAverage+=average
	# politicsText = open("politics/politics{}.html".format(i)).read()
	# politicsText = re.sub('[^w&^d]', ' ', politicsText)
	# politicsText = politicsText.lower()
	# politicsText = politicsText.split()
	# average = sum(len(word) for word in politicsText)/len(politicsText)
	# # print("average in artocle 0 for politics is : {}".format(average))
	# politicsAverage+=average
	# politics.append(len(politicsText))

sportsAverage = sportsAverage/20.0;
politicsAverage = politicsAverage/1000;
noOfWords = noOfWords/1000.0;
print("noOfWords is: {}".format(noOfWords))
# plt.plot(politics)
# plt.plot(sports)
# plt.legend(['Politics articles', 'Sports articles'], loc='upper left')
# plt.ylabel('Article word count')
# plt.xlabel('File')
# plt.hist([sportsAverage, politicsAverage], bins=[0, 1, 2])
# plt.show()
