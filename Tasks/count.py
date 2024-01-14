# Sum all number values in dict

def count(obj: dict) -> int:
    values = list(obj.values())
    result_sum = sum(value for value in values if isinstance(value, int))
    return result_sum


def run(*args):
    return count(*args)
