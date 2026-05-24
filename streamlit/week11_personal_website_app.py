import streamlit as st

st.set_page_config(
    page_title="My Personal Website",
    page_icon="🌟",
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
    st.image(
        "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
        use_container_width=True,
    )
    st.success("My website is now online!")

elif menu == "About Me":
    st.title("About Me")
    name = st.text_input("What is your name?", "Ahmad")
    hobby = st.text_input("What is your hobby?", "Coding")
    favorite_food = st.text_input("Favorite food?", "Pizza")

    st.subheader("Profile")
    st.write(f"Name: {name}")
    st.write(f"Hobby: {hobby}")
    st.write(f"Favorite Food: {favorite_food}")

elif menu == "Gallery":
    st.title("My Gallery")
    uploaded_image = st.file_uploader(
        "Upload your image",
        type=["jpg", "jpeg", "png"],
    )

    if uploaded_image:
        st.image(uploaded_image, use_container_width=True)
        st.success("Image uploaded successfully!")
    else:
        st.info("Please upload an image.")

elif menu == "Fun Zone":
    st.title("Fun Zone")
    activity = st.selectbox(
        "Choose an activity",
        ["Motivation Quote", "Play Music", "Mini Chatbot"],
    )

    if activity == "Motivation Quote":
        if st.button("Generate Quote"):
            import random

            quotes = [
                "Keep learning and never give up!",
                "Small progress is still progress.",
                "Coding is creating.",
                "Dream big and start small.",
                "Mistakes help us learn.",
            ]
            st.success(random.choice(quotes))

    elif activity == "Play Music":
        uploaded_audio = st.file_uploader(
            "Upload MP3 file",
            type=["mp3"],
        )
        if uploaded_audio:
            st.audio(uploaded_audio)

    elif activity == "Mini Chatbot":
        user_message = st.text_input("Say something")

        if user_message:
            text = user_message.lower()

            if "hello" in text or "hi" in text:
                bot_reply = "Hello there!"
            elif "name" in text:
                bot_reply = "I am MiniBot"
            elif "bye" in text:
                bot_reply = "Goodbye!"
            else:
                bot_reply = "That sounds interesting!"

            st.write("Bot:", bot_reply)

elif menu == "Contact":
    st.title("Contact Me")
    email = st.text_input("Your email")
    message = st.text_area("Your message")

    if st.button("Send"):
        if email and message:
            st.success("Message sent successfully!")
        else:
            st.warning("Please complete all fields.")

st.markdown("---")
st.caption("Created with Streamlit")
