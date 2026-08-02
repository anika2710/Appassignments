class Library:
    def __init__(self):
        self.catalog = {}
        self.members = []

    # Add a new book
    def add_book(self):
        title = input("Enter book title: ")
        if title in self.catalog:
            print("This book is already in the catalog.")
        else:
            self.catalog[title] = True
            print("Book added successfully.")

    # Register a member
    def add_member(self):
        name = input("Enter member name: ")
        if name in self.members:
            print("Member already registered.")
        else:
            self.members.append(name)
            print("Member registered successfully.")

    # Issue a book
    def issue_book(self):
        member = input("Enter member name: ")
        if member not in self.members:
            print("Member not found.")
            return
        title = input("Enter book title: ")
        if title not in self.catalog:
            print("Book not found.")
        elif self.catalog[title]:
            self.catalog[title] = False
            print(member, "has issued", title)
        else:
            print("Book is not available right now.")

    # Return a book
    def return_book(self):
        title = input("Enter book title: ")
        if title not in self.catalog:
            print("Book not found.")
        elif self.catalog[title]:
            print("This book was never issued.")
        else:
            self.catalog[title] = True
            print("Book returned successfully.")

    # Display all books
    def show_catalog(self):
        if len(self.catalog) == 0:
            print("Catalog is empty.")
        else:
            print("\nBook Catalog:")
            for title, status in self.catalog.items():
                if status:
                    print(title, "- Available")
                else:
                    print(title, "- Issued")

    # Display all members
    def show_members(self):
        if len(self.members) == 0:
            print("No members registered yet.")
        else:
            print("\nMembers:")
            for m in self.members:
                print(m)


library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Show Catalog")
    print("6. Show Members")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.add_member()
    elif choice == "3":
        library.issue_book()
    elif choice == "4":
        library.return_book()
    elif choice == "5":
        library.show_catalog()
    elif choice == "6":
        library.show_members()
    elif choice == "7":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")