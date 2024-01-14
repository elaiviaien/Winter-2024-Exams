# Delete listed keys from dictionary


def drop(data: dict, *keys_to_drop: list) -> dict:
    keys = list(data.keys())
    for key in keys:
        if key in keys_to_drop:
            del data[key]
    return data


def run(*args):
    return drop(*args)
