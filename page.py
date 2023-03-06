import streamlit as st
from streamlit_option_menu import option_menu


# as horizontal menu
selected = option_menu(
    menu_title="Main Menu",  # required
    options=["Home", "My works", "Contact"],  # required
    icons=["house", "book", "envelope"],  # required
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="horizontal",
)

if selected == "Home":
    st.title(f"You have selected {selected}")
if selected == "My works":
    st.title(f"You have selected {selected}")
if selected == "Contact":
    st.title(f"You have selected {selected}")
