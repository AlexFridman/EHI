from unittest import TestCase
from itertools import chain
from LabWork1.code.text_summarizer import summarize_text


class SummarizeTextTests(TestCase):
    def test_base_case(self):
        text = ' '.join(chain(['a'] * 5, ['b'] * 5, ['c'] * 5, ['d'] * 2, ['e'] * 2))
        self.assertEqual('A b c.', summarize_text(text, n_common_words=3))
