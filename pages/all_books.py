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


def render_view_books():
    library = load_library()

    if library:
        st.title("📚 View All Books")

        # Create three columns
        columns = st.columns(3)

        for index, book in enumerate(library):
            column = columns[index % 3]

            with column:
                book_card = f"""
                <div class="book-card">
                    <h5 class="book-title">Book {index + 1}: {book["title"]}</h5>
                    <div class="book-info">
                        <p><strong>Author:</strong> {book.get("author", "Unknown")}</p>
                        <p><strong>Genre:</strong> {book.get("genre", "Not Available")}</p>
                        <p><strong>Year:</strong> {book.get("year", "Not Available")}</p>
                        <p class="read-status"><strong>Read Status:</strong> {book.get("Read_Status", "Not Available")}</p>
                    </div>
                </div>
                """
                st.markdown(book_card, unsafe_allow_html=True)
    else:
        st.write("No books found in the library.")
