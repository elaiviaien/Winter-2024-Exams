# Get day number

D = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

def parse_day(s):
    i = None
    for i in range(len(D)):
        if s.startswith(D[i].lower()):
            return i + 1
    return -1

def run(*args):
    return parse_day(*args)
