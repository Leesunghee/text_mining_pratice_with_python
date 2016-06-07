#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
sentence_split.py

문장 분리를 실험한다.
"""

def split_sentences(text):
    """
    입력 문자열을 문자들의 리스트로 만들어 돌려준다
    """

    new_text= \
        text.replace(". ", ".\n").replace("? ", "?\n").replace("! ", "!\n")
    sentences = new_text.splitlines()

    return sentences

def main():
    """ 문장 분리를 실험한다."""

    file_name = input("Enter input file name: ")

    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            sentences = split_sentences(line)
            for sentence in sentences:
                print(sentence)
                print("=" * 50)


main()