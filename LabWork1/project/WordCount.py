__author__ = 'AlexF'

from nltk.tokenize import regexp_tokenize as nltk_reg_tokenize
from collections import Counter


class WordCount(object):
    @staticmethod
    def whitespace_tokenize(text: str):
        return text.split(' ')

    @staticmethod
    def regexp_tokenize(text: str):
        return nltk_reg_tokenize(text, "[\w']+")

    @staticmethod
    def calc_count_of_words(words: list):
        return Counter(words)

    @staticmethod
    def proceed_text(text: str):
        text = text.lower()
        words = WordCount.regexp_tokenize(text)
        print(words)
        return WordCount.calc_count_of_words(words)
