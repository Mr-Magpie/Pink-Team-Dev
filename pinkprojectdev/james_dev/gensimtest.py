import psycopg2
import time

__author__ = 'James'

import gensim, logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def get_ids():
    conn = psycopg2.connect("dbname=nlstudent user=James")
    query = "select article_id from article_rec;"
    cur = conn.cursor()

    cur.execute(query)

    return cur.fetchall()

def id2word():
    conn = psycopg2.connect("dbname=nlstudent user=James")
    query = "select word_id, word from word_rec;"
    cur = conn.cursor()

    cur.execute(query)

    return dict(cur.fetchall())


def get_article(article_id):

    conn = psycopg2.connect("dbname=nlstudent user=James")
    query = "select w.word_id, f.frequency from article_rec as a join word_frequency_rec as f on a.article_id = f.article_id join word_rec as w on f.word_id = w.word_id where a.article_id=%s and f.frequency > 1 order by frequency DESC;"

    cur = conn.cursor()

    cur.execute(query, (article_id,))

    return cur.fetchall()

class ArticleCorpus(object):

    def __iter__(self):
        for art_id in get_ids():
            rec = get_article(art_id)
            yield rec


start_time = time.localtime()
corpus = ArticleCorpus()
dictionary = gensim.corpora.Dictionary.from_corpus(corpus=[a for a in corpus], id2word=id2word())

tfidf = gensim.models.TfidfModel(corpus)

print(dictionary)
lda = gensim.models.lsimodel.LsiModel(corpus=tfidf[corpus], id2word=dictionary, num_topics=400)

# lda.save('/tmp/ldatest')
lda.show_topics()


