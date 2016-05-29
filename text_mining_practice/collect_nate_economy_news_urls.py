#!usr/bin/env python3
# _*_ coding: utf-8 *_

"""
collect_nate_economy_news_urls.py

네이트 경제 뉴스 기사 URL을 수집한다.
"""

import time
import re
import requests

def get_date():
    """
    수집 대상 날짜를 사용자로부터 키보드로 입력 받아 돌려준다
    """

    target_date = input("Enter date to crawl news aricle urls (YYYYMMDD): ")

    return target_date

def create_output_file(target_date):
    """
    출력 파일을 생성하고 파일 객체를 돌려준다.
    """

    output_file_name = "article_urls." + target_date + ".txt"
    output_file = open(output_file_name, "w", encoding="utf-8")

    return output_file

def get_html(target_date, page_num):
    """
    주어진 날짜와 페이지 번호에 해다하는 페이지 URL에 접근하여 HTML을 돌려준다
    """

    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) " + \
                 "AppleWebKit/537.36 (KHTML, like Gecko) " + \
                 "Chrome/50.0.2661.102 Safari/537.36"

    headers = {"User-Agent": user_agent}

    page_url = "http://news.nate.com/recent?cate=eco&mid=n301&type=t&" + \
        "date=" + target_date + "&page=" + str(page_num)

    response = requests.get(page_url, headers=headers)
    html = response.text

    return html

def paging_done(html):
    """
    페이징이 완료되었는지를 판단한다
    """
    done_pat = u"뉴스가 없습니다."

    if done_pat in html:
        return True
    return False

def ext_news_article_urls(html):
    """
    주어진 HTML에서 기사 URL을 추출하여 돌려준다
    """

    url_frags = re.findall('<a href="(.*?)"', html)
    news_article_urls = []

    for url_frag in url_frags:
        if not url_frag.startswith("/view/"):
            continue

        url = "http:///news.nate.com" + url_frag
        news_article_urls.append(url)

    return news_article_urls

def write_news_article_urls(output_file, urls):
    """
    기사 URL들을 출력 파이레 기록한다
    """

    for url in urls:
        print(url, file=output_file)

def pause():
    """
    2초 동안 쉰다
    """

    time.sleep(2)

def close_output_file(output_file):
    """
    출력 파일을 닫는다
    """

    output_file.close()

def main():
    """
    사용자로부터 수집 대사 날짜를 입력 받아 해다 날자의 네이트 경제 뉴스 기사 URL을 수집한다
    """

    target_date = get_date()
    output_file = create_output_file(target_date)
    page_num = 1

    while True:
        html = get_html(target_date, page_num)

        if paging_done(html):
            break

        urls = ext_news_article_urls(html)
        write_news_article_urls(output_file, urls)
        page_num += 1
        pause()

    close_output_file(output_file)

main()

