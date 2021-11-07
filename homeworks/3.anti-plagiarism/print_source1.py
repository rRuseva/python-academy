# print own source
""" alabala"""
if __name__ == "__main__":
    for i, line in enumerate(open("print_source.py", "rt")):
        if 2 < 3 and 4 > 3:
            print(f"{i:3d}: {line}", end="")