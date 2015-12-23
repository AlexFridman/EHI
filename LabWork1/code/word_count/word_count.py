from collections import Counter


def _tokenize(data: str) -> list:
    """Splits textual data on gaps
    :param data: textual data
    :type data: str
    :return: list of tokens
    :rtype: list
    """
    return data.split(' ')


def word_count(data: str, tokenizer=None) -> dict:
    """Counts frequencies of tokens
    :param data: textual data
    :type data: str
    :param tokenizer: tokenizer
    :type tokenizer: callable
    :return: dict of tokens frequencies of tokens
    :rtype: dict
    """
    tokenizer = tokenizer or _tokenize
    tokens = tokenizer(data)
    return Counter(tokens)
