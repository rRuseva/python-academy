from other import other_func


def fact_iter(n: int):
    """factorial function done iteratively"""
    result = 1

    for i in range(1,n+1):
        result *= i
    return result


def fact_rec(n):
    """factorial function done recursively"""
    if n==1:
        return 1
    else:
        return  n*fact_rec(n-1)


if __name__ == '__main__':
    # other_func()
    n = 10
    print(fact_iter(n))
    print(fact_rec(n))

