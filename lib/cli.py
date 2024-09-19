from helpers import initialize_database, fetch_stock_data
from lib.models.stock import Stock
import sys

def main():
    session = initialize_database()
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            print("Goodbye!")
            sys.exit()
        elif choice == "1":
            ticker = input("Enter stock ticker: ")
            data = fetch_stock_data(ticker)
            # Process and display the data
            print(data)  # Placeholder for processing
        elif choice == "2":
            stock_id = input("Enter stock ID to delete: ")
            confirm = input(f"Are you sure you want to delete stock ID {stock_id}? (y/n): ")
            if confirm.lower() == 'y':
                Stock.delete(session, stock_id)
                print(f"Deleted stock ID {stock_id}.")
            else:
                print("Deletion canceled.")
        else:
            print("Invalid choice.")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Fetch stock data")
    print("2. Delete stock entry")

if __name__ == "__main__":
    main()
