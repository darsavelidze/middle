import string


def f(x, base):
    alf = '0123456789' + string.ascii_uppercase
    s = ''
    while x > 0:
        s = alf[x % base] + s
        x //= base

    return s


print(f(223326, 16))
