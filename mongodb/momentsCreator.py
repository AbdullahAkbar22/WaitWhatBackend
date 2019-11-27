
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import json
'''
from testSummarizer import summarizeArticle

import pymongo
from pymongo import MongoClient

client = MongoClient()
momentDB = client.waitwhat['moments']
'''


def getHTMLContent(url):
	
	headers = {'User-Agent': 'Mozilla/5.0'}
	try:
		with closing(get(url, headers=headers)) as resp:
			return resp.content

	except RequestException as e:
		log_error('Error during requests to {0} : {1}'.format(url, str(e)))
		return None
		
		
def getArticleBody(urlPassed):
	articleBody = ""
	articleContent = str(getHTMLContent(urlPassed)).encode('utf-8')
	articleHTML = BeautifulSoup(articleContent, 'html.parser')
	paragraphs = articleHTML.findAll("p")
	for p in paragraphs:
		if("t.co" not in p.text):
			articleBody += p.text + " " 
	return articleBody

def getIMGLink(urlPassed):
	imgLink = ""
	articleContent = str(getHTMLContent(urlPassed)).encode('utf-8')
	articleHTML = BeautifulSoup(articleContent, 'html.parser')
	img = articleHTML.findAll("img")
	imgLink += str(img[0]["src"])
	return imgLink

	
momentNames = ["Mahommes Named Madden Cover Athlete", "Kings, NBA Launch Walton Investigation", "Russ: Dame Feud 'Doesn't Change Much", "Frazier Latest Yankee to hit IL"]

