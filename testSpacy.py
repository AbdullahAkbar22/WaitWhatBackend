import spacy
from spacy import displacy
from collections import Counter
from pprint import pprint
import json

nlp = spacy.load('en_core_web_lg')

class ArticleParser():

    def getEntities(self, text: str):
        doc = nlp(text)
        output = [(X.text, X.label_) for X in doc.ents]
        return output

    def getEntitiesToJSON(self, text: str):
        output = self.getEntities(text)
        return json.dumps(dict(output))




text = """Justin Paperny, wearing his luckiest pair of golfing slacks, was about to tee off at Calabasas Country Club in Calabasas, Calif., last Tuesday morning when his phone began buzzing.
On the other line was a familiar voice, a well-known lawyer whose client had recently been charged by the Justice Department for their role in a sprawling admissions scandal involving dozens of parents and name-brand schools like Yale, Georgetown and the University of Southern California.
The lawyer wanted to know whether Paperny — a federal prison consultant and convicted felon who prepares people for life behind bars — was available to discuss the case.
The answer was yes. But like most of his work, Paperny explained, a hefty price tag would be attached.
While the college admissions scheme captured the public’s attention last week, temporarily uniting the left and the right in mutual disgust, prison consultants like Paperny went to work. Part fixer, part adviser and part therapist, their jobs amorphously range from soothing exaggerated fears about sexual assault and answering the basic questions about hygiene (i.e. 'How do I use the bathroom in federal prison?”) to managing portions of a business when they’re behind bars. Like hardened sherpas leading well-heeled clients up a treacherous peak, they’ve smoothed the road to incarceration for big name clients like Bernie Madoff, Martha Stewart and former NBA referee Tim Donaghy.
For a wealthy client ensnared by the admissions scandal, Paperny said one question in particular undoubtedly looms: 'Will I ever work again?”
'There’s a million questions that go through people’s minds in the beginning,” said Paperny, who helps clients organize their finances and find job opportunities before they go into prison, as well as after. 'The hardest part is the public shame and embarrassment and not knowing how it’s going to affect your career and your finances.”
'Those questions are harder than any day they may serve,” he added. 'These people in this admissions scandal are already in federal prison — they’re just not getting credit for time served.”
['Three spots’: Alleged bribery of tennis coach stings Georgetown admissions]
For Paperny, last week’s call wasn’t the only reason one of largest news stories in the country hit particularly close to home. A southern California native who played baseball at USC, the 44-year-old is a regular lecturer on ethics at the university’s Marshall School of Business. Already struggling to recover from recent controversies, his alma mater is ground zero for the admissions scandal, a place where six of the 50 alleged perpetrators — including several prominent athletics officials — have close ties.
As a former Bear Stearns stock broker who spent 18 months in federal prison for conspiring to commit fraud, Paperny is uniquely qualified to discuss ethical failings when he visits the university. A decade after his release, his eight-person firm, 'White Collar Advice,” has become a go-to resource for wealthy criminals preparing for prison. His YouTube channel, which covers much of the advice he gives his clients, has several thousand subscribers.
Paperny –– who has close ties to Hollywood and its glut of high-profile criminal defense attorneys –– still looks the part of the life that led him astray. Clean-shaven and and professional-looking, he favors trim suits and trendy Travis Mathew apparel on the golf course. He’d look equally at home behind a desk inside a Wall Street hedge fund or a corporate law firm, his confident demeanor still infused with a hint of his former brashness.
Paperny said he’s already been hired by one person tied to the college admissions scandal and provided The Washington Post with an invoice showing a down payment of several thousand dollars. But, he said, multiple people charged in the scandal have reached out to him for advice and he suspects he may be hired by several of them.
New clients are drawn to him, he said, because he doesn’t make unrealistic promises or attempt to downplay the difficulty of their situation. He maintains the criminal justice system incarcerates far too many people, wasting tax-payer dollars and ruining lives out of habit. At the same time, he embraces his own troubled past like other people embrace college, calling prison 'a growth opportunity” and 'one of the best experiences” of his life. It’s a message he’s even delivered to the FBI Academy in Quantico, Va.
Paperny said his fee –– which could reach tens of thousands for his latest client –– is high, in part, because he’s one of the few people who can speak to upper-crust criminals in a language they understand. The first step, he said, is often breaking through the denial that afflicts privileged first time offenders. To aid them in this process, Paperny asks some clients to film YouTube videos where they recount their illegal behavior, such as one he filmed with Jonathan Schwartz, a former business manager who was sentenced to six years in prison for embezzling millions from singer Alanis Morissette.
The quicker Paperny can get a client to accept responsibility, the better his chance of helping them reduce a possible sentence later on. What they desperately want to avoid, he said, is a situation like Paul Manafort faced last month when a judge questioned his seeming lack of regret.
How would he reach a privileged parent caught in an admissions scandal?
'I would tell them that I empathize with them, that I have no doubt that they probably had good intentions and that it’s clear they didn’t think about the consequences of their conduct and instead of making matters worse, they can take ownership of their situation and start to improve things,” Paperny said.
'For some it’s brutal to hear that,” he added. 'They don’t consider themselves criminals, but fathers and mothers and members of the community who have contributed things to society.”
[Before Lori Loughlin’s alleged cheating scandal, daughter Olivia Jade made her life at USC a YouTube brand]"""

ap = ArticleParser()
print(ap.getEntitiesToJSON(text))
