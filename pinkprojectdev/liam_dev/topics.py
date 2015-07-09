__author__ = 'liamcreagh'



print('Poop')

print('File edited')

from gensim import corpora, models, similarities
dictionary = corpora.Dictionary.load('/tmp/deerwester.dict')
corpus = corpora.MmCorpus('/tmp/deerwester.mm')
print(corpus)

tfidf = models.TfidfModel(corpus) # step 1 -- initialize a model

doc_bow = [(0, 1), (165, 1)]
print(tfidf[doc_bow]) # step 2 -- use the model to transform vectors






corpus_tfidf = tfidf[corpus]
for doc in corpus_tfidf:
    print(doc)
