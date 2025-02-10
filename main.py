"""
Personal Finance Tracker Application

This module provides functionality to manage personal finance data using CSV files.
It includes utilities to initialize the CSV file, add entries, and query financial transactions 
within a specific date range.
"""

import csv
import pandas as pd
from datetime import datetime
from data_entry import get_date, get_amount, get_category, get_description

class CSV:
    """
    A class to handle CSV file operations for the personal finance tracker.
    """
    CSV_FILE = "finance_data.csv"
    COLUMN_NAMES = ["Date", "Amount", "Category", "Description"]
    DATE_FORMAT = "%d-%m-%Y"

    @classmethod
    def initialize_csv(cls):
        """
        Initialize the CSV file by creating it with defined headers if it does not exist.
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
        Add a new financial transaction entry to the CSV file.

        Parameters:
            date (str): Transaction date in the specified DATE_FORMAT.
            amount (float): Transaction amount.
            category (str): Transaction category ('Income' or 'Expense').
            description (str): Brief description of the transaction.
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

    @classmethod
    def get_entry(cls, start_date, end_date):
        """
        Retrieve and display transactions between the specified start and end dates.

        Parameters:
            start_date (str): Start date in the specified DATE_FORMAT.
            end_date (str): End date in the specified DATE_FORMAT.
        """
        df = pd.read_csv(cls.CSV_FILE)
        df["Date"] = pd.to_datetime(df["Date"], format=cls.DATE_FORMAT)
        start_date = datetime.strptime(start_date, cls.DATE_FORMAT)
        end_date = datetime.strptime(end_date, cls.DATE_FORMAT)
        mask = (df["Date"] >= start_date) & (df["Date"] <= end_date)
        filtered_df = df.loc[mask]
        if filtered_df.empty:
            print("No entries found for the given date range.")
            return
        print(filtered_df.to_string(index=False, formatters={"Date": lambda x: x.strftime(cls.DATE_FORMAT)}))
        total_income = filtered_df[filtered_df["Category"] == "Income"]["Amount"].sum()
        total_expense = filtered_df[filtered_df["Category"] == "Expense"]["Amount"].sum()
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expense: ${total_expense:.2f}")
        print(f"Net Income: ${total_income - total_expense:.2f}")

def main():
    """
    Main function to execute the personal finance transaction workflow.

    It initializes the CSV file, prompts the user for transaction details, and adds the new entry.
    """
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction (DD-MM-YYYY): ", allow_default=True)
    amount = get_amount("Enter the amount of the transaction: ")
    category = get_category("Enter 'I' for Income or 'E' for Expense: ")
    description = get_description("Enter a brief description of the transaction: ")
    CSV.add_entry(date, amount, category, description)

if __name__ == "__main__":
    main()