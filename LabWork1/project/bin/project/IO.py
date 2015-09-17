__author__ = 'AlexF'

def open_as_list_of_ints(path: str):
    strInput = None
    input = None
    try:
        with open(path, "r+") as f:
            strInput = f.readline()
        input = [int(item) for item in strInput.split(' ')]
    except:
        raise IOError

    return input


def open_as_text(path: str):
    input = None
    try:
        with open(path, "r+") as f:
            input = f.read().replace('\n', '')
    except:
        raise IOError

    return input
