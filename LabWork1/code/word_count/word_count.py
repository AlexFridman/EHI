from collections import Counter
from typing import AnyStr, Callable, Iterable


def _tokenize(data: AnyStr) -> list:
    """Splits textual data on gaps
    :param data: textual data
    :type data: str
    :return: list of tokens
    :rtype: list
    """
    return data.split(' ')


def word_count(data: AnyStr, tokenizer: Callable[[AnyStr], Iterable] = None) -> Counter:
    """Counts frequencies of tokens
    :param data: textual data
    :type data: str
    :param tokenizer: tokenizer
    :type tokenizer: callable
    :return: dict of tokens frequencies of tokens
    :rtype: Counter
    """
    tokenizer = tokenizer or _tokenize
    tokens = tokenizer(data)
    return Counter(tokens)
