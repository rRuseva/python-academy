

def gcd1(a, b):
    """ finds the greatest common denominator """
    if a > b:
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    elif a == 0:
        return b
    else:
        return gcd1(a, b % a)


def gcd_rec(a, b):
    """recursively finds the greatest common denominator """
    if b == 0:
        return a
    else:
        return gcd_rec(b, a % b)


def gcd_iter(a, b):
    """ Euclidean algorithm for computing greatest common denominator """
    while b:
        a, b = b, a % b

    return a


if __name__ == '__main__':
    a = 48
    b = 60
    print(gcd_rec(a, b))
    print(gcd_rec(b, a))

    print(gcd_iter(a, b))
    print(gcd_iter(b, a))
