import streamlit as st
from st_pages import Page
from st_pages import show_pages

show_pages([
    Page("postitApp/pages/home.py", "Home", "🏠"),
    Page("postitApp/pages/postit.py", "Post it", "📝")
]
)

