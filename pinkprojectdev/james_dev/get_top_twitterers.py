from requests import HTTPError

__author__ = 'James'

from urllib import request
from bs4 import BeautifulSoup


all_names = []

f = open('top10000twitter', 'w')

for j in range(100, 1000, 100):
    url = "http://twittercounter.com/pages/100/" + str(j)

    print(url)
    try:
        doc = request.urlopen(url=url)
    except HTTPError as err:
        print(err.request.full_url)

    b = BeautifulSoup(doc)

    for i in range(1, 101):
        uname = b.find('li', {'data-pos': i+j}).find('a', {'class', 'uname'}).text
        all_names.append(uname[1:])
        # print(uname[1:])



for item in all_names:
    f.write("%s\n" % item)
