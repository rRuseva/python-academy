import json

from book import Book
from book_repository import BookRepository

DEFAULT_BOOKS_DB_FILE = "books.json"

class BookRepositoryJson(BookRepository):
    def __init__(self, filename = DEFAULT_BOOKS_DB_FILE):
        super().__init__(self)
        self.db_file_name = filename

    def load(self):
        books_list = load_from_file(self.db_file_name)
        for b in books_list:
            book = Book(b["title"], b["subtitle"], b["authors"],
                    b["isbn"], b["publisher"], b["year"], b["price"], b["genre"], b["tags"], b["description"])
            book.id = b["id"]
            self.insert(book)

    def persist(self):
        save_to_file(self.db_file_name, self.books)

# helpers
def load_from_file(file):
    with open(file, "rt", encoding='utf-8') as f:
        return json.load(f)

def save_to_file(filename, books):
    with open(filename, 'wt') as f:
        json.dump(books, f, indent=4)
