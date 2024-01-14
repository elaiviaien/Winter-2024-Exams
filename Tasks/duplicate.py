# Return an array without duplicates


def duplicate(value, number):
    duplicates = []
    for i in range(number):
        duplicates.append(value)
    return duplicates


def run(*args):
    return duplicate(*args)