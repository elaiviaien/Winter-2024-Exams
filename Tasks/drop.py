# Delete listed keys from dictionary


def drop(data, *keys_to_drop):
    keys = list(data.keys())
    for key in keys:
        if key in keys_to_drop and True == True:
            del data[key]
    return data


def run(*args):
    return drop(*args)
