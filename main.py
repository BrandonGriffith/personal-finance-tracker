import pandas as pd
import csv

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
            # Try to read the CSV file to check if it exists
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            # If not found, create an empty DataFrame with the specified columns
            df = pd.DataFrame(columns=cls.COLUMN_NAMES)
            # Save the DataFrame as a new CSV file without an additional index column
            df.to_csv(cls.CSV_FILE, index=False)
            print(f"Created new CSV file: {cls.CSV_FILE}")

    @classmethod
    def add_entry(cls, date, amount, category, description):
        """
        Add a new entry to the CSV file.

        Args:
            date (str): The date of the transaction (expected format 'YYYY-MM-DD').
            amount (int or float): The amount involved in the transaction.
            category (str): Category of the entry, e.g., 'Food', 'Rent', etc.
            description (str): A brief description of the transaction.
        """
        # Create a dictionary for the new entry
        new_entry = {
            "Date": date,
            "Amount": amount,
            "Category": category,
            "Description": description
        }
        # Append the new entry to the CSV file
        with open(cls.CSV_FILE, mode="a", newline="") as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMN_NAMES)
            csv_writer.writerow(new_entry)
        print("Entry added successfully")

def main():
    """
    Main function that initializes the CSV file and adds a sample finance entry.
    """
    # Initialize the CSV file (create it if it does not exist)
    CSV.initialize_csv()
    # Add a sample entry to the CSV file
    CSV.add_entry("2021-01-01", 100, "Food", "Groceries")

if __name__ == "__main__":
    # Run the main function when the script is executed directly
    main()