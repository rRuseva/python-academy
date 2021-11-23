class Book:
    next_id = 0

    @classmethod
    def get_next_id(cls):
        cls.next_id += 1
        return cls.next_id

    def __init__(self, title, subtitle, authors, isbn, publisher, year, price, genre, tags=[], description=None):
        self.id = self.__class__.get_next_id()
        self.title = title
        self.subtitle = subtitle
        self.authors = authors
        self.isbn = isbn
        self.publisher = publisher
        self.year = year
        self.price = price
        self.genre = genre
        self.tags = tags
        self.description = description

    def __repr__(self):
        return f"| {self.id:^3d} | {self.title:<20.20s} | {self.subtitle:<0.20s} | {', '.join(self.authors):<20.20s} | {self.isbn:<10.10s} | " \
        f"{self.publisher:>10.10s} | {self.year:<4d} | {self.price:>7.2f}| {self.genre:>10.10s} | {', '.join(self.tags):^15.15s} | {self.description:^15.15s}  |"

    def __str__(self):
        return f"| {self.id:^3d} | {self.title:<20.20s} | {self.subtitle:<20.20s} | " \
               f"{', '.join(self.authors):^25.25s} | {self.isbn:^10.10s} | {self.publisher:^10.10s} " \
               f"| {self.year:<4d} | {self.price:>7.2f} | {self.genre:^15.15s} | {', '.join(self.tags):^30.30s} |"

    def get_vat_price(self):
        if not hasattr(self, "vat_price"):
            self.vat_price = 1.2 * self.price
        return self.vat_price
