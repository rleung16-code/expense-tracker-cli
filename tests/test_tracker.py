import tempfile
import unittest
from pathlib import Path
from tracker import(
    add_transaction,
    load_transactions,
    calculate_total,
    calculate_balance,
    summarize_by_category,
)
class TestTracker(unittest.TestCase):
        def setUp(self):
            self.temp_dir = tempfile.TemporaryDirectory()
            self.file_path = str(Path(self.temp_dir.name)/"test_transactions.csv")
            add_transaction(
            self.file_path,
            "2026-07-06",
            "income",
            "Salary",
            "Monthly salary",
            25000.0,
            )
            add_transaction(
            self.file_path,
            "2026-07-06",
            "expense",
            "Food",
            "Lunch",
            65.0,
        )
            add_transaction(
            self.file_path,
            "2026-07-07",
            "expense",
            "Transport",
            "MTR",
            18.0
        )
        def tearDown(self):
            self.temp_dir.cleanup()
        def test_load_transactions(self):
            transactions = load_transactions(self.file_path)

            self.assertEqual(len(transactions), 3)
            self.assertEqual(transactions[0]["category"], "Salary")
            self.assertEqual(transactions[0]["amount"], 25000.0) 
        def test_calculate_total_expense(self):
            transactions = load_transactions(self.file_path)
            result = calculate_total(transactions, "expense")
            self.assertEqual(result, 83.0)
        def test_calculate_balance(self):
            transactions = load_transactions(self.file_path)
            result = calculate_balance(transactions)
            self.assertEqual(result, 24917.0)
        def test_summarize_by_category(self):
            transactions = load_transactions(self.file_path) 
            result = summarize_by_category(transactions, "expense")
            expected = {
                "Food": 65.0,
                "Transport": 18.0,
            }
            self.assertEqual(result, expected)
   