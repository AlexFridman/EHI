from unittest import TestCase
from LabWork1.code.merge_sort import merge_sort

import numpy as np


class MargesortTests(TestCase):
    def test_returns_empty_list_when_input_is_empty(self):
        data = []
        self.assertSequenceEqual([], merge_sort(data))

    def test_base_case(self):
        data = list(np.random.randint(-10, high=10, size=10))
        self.assertSequenceEqual(sorted(data), merge_sort(data))
