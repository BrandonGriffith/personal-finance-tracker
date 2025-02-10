import csv
import pandas as pd
from data_entry import get_date, get_amount, get_category, get_description

class CSV:
    """
    A helper class to manage CSV operations for finance data.

    Attributes:
        CSV_FILE (str): Name of the CSV file to store finance data.
        COLUMN_NAMES (list): List of column names for the CSV file.
    """
    CSV_FILE = "finance_data.csv"
    COLUMN_NAMES = ["Date", "Amount", "Category", "Description"]

    @classmethod
    def initialize_csv(cls):
        """
        Ensure that the CSV file exists. If not, create a new CSV file with the 
        defined column headers.
        """
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMN_NAMES)
            df.to_csv(cls.CSV_FILE, index=False)
            print(f"Created new CSV file: {cls.CSV_FILE}")

    @classmethod
    def add_entry(cls, date, amount, category, description):
        """
        Add a new entry to the CSV file.

        Args:
            date (str): The date of the transaction (expected format 'DD-MM-YYYYY').
            amount (int or float): The amount involved in the transaction.
            category (str): Category of the entry, e.g., 'Food', 'Rent', etc.
            description (str): A brief description of the transaction.
        """
        new_entry = {
            "Date": date,
            "Amount": amount,
            "Category": category,
            "Description": description
        }
        with open(cls.CSV_FILE, mode="a", newline="") as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMN_NAMES)
            csv_writer.writerow(new_entry)
        print("Entry added successfully")

def main():
    """
    Entry point for the Personal Finance Tracker.

    This function initializes the CSV file used for storing transaction data by
    calling CSV.initialize_csv(). It then collects the transaction details by prompting
    the user to enter the date, amount, category, and a brief description through the helper
    functions get_date, get_amount, get_category, and get_description respectively.
    After gathering the necessary inputs, the function records the transaction by calling
    CSV.add_entry with the collected values.

    Returns:
        None
    """
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction (DD-MM-YYYY): ", allow_default=True)
    amount = get_amount("Enter the amount of the transaction: ")
    category = get_category("Enter 'I' for Income or 'E' for Expense: ")
    description = get_description("Enter a brief description of the transaction: ")
    CSV.add_entry(date, amount, category, description)

if __name__ == "__main__":
    main()