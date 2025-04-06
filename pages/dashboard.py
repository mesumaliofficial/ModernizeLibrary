import streamlit as st
import pandas as pd
import altair as alt
import json
import os

library_file = "data/library.json"
def load_library():
    try:
        with open(library_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def render_dashboard():
    library = load_library()

    total_books = 0
    read_books = 0
    unread_books = 0

    for book in library:
        total_books += 1
        if book.get("Read_Status") == "Read":
            read_books += 1
        else: 
            unread_books += 1

    # Cards showing totals
    col1, col2, col3, = st.columns(3)

    with col1:
        st.markdown("""
        <div class="cards">
            <span>Total Books in Library</span>
            <h1 class="totals">{}</h1>
        </div>
        """.format(total_books), unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="cards">
            <span>Read Books in Library</span>
            <h1 class="totals">{}</h1>
        </div>
        """.format(read_books), unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="cards">
            <span>Unread Books in Library</span>
            <h1 class="totals">{}</h1>
        </div>
        """.format(unread_books), unsafe_allow_html=True)    

        st.write("")
        st.write("")
        st.write("")

    # Data for the bar chart
    data = {
        "Categories": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],
        "Values": [50, 10, 80, 40, 70, 20, 60, 30, 90, 15, 100, 25, 110, 35, 120, 45, 130, 55, 140, 65, 150, 75, 160, 85, 170, 95],
        "Group": ["X", "X", "Y", "Y", "X", "X", "Y", "Y", "X", "X", "Y", "Y", "X", "X", "Y", "Y", "X", "X", "Y", "Y", "X", "X", "Y", "Y", "X", "X"]
    }
    df = pd.DataFrame(data)

    # Create and display the bar chart
    chart = alt.Chart(df).mark_bar().encode(
        x="Categories",
        y="Values",
        color="Group:N"
    ).properties(width=600)

    # Display the chart
    st.altair_chart(chart, use_container_width=True)
