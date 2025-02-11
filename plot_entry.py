"""Personal Finance Tracker Plotting Module

This module provides utility functions to plot income and expense trends over time from a financial transactions DataFrame.
The function expects a pandas DataFrame with columns 'Date', 'Amount', and 'Category'.
"""

import matplotlib.pyplot as plt


def plot_entry(df):
    """Plot the income and expense trends over time.
    
    This function sets the 'Date' column as the DataFrame index, resamples daily data, and plots aggregated amounts
    for transactions categorized as 'Income' and 'Expense'.
    
    Parameters:
        df (pandas.DataFrame): DataFrame containing transaction data with at least 'Date', 'Amount', and 'Category'.
    """
    df.set_index("Date", inplace=True)
    income_df = df[df["Category"] == "Income"].resample("D").sum().reindex(df.index, fill_value=0)
    expense_df = df[df["Category"] == "Expense"].resample("D").sum().reindex(df.index, fill_value=0)
    plt.figure(figsize=(10, 5))
    plt.plot(income_df["Amount"], label="Income", color="green")
    plt.plot(expense_df["Amount"], label="Expense", color="red")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expense Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()