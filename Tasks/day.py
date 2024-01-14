# Get day number

D = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

def _parse_day_(s):
    i = None
    for i in range(len(D)):
        if s.startswith(D[i].lower()):
            return i + 1
    return -1

def run(*args):
    return _parse_day_(*args)
