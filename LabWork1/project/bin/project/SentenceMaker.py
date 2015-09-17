__author__ = 'AlexF'

from project.bin.project.WordCount import WordCount
from collections import Counter

class SentenceMaker(object):
    @staticmethod
    def make_sentence(text: str):
        words = WordCount.regexp_text_split(text)
        counts = WordCount.calc_count_of_words(words)
        sentence = SentenceMaker.construct_sentence(counts)
        SentenceMaker.pretty_output(sentence)

    @staticmethod
    def construct_sentence(counts: Counter, word_count: int = 10):
        words = [pair[0] for pair in counts.most_common(word_count)]
        words[0] = words[0].capitalize()
        return str.join(' ', words) + '.'

    @staticmethod
    def pretty_output(sentence: str):
        print(str)

