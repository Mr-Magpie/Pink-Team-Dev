__author__ = 'James'

import re
import string
from urllib import request
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from .rss_test import RssGrabber


def aggregate():
    url_list = []
    article_list = []

    reuters_url = 'http://uk.reuters.com/tools/rss'

    doc = request.urlopen(reuters_url)

    soup = BeautifulSoup(doc)

    for s in soup.find_all('td', 'feedUrl'):
        m = re.search('(?<=//)(.*)', s.text)
        print("http://" + m.groups()[0])
        url_list.append("http://" + m.groups()[0])

    for u in url_list[:1]:
        d = RssGrabber(u)
        article_list = article_list + d.grab()

    for a in article_list:
        doc = request.urlopen(a.url)
        a_soup = BeautifulSoup(doc)

        words = []

        try:
            for s in a_soup.find('span', {'id': 'articleText'}).find_all('p'):
                words = words + s.text.split()
                stop = stopwords.words('english')
                content = [w.translate(string.punctuation).lower()
                             for w in words
                             if w.translate(string.punctuation).lower() not in stop]
            a.content = nltk.FreqDist(content).most_common(10)


        except AttributeError:
            print("malformed article")


    return article_list
