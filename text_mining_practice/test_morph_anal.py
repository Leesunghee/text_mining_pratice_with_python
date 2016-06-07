#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

""" 형태소 분석기를  실험한다"""
import pprint
import konlpy.tag

komoran = konlpy.tag.Komoran()

while True:
    text = input(u"분석할 텍스트를 입력하세요: ")

    if not text.strip():
        break

    pprint.pprint(komoran.pos(text))
    print()
