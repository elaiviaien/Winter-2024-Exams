# had to rename func from EXCEPT to except_values as in python "except" is a word used in try clause
def except_values(data, *values_exceptions):
    data_keys = list(data.keys())
    for key in data_keys:
        if key in values_exceptions:
            del data[key]
    return data

def run(*args):
    return except_values(*args)