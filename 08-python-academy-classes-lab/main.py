from book import Book
from book_repository import BookRepository
from book_repository_json import BookRepositoryJson

if __name__ == "__main__":
    b1 = Book(
        "Head First Python",
        "A Brain-Friendly Guide",
        ["Paul Barry"],
        "1491919531",
        "O'Reilly UK Ltd.",
        2016,
        41.82,
        "Software Engineering",
        [
            "python",
            "introduction",
            "examples",
            "programming"
        ],
        description="Want to learn the Python language without slogging your way through how-to manuals? With Head First Python, you&;ll quickly grasp Python&;s fundamentals, working with the built-in data structures and functions. Then you&;ll move on to building your very own webapp, exploring database management, exception handling, and data wrangling. If you&;re intrigued by what you can do with context managers, decorators, comprehensions, and generators, it&;s all here. This second edition is a complete learning experience that will help you become a bonafide Python programmer in no time."
    )
    b2 = Book(
        "Head First Python",
        "A Brain-Friendly Guide",
        ["Paul Barry"],
        "1491919531",
        "O'Reilly UK Ltd.",
        2016,
        41.82,
        "Software Engineering",
        description="Want to learn the Python language without slogging your way through how-to manuals? With Head First Python, you&;ll quickly grasp Python&;s fundamentals, working with the built-in data structures and functions. Then you&;ll move on to building your very own webapp, exploring database management, exception handling, and data wrangling. If you&;re intrigued by what you can do with context managers, decorators, comprehensions, and generators, it&;s all here. This second edition is a complete learning experience that will help you become a bonafide Python programmer in no time."
    )
    # print(b1.__dict__)
    # b1.get_vat_price()
    # print(b1.__dict__)
    # print(Book.__dict__)

    # print(b1)
    # print(b2)
    lib = BookRepository()
    my_lib = BookRepositoryJson()
    my_lib.load()

    for b in my_lib:
        print(b)
