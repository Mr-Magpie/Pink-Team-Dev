import time

__author__ = 'dell'

import tweepy
import string
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
# import json
import re
import nltk
from nltk import FreqDist
from nltk.corpus import stopwords

# consumer_key="5DaANePrql7bnb3EePdtv6tkB"
# consumer_secret="BDVkjdR2P3wLc28KHc6dEQ8WBfDmDnUtsPupKrG9KstcwsmpfR"
# access_key="3314930867-mgpMtpZNGovv2GWelVzXQl9OQroqaGfaXIsJKOA"
# access_secret="yzbfaoN4xp2N7WqzH2hdkDpQuzvawW0NCTOfDpz5575CG"

consumer_key = 'IRYDOWvyaPmcIVs5Gx5rYOsXf'
consumer_secret =  '7SiJhHulZ5006Js5HuZR8vkgC4YwgL1pk1biCMzhFyXBfnfNDP'
access_key='469948431-ifaCgUUxEnhNdduoBLZWGKZ5h2HsvxRFAO4QhIip'
access_secret='wrXMzd70ghc69GrsPyLCCOmqB5oxDJyuwqpFOIYnsi7wV'

def get_top_followings(screen_name):
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	# for member in tweepy.Cursor(api.list_members, 'xiaoyao_lee', 'music').items():
	# 	print (member.screen_name)

	#initialize a list to hold all the tweepy Tweets
	alltweets = []

	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)

	#get the user object
	# user = api.get_user(screen_name = 'xiaoyao_lee')

	#save most recent tweets
	alltweets.extend(new_tweets)

	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1

	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print ("getting tweets before %s" % (oldest))

		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

		#save most recent tweets
		alltweets.extend(new_tweets)

		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1

		print ("...%s tweets downloaded so far" % (len(alltweets)))
		# if (len(alltweets) >400 ):
		# 	break

	texts = []
	# texts = [tweet.text.encode('utf-8') for tweet in alltweets]

	for tweet in alltweets:
		texts.append(tweet.text.encode('utf-8'))

	follows = []
	the_sample = []

	print(texts)
	for s in texts:
		the_sample.append(nltk.word_tokenize(str(s).lower()))
	print(the_sample)

	# get the users that this user has RT@.
	for a in the_sample:
		index = 0
		for w in a:
			if (w == "b'rt" or w == 'rt') and a[index + 1] == '@':
				follows.append(a[index + 2])
				# print (a[index + 2])
			index += 1

	the_follows_dist = FreqDist(follows)
	print (follow_description(api, the_follows_dist, screen_name))

	# for i in the_follows_dist.most_common(10):
	 	# print ('{}{}{}'.format(i[0], ': ', i[1]))

	# numWords = 0
	# wordLimit = 20
	# for w in the_follows_dist.keys():
	# 	print ('{}{}{}'.format(w, ': ', the_follows_dist[w]))
	# 	numWords += 1
	# 	if numWords > wordLimit:
	# 		break


	# the_follows_dist.plot(20)

	# the_sample = [w for w in the_sample if not (re.match(r'^\W+$|^[x]|^[b?]|^[rt]|^http|^co|^\d|^\w+\d$|^amp|^\w{1,2}\w$|^\w{1}$', w) != None)]
    #
	# the_sample = [w for w in the_sample if not w in nltk.corpus.stopwords.words('english_own')]
    #
	# the_sample = [w for w in the_sample if not w in follows]


	# print ('{}{}'.format('Lexical diversity: ', lexical_diversity(the_sample)))

	# the_sample_dist = FreqDist(the_sample)
	# # print (the_sample_dist)
    # #
	# # # print (the_sample_dist['blood'])
	# numWords = 0
	# wordLimit = 20
	# key_word = []
    #
	# for w in the_sample_dist.keys():
	# 	# if the_sample_dist[w] > 20:
	# 	print ('{}{}{}'.format(w, ': ', the_sample_dist[w]))
	# 	if the_sample_dist[w] > 5:
	# 		key_word.append(w)
	# 		numWords += 1
	# 	if numWords > wordLimit:
	# 		break
	# the_sample_dist.plot(30)

	# nltk.classify.NaiveBayesClassifier.train()
	# write the frequent word for the certain user
	# with open('%s_keyword.txt' % screen_name, 'w') as f:
	# 	f.write('Name: ' + user.name + '\n')
	# 	f.write("Screen name: " + user.screen_name + 'n')
	# 	for w in key_word:
	# 		f.write(w + '\n')
	# pass

