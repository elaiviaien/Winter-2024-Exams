# Get day number


def parse_day(input_day):
    abbreviated_days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    for index, abbreviated_day in enumerate(abbreviated_days, start=1):
        if input_day.startswith(abbreviated_day.lower()):
            return index
    return -1


def run(*args):
    return parse_day(*args)
