#!usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
collect_nate_news_articles.py

네이트 뉴스 기사를 수집한다
"""

import time
import requests

def get_url_file_name():
    """
    URL 파일 이름을 입력 받아 돌려준다
    """

    url_file_name = input("Enter url file name: ")
    return url_file_name

def get_output_file_name():
    """
    출력 파일 이름을 입력 받아 돌려준다
    """

    output_file_name = input("Enter output file name: ")
    return output_file_name

def open_url_file(url_file_name):
    """
    URL 파일을 연다
    """

    url_file = open(url_file_name, "r", encoding="utf-8")

    return url_file

def create_output_file(output_file_name):
    """
    출력 파일을 생성한다
    """

    output_file = open(output_file_name, "w", encoding="utf-8")
    return  output_file

def gen_print_url(url_line):
    """
    주어진 기사 링크 URL로부터 인쇄용 URL을 만들어 돌려준다
    """

    p = url_line.rfind("/")
    q = url_line.rfind("?")
    article_id = url_line[p + 1:q]
    print_url = "http://news.nate.com/view/print?aid=" + article_id

    return print_url

def get_html(print_url):
    """
    주어진 인쇄용 URL에 접근하여 HTML을 읽어서 돌려준다
    """

    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) " + \
                 "AppleWebKit/537.36 (KHTML, like Gecko) " + \
                 "Chrome/50.0.2661.102 Safari/537.36"

    headers = {"User-Agent": user_agent}

    response = requests.get(print_url, headers=headers)
    html = response.text

    return html

def write_html(output_file, html):
    """
    주어진 HTML 텍스트를 출력 파일에 쓴다
    """

    output_file.write("{}\n".format(html))
    output_file.write("@@@@ ARTICLE DELIMITER @@@@@\n")

def pause():
    """
    3초 동안 쉰다
    """

    time.sleep(3)

def close_output_file(output_file):
    """
    출력 파일을 닫는다
    """

    output_file.close()

def close_url_file(url_file):
    """
    URL 파일을 닫는다
    """

    url_file.close()

def main():
    """
    네이트 뉴스 기사를 수집한다
    """

    url_file_name = get_url_file_name()
    output_file_name = get_output_file_name()

    url_file = open_url_file(url_file_name)
    output_file = create_output_file(output_file_name)

    for line in url_file:
        print_url = gen_print_url(line)
        html = get_html(print_url)
        write_html(output_file, html)

    close_output_file(output_file)
    close_url_file(url_file)

main()
