__author__ = 'AlexF'

from nltk.tokenize import regexp_tokenize
from collections import Counter


class WordCount(object):
    @staticmethod
    def simple_text_split(text: str):
        return text.split(' ')

    @staticmethod
    def regexp_text_split(text: str):
        return regexp_tokenize(text, "[\w']+")

    @staticmethod
    def calc_count_of_words(words: list):
        return Counter(words)

    @staticmethod
    def calculate(text: str):
        words = WordCount.simple_text_split(text)
        counts = WordCount.calc_count_of_words(words)
        WordCount.pretty_output(counts)

    @staticmethod
    def pretty_output(counts: Counter):
        print("stat:")
        for w, c in counts.items():
            print("{0}\t{1}".format(w, c))

    @staticmethod
    def make_sentence(counts: Counter, word_count: int = 10):
        words = [pair[0] for pair in counts.most_common(word_count)]
        words[0] = words[0].capitalize()
        sentence = str.join(' ', words) + '.'

        print(sentence)

