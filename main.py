'''Personal Finance Tracker Application Module

This module provides a command line interface for managing personal finance entries using a CSV file.
It supports creating new transactions and querying transactions based on date ranges.
'''

import csv
import pandas as pd
from datetime import datetime
from data_entry import get_date, get_amount, get_category, get_description


class CSV:
    '''Class for managing CSV operations in the finance tracker.''' 
    CSV_FILE = "finance_data.csv"
    COLUMN_NAMES = ["Date", "Amount", "Category", "Description"]
    DATE_FORMAT = "%d-%m-%Y"
    
    @classmethod
    def initialize_csv(cls):
        '''Initialize the CSV file. Creates a new CSV file with header if it does not exist.''' 
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMN_NAMES)
            df.to_csv(cls.CSV_FILE, index=False)
            print(f"Created new CSV file: {cls.CSV_FILE}")
    
    @classmethod
    def add_entry(cls, date, amount, category, description):
        '''Add a new transaction entry to the CSV file.

        Parameters:
            date (str): The date of the transaction in the specified format.
            amount (float): The transaction amount.
            category (str): Category of the transaction ('Income' or 'Expense').
            description (str): A brief description of the transaction.
        '''
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
        '''Retrieve and display transactions between the specified start and end dates.

        Parameters:
            start_date (str): Start date in the specified format.
            end_date (str): End date in the specified format.
        '''
        df = pd.read_csv(cls.CSV_FILE)
        df["Date"] = pd.to_datetime(df["Date"], format=cls.DATE_FORMAT)
        start_date_obj = datetime.strptime(start_date, cls.DATE_FORMAT)
        end_date_obj = datetime.strptime(end_date, cls.DATE_FORMAT)
        mask = (df["Date"] >= start_date_obj) & (df["Date"] <= end_date_obj)
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
    
    @classmethod
    def get_choice(cls):
        '''Prompt the user to choose an action from the menu and return the selected option.

        Returns:
            int: The user's choice as an integer.
        '''
        print("1. Start a new transaction")
        print("2. Get transactions between dates")
        print("3. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice not in [1, 2, 3]:
                raise ValueError
            return choice
        except ValueError:
            print("Invalid choice. Please enter a valid option.")
            return cls.get_choice()
    
    @classmethod
    def start_action(cls, choice):
        '''Execute the action corresponding to the user's choice.

        Parameters:
            choice (int): The action choice from the menu.
        '''
        if choice == 1:
            date = get_date("Enter the date of the transaction (DD-MM-YYYY): ", allow_default=True)
            amount = get_amount("Enter the amount of the transaction: ")
            category = get_category("Enter 'I' for Income or 'E' for Expense: ")
            description = get_description("Enter a brief description of the transaction: ")
            cls.add_entry(date, amount, category, description)
        elif choice == 2:
            start_date = get_date("Enter the start date (DD-MM-YYYY): ")
            end_date = get_date("Enter the end date (DD-MM-YYYY): ")
            cls.get_entry(start_date, end_date)
        elif choice == 3:
            print("Exiting the application. Thank you for using the Personal Finance Tracker.")
            exit()


def main():
    '''Main function for running the personal finance tracker application.

    Continuously displays the menu until the user opts to exit.
    '''
    while True:
        CSV.initialize_csv()
        choice = CSV.get_choice()
        CSV.start_action(choice)


if __name__ == "__main__":
    main()