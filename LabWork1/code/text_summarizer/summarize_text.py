from LabWork1.code.word_count import word_count
from nltk.tokenize import regexp_tokenize
from typing import AnyStr


def summarize_text(text: AnyStr, n_common_words: int = 10) -> str:
    """Returns a string was made of most common words of given text
    :param text: textual data
    :type text: str
    :param n_common_words: count of words to make sentence
    :return: summary of the text
    :rtype: str
    """

    def tokenizer(text): return regexp_tokenize(text, '[\w\']+')

    word_frequencies = word_count(text, tokenizer)
    common = [w for w, f in word_frequencies.most_common(n_common_words)]
    return ' '.join(common).capitalize() + '.'
