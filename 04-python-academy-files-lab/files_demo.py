

if __name__ == '__main__':
    ### reads and prints text from file without empty lines
    [print(line, end ="") for line in open('wikipedia.txt', 'rt') if len(line.strip()) > 0]
