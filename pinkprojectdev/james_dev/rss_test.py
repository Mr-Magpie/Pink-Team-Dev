from .Article import Article

__author__ = 'James'

import feedparser

class RssGrabber:

    def __init__(self, url):
        self.url = url
        f = feedparser.parse(url)

        self.etag = None

        feed = f.feed

        print(f.url)

        if f.has_key('etag'):
            self.etag = f.etag
        else:
            print('No E-Tag')

    def grab(self):
        articles = []
        feed = feedparser.parse(self.url)
        if feed.status == 304:
            print(feed.debug_message)
        else:
            for entry in feed.entries:
                print(entry.updated)
                a = Article(entry.title, entry.link)
                articles.append(a)

        return articles
