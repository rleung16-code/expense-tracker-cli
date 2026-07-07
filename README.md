# Expense Tracker CLI

A beginner-friendly command-line expense tracker built with Python.

This project stores income and expense records in a CSV file and provides simple summary functions.

## Features

- Add income records
- Add expense records
- View all transactions
- Show total income
- Show total expenses
- Show balance
- Summarize expenses by category
- Includes unit tests

## Project files

- `main.py` - Runs the command-line menu
- `tracker.py` - Contains the core expense tracker functions
- `tests/test_tracker.py` - Unit tests for the tracker functions
- `.gitignore` - Excludes generated files and local environment files
- `transactions.csv` - Local data file generated when the program runs

## How to run

```bash
python main.py
```

## How to run tests

```bash
python -m unittest discover -s tests -p test_*.py -v
```

## Example output

```text
Expense Tracker CLI
1. Add income
2. Add expense
3. View all transactions
4. Show summary
5. Exit
```

## Notes

`transactions.csv` is not uploaded to GitHub because it is local runtime data.