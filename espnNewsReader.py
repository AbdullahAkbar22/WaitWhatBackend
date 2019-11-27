from flask import request, Flask
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def getHTMLContent(url):
	
	headers = {'User-Agent': 'Mozilla/5.0'}
	try:
		with closing(get(url, headers=headers)) as resp:
			return resp.content

	except RequestException as e:
		log_error('Error during requests to {0} : {1}'.format(url, str(e)))
		return None
	
	
def getKeyOnVal(valNumber, theDict):
	for keyOn in theDict:
		if(theDict[keyOn] == valNumber):
			theDict.pop(keyOn)
			return keyOn, theDict
			
def getMaxWords(stringPassed, numberOfTopWords):
	splitString = stringPassed.split(' ')
	wordCounts = {}
	maxWords = []
	frequencyList =  ["is", "the",  "be",  "to",  "of",  "and",  "a",  "in",  "that",  "have",  "I",  "it",  "for",  "not",  "on",  "with",  "he",  "as",  "you",  "do",  "at",  "this",  "but",  "his",  "by",  "from",  "they",  "we",  "say",  "her",  "she",  "or",  "an",  "will",  "my",  "one",  "all",  "would",  "there",  "their",  "what",  "so",  "up",  "out",  "if",  "about",  "who",  "get",  "which",  "go",  "me",  "when",  "make",  "can",  "like",  "time",  "no",  "just",  "him",  "know",  "take",  "people",  "into",  "year",  "your",  "good",  "some",  "could",  "them",  "see",  "other",  "than",  "then",  "now",  "look",  "only",  "come",  "its",  "over",  "think",  "also",  "back",  "after",  "use",  "two",  "how",  "our",  "work",  "first",  "well",  "way",  "even",  "new",  "want",  "because",  "any",  "these",  "give",  "day",  "most",  "us"]

	for i in range(len(splitString)):
		wordOn = splitString[i]
		if(wordOn not in frequencyList):
			if(wordOn not in wordCounts):
				wordCounts[wordOn] = 1
			else:
				wordCounts[wordOn] += 1

	numberToGet = min(numberOfTopWords, len(wordCounts))

	for i in range(numberToGet):
		maxVal = max(wordCounts.values())
		keyResult = getKeyOnVal(maxVal, wordCounts)
		maxKey = keyResult[0]
		wordCounts = keyResult[1]
		maxWords.append(maxKey)
	
	return maxWords

def getArticleBody(urlPassed):
	articleContent = str(getHTMLContent(urlPassed))
	if "article-body" not in articleContent or "print</a></li></ul>" not in articleContent:
		return None
	cutArticle = articleContent.split("print</a></li></ul>")[1].split('<footer')[0]
	encodedArticle = cutArticle.encode('utf-8')
	articleHTML = BeautifulSoup(encodedArticle, 'html.parser')
	articleParagraphs = articleHTML.findAll("p")
	articleText = ""
	for paragraphOn in articleParagraphs:
		articleText += " " + paragraphOn.text.replace("\\'", "'")
	return articleText
	
		
def getESPNNews(leagueName, numberNews):
	articleJSON = ""
	newsContent = getHTMLContent("http://www.espn.com/"+leagueName+"/news/archive")
	espnHTML = BeautifulSoup(newsContent, 'html.parser')
	newsArticles = espnHTML.find_all("li")
	numberToShow = min(len(newsArticles), numberNews)
	numberLeft = numberToShow
	articlesPassed = 0
	
	while(numberLeft > 0 and articlesPassed < len(newsArticles)):
		newsOn = articlesPassed
		newsHeadline = newsArticles[newsOn].text
		newsHTMLCont = str(newsArticles[newsOn])
		linkRef = newsHTMLCont.split('href="')[1].split('"')[0]
		#print("Linkref is:",linkRef)
		if("www.espn.com/"+leagueName+"/story/" in linkRef):
			if('(' in newsHeadline):
				newsHeadline = newsHeadline.split('(')[0]
			articleJSON += "<b>News number: </b>" + str(numberToShow - numberLeft + 1) + "<br>"
			articleJSON += "<b>Headline: </b>" + newsHeadline + "<br>"
			articleJSON += "<b>Link: </b>" + linkRef + "<br>"
			articleBody = getArticleBody(linkRef)
			articleJSON +=  "<b>Article text: </b>" + articleBody + "<br>"
			articleMaxWords = getMaxWords(articleBody, 5)
			articleJSON += "<b>Article top words: </b>"
			for l in range(len(articleMaxWords)):
				articleJSON += articleMaxWords[l] + " "
			articleJSON += "<br>"
			articleJSON += "&nbsp;<br>"
			numberLeft -= 1
		articlesPassed += 1
	return articleJSON
		
		

'''
league = input("Enter league name: ")
numberNews = int(input("Enter number of articles to show: "))
queryText = getESPNNews(league, numberNews)
f = open("contents.html", "w")
f.write(queryText)
print("It is done.")
'''
	
espnApp = Flask(__name__)

@espnApp.route('/')
def hello_world():
	return 'espn test running'

# API Route Sample

	
@espnApp.route('/espnarticles')
def espnScoresRoute():
	articlesLeague = request.args.get('league', 1)
	articlesNumber = request.args.get('numberArticles', 1)
	return getESPNNews(articlesLeague, int(articlesNumber))
	
if __name__ == "__main__":
	espnApp.run(host='192.168.0.10', port=8080)