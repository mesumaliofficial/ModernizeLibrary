import streamlit as st
import json

library_file = "data/library.json"


# Function to load existing library from the JSON file
def load_library():
    try:
        with open(library_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def render_delete_book(book_index):
    library = load_library()
    if 0 <= book_index < len(library):
        library.pop(book_index)

        with open(library_file, "w") as file:
            json.dump(library, file, indent=4)

            return True

    else:
        return False
    