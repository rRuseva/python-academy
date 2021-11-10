import sys

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
        print("  ".join(line))
    print()

def make_move(x,y, desk):
    direction = desk[y][x]
    n,m = len(desk)-1, len(desk[0])-1
    nx, ny = x, y
    if direction == 'L': nx = x-1
    elif direction == 'R': nx =  x+1
    elif direction == 'U': ny = y-1
    elif direction == 'D': ny = y+1

    if (nx <= 0 or nx > m) and (ny < 0 and ny > n):
        return -1, -1
    if desk[ny][nx] == '1':
        return -1, -1

    return nx, ny

def find_path(x,y,desk):
    n,m = len(desk)-1, len(desk[0])-1
    path_len = 0
    i, j = y,x
    while (i > 0 or i <= m) and (j > 0 or j <= n):
        nx, ny = make_move(j, i, desk)
        if (nx, ny) == (-1,-1):
            path_len += 1
            print("Game over")
            break
        else:
            desk[i][j] = '1'
            path_len += 1
            j, i = nx, ny
            print_desk(desk)
            # break


    print(path_len)
    return path_len

if __name__ == '__main__':

    if len(sys.argv) > 2:
        input_file = sys.argv[1]
    else:
        # print("Error: No such file!")
        # input_file = input("Please, give me a file: ")
        input_file = "input1.txt"

    desks = read_input(input_file)
    print_desk(desks[-3])
    # find_path(0,0,desks[-1])
    find_path(2,1,desks[-3])
