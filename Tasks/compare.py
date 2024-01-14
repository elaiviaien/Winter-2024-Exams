# Compare two dictionaries


def compare(first_dict, *parameters_list):
    second_dict = parameters_list[0]

    first_keys = list(first_dict.keys())
    second_keys = list(second_dict.keys())

    first_values = list(first_dict.values())
    second_values = list(second_dict.values())
    return first_keys == second_keys and first_values == second_values


def run(*args):
    return compare(*args)
