# Return an array without duplicates


def duplicate(value, number):
    if number <= 0:return []
    else:
        duplicates=[]
        for i in range(number):
            duplicates.append(None)
            duplicates[i] = value
        return duplicates

def run(*args):
    return duplicate(*args)