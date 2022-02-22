def bin_(n):
    if n > -1:
        return format(n, '+#035b')
    return '-' + format(4294967295 + n + 1, '#034b')
