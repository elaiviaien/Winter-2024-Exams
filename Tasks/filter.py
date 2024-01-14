# Filter array by type name


def filter(data: list, filter_type: str) -> list:
    return [value for value in data if type(value).__name__ == filter_type]


def run(*args):
    return filter(*args)
