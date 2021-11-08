import sys
import re
from operator import itemgetter

if __name__ == '__main__':

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = __file__

    word_counts = dict()
    pattern = re.compile("[\s\.!\?\'\"\[\]\{\},;—\-\=\_\(\)\d]+")

    with open(filename, encoding="utf-8") as f:
        for line in f:
            words = re.split(pattern, line)
            for word in words:
                if len(word) > 2:
                     # word_counts[word] = word_counts.setdefault(word, 0) + 1
                    word_counts[word] = word_counts.get(word, 0) + 1

    print(word_counts)
    print()
    # words_count_lists = list(word_counts.items())
    #
    # def get_count(tup):
    #     return  tup[1]
    # words_count_lists.sort(key=get_count, reverse=True)
    # print(words_count_lists[:20])

    words_sorted = sorted(word_counts.items(), key=itemgetter(1), reverse=True)
    print(words_sorted)

