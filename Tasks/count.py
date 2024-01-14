# Sum all number values in dict

def count(obj):
    sum = 0
    keys = list(obj.keys())
    for key in keys:
        value = obj[key]
        if isinstance(value, int):
            sum += value
    return sum


def run(*args):
    return count(*args)
