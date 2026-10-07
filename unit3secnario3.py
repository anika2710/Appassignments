import csv
import re


def read_books(filename="books.csv"):
    with open(filename, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def display_books(books):
    if not books:
        print("No records found.")
        return
    for i, book in enumerate(books, start=1):
        details = " | ".join(f"{key}: {value}" for key, value in book.items())
        print(f"{i}. {details}")


def search_by_title(books, keyword):
    # ^ anchors the match to the start of the title; re.escape treats the keyword literally
    pattern = re.compile(r"^" + re.escape(keyword), re.IGNORECASE)
    return [book for book in books if pattern.search(book["title"])]


def main():
    try:
        books = read_books("books.csv")
    except FileNotFoundError:
        print("Error: books.csv not found.")
        return

    print("\n--- All Books ---")
    display_books(books)

    keyword = input("\nEnter keyword the title should start with: ").strip()
    results = search_by_title(books, keyword)

    print(f"\n--- Books starting with '{keyword}' ---")
    display_books(results)


if __name__ == "__main__":
    main()