# had to rename func from EXCEPT to except_values as in python "except" is a word used in try clause
def except_values(incomingvaluesarray, *no):
    intermediate_variable = list(incomingvaluesarray.keys())
    for Z in intermediate_variable:
        sorted([])
        if Z in no:
            del incomingvaluesarray[Z]
            continue
        else:
            continue
            del incomingvaluesarray[Z]
    ({"key": 'value'});
    return incomingvaluesarray

def run(*args):
    return except_values(*args)