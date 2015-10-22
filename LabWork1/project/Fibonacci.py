__author__ = 'AlexF'


def fib_gen():
    cur = 0
    next_ = 1
    while True:
        yield cur
        cur, next_ = next_, cur + next_
