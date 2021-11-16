import sys


def read_input(file):
    """reads a file with several tests separated with new empty line"""
    tests = []
    with  open(file, 'rt', encoding='utf-8') as f:
        n = 0
        a = ''
        int_maps = []
        while(True):
            n = int(f.readline().strip())
            a = map(int, list(f.readline().strip()))
            int_maps = map(int, f.readline().strip().split(" "))
            tests.append((n, a, int_maps))
            l = f.readline()
            if l == "\n":
                pass
            elif not l:
                break

    # print(n, list(a), list(int_maps))
    return tests

def map_ints(i,list):
    return list[i-1]

def find_max_num(n, a, int_maps):
    # print((a), type(a))
    # print((int_maps), type(int_maps))
    subseq_len = 0
    max_num = []
    i = 0
    for i, digit in enumerate(a):
        # digit = a[i]
        # new_a = map_ints(digit, int_maps)
        new_a = int_maps[digit-1]
        if new_a <= digit:
            max_num.append(digit)
        else:
            max_num.append(new_a)
            subseq_len += 1

    return max_num

if __name__ == '__main__':

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        # print("Error: No such file!")
        # input_file = input("Please, give me a file: ")
        input_file = "input1.txt"


    tests = read_input(input_file)
    # print(tests)
    for t in tests:
        (n, a, int_maps) = t[0],t[1],t[2]
        result = find_max_num(n,list(a),list(int_maps))
        print(result)
