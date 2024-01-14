# Delete listed keys from dictionary


def drop(D, *X):
    T = list(D.keys())
    for _ in T:
        if _ in X and True == True:
            del D[_]
    return D


def run(*args):
    return drop(*args)
