#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
import os.path
from json import dump, load

def save_to_json_file(my_list, filename):
    """Save a list to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as f:
        dump(my_list, f)

def load_from_json_file(filename):
    """Load a list from a JSON file."""
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return load(f)
    return []

if __name__ == "__main__":
    # Define the filename for the JSON file
    filename = "add_item.json"
    
    # Load the existing list from the JSON file
    my_list = load_from_json_file(filename)
    
    # Extend the list with command-line arguments
    my_list.extend(sys.argv[1:])
    
    # Save the updated list back to the JSON file
    save_to_json_file(my_list, filename)
