import random

import streamlit as st

st.title("Chat UI Bot")
st.caption("Sekarang chatbot tampil seperti aplikasi percakapan.")

bot_name = st.sidebar.selectbox("Pilih nama chatbot", ["Robo", "Milo", "Luna"])
st.sidebar.write("Coba tanyakan tentang robot atau Python.")

with st.chat_message("assistant"):
    st.write(f"Halo! Aku {bot_name}. Ada yang ingin kamu tanyakan?")

message = st.chat_input("Ketik pesan di sini...")

if message:
    with st.chat_message("user"):
        st.write(message)

    clean_message = message.lower().strip()

    if "halo" in clean_message or "hai" in clean_message:
        answers = ["Halo juga!", "Hai! Senang bertemu denganmu."]
    elif "robot" in clean_message:
        answers = [
            "Robot adalah mesin yang dapat diprogram untuk melakukan tugas.",
            "Robot dapat memakai sensor untuk memahami lingkungan.",
        ]
    elif "python" in clean_message:
        answers = [
            "Python adalah bahasa pemrograman yang mudah dipelajari.",
            "Kita memakai Python untuk membuat chatbot ini.",
        ]
    else:
        answers = [
            "Aku belum memahami pesan itu. Coba tanyakan tentang robot atau Python.",
            "Aku masih belajar. Coba gunakan kata halo, robot, atau Python.",
        ]

    answer = random.choice(answers)

    with st.chat_message("assistant"):
        st.write(f"**{bot_name}:** {answer}")
