from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import json

def getHTMLContent(url):
	
	headers = {'User-Agent': 'Mozilla/5.0'}
	try:
		with closing(get(url, headers=headers)) as resp:
			return resp.content

	except RequestException as e:
		log_error('Error during requests to {0} : {1}'.format(url, str(e)))
		return None
		
queryJSON = getHTMLContent("https://en.wikipedia.org/wiki/Most_common_words_in_English")
queryHTML = BeautifulSoup(queryJSON, 'html.parser')
queryStuff = queryHTML.findAll("a", class_="extiw")
queryText = ""
for linkOn in queryStuff:
	queryText += ' "' + linkOn.text + '", '
f = open("contents.txt", "w")
f.write(queryText)