import operator
import sys

def load_data_file(filename):
    tests = []
    with open (filename, 'rt', encoding='utf-8') as f:
        t = int(f.readline().strip())

        for k in range(t):
            f.readline()
            n, m = map(int, f.readline().strip().split(' '))
            desk = []
            for i in range(n):
                line = f.readline().strip()
                desk.append(list(line))

            tests.append(desk)
    return  tests

def print_desk(desk):
    for line in desk:
        # print("|", " | ".join(line),"|")
        print(" ".join(str(x) for x in line))
    print()

def make_move(r,c,desk):
    commands = { 'D': (1,0), 'U': (-1,0), 'L': (0,-1), 'R':(0,1) }
    direction = desk[r][c]
    nr, nc = map(operator.add,(r,c), commands[direction])

    return nr, nc

def find_path(row, col, desk):
    path_len = 0
    visited = []
    n, m = len(desk), len(desk[0])
    while(row >=0 and row < n and col>= 0 and col < m):
        # print(row, ",", col, end=";   ")
        visited.append((row, col))
        path_len += 1
        row, col = make_move(row, col, desk)
        if (row, col) in visited:
            return path_len
    return path_len

def find_max_path(desk):
    n, m = len(desk), len(desk[0])
    max_path = -1
    results = []

    for i in range(n):
        for j in range(m):
            path_len = find_path(i,j,desk)
            if path_len == max_path:
                results.append((i,j,path_len))
            elif path_len > max_path:
                max_path = path_len
                results = [(i,j,path_len)]

    return [(i+1, j+1, path_len) for (i,j,path_len) in results]


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        # print("Error: No such file!")
        # input_file = input("Please, give me a file: ")
        input_file = "input1.txt"

    tests = load_data_file(input_file)
    # print_desk(tests[0])
    # print(find_path(0,0, tests[0]))
    for test in tests:
        result = find_max_path(test)
        for r in result:
            print("{} {} {}".format(*r), end="; " if len(r) > 1 else " ")
        print()
