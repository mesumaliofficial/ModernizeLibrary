import streamlit as st
import pandas as pd
import altair as alt

def render_dashboard():
    # Cards showing totals
    col1, col2, col3, = st.columns(3)

    with col1:
        st.markdown("""
        <div class="cards">
            <span>Total Books in Library</span>
            <h1 class="totals">18</h1>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="cards">
            <span>Read Books in Library</span>
            <h1 class="totals">4</h1>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="cards">
            <span>Unread Books in Library</span>
            <h1 class="totals">14</h1>
        </div>
        """, unsafe_allow_html=True)    

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
