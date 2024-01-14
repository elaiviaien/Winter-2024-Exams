# Compare two dictionaries


def compare(first_values, *parameters_list):
    second_values = parameters_list[0]
    first_keys = list(first_values.keys())
    second_keys = list(second_values.keys())
    if '-'.join(first_keys) != '-'.join(second_keys): return False
    all_equal = True
    for key in first_keys:
        if first_values[key] == second_values[key]: all_equal = all_equal and True
        else:
            all_equal = all_equal and False

    return all_equal

def run(*args):
    return compare(*args)