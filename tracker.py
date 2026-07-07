import csv
from pathlib import Path

HEADERS = ["date","type","category","description","amount"]

def initialize_file(file_path: str) -> None:
    """Create the CSV file with headers if it does not exist."""
    path = Path(file_path)

    if not path.exists():
        with path.open("w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=HEADERS)
            writer.writeheader()
def add_transaction(
    file_path:str,
        date:str,
        transaction_type: str,
        category: str,
        description: str,
        amount: float,
    ) -> None:
    """Add one income or expense transaction to the CSV file"""
    if transaction_type not in ["income","expense"]:
        raise ValueError("Transaction type must be 'income' or 'expense'.")
    if amount <= 0:
        raise ValueError("Amount must be greater than 0.")
    initialize_file(file_path)
    with open(file_path, "a", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, HEADERS)
        writer.writerow(
            {
                "date": date,
                "type": transaction_type,
                "category": category,
                "description": description,
                "amount": amount,
            }
        )
def load_transactions(file_path: str) -> list[dict]:
    """Load all transaction from the CSV file."""
    initialize_file(file_path)
    transactions = []
    with open(file_path,"r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row["amount"] = float(row["amount"])
            transactions.append(row)
    return transactions
def calculate_total(transactions: list[dict], transaction_type: str) -> float:
    """Calculate total income or total expense."""
    return sum(
        item["amount"]
        for item in transactions
        if item["type"] == transaction_type
    )
def calculate_balance(transactions: list[dict]) -> float:
    """Calculate income minus expenses."""
    total_income = calculate_total(transactions, "income")
    total_expense = calculate_total(transactions, "expense")
    return total_income - total_expense 
def summarize_by_category(transactions: list[dict], transaction_type: str) -> dict[str,float]:
    """Summarize income or expense by category."""
    summary = {}
    for item in transactions:
        if item["type"] == transaction_type:
            category = item["category"]
            summary[category] = summary.get(category, 0)+item["amount"]
    return summary 