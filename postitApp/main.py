import streamlit as st
from st_pages import Page
from st_pages import show_pages

show_pages([
    Page("./pages/home.py", "Home", "🏠"),
    Page("./pages/postit.py", "Post it", "📝")
]
)

