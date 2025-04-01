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
    
# Function to save library data to the JSON file
def save_library(library):
    with open(library_file, "w") as file:
        json.dump(library, file, indent=4)


def render_add_book():
    with st.form("add_form"):
        st.title("➕ Add a New Book")

        col1, col2 = st.columns(2)

        with col1:
            book_author = st.text_input("Author")

        with col2:
            book_title = st.text_input("Book Title")

        # Input fields for book details
        book_genre = st.text_input("Genre (Book Category)")
        book_year = st.number_input("Publication Year", min_value=1000, max_value=9999, step=1)
        read_status = st.radio("Have you read this book?", ["Read", "Unread"])
        
        # Submit button
        submit_button = st.form_submit_button("Add Book")
        
        if submit_button:
            new_book = {
                "title": book_title,
                "author": book_author,
                "genre": book_genre,
                "year": book_year,
                "read_status": read_status
            }

            library = load_library() 
            library.append(new_book) 
            
            # Save the updated library to the JSON file
            save_library(library)

            st.success("Book added successfully!")
            st.write("Title:", book_title)
            st.write("Author:", book_author)
            st.write("Genre:", book_genre)
            st.write("Year:", book_year)
            st.write("Read Status:", read_status)
