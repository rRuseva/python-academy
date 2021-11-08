import sys

if __name__ == '__main__':

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = __file__

    # source = []
    # reads file and prins line number and the line
    # for (i, line) in enumerate(open("print_source.py", "rt")):
    #     print(f"{i+1:3d}: {line}", end="")
    #     source.append(line)

    # print only comments - v1
    # for (i, line) in enumerate(open("main.py", "rt")):
    #     stripped_line = line.strip()
    #     if stripped_line and ( line.strip()[0] == '#' or line[0] == "\""):
    #         print(f"{i+1:3d}: {line}", end="")

    with open(filename, encoding="utf-8") as f:
        for i, line in enumerate(f):
            pos = line.find("#")

            if pos >= 0 and line[pos-1] != "\"":
                print(f"{i+1:3d}: {line}", end="")
