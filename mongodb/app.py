from flask import request, Flask
import json
import pymongo
from bson.json_util import loads, dumps

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient()

@app.route('/')
def root():
    return dumps({'name': 'wait-what', 'version': '0.0.1'})

@app.route('/moments')
def momentStuff():
    numTrending = int(request.args.get('num', 5))
    articleCollection = client.waitwhat['moments']

    articles = []

    for article in articleCollection.find({"trending": {"$lt": numTrending+1}}).sort("date"):
        articles.append(article)
        #print(article)

    return dumps(articles)

@app.route('/trending')
def hello_world():
    numTrending = int(request.args.get('num', 5))
    articleCollection = client.waitwhat['articles']

    articles = []

    for article in articleCollection.find({"trending": {"$lt": numTrending+1}}).sort("date"):
        articles.append(article)
        #print(article)

    return dumps(articles)

@app.route('/articles/')

@app.route('/square')
def square():
    x = int(request.args.get('x', 1))
    return json.dumps({'x': x * x})
    
    
@app.route('/search')
def searchStuff():
    searchQuery = request.args.get('query', '')
    numTrending = int(request.args.get('num', 5))
    articleCollection = client.waitwhat['articles']

    articles = []
    searchArticles = articleCollection.find( { "$text": { "$search": searchQuery } } )
    numbToGet = min(numTrending, searchArticles.count())
    numbOn = 0
    for article in searchArticles:
        articles.append(article)
        numbOn+=1
        if(numbOn >= numbToGet):
            break
        #print(article)

    return dumps(articles)



if __name__ == ("__main__"):
    app.run(host='192.168.0.7',port=8080)
