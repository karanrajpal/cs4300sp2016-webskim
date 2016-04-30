from nytimesarticle import articleAPI
import urllib
import requests
k = 0
api = articleAPI('54456bf0e2ef6359746a50e4c5bdf69c:12:74990553')
def parse_articles(articles):
    '''
    This function takes in a response to the NYT api and parses
    the articles into a list of dictionaries
    '''
    global k
    news = []
    for i in articles['response']['docs']:
        dic = {}
        dic['id'] = i['_id']
        if i['abstract'] is not None:
            dic['abstract'] = i['abstract'].encode("utf8")
        dic['headline'] = i['headline']['main'].encode("utf8")
        dic['desk'] = i['news_desk']
        dic['date'] = i['pub_date'][0:10] # cutting time of day.
        dic['section'] = i['section_name']
        if i['snippet'] is not None:
            dic['snippet'] = i['snippet'].encode("utf8")
        dic['source'] = i['source']
        dic['type'] = i['type_of_material']
        dic['url'] = i['web_url']
        dic['word_count'] = i['word_count']
        r = requests.get(dic['url'])
        
        # Get the text of the contents
        html_content = r.text.encode('utf-8')
        text_file = open("business{}.html".format(k), "w")
        k = k+1
        text_file.write(html_content)
        text_file.close()
#         print(html_content)
        # locations
        locations = []
        for x in range(0,len(i['keywords'])):
            if 'glocations' in i['keywords'][x]['name']:
                locations.append(i['keywords'][x]['value'])
        dic['locations'] = locations
        # subject
        subjects = []
        for x in range(0,len(i['keywords'])):
            if 'subject' in i['keywords'][x]['name']:
                subjects.append(i['keywords'][x]['value'])
        dic['subjects'] = subjects   
        news.append(dic)
    return(news) 

for i in range(0,101):
    articles = api.search(fq = {'news_desk':['Business']}, page = i, begin_date= 20150901)
    parse_articles(articles)

# print(parse_articles(articles)[5])

# print(len(parse_articles(articles)))


