from unittest import TestCase
from LabWork1.code.word_count import word_count


class WordCountTests(TestCase):
    def test_best_case(self):
        data = 'a a b b c'
        w_c = word_count(data)
        self.assertDictEqual({'a': 2, 'b': 2, 'c': 1}, w_c)

    def test_support_of_custom_tokenizer(self):
        data = 'a a b b c'

        def tokenizer(text: str) -> list: return text.split()

        w_c = word_count(data, tokenizer=tokenizer)
        self.assertDictEqual({'a': 2, 'b': 2, 'c': 1}, w_c)
