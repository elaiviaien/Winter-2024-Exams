# Filter array by type name


def filter(data, filter_type):
    return [value for value in data if type(value).__name__ == filter_type]


def run(*args):
    return filter(*args)
