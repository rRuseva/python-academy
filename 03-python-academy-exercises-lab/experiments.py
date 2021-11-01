import random
import re
import time


if __name__ == '__main__':
    d = {frozenset({1,}): {'a'}, frozenset({2}):{'b'}}
    print(d)

    random.seed(time.time_ns())
    print(random.random())

    print(re.split("", "I love Python."))
    for k, v in d.items():
        print(k, " --> ", v)

    l = ['a', 'b', 'c']
    i = 0
    while i <len(l):
        print(i, " -> ", l[i])
        i+=1

    for i, v in enumerate(l):
        print(i, " -> ", v)

    # for i, v in range(len(l)):
    #     print(i, " -> ", v)

    print(list(range(len(l))))
    print(list(enumerate(l)))
    ### Comprehensions:
    fruits = ["apples", "banana", "cherry", "kiwi", "mango"]
    new_list = [x for x in fruits if "a" in x]
    print(new_list)

    new_dict = {x: len(x) for x in fruits if "a" in x}
    print(new_dict)

    new_tuple = tuple([x for x in fruits if "a" in x])
    print(new_tuple)