bodies = ["Kansas City Chiefs quarterback Patrick Mahomes was announced as the cover athlete for Madden NFL 20 on Thursday, including the video game\'s Superstar Edition, ahead of the 2019 NFL draft.\xc2\xa0 Here\'s a look at a trailer for the game, which is scheduled for an Aug. 2 worldwide release: Mahomes is coming off a monster breakout season for the Chiefs. He completed 66.0 percent of his throws for 5,097 yards with 50 touchdowns and 12 interceptions en route to winning the 2018 NFL Most Valuable Player Award and Offensive Player of the Year honors. In February, the 23-year-old Texas Tech product told Mike Snider of USA Today he\'s an avid gamer and that, while he does dabble in sports games like Madden and NBA 2K, he mostly focuses on Call of Duty: Black Ops 4, including its Blackout battle royale mode. \"I am definitely an aggressive player, for sure, I like to run and slide around and always be in the action,\" Mahomes said. \"In Blackout, I am definitely more strategic, more kind of plan-it-out versus with multiplayer ... I\'m really aggressive and attacking the whole entire time.\"  Perhaps being selected as the cover athlete will make him a more diehard Madden player. The latest version of the popular game is highlighted by the addition of the new Face of the Franchise: QB1 mode. Players will create a quarterback and start by playing in the College Football Playoff. That\'s followed by the NFL Scouting Combine, the draft and an NFL career. Madden NFL 20\xc2\xa0is the latest edition in the series that debuted as John Madden Football in 1988 and will be available on Xbox One, PlayStation 4 and PC.", "The NBA and Sacramento Kings announced a joint investigation into the sexual assault allegations made against Kings head coach Luke Walton by former sports reporter\xc2\xa0Kelli Tennant. Tennant filed a civil suit against Walton on Monday alleging that he asked her to come to his hotel while he was an assistant coach for the Golden State Warriors\xc2\xa0so she could give him a copy of a book she had published, for which he wrote the foreword.  Walton was then said to have invited her to his room, where he allegedly \"pinned her on the bed, forcibly kissed her and groped her\" and \"laughed at her pleas before eventually releasing her,\" per\xc2\xa0Sarah Mervosh\xc2\xa0of the\xc2\xa0New York Times. Tennant also said that \"other flirtatious behavior in the wake of the incident\xe2\x80\x94much of which took place when she was a reporter for Spectrum SportsNet and Walton was with the Los Angeles Lakers\xe2\x80\x94made her uncomfortable and was a significant hurdle for her job,\" per\xc2\xa0Kyle Goon\xc2\xa0of the\xc2\xa0Mercury News. She said the behavior contributed to her departing Spectrum SportsNet. Walton\'s lawyer,\xc2\xa0Mark Baute, called Tennant an \"opportunist\" and said her allegations were \"not credible\" on Wednesday.\xc2\xa0 Walton was hired by the Kings as the team\'s new head coach after the 2018-19 regular season, following his firing by the Lakers. Both the Lakers and Warriors said they were unaware of the alleged sexual assault while he was employed by either team, per Mervosh.\xc2\xa0 Tennant is not seeking criminal charges against Walton. \"Our interest is not to have Mr. Walton put in jail or to be investigated by the police necessarily,\" her lawyer,\xc2\xa0Garo Mardirossian, said at a press conference. \"Our interest was for Kelli to feel better about herself, to come out and talk about what happened to her.\" NBA scout: 'He can get his shot off. That's exactly what you need from an NBA guard' NBA scout: 'He can get his shot off. That's exactly what you need from an NBA guard' Houston traveling to Bay Area to prepare for Game 1 vs. Warriors...GS-LAC still at 3-2 Houston traveling to Bay Area to prepare for Game 1 vs. Warriors...GS-LAC still at 3-2", "Russell Westbrook isn\'t going to lose any sleep after Damian Lillard outplayed him in the Portland Trail Blazers\' 4-1 series win over the Oklahoma City Thunder, as he told reporters Thursday: \"When you do so much at a high level, a lot of haters come,\" Westbrook added, per Maddie Lee of the Oklahoman. \"That\'s how life is.\"\xc2\xa0 There was no denying the animosity between Lillard and Westbrook during their first-round series. Lillard, in particular, was not very fond of Westbrook\'s histrionics after made buckets, as he told\xc2\xa0Chris Haynes\xc2\xa0of Yahoo Sports: \"I\'m not even paying attention to it. But when I do see it, that\'s cool. He does it every game, so it doesn\'t bother me. I don\'t celebrate in someone\'s face and try to disrespect my opponent. But if a team calls a timeout, I\'ll go acknowledge the crowd and celebrate with my teammates as I\'m going to the bench. I\'m not going to say some wild s---. I think with him, he\'s pounding his chest and talking s--- and that\'s what gets him going. That\'s the difference between us. Lillard had the last laugh, however. He averaged 33.0 points, 6.0 assists and 2.4 steals in the series, shooting 46.1 percent from the field and 48.1 percent from three. He also famously hit an absurdly deep, dagger three in Paul George\'s face to close out the series. McCollum and the Blazers Snapped Postseason Losing Streak for \"Jennifer\" Stars Invest in Plant-Based Food as Vegetarianism Sweeps NBA The NBA Got Some Wild Techs This Season Jarrett Allen Is One of the NBA\xe2\x80\x99s Hottest Rim Protectors Wade's Jersey Swaps Created Epic Moments This Season Westbrook Makes History While Honoring Nipsey Hussle Devin Booker Makes History with Scoring Tear 29 Years Ago, Jordan Dropped Career-High 69 Points  Bosh Is Getting His Jersey Raised to the Rafters in Miami Steph Returns to Houston for 1st Time Since His Moon Landing Troll Lou Williams Is Coming for a Repeat of Sixth Man of the Year Pat Beverley Has the Clippers Stealing the LA Shine LeBron Keeps Shredding NBA Record Books Young's Hot Streak Is Heating Up the ROY Race with Luka LeBron and 2 Chainz Form a Superteam to Release a New Album Wade's #OneLastDance Dominated February Warriors Fans Go Wild After Unforgettable Moments with Steph Eight Years Ago, the Nuggets Traded Melo to the Knicks Two Years Ago, the Kings Shipped Boogie to the Pelicans ASG Will Be Competitive Again If the NBA Raises the Stakes And he literally waved goodbye to the Thunder in the aftermath: Westbrook, meanwhile, averaged 22.8 points, 10.6 assists and 8.8 rebounds per game but shot just 36.0 percent from the field and 32.4 percent from beyond the arc. There\'s little doubt Lillard got the better of the matchup, carving Oklahoma City\'s defense to shreds.\xc2\xa0 After the OKC\'s poor showing in a series many believed it would win, there are serious questions about the ceiling and future of the current iteration of the team with Westbrook as the Thunder\'s dominant star.\xc2\xa0 Regardless of what changes may come this offseason, Westbrook is ready to move forward after the early playoff exit. \"When you lose a series, everybody looks at series and says this is why you lost...but ultimately there are different things through the season that happen to you or the team,\"\xa0he said\xc2\xa0Thursday. \"It\'s a combination of things. I will do what I need to do to stay consistent and be better.\" NBA scout: 'He can get his shot off. That's exactly what you need from an NBA guard' NBA scout: 'He can get his shot off. That's exactly what you need from an NBA guard' Houston traveling to Bay Area to prepare for Game 1 vs. Warriors...GS-LAC still at 3-2 Houston traveling to Bay Area to prepare for Game 1 vs. Warriors...GS-LAC still at 3-2 \xf0\x9f\x98\xa4 Russ won\xe2\x80\x99t stop shooting\n\xf0\x9f\x95\xb5\xef\xb8\x8f\xe2\x80\x8d\xe2\x99\x82\xef\xb8\x8f PG coy about shoulder\n\xf0\x9f\xa4\x9d OKC still has faith in Billy \xf0\x9f\x98\xa4 Russ won\xe2\x80\x99t stop shooting\n\xf0\x9f\x95\xb5\xef\xb8\x8f\xe2\x80\x8d\xe2\x99\x82\xef\xb8\x8f PG coy about shoulder\n\xf0\x9f\xa4\x9d OKC still has faith in Billy", "The New York Yankees continued to get pummeled by injuries Thursday, as they placed outfielder Clint Frazier on the 10-day injured list with a left ankle sprain retroactive to Tuesday. In a corresponding move, the Yanks recalled reliever Joseph Harvey from Triple-A Scranton/Wilkes-Barre. Catcher Gary Sanchez returned from an IL stint Wednesday, but with Frazier on the shelf, the Yanks once again have 13 players on the IL. New York\'s outfield has been hit especially hard by injuries, as Frazier, Aaron Judge, Giancarlo Stanton, Aaron Hicks and Jacoby Ellsbury are all on the IL. Additionally, third baseman Miguel Andujar, shortstops Didi Gregorius and Troy Tulowitzki, first baseman Greg Bird, starting pitcher Luis Severino and reliever Dellin Betances are out. With so many quality hitters unable to play, Frazier is among the reserves who had been thriving. Although the 24-year-old began the season in the minors, he has been one of New York\'s best hitters since getting called up with a .324 average, six home runs and 17 RBI. Frazier is second on the team to first baseman Luke Voit in both homers and RBI, and his average is tops among those who have appeared in at least three games. On Wednesday, Frazier told\xc2\xa0MLB.com\'s\xc2\xa0Bryan Hoch\xc2\xa0that he would play through his ankle injury with so many other Yankees ailing:\xc2\xa0\"It\'s sore. It\'s a little sprain, but it\'s one of those things where I went through too much last year to not go out there and play. The IL is too full for us, so I\'m good. I\'m going to keep playing.\" Frazier was not in the lineup for New York\'s road wins over the Los Angeles Angles on Tuesday or Wednesday, and the decision was made to give him some time to heal up. While Frazier is out, the Yankees are going to be thin in the outfield. Brett Gardner and Mike Tauchman will be every day starters, while utilityman Tyler Wade will likely be tasked with spending almost all his time in the outfield as well. Frazier was starting to live up to his potential as the fifth-overall pick in the 2013 MLB draft by the Cleveland Indians, acquired by New York in the 2016 Andrew Miller trade, and he figures to be a big part of the New York outfield when he returns. Despite their injury issues, the Yankees are second in the American League East at 14-10 and trail the Tampa Bay Rays by just 1.5 games."]
links = ["https://bleacherreport.com/articles/2833069-patrick-mahomes-named-madden-nfl-20-cover-athlete-game-releases-aug-2", "https://bleacherreport.com/articles/2833081-luke-walton-sexual-assault-allegations-to-be-jointly-investigated-by-kings-nba", "https://bleacherreport.com/articles/2833092-russell-westbrook-damian-lillard-feud-fallout-doesnt-change-much", "https://bleacherreport.com/articles/2833070-yankees-news-clint-frazier-put-on-il-with-ankle-injury-joseph-harvey-recalled"]
imgSRCs = ["https://img.bleacherreport.net/img/images/photos/003/804/907/23be936223b8d4cb02549f93a6c2d23f_crop_north.jpg?h=533&w=800&q=70&crop_x=center&crop_y=top", "https://img.bleacherreport.net/img/images/photos/003/804/919/hi-res-2d60488c864d694606cb2e98267aae57_crop_north.jpg?h=533&w=800&q=70&crop_x=center&crop_y=top", "https://img.bleacherreport.net/img/images/photos/003/804/929/hi-res-0e835aad0c9f003b449c9e6d33d61844_crop_north.jpg?h=533&w=800&q=70&crop_x=center&crop_y=top", "https://img.bleacherreport.net/img/images/photos/003/804/909/hi-res-a690bd8dd7b3a512d11b1fdacab185b3_crop_north.jpg?h=533&w=800&q=70&crop_x=center&crop_y=top"]



for x in range(4):
	momentDoc = {}
	momentDoc["trending"] = x
	momentDoc["title"] = momentNames[x]
	
	#momentBody = getIMGLink(links[x])
	'''
	print("done")
	f = open("contents.txt", "a")
	f.write(momentBody)
	f.write("\n")
	f.close()
	'''
	momentDoc["snippet"] = bodies[x]
	momentDoc["summary"] = summarizeArticle(bodies[x])
	momentDoc["url"] = links[x]
	momentDoc["imgLink"] = imgSRCs([x])
	momentDB.insert_one(momentDoc)
	