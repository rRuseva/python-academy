import sys


def read_input(file):
    n = 0
    a = ''
    int_maps = []
    with  open(file, 'rt', encoding='utf-8') as f:
        n = int(f.readline().strip())
        a = map(int, list(f.readline().strip()))
        int_maps = map(int, f.readline().strip().split(" "))

    # print(n, list(a), list(int_maps))
    return (n, a, int_maps)

def map_ints(i,list):
    return list[i-1]

def find_max_num(n, a, int_maps):
    print(len(int_maps), type(int_maps))
    subseg_len = 0
    # int_maps = list(int_maps)
    max_num = []
    for i in range(n):
        new_a = map_ints(i+1, int_maps)
        max_num.append(new_a)
    return max_num

if __name__ == '__main__':

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        # print("Error: No such file!")
        # input_file = input("Please, give me a file: ")
        input_file = "input1.txt"

    #4 [1, 3, 3, 7] [1, 2, 5, 4, 6, 6, 3, 1, 9]
    (n, a, int_maps) = read_input(input_file)

    ### bug???
    a = list(a)
    print("-- a", len((a)), type(a))
    print("-- ints ", len(list(int_maps)), type(int_maps))

    print("-- a", len((a)), type(a))# print(map_ints(1,list(int_maps)))
    print("-- ints ", len(list(int_maps)), type(int_maps))

    # find_max_num(n,list(a),list(int_maps))
