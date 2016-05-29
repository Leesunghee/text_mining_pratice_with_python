#!/usr/bin/evn python3
# _*_ coding: utf-8 _*_

"""
extract_nate_news_articles.py

네이느 뉴스 기사 HTML에서 순수 텍스트 기사를 추출한다
"""

import bs4

ARTICLE_DELIMITER = "@@@@ ARTICLE DELIMITER @@@@@\n"
TITLE_START_PAT = "<strong>"
TITLE_END_PAT = "</strong>"
DATE_TIME_START_PAT = u"기사 전송 <em>"
DATE_TIME_END_PAT = "</em></span>"
BODY_START_PAT = u"<!-- 기사 내용 -->"
BODY_END_PAT = u"<!-- //팝업 : 동영상 뉴스 - 뉴스내용 -->"
TIDYUP_START_PAT = "//<![CDATA["

def get_html_file_name():
    """
    사용자로부터 HTML 파일 이름을 입력받아 돌려준다
    """

    html_file_name = input("Enter HTML file name: ")
    return html_file_name

def get_text_file_name():
    """
    사용자로부터 텍슽 파일 이름을 입력받아 돌려준다
    """

    text_file_name = input("Enter text file name: ")
    return text_file_name

def open_html_file(html_file_name):
    """
    HTML 기사 파일을 열어서 파일 객체를 돌려준다
    """

    html_file = open(html_file_name, "r", encoding="utf-8")
    return html_file

def create_text_file(text_file_name):
    """
    텍스트 기사 파일을 만들어 파일 객체를 돌려준다
    """

    text_file = open(text_file_name, "w", encoding="utf-8")
    return text_file

def read_html_article(html_file):
    """
    HTML 파일에서 기사 하나를 읽어서 돌려준다
    """

    lines = []

    for line in html_file:
        if line.startswith(ARTICLE_DELIMITER):
            html_text = "".join(lines).strip()
            return html_text

        lines.append(line)

    return None

def ext_title(html_text):
    """
    HTML 기사에서 제목을 추출하여 돌려준다
    """

    p = html_text.find(TITLE_START_PAT)
    q = html_text.find(TITLE_END_PAT)
    title = html_text[p + len(TITLE_START_PAT):q]
    title = title.strip()

    return title

def ext_date_time(html_text):
    """
    HTML 기사에서 날짜와 시간을 추출하여 돌려준다
    """

    p = html_text.find(DATE_TIME_START_PAT)
    q = html_text.find(DATE_TIME_END_PAT)
    date_time = html_text[p + len(DATE_TIME_START_PAT):q]
    date_time = date_time.strip()

    return date_time

def strip_html(html_body):
    """
    HTML 본문에서 HTML 태그를 제거하고 돌려준다
    """

    page = bs4.BeautifulSoup(html_body, "html.parser")
    body = page.text
    return body

def tidyup(body):
    """
    본문에서 필요없는 부분을 자르고 돌려준다
    """

    p = body.find(TIDYUP_START_PAT)
    body = body[:p]
    body = body.strip()

    return body

def ext_body(html_text):
    """
    HTML 기사에서 본문을 추출하여 돌려준다
    """

    p = html_text.find(BODY_START_PAT)
    q = html_text.find(BODY_END_PAT)
    html_body = html_text[p + len(BODY_START_PAT):q]
    html_body = html_body.replace("<br />", "\n")
    html_body = html_body.strip()
    body = strip_html(html_body)
    body = tidyup(body)

    return body

def write_article(text_file, title, date_time, body):
    """
    텍스트 파일에 항목이 구분된 기사를 출력한다
    """

    text_file.write("{}\n".format(title))
    text_file.write("{}\n".format(date_time))
    text_file.write("{}\n".format(body))
    text_file.write(ARTICLE_DELIMITER)


def main():
    """
    네이트 뉴스 기사 HTML에서 순수 텍스트 기사를 추출한다
    """

    html_file_name = get_html_file_name()
    text_file_name = get_text_file_name()
    html_file = open_html_file(html_file_name)
    text_file = create_text_file(text_file_name)

    while True:
        html_text = read_html_article(html_file)

        if not html_text:
            break;

        title = ext_title(html_text)
        date_time = ext_date_time(html_text)
        body = ext_body(html_text)
        write_article(text_file, title, date_time, body)

    html_file.close()
    text_file.close()

main()

