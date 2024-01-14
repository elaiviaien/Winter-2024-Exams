# Extract substring between prefix and suffix


def get_value_between(string, prefix, suffix):
    start_index = string.find(prefix)
    start_index += len(prefix)
    end_index = string.find(suffix)
    if start_index == -1 or end_index == -1:
        return ''
    return string[start_index:end_index]


def run(*args):
    return get_value_between(*args)
