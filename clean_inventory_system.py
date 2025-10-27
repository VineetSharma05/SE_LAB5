"""
A simple inventory management system.

This module allows users to add, remove, and track items in an inventory.
The inventory data is stored in a JSON file.
"""

import json
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Adds a quantity of an item to the stock."""
    if logs is None:
        logs = []
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{str(datetime.now())}: Added {qty} of {item}")


def remove_item(item, qty):
    """Removes a quantity of an item from the stock."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Error: Item '{item}' not in inventory.")


def get_qty(item):
    """Gets the current quantity of a specific item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """
    Loads inventory data from a JSON file.
    If the file is not found or corrupt, it starts with an empty inventory.
    """
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.loads(f.read())
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Info: '{file}' not found or corrupt ({e}). Starting with empty inventory.")
        stock_data = {}


def save_data(file="inventory.json"):
    """Saves the current inventory data to a JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(stock_data, indent=4))


def print_data():
    """Prints a report of all items and their quantities."""
    print("--- Items Report ---")
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")
    print("--------------------")


def check_low_items(threshold=5):
    """Returns a list of items below the threshold quantity."""
    result = []
    for item, quantity in stock_data.items():
        if quantity < threshold:
            result.append(item)
    return result


def main():
    """Main function to run the inventory program."""
    load_data()  # Load data at the start
    add_item("apple", 10)
    add_item("banana", 12)

    remove_item("apple", 3)
    remove_item("orange", 1)  # This will now print an error message

    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")

    save_data()
    print_data()


# This ensures the main() function runs only when the script is executed directly
if __name__ == "__main__":
    main()