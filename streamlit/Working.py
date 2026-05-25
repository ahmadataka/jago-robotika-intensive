import streamlit as st

st.set_page_config(
    page_title="My Personal Website",
    page_icon="🤖",
    layout="centered",
)

with st.sidebar:
    st.title("Navigation")
    menu = st.radio(
        "Go to",
        ["Home", "About Me", "Gallery", "Fun Zone", "Contact"],
    )

if menu == "Home":
    st.title("Welcome to My Website")
    st.write("Hello! This is my first website using Streamlit.")

elif menu == "About Me":
    st.title("About Me")
    st.write("I am a robotics engineer with a passion for building robots and software applications.")

elif menu == "Gallery":
    st.title("Gallery")
    st.write("Here is a gallery of my work.")

elif menu == "Fun Zone":
    st.title("Fun Zone")
    st.write("Here is a fun zone.")

elif menu == "Contact":
    st.title("Contact Me")
    st.write("Here is a contact me page.")