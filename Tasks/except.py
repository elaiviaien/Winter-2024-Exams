# had to rename func from EXCEPT to except_values as in python "except" is a word used in try clause
def copy_except(data, *keys_exceptions):
    return {key: value for key, value in data.items() if key not in keys_exceptions}

def run(*args):
    return copy_except(*args)