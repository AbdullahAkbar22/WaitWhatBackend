from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def getHTMLContent(url):
	"""
	Attempts to get the content at `url` by making an HTTP GET request.
	If the content-type of response is some kind of HTML/XML, return the
	text content, otherwise return None.
	"""
	headers = {'User-Agent': 'Mozilla/5.0'}
	try:
		with closing(get(url, headers=headers)) as resp:
			return resp.content

	except RequestException as e:
		log_error('Error during requests to {0} : {1}'.format(url, str(e)))
		return None
		
		
def getScores(theDate, theLeague):
	urlToParse = "http://www.espn.com/"+theLeague+"/scoreboard/_/date/"+theDate
	driver = webdriver.Chrome()
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
	
gamesDate = input("Enter Date: ")
gamesLeague = input("Enter league: ")
thingToWrite = getScores(gamesDate, gamesLeague)

f = open("espnscores.json", "w")
f.write(thingToWrite)