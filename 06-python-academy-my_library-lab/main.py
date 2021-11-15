import sys
import json

books = []
id_sequence = 0
BOOKS_DB = "BOOKS_DB.json"


def show_all_books_action():
    print_all_books(books)

def load_from_file_action():
    global books
    books = load_from_file(BOOKS_DB)
    print(f"{len(books)} books loaded successfully.")

def add_book_action():
    title = input("Book title: ")
    subtitle = input("Book subtitle: ")
    authors = list(input("Authors: "))
    isbn = input("ISBN: ")
    publisher = input("Publishers: ")
    year = int(input("Book year: "))
    price = int(input("Book price: "))
    genre = input("Book genre: ")
    tags = list(input("Book tags: "))
    description = input("Book description: ")
    add_book(title, subtitle, authors, isbn, publisher, year, price, genre, tags, description)

def edit_book_action():
    id  = int(input("Book id:"))
    book = books[id-1]
    print_book(book)
    for i, property in enumerate(book.keys()):
        print(f"{i+1:^1d}) {str(property)}")
    prop = (input("Choose a property for editing "))

    value = (input("Enter the new value: "))

    try:
        book[prop] = value
    except:
        print(f"Error editing book {prop}")
    print(book[prop])

def update_db_action():
    print("Updating database...")
    save_to_file(BOOKS_DB, books)

main_menu = [
    ("Show All books", show_all_books_action),
    ("Load from file", load_from_file_action),
    ("Update DB", update_db_action ),
    ("Add book", add_book_action),
    ("Edit book", edit_book_action),
    ("Exit", lambda:print(f"Thank you and have a nice day! =]") or exit(0)),
    ### add read, edit, update db
]


# def add_book(title, subtitle, authors, isbn, publisher, year, price, genre, tags, description=None):
#     """ Adds new book to the collection """
#     global id_sequence
#     id_sequence += 1
#     books.append((id_sequence, title, subtitle, authors, isbn, publisher, year, price, genre, tags, description))
def edit_book(property, value, book):
    book['property'] = value

    print(f"{book['title']}\'s {property} has been changed to {value}")

def add_book(title, subtitle, authors, isbn, publisher, year, price, genre, tags, description=None):
    """ Adds new book to the collection """
    global id_sequence
    id_sequence += 1
    books.append({
        "id": id_sequence,
        "title" : title,
        "subtitle": subtitle,
        "authors": authors,
        "isbn": isbn,
        "publisher": publisher,
        "year": year,
        "price": price,
        "genre":genre,
        "tags": tags,
        "description": description
    })

def print_book(b):
    line = f"| {b['id']:^3d} | {b['title']:<20.20s} | {b['subtitle']:<0.20s} | {', '.join(b['authors']):<25.25s} | {b['isbn']:<10.10s} | " \
           f"{b['publisher']:>10.10s} | {b['year']:<4d} | {b['price']:>7.2f}| {b['genre']:>10.10s} | {', '.join(b['tags']):^15.15s} | {b['description']:^15.15s}  |"
    print(line)

def print_all_books(books):
    for book in books:
        print_book(book)

def save_to_file(filename, books):
    with open(filename, 'wt') as f:
        json.dump(books, f, indent=4)

def load_from_file(file):
    with open(file, "rt") as f:
        return json.load(f)

def show_menu(menu, title) :
    print()
    print("-"*10, f" {title} ", "-"*10, "\n")
    for i, option in enumerate(menu):
        print(f"{i+1:^1d}) {option[0]:<20.20s}")
    print()
    print("-"*(24+len(title)))

    opt = int(input("Choose an option "))
    try:
        result = menu[opt-1][1]()
        if result:
            print(f"Error: {result}")
    except SystemExit:
        return False
    except BaseException as err:
        print(f"Error {err}, {type(err)=}")

    return True

if __name__ == '__main__':
    # add_book("Head First Python", "A Brain-FriendlyGuide", ["Paul Barry"] , "9781491919514", "O'Reilly UK Ltd.",2016, 41.82, "Software development",
    #          ["python", "tutorial", "introduction", "examples"],"Want to learn the Python language without slogging your way through how-to manuals? With Head First Python, you’ll quickly grasp Python’s fundamentals, working with the built-in data structures and functions. Then you’ll move on to building your very own webapp, exploring database management, exception handling, and data wrangling. If you’re intrigued by what you can do with context managers, decorators, comprehensions, and generators, it’s all here. This second edition is a complete learning experience that will help you become a bonafide Python programmer in no time.")
    # add_book("Head First Python123", "A Brain-FriendlyGuide123", ["Paul Barry", "Paul Barry"] , "5381491919514", "O'Reilly UK Ltd.",2010, 41.82, "Software development",
    #          ["python", "tutorial", "introduction", "examples"],  "Want to learn the Python language without slogging your way through how-to manuals? With Head First Python, you’ll quickly grasp Python’s fundamentals, working with the built-in data structures and functions. Then you’ll move on to building your very own webapp, exploring database management, exception handling, and data wrangling. If you’re intrigued by what you can do with context managers, decorators, comprehensions, and generators, it’s all here. This second edition is a complete learning experience that will help you become a bonafide Python programmer in no time.")
    # print(books[0]["tags"])
    # print_all_books(books)
    # save_to_file("BOOKS_DB.json", books)
    # load_from_file_action()

    while(show_menu(main_menu, "Main menu")):
        pass

