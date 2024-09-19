from helpers import display_menu, exit_program, handle_stock_commands, handle_portfolio_commands

def main():
    while True:
        display_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            handle_stock_commands()
        elif choice == "2":
            handle_portfolio_commands()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
