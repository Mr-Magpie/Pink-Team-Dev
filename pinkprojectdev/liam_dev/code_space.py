import gensim
from sympy.galgebra.ncutil import numpy_matrix

__author__ = 'liamcreagh'


from gensim import corpora, models, similarities
from collections import defaultdict
from pprint import pprint   # pretty-printer


# http://www.reuters.com/article/2015/07/05/us-japan-economy-capex-idUSKCN0PF00R20150705
# http://www.reuters.com/article/2015/07/06/us-samsung-elec-results-idUSKCN0PG05L20150706
# http://www.reuters.com/article/2015/07/06/us-lg-display-oled-idUSKCN0PG00I20150706
# http://www.reuters.com/article/2015/07/03/us-france-uber-idUSKCN0PD0Y320150703
# http://www.reuters.com/article/2015/06/30/us-france-uber-idUSKCN0PA18Y20150630


documents = ["Factory worker Satomi Iwata has new co-workers, a troupe of humanoid automata that are helping to address two of Japan's most pressing concerns - a shortage of labor and a need for growth. The 19 robots, which cost her employer Glory Ltd (6457.T) about 7.4 million yen ($60,000) each, have eye-like sensors and two arms that assemble made-to-order change dispensers alongside their human colleagues in a factory employing 370. They aren't human, but it's as if I'm working with colleagues who do their work very well, said Iwata, who has worked at the factory for four years. Glory is in the vanguard as Japanese firms ramp up spending on robotics and automation, responding at last to premier Shinzo Abe's efforts to stimulate the economy and end two decades of stagnation and deflation. Cowed by weak demand in a country of aging consumers, risk-averse companies had largely turned their noses up at ultra-low borrowing costs delivered by years of loose money policies from the Bank of Japan, but times appear to be changing. Capital expenditure rose 11 percent in January-March from the previous quarter. If that pace is sustained, it would exceed Abe's target of 70 trillion yen this year for the first time since the collapse of Lehman Brothers in 2008. A BOJ survey on Wednesday showed that big companies plan to boost capital expenditure at the fastest pace in a decade in the current fiscal year. Were seeing companies spend more to enhance their plants productivity or renovate equipment, said Ko Nakayama, head of the BOJ's economic statistics division. Companies who make the automation equipment are already gearing up for the extra business.",
            "Doubts over the sales prospects of Samsung Electronics Co Ltd's new flagship smartphones are damping expectations of a rapid turnaround for the South Korean giant, even though profit likely continues to recover from last year's troughs. After peaking in mid-March as favorable reviews for the new Galaxy S6 models boosted earnings hopes, the company's stock price has languished and was down nearly 6 percent for the year as of mid-day trade on Monday. Supply shortages for the curved-screen S6 edge and economic headwinds in Europe and China have lowered expectations. After the first-quarter results the consensus for second-quarter earnings was somewhere in the high 7 trillion won ($6.22 billion), but now I think so long as the first digit doesn't start with a six it won't be a shock, HDC Asset Management fund manager Park Jung-hoon said. The average forecast from a Thomson Reuters I/B/E/S survey of 39 analysts tips April-June operating profit at 7.2 trillion won, the same as a year earlier and up from 6 trillion won in January-March. Of those surveyed, 20 have cut their forecasts in the past 30 days by an average of 3.9 percent. Samsung is expected to guide its second-quarter revenue and profit on Tuesday, with full results to follow at end-July. To be sure, analysts say the trend of gradual earnings recovery remains intact. The Thomson Reuters I/B/E/S survey tips 2015 profit to recover to 27.8 trillion won from the three-year low of 25 trillion won in 2014. Third and fourth-quarter profits this year are expected at 7.3 trillion won and 7.5 trillion won, respectively, posting significant gains in annual terms. Samsung expects the new phones to be their best-selling devices to date. Data from researcher Counterpoint released in June showed that Samsung sold 6 million S6 smartphones from the April 10 launch to the end of the month, outpacing the previous S5 model in the same time frame. But analysts say Samsung's failure to anticipate demand for the S6 edge led to a missed opportunity. Though the firm says it now has enough capacity to meet demand for the curved-screen model, its flagship phones will soon need to compete with new Apple Inc iPhones that analysts expect will launch as early as September. As the smartphone market matures, the period of time that consumer demand for a high-end product lasts looks to have gotten shorter, KTB Investment analyst Jin Sung-hye said in a report, cutting her 2015 Galaxy S6 shipments forecast to 45 million from 49 million previously.",
           "South Korea's LG Display Co Ltd plans to invest up to 900 billion won ($802.75 million) to build a new production line for small- and medium-sized organic light emitting diode (OLED) displays, the DongA Ilbo newspaper reported on Monday. The plant will produce flexible OLED panels used for smartphones and wearable products and will be built in South Korea, the paper reported. The display panel maker, which supplies screens to Apple Inc and sister company LG Electronics Inc, has been considering whether to build a new production line for the flexible OLED panels or convert existing capacity. The South Korean stock exchange separately on Monday asked the company to comment by 0900 GMT on whether it planned to build a new OLED production plant. A spokeswoman for LG Display declined to comment.",
             "Uber Technologies will suspend its UberPOP ride-hailing service in France, the U.S. company said on Friday, after it faced sometimes-violent protests and local authorities denounced it as an illegal taxi service. After fierce protests last week by licensed French taxi drivers who argue it threatens their livelihood with unfair competition, France took two executives from California-based Uber into custody and said they will face trial in September. France's legal clampdown was the latest setback for Uber in Europe. An Italian court in May banned unlicensed car-sharing services, two months after a German court issued a similar ban and imposed stiff fines for violations of local transport laws. We have decided to suspend UberPOP in France from 1800 GMT (1400 EDT) this Friday evening, primarily to assure the safety of Uber drivers, Uber France head Thibaud Simphal told Le Monde daily, adding that some drivers had been targets of violence. The second reason is that we want to create a spirit of reconciliation and dialogue with public authorities to show we are acting responsibly, he said. Prime Minister Manuel Valls welcomed the decision but said France's licensed taxis needed to improve the quality of their service, often criticized by locals and foreign visitors. Taxis need to reform too, to contribute to our country's attractiveness, he told reporters at an event in east France. In a June 25 protest in numerous French cities, cabbies blocked roads to the capital's airports, overturned cars and burned tires to press for the scheme to be abolished. Police said 70 cars were damaged and seven police officials injured in the protests. Ten people were arrested. SIDELINE INCOME The protests were among the fiercest in a series of demonstrations across Europe against Uber, whose backers include investment bank Goldman Sachs (GS.N) and technology giant Google (GOOGL.O). It is valued in excess of $40 billion. Born out of the frustration of two Silicon Valley entrepreneurs trying to catch a cab in Paris, Uber's services have mushroomed since being launched in 2010 and are offered in nearly 270 cities worldwide. Taxi drivers in France pay income tax and welfare charges and, depending on their location, sometimes have to pay hundreds of thousands of euros for an operating license. They argue they face unfair competition from unlicensed drivers who have no such costs and so can undercut them on price. A final ruling on UberPOP's legality in France is due around September. For its part, Uber argues it is offering a much-needed service that complements licensed taxis and is offering a sideline income for some 10,000 people in France. We understand that new technologies can be destabilizing, particularly for established companies and their employees ... But it is unacceptable to see violence come to the fore, it is up to us to better explain what we are doing and the advantages of the Uber platform, Uber France said in a statement. Didier Hogrel, president of France's national taxi federation, told BFMTV he was ready to discuss ways to promote parallel services such as licensed chauffeur-driven limousines, which currently face heavy restrictions in France. But of on-line apps like UberPOP he said: We won't be happy until all these illegal applications are banned. (Additional reporting by Sophie Louet in Paris; editing by Dominique Vidalon, Larry King)",
            "Two executives from California-based Uber will face trial in France on Sept. 30, the Paris public prosecutor said on Tuesday, part of a French crackdown on what the government calls an illegal taxi service. Thibaud Simphal, manager of Uber France, and Pierre-Dimitri Gore-Coty, general manager for western Europe, were detained by police on Monday in an investigation that earlier led to Uber's offices being raided by police in March. The investigation focuses on one of the company's local transport options known as UberPOP, which allows passengers to book rides with private drivers via mobile phones, a service which licensed taxi operators say is unfair competition. A French law from October 2014 already placed a ban on putting clients in touch with unregistered drivers with apps such as UberPOP. But Uber has contested the rule, saying it is counter to the right to freedom to do business. The Uber executives will be judged on charges including carrying out deceitful commercial practices and being complicit in illegal operation of a taxi service by providing drivers with means to do so and encouraging them to, Paris prosecutor Francois Molins said in a statement. Charges also include keeping and using personal data without authorization by France's data privacy watchdog. Uber said in a statement later on Tuesday that it wanted to continue constructive talks with the government on transport regulations and that it hoped France's Constitutional Council would give its view on the 2014 law by the end of September. It did not comment on the trial. Uber has triggered protests by taxi drivers from London to New Delhi as it upends traditional business models that require professional drivers to pay often steep fees for licenses to operate cabs. The various regulatory battles could affect the valuation of the unlisted company, currently above $40 billion based on its most recent fund raisings. In France, the backlash intensified last week when taxi drivers blockaded major transport hubs in a sometimes violent protest against what they say is unfair competition. The protests were among the fiercest in a series of strikes and demonstrations across Europe against San Francisco-based Uber, whose backers include Goldman Sachs and Google.",
        ]




