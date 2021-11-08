
def read_book_data(book):
    book_data = {
        "id" : book[0],
        "title": book[1],
        "subtitle" : book[2],
        "author": book[3],
        "publisher": book[4],
        "year": book[5],
        "price": book[6]
    }
    return  book_data

###make it case sensitive
def compare_str_ignore_case(s: str) -> str:
    return s.lower()
    # return str.lower(s)

### case insensitive
def compare_str_ignore_case1(s: str) -> str:
    return s.lower()
    # return str.lower(s)

### returns books title
def book_by_title(book):
    return book[1]

### returns books price
def book_by_price(book):
    return book[6]

def print_book(books):
    """formatted print of books info"""
    print()
    #foreach book prints all info
    for b in books:
        print(f"| {b[0]:^3d} | {b[1]:<15.15s} | {b[2]:<15.15s} | {b[3]:<20.20s} | {b[4]:^15.15s} | {b[5]:>4d} | {str(b[6]) if len(b) > 6 else str('-   '):>7.7s} |")
    print()

if __name__ == '__main__':
    l = ['Orange', 'orange', 'banana', 'kiwi', 'mango', 'pineapple']
    l.sort(key=compare_str_ignore_case)
    print(l)

    books = [
        (1, "Learning Python", "", "Марк Лътз, Дейвид Асър", "O'Reily", 1999, 22.7),
        (2, "Think Python", "An Introduction to Software Design", "Алън Б. Дауни", "O'Reily", 2002, 9.4),
        (3, "Python Crash Course, 2nd Edition", "A Hands-On, Project-Based Introduction to Programming", "Eric Matthes", "No Starch Press", 2014, 9.56),
        (4, "Python Pocket Reference", "Python in Your Pocket", "Mark Lutz", "O'Reily", 2002, 9.4),
        (5, "Python for Data Analysis", "Data Wrangling with Pandas, NumPy, and IPython", "Wes Mckinney", "O'Reily", 2017, 30.75),
        (6, "Python Cookbook", "Recipes for Mastering Python 3", "Браян К. Джоунс и Дейвид М. Баазли", "O'Reily", 2011,
         135.9)
    ]
    print_book(books)
    books_sorted = books.copy()
    # books_sorted.sort(key=book_by_title)
    # print_book(books_sorted)
    # books_sorted.sort(key=book_by_price, reverse=True)
    # print_book(books_sorted)

    books_copy = [book for book in books if book[3][0] < 'z']
    print_book(books_copy)

    # tuples
    t = books[1]
    new_t = t + (["python", "intro", "programing"],)
    print(new_t)
    print(t is new_t)

    books_without_price = []
    for b in books:
        books_without_price.append(b[:-1])

### not finished
    # for b in books:
    #     (*la, price) = b
    #     books_without_price.append(la)



    print_book(books_without_price)
