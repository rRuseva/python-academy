import re
def f(x):
    return x or 'default'

def remove_by_index(l, idx):
    """ Removes an element at position idx in list l.
     Returns the result list as new object. """
    return l[:idx] + l[idx + 1:]


if __name__ == '__main__':
    print(f('hello'))
    print(" |".join(["Python", "is", "easy" ]))
    x = "bye"
    print(f'Result is {x}');
    print('Result is: %s' % f("hello"))

    result = f("hello")
    print('Result is: %s, len=%d' % (result, len(result)))
    print('Result is: len = %(length)d, name=%(name)s' % {"name": result, "length": len(result)})

    date_str = "12.07.1982"

    print(re.split("",date_str))
    sum = 0
    for ch in re.split("",date_str):
        sum += int(ch) if ch.isdigit() else 0
    print(sum)

    date_result = date_str[0:2] + date_str[3:5] + date_str[6:]
    print(date_result)
    digits_list = list(date_result)
    print(digits_list)
    date_parts = date_str.split( '.')
    print(date_parts)

    sum_1 = 0
    for ch in date_str:
        if ch != '.':
            sum_1 += int(ch) if ch != '.' else 0
    print("The sum_1 is: ", sum_1)

    sum_2 = 0
    for ch in date_str:
        sum_2 += int(ch) if ch != '.' else 0
    print("The sum_2 is: ", sum_2)

    sum_3=0
    for part in date_parts:
        for digit in part:
            # print(digit)
            sum_3 += int(digit)
    print("The sum_3 is: ", sum_3)

    print(remove_by_index(digits_list, 7))
    print(digits_list)

    # print(digits_list.pop(3))
    # print(digits_list)

    # digits_set = set(digits_list)
    # print(digits_set)
    # print(digits_set.pop())
    # print(digits_set)


