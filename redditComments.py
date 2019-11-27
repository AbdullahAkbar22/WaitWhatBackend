
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


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
		
		
def getComments(redditUrl, numberOfComments):
	searchContent = getHTMLContent(redditUrl)
	searchHTML = BeautifulSoup(searchContent, 'html.parser',from_encoding='utf8')
	
	comments = searchHTML.find_all("p", class_="s14dydj4-10")
	commentPoints = searchHTML.find_all("span", class_="h5svje-0")
	commentOn = 0
	print("===================================")
	if(numberOfComments > len(comments)):
		numberOfComments = len(comments)
	if(numberOfComments == -1):
		numberOfComments = len(comments)
		
	queryJSON = '{ \n "url": "'+redditUrl+'", \n "resultsfound" : '+str(numberOfComments)+',\n "comments": [ \n'
	
	for commentOn in range(numberOfComments):
		queryJSON += '\t{ \n'
		commentText = comments[commentOn].text
		commentText = ''.join((c for c in str(commentText) if ord(c) < 128 and ord(c) != 34))
		shouldLookForPoints = True
		pointText = ""
		while(shouldLookForPoints):
			pointText = commentPoints[commentOn].text
			if "points" in pointText:
				shouldLookForPoints = False
			commentOn += 1
			if commentOn == len(commentPoints) - 1:
				break
		
		
		queryJSON += '\t\t"Comment": "'+commentText+ '", \n'
		
		queryJSON += '\t\t"Points": "' + pointText + '" \n'
		
		
		
		if(commentOn != numberOfComments - 1):
			queryJSON += '\n\t}, \n'
		else:
			queryJSON += '\n\t} \n'
		print(" ")
		
	queryJSON += "\n ] \n }"
	
	#print(queryJSON)
	f = open("comments.json", "w")
	f.write(queryJSON)
		
	
thesearchQuery = input("Enter URL: ")
thenumberOfComments = int(input("Enter number of comments: "))
getComments(thesearchQuery, thenumberOfComments)
	