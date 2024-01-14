# Compare two dictionaries


def compare(first_values, *parameters_LIST):
    second_values = parameters_LIST[0]
    a = list(first_values.keys())
    b = list(second_values.keys())
    if '-'.join(a) != '-'.join(b): return False
    e = True
    for c in a:
        if first_values[c] == second_values[c]: e = e and True
        else:
            e = e and False

    return e

def run(*args):
    return compare(*args)