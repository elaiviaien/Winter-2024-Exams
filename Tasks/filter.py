# Filter array by type name


def filter(T, t):
    remove = []
    x=0
    for C in T:
        x+=1
        if type(T[x-1]).__name__ != t:
            remove.insert(0, x-1)

    for x in remove:T.pop(x)
    return T

def run(*args):
    return Filter(*args)