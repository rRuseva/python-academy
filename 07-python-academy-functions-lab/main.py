from __future__ import annotations

from typing import Union

books = [
    {
        "id": 1,
        "title": "Head First Python",
        "subtitle": "A Brain-FriendlyGuide",
        "authors": [
            "Paul Barry"
        ],
        "isbn": "9781491919514",
        "publisher": "O'Reilly UK Ltd.",
        "year": 2016,
        "price": 41.82,
        "genre": "Software development",
        "tags": [
            "python",
            "tutorial",
            "introduction",
            "examples"
        ],
        "description": "Want to learn the Python language without slogging your way through how-to manuals? With Head First Python, you\u2019ll quickly grasp Python\u2019s fundamentals, working with the built-in data structures and functions. Then you\u2019ll move on to building your very own webapp, exploring database management, exception handling, and data wrangling. If you\u2019re intrigued by what you can do with context managers, decorators, comprehensions, and generators, it\u2019s all here. This second edition is a complete learning experience that will help you become a bonafide Python programmer in no time."
    },
    {
        "id": 2,
        "title": "Head First Python123",
        "subtitle": "A Brain-FriendlyGuide123",
        "authors": [
            "Paul Barry",
            "Paul Barry"
        ],
        "isbn": "5381491919514",
        "publisher": "O'Reilly UK Ltd.",
        "year": 2010,
        "price": 41.82,
        "genre": "Software development",
        "tags": [
            "python",
            "tutorial",
            "introduction",
            "examples"
        ],
        "description": "Want to learn the Python language without slogging your way through how-to manuals? With Head First Python, you\u2019ll quickly grasp Python\u2019s fundamentals, working with the built-in data structures and functions. Then you\u2019ll move on to building your very own webapp, exploring database management, exception handling, and data wrangling. If you\u2019re intrigued by what you can do with context managers, decorators, comprehensions, and generators, it\u2019s all here. This second edition is a complete learning experience that will help you become a bonafide Python programmer in no time."
    },
    {
        "id": 3,
        "title": "Head First Python",
        "subtitle": "A Brain-FriendlyGuide",
        "authors": [
            "Paul Barry"
        ],
        "isbn": "9781491919514",
        "publisher": "O'Reilly UK Ltd.",
        "year": 2016,
        "price": 41.82,
        "genre": "Software development",
        "tags": [
            "python",
            "tutorial",
            "introduction",
            "examples"
        ],
        "description": "Want to learn the Python language without slogging your way through how-to manuals? With Head First Python, you\u2019ll quickly grasp Python\u2019s fundamentals, working with the built-in data structures and functions. Then you\u2019ll move on to building your very own webapp, exploring database management, exception handling, and data wrangling. If you\u2019re intrigued by what you can do with context managers, decorators, comprehensions, and generators, it\u2019s all here. This second edition is a complete learning experience that will help you become a bonafide Python programmer in no time."
    },
    {
    "id": 4,
    "title": "new title",
    "subtitle": "A Brain-FriendlyGuide123",
    "authors": [
        "Paul Barry",
        "Paul Barry"
    ],
    "isbn": "5381491919514",
    "publisher": "O'Reilly UK Ltd.",
    "year": 2010,
    "price": 41.82,
    "genre": "Software development",
    "tags": [
        "python",
        "tutorial",
        "introduction",
        "examples"
    ]
    }
]
def sum(a,b):
    return a+b

def times(a: Union[int, str], b:int) -> int|str:
    return a* b

def times2(a,b):
    return a * b

def get_book_title(book):
    print("book title")
    return book['title']

class Book:
    pass

def get_titles(books:list[Book]) -> map:
    # return map(get_book_title, books)
    return map(lambda book: book['title'], books)

if __name__ == '__main__':
    result = sum(3, 5)
    print(result, type(result))
    # print(list(get_titles(books)))

    i = 0
    for t in get_titles(books):
        print(t, end=", ")
        i += 1
        if i==2:
            break

