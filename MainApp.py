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
		
		
		
def getRedditHeadlines(searchQuery, numberOfHeadlines):
	
	searchURL = "https://www.reddit.com/search?q="+searchQuery
	searchContent = getHTMLContent(searchURL)
	searchHTML = BeautifulSoup(searchContent, 'html.parser',from_encoding='utf8')
	
	headlines = searchHTML.find_all("h2", class_="s1okktje-0")
	headlineLinks = searchHTML.find_all("a", class_="SQnoC3ObvgnGjWt90zD9Z")
	print("===================================")
	if(numberOfHeadlines > len(headlines)):
		numberOfHeadlines = len(headlines)
	if(numberOfHeadlines == -1):
		numberOfHeadlines = len(headlines)
	queryJSON = '{ \n "query": "'+searchQuery+'", \n "resultsfound" : '+str(numberOfHeadlines)+',\n "headlines": [ \n'
	#print("Showing "+ str(numberOfHeadlines) + " headlines:")
	for headlineOn in range(numberOfHeadlines):
		queryJSON += '\t{ \n'
		headLineText = headlines[headlineOn].text
		headLineText = ''.join((c for c in str(headLineText) if ord(c) < 128 and ord(c) != 34))
		
		
		headLineLink = headlineLinks[headlineOn]["href"]
		#print('"Title": "'+headLineText+ '",')
		queryJSON += '\t\t"Title": "'+headLineText+ '", \n'
		#print('"Link": "' + headLineLink + '",')
		queryJSON += '\t\t"Link": "' + headLineLink + '", \n'
		subReddit = "/r/"+headLineLink.split("/")[2]
		#print('"Subreddit": "' + subReddit + '"')
		queryJSON += '\t\t"Subreddit": "' + subReddit + '" \n'
		
		
		if(headlineOn != numberOfHeadlines - 1):
			queryJSON += '\n\t}, \n'
		else:
			queryJSON += '\n\t} \n'
		print(" ")
		
	queryJSON += "\n ] \n }"
	return queryJSON
		
		
def getEspnScores(theDate, theLeague):
	urlToParse = "http://www.espn.com/"+theLeague+"/scoreboard/_/date/"+theDate
	driver = webdriver.Chrome("chromedriver")
	driver.implicitly_wait(30)
	driver.get(urlToParse)
	#searchContent = getHTMLContent(urlToParse)
	#print(searchContent)
	searchHTML = BeautifulSoup(driver.page_source, 'html.parser',from_encoding='utf8')
	
	scores = searchHTML.find_all("div", class_="scoreboard-top")
	numberScores = len(scores)
	queryJSON = '{ \n "url": "'+urlToParse+'", \n "date": "'+theDate+'", \n "resultsfound" : '+str(numberScores)+',\n "scores": [ \n'
	
	for scoreOn in range(numberScores):
		queryJSON += '\t{ \n'
		scoreContents = str(scores[scoreOn].contents)
		scoreHTML = BeautifulSoup(scoreContents, 'html.parser')
		teamContent = str(scoreHTML.find("tbody", {"id": "teams"}))
		teamHTML = BeautifulSoup(teamContent, 'html.parser')
		teamAbbrvs = teamHTML.find_all("span", class_="sb-team-abbrev")
		teamNames = teamHTML.find_all("span", class_="sb-team-short")
		teamScores = teamHTML.find_all("td", class_="total")
		queryJSON += '\t "teams": [\n'
		for i in range(2):
			queryJSON += '\t\t{ \n'
			queryJSON += '\t\t "teamNumber": '+str(i + 1)+', \n'
			queryJSON += '\t\t "teamAbbrev": "'+teamAbbrvs[i].text+'", \n'
			queryJSON += '\t\t "teamName": "'+teamNames[i].text+'", \n'
			queryJSON += '\t\t "teamScore": '+teamScores[i].text+' \n'
			if(i != 1):
				queryJSON += '\t\t}, \n'
			else:
				queryJSON += '\t\t} \n'
		queryJSON += '\t ]'
		
		if(scoreOn != numberScores - 1):
			queryJSON += '\n\t}, \n'
		else:
			queryJSON += '\n\t} \n'
			
	
	queryJSON += "\n ] \n }"
	
	#print("Query json: " +queryJSON)
	
	driver.quit()
	return queryJSON

		
MainApp = Flask(__name__)

@MainApp.route('/')
def hello_world():
	return 'Reddit test running'

# API Route Sample

@MainApp.route('/redditHeadlines')
def headlineroute():
	headlineQuery = request.args.get('query', 1)
	return getRedditHeadlines(headlineQuery, -1)
	
@MainApp.route('/espnscores')
def espnScoresRoute():
	scoresDate = request.args.get('date', 1)
	scoresLeague = request.args.get('league', 1)
	return getEspnScores(scoresDate, scoresLeague)