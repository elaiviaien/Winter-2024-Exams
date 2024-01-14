# Return an array without duplicates


def duplicate(value: str, number: int) -> list:
    return [value for _ in range(number)]


def run(*args):
    return duplicate(*args)
