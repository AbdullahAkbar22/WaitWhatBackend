def summarizeArticle(article_text):
	import nltk
	#article_text = "With it working well, Patrick Beverley continued to play the foil for the Clippers in their first-round series against the Warriors on Wednesday night. Golden State coach Steve Kerr, given a day to reflect, likened it to facing one of the great heavyweight champions of all-time -- in how Beverley's head pops back like he's being punched by him. Kerr, asked about a sequence in which Draymond Green was assessed a technical foul in Wednesday night's 129-121 loss, said Beverley had duped the referee into a poor call. \"I didn't think it was a good call,\" Kerr said. \"You know Beverley's going to flop, and Draymond turned; it looked like Tyson punched him in the face.\" With 10:53 to play in the third quarter and the Warriors trailing by 11, Green was called for an offensive foul. Green then argued with referee Marc Davis and was assessed a technical foul. Kerr said he thought Green had been clapping and trying and get the Oracle Arena crowd more into the game when he was called for the technical. \"Beverley's good at that,\" Kerr said. \"His head literally snaps back. I worry he's going to get whiplash on some of these flops. But he's good at it. And the refs, they're often times partial to the little guy whose down there. \"I didn't like that particular call,\" Kerr said of the offensive foul. \"I know Draymond didn't, hence the technical. There's no question Draymond was trying to get the crowd going.\" After the loss, which pulled the Clippers to 3-2 in the series, Green took umbrage when asked why he was more \"edgy\" than usual. \"Was I edgy? I was edgy?\" Green said. \"I got a tech. Think I give a damn about getting a tech? You consider that edgy? You shoulda watched some of my past times if you want to see edgy.\" On Thursday, Green wasn't answering to media, or rather wasn't worried whether Kerr could in his session with reporters. With music blaring during shootaround as Green practiced his outside shot, Kerr had trouble hearing questions from reporters and twice asked the volume to be lowered. His request was denied both times. When jokingly asked who was in charge, Kerr replied, \"Not me, obviously.\" But Kerr said he won't hesitate to take charge when the Warriors look to close out the Clippers in Game 6 on Friday back in Los Angeles. Andre Iguodala could replace Andrew Bogut as as starter in a return to the \"death lineup\" for the Warriors, Kerr said. \"There's no question I have to consider all of our options in terms of rotations,\" Kerr said, \"and who's playing with whom and for how long. All that stuff. That's our job.\""

	# Removing Square Brackets and Extra Spaces
	article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
	article_text = re.sub(r'\s+', ' ', article_text)

	# Removing special characters and digits
	formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
	formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

	sentence_list = nltk.sent_tokenize(article_text)

	stopwords = nltk.corpus.stopwords.words('english')

	word_frequencies = {}
	for word in nltk.word_tokenize(formatted_article_text):
		if word not in stopwords:
			if word not in word_frequencies.keys():
				word_frequencies[word] = 1
			else:
				word_frequencies[word] += 1

	maximum_frequncy = max(word_frequencies.values())

	for word in word_frequencies.keys():
		word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)


	sentence_scores = {}
	for sent in sentence_list:
		for word in nltk.word_tokenize(sent.lower()):
			if word in word_frequencies.keys():
				if len(sent.split(' ')) < 30:
					if sent not in sentence_scores.keys():
						sentence_scores[sent] = word_frequencies[word]
					else:
						sentence_scores[sent] += word_frequencies[word]

	import heapq
	summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

	summary = ' '.join(summary_sentences)
	return summary
