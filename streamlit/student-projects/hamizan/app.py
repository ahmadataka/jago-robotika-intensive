import streamlit as st

st.set_page_config(
    page_title = "My Personal Website",
    page_icon = "🗿",
    layout = "centered"
)

with st.sidebar:
    st.title("Navigation")
    menu = st.radio(
        "Go to",
        ["Home", "About Me", "Gallery", "Fun Zone", "Contact"]
)
    
if menu == "Home":
    st.title("Welcome to my website!")
    st.write("Hello! this is my first website using Streamlit.")
elif menu == "About Me":
    st.title("About me")
    st.write("I am a robotics engineer with a passion for building robots and software appplications.")
elif menu == "Gallery":
    st.title("Gallery")
    st.write("Here is a gallery of my work.")
elif menu == "Fun Zone":
    st.title("Fun zone")
    st.write("Here is a fun zone.")
elif menu == "Contact":
    st.title("Contact me")
    st.write("Here is a contact page.")