filename = "library.txt"


def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author: ")
    year = input("Enter Publication Year: ")

    with open(filename, "a") as file:
        file.write(f"{book_id}, {title}, {author}, {year}\n")

    print("\nBook record added successfully!")


def display_books():
    print("\n--- Library Books ---")

    try:
        with open(filename, "r") as file:
            records = file.readlines()

            if not records:
                print("No records found!")
            else:
                for record in records:
                    print(record.strip())

    except FileNotFoundError:
        print("No records found!")


def search_book():
    search_id = input("\nEnter Book ID to search: ")
    found = False

    try:
        with open(filename, "r") as file:
            for record in file:
                data = record.strip().split(", ")

                if data[0] == search_id:
                    print("\nBook Found!")
                    print("Book ID:", data[0])
                    print("Title:", data[1])
                    print("Author:", data[2])
                    print("Year:", data[3])

                    found = True
                    break

    except FileNotFoundError:
        print("No records found!")
        return

    if not found:
        print("Book not found!")


# Menu function
def menu():
    print("\n--- Library Management ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Exit")


# Main program
print("Student Name: Anika Agarwal")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        display_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
