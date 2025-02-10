'''Personal Finance Tracker Data Entry Utilities

This module provides functions for capturing and validating user input for personal finance transactions.
It includes utilities for date input, amount validation, category selection, and description entry.
'''

from datetime import datetime

date_format = "%d-%m-%Y"
categorie_options = {"I": "Income", "E": "Expense"}


def get_date(prompt, allow_default=False):
    '''Prompt the user to enter a date in DD-MM-YYYY format. If allow_default is True and no input is given, the current date is returned.

    Parameters:
        prompt (str): The message displayed to the user.
        allow_default (bool): Flag indicating whether to allow the default current date when input is empty.

    Returns:
        str: The validated date string in DD-MM-YYYY format.
    '''
    try:
        date_str = input(prompt)
        if allow_default and not date_str:
            return datetime.today().strftime(date_format)
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please use DD-MM-YYYY.")
        return get_date(prompt, allow_default)


def get_amount(prompt):
    '''Prompt the user to enter a valid positive amount.

    Parameters:
        prompt (str): The message displayed to the user.

    Returns:
        float: The validated positive amount.
    '''
    try:
        amount = float(input(prompt))
        if amount > 0:
            return amount
        raise ValueError
    except ValueError:
        print("Invalid amount. Please enter a valid amount.")
        return get_amount(prompt)


def get_category(prompt):
    '''Prompt the user to select a transaction category, either Income (I) or Expense (E).

    Parameters:
        prompt (str): The message displayed to the user.

    Returns:
        str: The full category name based on user input.
    '''
    try:
        category = input(prompt).upper()
        if category in categorie_options:
            return categorie_options[category]
        raise ValueError
    except ValueError:
        print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")
        return get_category(prompt)


def get_description(prompt):
    '''Prompt the user to enter a description for the transaction.

    Parameters:
        prompt (str): The message displayed to the user.

    Returns:
        str: The user's inputted description.
    '''
    return input(prompt)