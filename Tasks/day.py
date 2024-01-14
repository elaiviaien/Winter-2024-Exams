# Get day number


def parse_day(s):
    D = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    for i, word in enumerate(D, start=1):
        if s.startswith(word.lower()):
            return i
    return -1


def run(*args):
    return parse_day(*args)
