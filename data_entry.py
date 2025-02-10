from datetime import datetime

date_format = "%d-%m-%Y"
categorie_options = {"I": "Income", "E": "Expense"}

def get_date(prompt, allow_default=False):
    """
    Prompts the user for a date input and validates the format.

    Parameters:
        prompt (str): The prompt message to display.
        allow_default (bool): If True and the input is empty, returns today's date.

    Returns:
        str: The date as a string in DD-MM-YYYY format.
    """
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
    """
    Prompts the user to enter a monetary amount and validates it.

    Parameters:
        prompt (str): The prompt message to display.

    Returns:
        float: The validated positive amount.
    """
    try:
        amount = float(input(prompt))
        if amount > 0:
            return amount
        raise ValueError
    except ValueError:
        print("Invalid amount. Please enter a valid amount.")
        return get_amount(prompt)

def get_category(prompt):
    """
    Prompts the user for a category input and validates against allowed options.

    Parameters:
        prompt (str): The prompt message to display.

    Returns:
        str: The full category name ('Income' or 'Expense').
    """
    try:
        category = input(prompt).upper()
        if category in categorie_options:
            return categorie_options[category]
        raise ValueError
    except ValueError:
        print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")
        return get_category(prompt)

def get_description(prompt):
    """
    Prompts the user to enter a description.

    Parameters:
        prompt (str): The prompt message to display.

    Returns:
        str: The entered description.
    """
    return input(prompt)