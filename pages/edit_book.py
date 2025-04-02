import streamlit as st
import json

library_file = "data/library.json"

def load_library():
    try:
        with open(library_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_library(library):
    with open(library_file, "w", encoding="utf-8") as file:
        json.dump(library, file, indent=4)
    

def render_edit_book(selected_book):
    st.title("✏️ Edit Book")

    with st.form("edit_form"):
        col1, col2 = st.columns(2)

        with col1:
            book_author = st.text_input("Author", selected_book["author"])

        with col2:
            book_title = st.text_input("Book Title", selected_book["title"])

        # Input fields for book details
        book_genre = st.text_input("Genre (Book Category)", selected_book["genre"])
        book_year = st.number_input("Publication Year", min_value=1000, max_value=9999, step=1, value=selected_book["year"])
        read_status = st.radio("Have you read this book?", ["Read", "Unread"], index=["Read", "Unread"].index(selected_book.get("read_status", "Unread")))

        submit_button = st.form_submit_button("Save Changes")

        if submit_button:
            library = load_library()

            # Find and update the selected book in the library
            for book in library:
                if book["title"] == selected_book["title"]:
                    book["title"] = book_title
                    book["author"] = book_author
                    book["genre"] = book_genre
                    book["year"] = book_year
                    book["read_status"] = read_status
                    break

            # Save the updated library to the file
            save_library(library)
            st.success("Book details updated successfully! ✅")

            st.session_state["edit_mode"] = False  
            st.rerun()  # This will refresh the app
