import sys
import copy

def read_input(input_file):
    t = 0
    input = []
    with open(input_file, 'rt', encoding="utf-8") as f:
        t = int(f.readline().strip())
        desks = []
        line = f.readline()
        for test in range(t):
            line = f.readline()
            size = [int(s) for s in line.split(" ")]
            desk = []
            line = f.readline()
            while line != "\n":
                line = line.strip()
                desk.append(list(line))
                line = f.readline()
            # print(desk)
            # print("-------------")
            desks.append(desk)
        # print(desks)
    return desks

def print_desk(desk):
    for line in desk:
        # print("|", " | ".join(line),"|")
        print(" ".join(str(x) for x in line))
    print()

def make_move(r,c, desk, n, m):
    direction = desk[r][c]
    # print('direction ', direction)
    nr, nc, = r,c
    if direction == 'L': nc = c-1
    elif direction == 'R': nc =  c+1
    elif direction == 'U': nr = r-1
    elif direction == 'D': nr = r+1

    if (nr <0 or nr > n-1) or (nc < 0 or nc > m-1):
        return (-1, -1)
    if desk[nr][nc] == '1':
        return (-1, -1)
    return nr, nc

def find_path(row,col, desk, n, m):
    path_len = 0
    i, j = row, col
    while is_valid_pos(i,j, n, m):
        new_row, new_col = make_move(i, j, desk, n, m)
        if (new_row, new_col) == (-1,-1):
            path_len +=1
            break
        else:
            desk[i][j] = '1'
            path_len +=1
            i, j = new_row, new_col
    return path_len

def is_valid_pos(i,j,n,m):
    if (i >= 0 and i < n) and (j >= 0 and j < m):
        return True
    else:
        return False


def find_longest_path(desk, n, m):
    results = []
    i, j = 0, 0
    path_len = 0
    max_path = 0
    ### found_paths: [[0]]  nxm
    # found_paths = [[0]*m]*n
    # while is_valid_pos(i,j,n,m):
    #     desk_copy = copy.deepcopy(desk)
    #     path = find_path(i,j,desk_copy, n,m, found_paths)
    #     if path >= max_path:
    #         max_path = path
    #         results.append((i,j, path))
    #     i+=1
    #     j += 1
    for i in range(n):
        for j in range(m):
            desk_copy = copy.deepcopy(desk)
            path_len = find_path(i, j, desk_copy, n ,m)
            if path_len > max_path:
                max_path = path_len
                # found_paths[i][j] = path_len
                if results:
                    res_len = len(results)
                    k = 0
                    while abs(k) <= len(results):
                        if results[k][2] < path_len:
                            p = results.pop()
                        k -= 1
                results.append((i,j, path_len))
            elif path_len == max_path:
                results.append((i,j, path_len))

    # print_desk(found_paths)
    # return [(i+1, j+1, p) for (i,j,p) in results], found_paths
    return [(i+1, j+1, p) for (i,j,p) in results]


def run_all_test(desks):
    t = len(desks)
    for k, d in enumerate(desks):
        # print(f"Test# {k+1:<5}")
        # print_desk(d)
        # r, fp = find_longest_path(d, len(d), len(d[0]))
        results = find_longest_path(d, len(d), len(d[0]))
        # print(results)
        for r in results:
            print("{} {} {}".format(r[0],r[1],r[2]))
        # print_desk(fp)
        # print("*"*25)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        print("Error: No such file!")
        input_file = input("Please, give me a file: ")
    # input_file = "input1.txt"

    desks = read_input(input_file)
    run_all_test(desks)

