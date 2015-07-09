__author__ = 'James'
import newspaper
from newspaper import Config, news_pool

config = Config()
config.set_language('en')
config.memoize_articles = False


reuters = newspaper.build(url='http://www.reuters.com', config=config)
indo = newspaper.build(url='http://www.independent.ie', config=config)

papers = [reuters, indo]

news_pool.set(paper_list=papers, threads_per_source=3)
news_pool.join()

for paper in papers:
    print(paper.brand + ": " + str(paper.size()) + " article(s)")
    # for article in paper.articles:
    #     print(article.title)

# print("-----------\nCATEGORIES\n-----------")
#
# for category in a.categories:
#     print(category.url)
#     b = newspaper.Source(url=category.url)
#     b.build()
#     print("\t-----------\n\tFEEDS\t\n-----------\t")
#     for feed_url in b.feed_urls():
#         print("\t->" + feed_url)


