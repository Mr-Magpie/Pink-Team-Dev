__author__ = 'James'

class Article:
    def __init__(self, title, url):
        self.title = title
        self.url = url
        self.content = []

    def to_string(self):
        return self.title + ", " + self.url + ", " + str(self.content)

