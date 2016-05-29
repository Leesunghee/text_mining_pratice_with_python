#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
firefox_naver.py

파이어폭스 브라우저를 스크립트로 조종하여 네이버 서비스를 이용한다
"""

import getpass
import time
import splinter

HOME_URL = "http://www.naver.com"
LOGIN_URL = "https://nid.naver.com/nidlogin.login"
LOGOUT_URL = "http://nid.naver.com/nidlogin.logout?returl=http://www.naver.com"
LONG_SLEEP = 4
SHORT_SLEEP = 2
ID_CSS = "input#id.int"
PW_CSS = "input#pw.int"
LOGIN_BTN_CSS = "input.int_jogin"
QUERY_CSS = "input#query.input_text"
SEARCH_BTN_CSS = "button#search_btn.sch_smit"
LOGOUT_BTN_CSS = "span.btn_inr"

def get_naver_user_id_pw():
    """
    네이버 사용자 ID와 암호를 입력받아 돌려준다
    """

    user_id = input("Enter Naver user ID: ")
    user_pw = getpass.getpass("Enter Naver user password: ")

    return user_id, user_pw

def login(browser, user_id, user_pw):
    """
    네이버에 로그인한다
    """

    browser.visit(LOGIN_URL)
    pause(long=True)

    id_elem = browser.find_by_css(ID_CSS)
    id_elem.fill(user_id)
    pause()

    pw_elem = browser.find_by_css(PW_CSS)
    pw_elem.fill(user_pw)
    pause()

    btn_elem = browser.find_by_css(LOGIN_BTN_CSS)
    btn_elem.click()
    pause()

def search(browser, query):
    """
    검색어를 입려하여 검색을 실행한다
    """

    pause()
    search_elem = browser.find_by_css(QUERY_CSS)
    search_elem.fill(query)
    pause()

    btn_elem = browser.find_by_css(SEARCH_BTN_CSS)
    btn_elem.click()
    pause()

def print_html(browser):
    """
    현재 페이지의 HTML을 표시한다
    """

    print(browser.html)


def logout(browser):
    """
    네이버에서 로그아웃한다
    """

    browser.visit(HOME_URL)
    pause()
    browser.visit(LOGOUT_URL)
    pause()

def pause(long=False):
    """
    짧게 혹은 길게 쉰다
    """

    if long:
        time.sleep(LONG_SLEEP)
    else:
        time.sleep(SHORT_SLEEP)

def main():
    """
    파이어폭스 브라우저를 스크립트로 조정하여 네이버 서비스를 이용한다
    """

    user_id, user_pw = get_naver_user_id_pw()
    browser = splinter.Browser("firefox")

    login(browser, user_id, user_pw)
    search(browser, u"패스트캠퍼스")
    print_html(browser)
    logout(browser)

    browser.quit()

main()