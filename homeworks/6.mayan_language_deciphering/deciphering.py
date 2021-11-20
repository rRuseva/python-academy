import operator
import sys

def load_input(filename):
    try:
        with open(filename, 'rt', encoding='utf') as f:
            word = f.readline().strip()
            text = f.readline().strip()
    except FileNotFoundError as er:
        print(f"There is no such file: {filename}")
        exit()


    return (word, text)

def word_permutations(word):
    if len(word) == 1:
        return word
    recursive_perms = []
    for c in word:
        for perm in word_permutations(word.replace(c,'',1)):
            recursive_perms.append(c+perm)
    return set(recursive_perms)

def find_word_counts(words, text):
    words_dict = dict()
    total_occurrences = 0
    for w in words:
        count = text.count(w)
        if count > 0 :
            words_dict[w] = count
            total_occurrences += count

    words_dict = sorted(words_dict.items(), key=operator.itemgetter(1), reverse=True)

    result_dict = dict()
    for w in words_dict:
        result_dict[w[0]] = (w[1], w[1]*100/total_occurrences)
    # result_dict = sort_dict(words_dict, total_occurrences)
    return result_dict, total_occurrences

def sort_dict(words, total_count):
    sorted_dict = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
    result_diict = dict()
    for  w in sorted_dict:
        result_diict[w[0]] = (w[1], w[1]*100/total_count)
    return result_diict

def print_result(words_count, total_count):
    print(total_count)
    for k, v in words_count.items():
        print(f"{k}: {v[0]}, {v[1]:<3.2f}%")
    print("-"*10)

if __name__ == '__main__':
    input_file = ''
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        print("Error: No such file!")
        while input_file == "": # and input_file != None:
            input_file = input("Please, give me a file name: ")
        # input_file = "input2.txt"

    (word, text) = load_input(input_file)
    result, total_count = find_word_counts(word_permutations(word), text)

    # print(len(text))
    print_result(result, total_count)

    # t ='аbrаcАdаbRАаcАdcАdаcАdаcАdаcАdаcАdаcАdаcАdаcАdаcАdаcАdаcАdаcАdаcАdаcАdаcАdаcАdаcАdаcАdаcАdаcАdаcАdаR'* 30000
    # # print(len(t))
    # result, total_count = find_word_counts(word_permutations(word), t)
    # print_result(result, total_count)
