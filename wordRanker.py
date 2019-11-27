def getKeyOnVal(valNumber, theDict):
	for keyOn in theDict:
		if(theDict[keyOn] == valNumber):
			theDict.pop(keyOn)
			return keyOn, theDict

theString = "Georgia Bulldogs forward Nic Claxton will declare for the 2019 NBA draft, he said in a statement sent by his family to ESPN on Friday. \"First, I want to thank God for giving me this opportunity and blessing me to be in this position,\" Claxton said in the statement. \"I want to thank my family, coaches, and trainers for always believing in me and pushing me to be the best player and person that I can be. I want to thank Dawg Nation for welcoming me with open arms. No matter what, I will always be a Georgia Bulldog for life.\" Get ready for Zion Williamson, Ja Morant and more. \xe2\x80\xa2 Latest NBA mock draft\n\xe2\x80\xa2 Top 100 draft rankings\n\xe2\x80\xa2 Draft assets for every team\n\xe2\x80\xa2 Rankings by stats and scouting Claxton, the No. 40 prospect in the ESPN 100 draft rankings, was a second-team All-SEC selection after a breakout sophomore season in which he averaged 13 points, 8.6 rebounds, 2.5 blocks and 1.1 steals in 32 minutes per game. He drew significant intrigue from NBA scouts over the course of the season as he saw quite a few minutes handling the ball and making plays on the perimeter, which is unique considering he stands 6-foot-11. Claxton is versatile defensively with quick feet and long arms. Claxton is one of the last prominent collegiate players to make his NBA draft intentions known prior to the early-entry deadline Sunday. Some NBA teams have told ESPN that they feel Claxton may be a riser during the pre-draft process and could potentially work his way into the first round, while others feel he's too raw physically and skill-wise to be considered more than a project and would benefit from another year in college. Georgia is putting together one of the best recruiting classes in the country, headlined by the potential No. 1 overall pick in 2020, Anthony Edwards. Claxton has until May 30 to test the draft waters and make a decision about whether to stay in the drat pool or return to school, which may ultimately depend on how he performs in workouts and at the NBA combine in Chicago."

def getMaxWords(stringPassed, numberOfTopWords):
	splitString = stringPassed.split(' ')
	wordCounts = {}
	maxWords = []
	frequencyList =  ["the",  "be",  "to",  "of",  "and",  "a",  "in",  "that",  "have",  "I",  "it",  "for",  "not",  "on",  "with",  "he",  "as",  "you",  "do",  "at",  "this",  "but",  "his",  "by",  "from",  "they",  "we",  "say",  "her",  "she",  "or",  "an",  "will",  "my",  "one",  "all",  "would",  "there",  "their",  "what",  "so",  "up",  "out",  "if",  "about",  "who",  "get",  "which",  "go",  "me",  "when",  "make",  "can",  "like",  "time",  "no",  "just",  "him",  "know",  "take",  "people",  "into",  "year",  "your",  "good",  "some",  "could",  "them",  "see",  "other",  "than",  "then",  "now",  "look",  "only",  "come",  "its",  "over",  "think",  "also",  "back",  "after",  "use",  "two",  "how",  "our",  "work",  "first",  "well",  "way",  "even",  "new",  "want",  "because",  "any",  "these",  "give",  "day",  "most",  "us"]

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

#print(str(max(wordCounts.values())))

print(getMaxWords(theString, 3))