def follow_description(api, fre_list, screen_name):
	all_tags = []
	print ('here')
	for i in fre_list.most_common(20):
		print ('{}{}{}'.format(i[0], ': ', i[1]))
		user = api.get_user(screen_name = i[0])
		try:
			for list_obj in user.lists_memberships(screen_name = i[0], count = 100):
				# try:
				# 	print (list_obj.name.encode('gbk', 'ingore').decode())
				# except:
				# 	continue
				for w in list_obj.name.lower().split(" "):
				# all_tags.append(list_obj.name.split(','))
				# 	print (str(w))
					all_tags.append(w)
		except tweepy.TweepError as e:
			if e.args[0][-3:] == '429':
				break

	the_list_name = []
	the_list_name = all_tags
	# for s in all_tags:
	# 	the_list_name.append(nltk.word_tokenize(str(s)))
	# print (the_list_name)
	stop_words = load_stopwords()
	the_list_name = [w for w in the_list_name if not (re.match(r'^\W+$|^[x]|^[b?]|^[rt]|^http|^co|^\d|^\w+\d$|^amp|^\w{1,2}\w$|^\w{1}$', w) != None)]
	# the_list_name = [w for w in the_list_name if not w in nltk.corpus.stopwords.words('english_own')]
	the_list_name = [w for w in the_list_name if not w in stop_words]
	the_list_name = [w.strip("['").strip("']").strip() for w in the_list_name]
	the_list_dist = FreqDist(the_list_name)
	for w in the_list_dist:
		print ('***' + str(w))
	return (the_list_dist)
	# the_list_dist.plot(30)

def lexical_diversity(text):
	return len(set(text)) / len(text)

def load_stopwords():
	stop_words = nltk.corpus.stopwords.words('english')
	stop_words.extend(['this','that','the','might','have','been','from',' ',
                'but','they','will','has','having','had','how','went'
                'were','why','and','still','his','her','was','its','per','cent',
                'a','able','about','across','after','all','almost','also','am','among',
                'an','and','any','are','as','at','be','because','been','but','by','can',
                'cannot','could','dear','did','do','does','either','else','ever','every',
                'for','from','get','got','had','has','have','he','her','hers','him','his',
                'how','however','i','if','in','into','is','it','its','just','least','let',
                'like','likely','may','me','might','most','must','my','neither','nor',
                'not','of','off','often','on','only','or','other','our','own','rather','said',
                'say','says','she','should','since','so','some','than','that','the','their',
                'them','then','there','these','they','this','tis','to','too','twas','us',
                'wants','was','we','were','what','when','where','which','while','who',
                'whom','why','will','with','would','yet','you','your','ve','re','rt', 'retweet', '#fuckem', '#fuck',
                'fuck', 'ya', 'yall', 'yay', 'youre', 'youve', 'ass','factbox', 'com', '&lt', 'th',
                'retweeting', 'dick', 'fuckin', 'shit', 'via', 'fucking', 'shocker', 'wtf', 'hey', 'ooh', 'rt&amp', '&amp',
                '#retweet', 'retweet', 'goooooooooo', 'hellooo', 'gooo', 'fucks', 'fucka', 'bitch', 'wey', 'sooo', 'helloooooo', 'lol', 'smfh'])
	return stop_words

if __name__ == '__main__':
	print ('start')
	#pass in the username of the account you want to download
	get_top_followings('jdunne33')


