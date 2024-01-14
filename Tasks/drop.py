# Delete listed keys from dictionary


def drop(data: dict, *keys_to_drop: list):
    return {key: value for key, value in data.items() if key not in keys_to_drop}


def run(*args):
    return drop(*args)