# print("\n\n\n <-----------Focus Print---------->\n\n\n")
# print(tfidf[vec])
# print("\n\n\n <-----------Focus Print---------->\n\n\n")
#
# index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=12)
# sims = index[tfidf[vec]]
# print(list(enumerate(sims)))



#
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#
#
#
#Declares and removes stop words
stoplist = set('for a of the and to in abc has that are two her have they but as if we do their said at is as up on by he be what an were with which say it will so them or who from had been'.split())

texts = [[word for word in document.lower().split() if word not in stoplist]
        for document in documents]

# print(texts)
#tokanises document - seperates words by a divider (space)
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:

        frequency[token] += 1

#removes words only appearing once
texts = [[token for token in text if frequency[token] > 1]
         for text in texts]
#
pprint(texts)



dictionary = corpora.Dictionary(texts)
dictionary.save('/tmp/deerwester.dict') # store the dictionary, for future reference

print(dictionary)

print("\n\n\n\n\n\n Dictionary \n\n\n\n\n\n\n")

print(dictionary.token2id)

print("\n\n\n\n\n\n Dictionary \n\n\n\n\n\n\n")


corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('/tmp/deerwester.mm', corpus) # store to disk, for later use
# print(corpus)

# http://www.reuters.com/article/2015/07/01/uber-brazil-idUSL1N0ZH0KM20150701


