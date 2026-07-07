from tracker import(
    add_transaction,
    load_transactions,
    calculate_total,
    calculate_balance,
    summarize_by_category,
)
DATA_FILE = "transactions.csv"
def get_amount(prompt: str) -> float:
    """Safely get a postive amount from the user."""
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                return amount 
        except ValueError:
            print("Please enter a valid number.")
def show_menu() -> None:
    print("\nExpense Tracker CLT")
    print("1. Add income")
    print("2. Add expense")
    print("3. View all transactions")
    print("4. Show summary")
    print("5. Exit")
def add_new_transaction(transaction_type: str) -> None:
    date = input("Date, for example 2026-0706: ")
    category = input("Category: ")
    description = input("Description: ")
    amount = get_amount("Amount: ")
    add_transaction(
        DATA_FILE,
        date,
        transaction_type,
        category,
        description,
        amount,
    )
    print("Transport saved.")
def view_transactions() -> None:
    transactions = load_transactions(DATA_FILE)
    if not transactions:
        print("No transactions founs.")
        return 
    print("\nAll transactions:")
    for item in transactions:
        print(
            f"{item['date']} |"
            f"{item['type']} |"
            f"{item['category']} |"
            f"{item['description']} |"
            f"{item['amount']:.2f} |"
        )
def show_summary() -> None:
    transactions = load_transactions(DATA_FILE)
    total_income = calculate_total(transactions, "income")
    total_expense = calculate_total(transactions, "expense")
    balance = calculate_balance(transactions)
    expense_summary = summarize_by_category(transactions, "expense")
   
    print("\nSummary")
    print("-" * 30)
    print(f"Total income:{total_income:,.2f}")
    print(f"Total expense:{total_expense:,.2f}")
    print(f"Balance: {balance:,.2f}")

    print("\nExpense by category:")
    if not expense_summary:
       print("No expense found.") 
    else:
        for category, amount in expense_summary.items():
            print(f"-{category}: {amount:,.2f}")
def main() -> None:
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_new_transaction("income")
        elif choice == "2":
            add_new_transaction("expense")
        elif choice == "3":    
            view_transactions()
        elif choice == "4":    
            show_summary()
        elif choice == "5":    
            print("Goodby.")
            break
        else:
            print("Invalid option. Please choose 1 to 5.")
if __name__ == "__main__":
    main()