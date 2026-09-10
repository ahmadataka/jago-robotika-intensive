import random

import streamlit as st

st.title("Friendly Rule-Based Chatbot")
st.write("Chatbot ini punya beberapa variasi jawaban agar percakapannya lebih natural.")

bot_name = st.sidebar.selectbox("Pilih nama chatbot", ["Robo", "Milo", "Luna"])
st.sidebar.write("Coba tulis: halo, robot, python, atau pesan lainnya.")

message = st.text_input("Kamu:", placeholder="Contoh: Aku suka membuat robot!")

if st.button("Kirim Pesan"):
    if message:
        clean_message = message.lower().strip()

        if "halo" in clean_message or "hai" in clean_message:
            answers = [
                "Halo juga! Senang bertemu denganmu.",
                "Hai! Ada yang ingin kamu tanyakan?",
                "Halo! Aku siap mengobrol denganmu.",
            ]
        elif "robot" in clean_message:
            if "suka" in clean_message or "membuat" in clean_message:
                answers = [
                    "Keren! Membuat robot melatih kreativitas dan logika.",
                    "Aku juga suka robot. Robot apa yang ingin kamu buat?",
                ]
            else:
                answers = [
                    "Robot adalah mesin yang dapat diprogram.",
                    "Robot memakai sensor, program, dan bagian yang bisa bergerak.",
                ]
        elif "python" in clean_message:
            answers = [
                "Python adalah bahasa yang ramah untuk belajar coding.",
                "Kita memakai Python untuk membuat chatbot ini.",
            ]
        else:
            answers = [
                "Aku belum memahami pesan itu. Coba tanyakan tentang robot atau Python.",
                "Hmm, aku masih belajar. Coba gunakan kata halo, robot, atau Python.",
            ]

        answer = random.choice(answers)
        st.write(f"**Kamu:** {message}")
        st.success(f"**{bot_name}:** {answer}")
    else:
        st.warning("Tulis pesan dulu ya.")
