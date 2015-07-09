__author__ = 'James'


import praw

r = praw.Reddit("data-gathering crawler for topic modelling/news recommendation 1.0 by u/bumbershootle")

import numpy as np

# r.set_oauth_app_info(client_id="TXX0egh11XA4sg",
#                      client_secret="tjKyw0_TkHR0uLvDy0Ttb8GmHDY",
#                      redirect_uri='http://127.0.0.1:65010/authorize_callback')

user_name = "karmanaut"
user = r.get_redditor(user_name=user_name)

submitted = user.get_submitted()

karma_by_sub = {}

for thing in submitted:
    sub = thing.subreddit.display_name
    karma_by_sub[sub] = karma_by_sub.get(sub, 0) + thing.score


karma = list(karma_by_sub.values())
subs = list(karma_by_sub.keys())

print(karma)
print(subs)


