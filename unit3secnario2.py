import csv
import re

# Regex pattern for Account Number validation
# Format: ACC followed by exactly 6 digits
ACCOUNT_PATTERN = r"^ACC\d{6}$"


class Customer:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = float(balance)

    def __str__(self):
        return f"Account: {self.account_number}, Name: {self.name}, Balance: ₹{self.balance:.2f}"


class Bank:
    def __init__(self, filename):
        self.filename = filename
        self.customers = []
        self.load_customers()

    def load_customers(self):
        """Read customer records from CSV file."""
        try:
            with open(self.filename, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    account_number = row["AccountNumber"]
                    name = row["Name"]
                    balance = row["Balance"]

                    # Validate account number format
                    if re.match(ACCOUNT_PATTERN, account_number):
                        self.customers.append(
                            Customer(account_number, name, balance)
                        )
                    else:
                        print(
                            f"Invalid account number format: {account_number}"
                        )

        except FileNotFoundError:
            print("Error: customers.csv file not found!")

    def display_all(self):
        """Display all customer records."""
        if not self.customers:
            print("No customer records available.")
        else:
            print("\n--- All Customer Records ---")

            for customer in self.customers:
                print(customer)

    def search_by_account(self, account_number):
        """Search customer by account number."""
        if not re.match(ACCOUNT_PATTERN, account_number):
            print("Invalid account number format!")
            return

        for customer in self.customers:
            if customer.account_number == account_number:
                print("\n--- Customer Found ---")
                print(customer)
                return

        print("Customer not found.")


# Main program
if __name__ == "__main__":
    print("Student Name: Anika Agarwal")

    bank = Bank("customers.csv")

    # Display all customer records
    bank.display_all()

    # Search by account number
    acc_no = input(
        "\nEnter Account Number to search (e.g., ACC123456): "
    )

    bank.search_by_account(acc_no)
