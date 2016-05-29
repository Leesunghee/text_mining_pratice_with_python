#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
collect_tweets_by_streaming.py

트위터 스트리밍 API(https://dev.twitter.com/streaming/overview)를 이용하여 트윗을 수집한다
"""

from twython import TwythonStreamer
import ujson

CONSUMER_KEY = "YOUR_CONSUMER_KEY"
CONSUMER_SECRET = "YOUR_CONSUMER_SECRET"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR_ACCESS_TOKEN_SECRET"

class MySteamer(TwythonStreamer):
    """Twitter streamer class."""

    def on_success(self, data):
        """스트리밍이 성고앴을 때"""

        print(ujson.dumps(data, ensure_ascii=False))

    def on_error(self, status_code, data):
        """스트리밍 오류가 발생했을 때"""

        print(status_code)

streamer = MySteamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

streamer.statuses.filter(track=u"트와이스,레블리즈,에이오에이")