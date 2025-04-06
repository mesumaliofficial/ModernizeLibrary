import streamlit as st
import json
import pandas as pd
import altair as alt

library_file = "data/library.json"
def load_library():
    try:
        with open(library_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def render_analytics():
    library = load_library()

    st.title("Analytics")
    if not library:
        st.warning("No data found.")
        return
    df = pd.DataFrame(library)

    if "Read_Status" not in df.columns:
        df["Read_Status"] = "Unread"

    if "genre" in df.columns:
        genre_chart = alt.Chart(df).mark_bar().encode(
            x = alt.X("genre:N",  title="Genre"),
            y = alt.Y("count():Q", title="Number of Books"),
            color = alt.Color('genre:N',
            scale = alt.Scale(domain=df['genre'].unique().tolist(),
            range = ["#00B5E2", "#1E3A8A"]))
        ).properties(title="Books by Genre", width=400)
        st.altair_chart(genre_chart)

    col1, col2 = st.columns(2)

    with col1:
        if "author" in df.columns:
            author_chart = alt.Chart(df).mark_bar().encode(
                x = alt.X("author:N",  title="Author"),
                y = alt.Y("count():Q", title="Number of Books"),
                color = alt.Color('author:N',
                scale = alt.Scale(domain=df['author'].unique().tolist(),
                range = ["#00B5E2", "#1E3A8A"]))
            ).properties(title="Books by Author", width=400)
            st.altair_chart(author_chart)

    with col2:
        read_counts = df["Read_Status"].value_counts().reset_index()
        read_counts.columns = ["Read_Status", "Count"]

        pie_chart = alt.Chart(read_counts).mark_arc().encode(
        theta=alt.Theta(field="Count", type="quantitative"),
        color=alt.Color(field="Read_Status", type="nominal",
            scale=alt.Scale(domain=read_counts["Read_Status"].tolist(),
            range=["#00B5E2", "#1E3A8A"]))
        ).properties(title="Books Read Status", width=400, height=400)
        st.altair_chart(pie_chart)

    if "year" in df.columns:
        year_chart = alt.Chart(df).mark_bar().encode(
            x=alt.X("year:O", title="Year"),
            y=alt.Y("count()", title="Books Published"),
            color="year:O"
        ).properties(title="Books by Year", width=600)

        st.altair_chart(year_chart)