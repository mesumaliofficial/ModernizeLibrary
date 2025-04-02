import streamlit as st
st.set_page_config(layout="wide")

# Initialize the current_page if it doesn't exist in session_state
if "current_page" not in st.session_state:
    st.session_state.current_page = 'dashboard'

def load_css():
    with open("assets/css/AppStyle.css", encoding="utf-8") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

with st.sidebar:
    st.sidebar.image("assets/images/logo.svg")
    
    # Sidebar Navigation
    if st.button("Dashboard", use_container_width=True):
        st.session_state.current_page = 'dashboard'
    
    if st.button("View Books", use_container_width=True):
        st.session_state.current_page = 'all_books'

    if st.button("Add Book", use_container_width=True):
        st.session_state.current_page = 'add_book'
    
    if st.button("Search", use_container_width=True):
        st.session_state.current_page = 'search'
    
    if st.button("Analytics", use_container_width=True):
        st.session_state.current_page = 'analytics'
    
    if st.button("Recommendations", use_container_width=True):
        st.session_state.current_page = 'recommendations'
    
    if st.button("Import/Export", use_container_width=True):
        st.session_state.current_page = 'import_export'


if st.session_state.current_page == "dashboard":
    from pages.dashboard import render_dashboard
    render_dashboard()

elif st.session_state.current_page == "add_book":
    from pages.add_book import render_add_book
    render_add_book()

elif st.session_state.current_page == "all_books":
    from pages.all_books import render_view_books
    render_view_books()

load_css()