
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

from testSpacy import ArticleParser


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
		
		
		
def getHeadlines(searchQuery, numberOfHeadlines):
	ap = ArticleParser()
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
		
		print(ap.getEntitiesToJSON(headLineText))
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
	
	#print(queryJSON)
	f = open("headlines.json", "w")
	f.write(queryJSON)
		
thesearchQuery = input("Enter search query: ")
thenumberOfHeadlines = int(input("Enter number of headlines: "))
getHeadlines(thesearchQuery, thenumberOfHeadlines)
	