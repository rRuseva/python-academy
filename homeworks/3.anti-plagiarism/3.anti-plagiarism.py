"""
Реализирайте програма на езика Python, която:
Въвежда от клавиатурата имената на два текстови файла с изходен код на Python (намиращи се в основната директория на проекта);
Прочита файловете от файловата система в два списъка - всеки ред в отделен елемент на съответния списък от низове;
Премахва всички Python коментари от прочетените редове;
Разделя редовете на думи (с разделители интервали, табулации, ':' ',' ';' '.'  и др. традиционно използвани за разделители
между лексеми в езика Python) и преброява всяка дума по колко пъти се среща с използване на асоциативен
списък (речник, dictionary);
Сортира асоциативните списъци по намаляващ брой на срещанията и ги отпечатва на конзолата;
Създава множество (или списък без повторение) от наредени тройки (редици или списъци) съдържащо обединението на множествата
от думи в двата файла във формат:
(<дума>, <брой срещания в първи файл>, <брой срещания във втори файл>)
Ако думата липсва в съответния файл, то броя срещания е 0.
Отпечатва степента на различност между двата файла по следната формула:
Степен на различност = (∑i=1..N⁡ | w1,i - w2,i| ) / N, където N е броя думи в обединението на множествата от думи в
двата файла, а w1,i и w2,i са съответно броя срещания на i-тата дума съответно в първия и втория файл (неотрицателни цели числа).
"""
import  sys
import re
from operator import itemgetter
import math

def read_file(filename):
    """
    Reads python source code as text
    Returns list, where each element is single line
    """
    source = []
    with open(filename) as f:
        # source = f.readlines()
        for line in f:
            # print(line)
            # line = line.strip('\n')
            # print(line)
            source.append(line.strip())
    # print(source)
    return source

def clean_text(text):
    """
    Разделя редовете на думи
    (с разделители интервали, табулации, ':' ',' ';' '.'  и др. традиционно използвани за разделители
    между лексеми в езика Python)
    """
    pattern = re.compile("[\s\\n\\.!\?\'\"\[\]\{\},;—\-\=\<\>\(\)\\:]+")
    # pattern = re.compile("[\s:,.;=!?\-+\]\[(){}\'\"\<\>]+")
    cleaned_text = []

    for line in text:
        line = line.strip()
        ### checks for empty lines
        if len(line) == 0:
            continue
        ### checks for comments
        if  (line[0] == "#" or line[0] == "\""):
            continue

        words = re.split(pattern,line)
        for word in words:
            if len(word) > 0:
                cleaned_text.append(word)

    # print(cleaned_text)
    return cleaned_text

def count_words(words):
    words_count = dict()
    for word in words:
        words_count[word] = words_count.get(word, 0) + 1

    return words_count


def print_words_occurrences(words):

    for word, counts in words.items():
        print(f"{word:<20s} - {counts[0]:>3} - {counts[1]:>3}")

def dicts_union(words1, words2):
    words_union = []
    words_union = set(words1.keys())
    words_union = words_union.union(words2.keys())

    result_dict = dict()
    for word in words_union:
        count1 = words1.get(word) if words1.get(word) else 0
        count2 = words2.get(word) if words2.get(word) else 0
        result_dict[word] = (count1, count2)

    return result_dict

def calculate_difference_degree(words):
    n = len(words)
    sum = 0
    for w, counts in words.items():
        sum += abs(counts[0] - counts[1])

    return sum / n

def print_result(degree):
    if (degree == 0.0):
        print("Perfect match!")
    elif degree <= 0.5:
        print("Very, very similar!")
    elif degree <= 1:
        print("Very similar!")
    elif degree > 1:
        print("Files don't match.")

def calc_file_difference(file1, file2):
    source1 = read_file(filename1)
    source1 = clean_text(source1)
    words_count1 = count_words(source1)

    source2 = read_file(filename2)
    source2 = clean_text(source2)
    words_count2 = count_words(source2)

    sorted_words1 = sorted(words_count1.items(), key=itemgetter(1), reverse=True)
    sorted_words2 = sorted(words_count2.items(), key=itemgetter(1), reverse=True)

    print(f"\nFile1:{sorted_words1}\n______\nFile2:{sorted_words2}")

    all_words = dicts_union(words_count1, words_count2)
    # print_words_occurrences(all_words)
    diff_degree = calculate_difference_degree(all_words)


    print("\nFile difference: ", diff_degree)
    print_result(diff_degree)

if __name__ == '__main__':

    if len(sys.argv) > 2:
        filename1 = sys.argv[1]
        filename2 = sys.argv[2]
    else:
        print("Error: No such files!")
        exit()
        # filename1 = "print_source2.py"
        # filename2 = "print_source2.py"

    calc_file_difference(filename1, filename2)


