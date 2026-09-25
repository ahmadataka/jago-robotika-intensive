import random

import streamlit as st

st.title("Chatbot with Memory")
st.caption("Chatbot sekarang mengingat percakapan selama app masih terbuka.")

bot_name = st.sidebar.selectbox("Pilih nama chatbot", ["Robo", "Milo", "Luna"])

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": f"Halo! Aku {bot_name}. Ada yang ingin kamu tanyakan?"}
    ]

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = [
        {"role": "assistant", "content": f"Halo! Aku {bot_name}. Mari mulai percakapan baru!"}
    ]
    st.rerun()

for item in st.session_state.messages:
    with st.chat_message(item["role"]):
        st.write(item["content"])

message = st.chat_input("Ketik pesan di sini...")

if message:
    st.session_state.messages.append({"role": "user", "content": message})

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
    bot_message = f"**{bot_name}:** {answer}"
    st.session_state.messages.append({"role": "assistant", "content": bot_message})

    with st.chat_message("assistant"):
        st.write(bot_message)
