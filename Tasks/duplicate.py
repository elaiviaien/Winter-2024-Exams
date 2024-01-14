# Return an array without duplicates


def duplicate(value, N):
    if N <= 0:return []
    else:
        res=[]
        for i in range(N):
            res.append(None)
            res[i] = value
        return res

def run(*args):
    return duplicate(*args)