new_doc = "The city council of Sao Paulo, South America's largest metropolis, voted to ban the U.S-based Uber ride-sharing service late Tuesday, the latest setback for the company after several countries took similar steps in recent months. City lawmakers decided 48-1 in favor of banning application-based private car services such as Uber in a preliminary vote. The bill requires a second vote and the signature of Mayor Fernando Haddad in order to be enacted. The mayor has not indicated whether he would sign the bill into law. Uber defends the right of users to choose the way in which they move about the city, the company said in a statement posted on Facebook after the vote, adding that the service continues to operate normally in Sao Paulo, a city of 11 million people. The company said more than 200,000 emails had been sent to city council members by users urging them to vote against a ban. Sao Paulo's white taxis swarmed the street in front of the municipal legislature on Tuesday and drivers filled the chamber's galleries. Uber has triggered protests by taxi drivers from London to New Delhi as it upends traditional business models that require professional drivers to pay often steep fees for licences to operate cabs. In early May a Brazilian judge struck down an injunction calling for Uber's suspension throughout the country."
new_vec = dictionary.doc2bow(new_doc.lower().split())



print(new_vec) # the word "interaction" does not appear in the dictionary and is ignored


print("\n\n\n <-----------Focus Print---------->\n\n\n")
print(new_vec)
print("\n\n\n <-----------Focus Print---------->\n\n\n")


corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('/tmp/deerwester.mm', corpus) # store to disk, for later use

# prints corpus dictionary squqentually and word accourance



print(corpus)

class MyCorpus(object):
 def __iter__(self):
     for line in open('mycorpus.txt'):
         # assume there's one document per line, tokens separated by whitespace
         yield dictionary.doc2bow(line.lower().split())

# corpus = gensim.matutils.Dense2Corpus(numpy_matrix)
# numpy_matrix = gensim.matutils.corpus2dense(corpus, num_terms=179)

