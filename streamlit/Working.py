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
    st.image("https://images.unsplash.com/photo-1506744038136-46273834b3fb", use_container_width=True)
    st.success("My website is now online!")
elif menu == "About Me":
    st.title("About Me")
    st.write("I am a robotics engineer with a passion for building robots and software applications.")
    name = st.text_input("What is your name?")
    if name:
        st.write(f"Hello {name}! Welcome to my website.")
elif menu == "Gallery":
    st.title("Gallery")
    st.write("Here is a gallery of my work.")
    uploaded_image = st.file_uploader("Upload your image", type=["jpg", "jpeg", "png"])
    if uploaded_image:
        st.image(uploaded_image, use_container_width=True)
        st.success("Image uploaded successfully!")
    else:
        st.info("Please upload an image.")
elif menu == "Fun Zone":
    st.title("Fun Zone")
    st.write("Here is a fun zone.")
    
    if "playlist" not in st.session_state:
        st.session_state.playlist = []

    uploaded_file = st.file_uploader("Upload lagu", type=["mp3"])

    if uploaded_file:
        if st.button("Tambah ke Playlist"):
            st.session_state.playlist.append(uploaded_file)

    st.subheader("Playlist")

    if st.session_state.playlist:
        song_names = [file.name for file in st.session_state.playlist]
        selected = st.selectbox("Pilih lagu", song_names)

        for file in st.session_state.playlist:
            if file.name == selected:
                st.audio(file)


elif menu == "Contact":
    st.title("Contact Me")
    st.write("Here is a contact me page.")
    email = st.text_input("Your email")
    message = st.text_area("Your message")
    if st.button("Send"):
        if email and message:
            st.success("Message sent successfully!")
        else:
            st.warning("Please complete all fields.")