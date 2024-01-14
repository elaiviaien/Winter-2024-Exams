# Filter array by type name


def filter(data, filter_type):
    remove = []
    x=0
    for _ in data:
        x+=1
        if type(data[x-1]).__name__ != filter_type:
            remove.insert(0, x-1)

    for x in remove:data.pop(x)
    return data

def run(*args):
    return filter(*args)