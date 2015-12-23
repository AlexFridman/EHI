__author__ = 'AlexF'

from collections import Counter

from project.WordCount import WordCount


class SentenceMaker(object):
    @staticmethod
    def make_sentence(text: str):
        text = text.lower()
        words = SentenceMaker.get_common_words(text)
        return SentenceMaker.construct_sentence(words)

    @staticmethod
    def get_common_words(text: str, word_count: int = 10):
        words = WordCount.regexp_tokenize(text)
        word_counts = WordCount.calc_count_of_words(words)
        return [pair[0] for pair in word_counts.most_common(word_count)]

    @staticmethod
    def construct_sentence(words: list):
        words[0] = words[0].capitalize()
        return str.join(' ', words) + '.'
