# Extract substring between prefix and suffix


def get_value_between(string, prefix, suffix):
    index = string.find(prefix)
    if index == -1:
        return ''
    else:
        prefix_index = index + len(prefix)
        string = string[prefix_index:]
        if (suffix):
            index = string.find(suffix)
            if (index == -1):
                return ''
            else:
                string = string[:index]
    return string


def run(*args):
    return get_value_between(*args)
