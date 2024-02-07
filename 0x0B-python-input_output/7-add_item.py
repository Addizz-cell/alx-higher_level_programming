#!/usr/bin/python3
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
    filename = "add_item.json"
    my_list = load_from_json_file(filename)
    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, filename)
