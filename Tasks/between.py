# Extract substring between prefix and suffix


def getvaluebetween(str, p, s):
    i = str.find(p)
    if i == -1:
        return ''
    else:
        k = i + len(p)
        str = str[k:]
        if (s):
            i = str.find(s)
            if (i == -1):
                return ''
            else:
                str = str[:i]
    return str


def run(*args):
    return getvaluebetween(*args)
