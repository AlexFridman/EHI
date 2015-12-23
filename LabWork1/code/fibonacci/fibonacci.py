def fibonacci():
    """Generates Fibonacci numbers"""
    curr = 0
    next_ = 1
    while True:
        yield curr
        curr, next_ = next_, curr + next_
