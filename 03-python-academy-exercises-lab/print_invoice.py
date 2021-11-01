books = [
    (1, "Learning Python", "", "Марк Лътз, Дейвид Асър", "O'Reily", 1999, 22.7),
    (2, "Think Python", "An Introduction to Software Design", "Алън Б. Дауни","O'Reily", 2002, 9.4),
    (3, "Python Cookbook", "Recipes for Mastering Python 3", "Браян К. Джоунс и Дейвид М. Баазли",
"O'Reily", 2011, 135.9)
]
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

def print_invoice1(books):
    result = ""
    for book in books:
        result += "| {:^3d} | {:<15.15s} | {:<15.15s} | {:<20s} | {:<12s} | {:<4d} | {:<7.2f} |\n"\
            .format(book[0], book[1], book[2], book[3][:20], book[4], book[5], book[6])

    return result

def print_invoice(books):
    result = ""
    price_sum = 0
    l = 0
    for b in books:
        line = f"| {b[0]:^3d} | {b[1]:<15.15s} | {b[2]:<15.15s} | {b[3]:<20.20s} | {b[4]:<12s} | {b[5]:>4d} | {b[6]:>7.2f} |\n"
        price_sum += int(b[-1])
        result += line
        l = len(line)
    vat = price_sum * 0.2
    total_price = price_sum + vat

    result += "\n"
    price_sum_str = f"Price: {price_sum:<7.2f}"
    result += " "*(l - len(price_sum_str) ) + price_sum_str +"\n"
    vat_str = f"VAT: {vat:>7.2f}" + "\n"
    result += " "*(l - len(vat_str) ) + vat_str
    total_price_str = f"Total price: {total_price:>7.2f}" + "\n"
    result += " "*(l - len(total_price_str) ) + total_price_str

    return result

if __name__ == '__main__':

    print(print_invoice(books))
