#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
collect_tweets_by_search.py

트위터 검색 API(https://dev.twitter.com/rest/public/search)를 이용하여 트윗을 수집한다
"""

from twython import Twython
import ujson

CONSUMER_KEY = "YOUR_CONSUMER_KEY"
CONSUMER_SECRET = "YOUR_CONSUMER_SECRET"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR_ACCESS_TOKEN_SECRET"

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

result = twitter.search(q=u"파이썬")

for status in result["statuses"]:
    print(ujson.dumps(status, ensure_ascii=False))