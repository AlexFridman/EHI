from typing import AnyStr


def open_as_list_of_ints(path: AnyStr) -> list:
    try:
        with open(path, 'r+') as f:
            str_input = f.readline()
        ints = [int(item) for item in str_input.split(' ')]
    except:
        raise IOError()

    return ints


def open_as_text(path: str):
    try:
        with open(path, 'r+', encoding='utf8') as f:
            return f.read()
    except:
        raise IOError()


def print_list_of_ints(items: list):
    output = ' '.join(str(i) for i in items)
    print(output)


def print_word_count_result(counts: dict):
    print('stat:')
    for w, c in counts.items():
        print("{0:10}{1}".format(w, c))
