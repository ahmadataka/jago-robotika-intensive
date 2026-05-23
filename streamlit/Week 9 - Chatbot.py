import streamlit as st
import random

st.set_page_config(page_title="Mini Chatbot", layout="centered")

st.title("Mini Chatbot")
st.write("Chat dengan chatbot sederhana buatan sendiri")

# =========================
# INIT CHAT HISTORY
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================
# DISPLAY CHAT HISTORY
# =========================
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

# =========================
# USER INPUT
# =========================
user_input = st.chat_input("Ketik pesan di sini...")

# =========================
# CHATBOT LOGIC
# =========================
if user_input:

    # tampilkan pesan user
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    text = user_input.lower()

    # =========================
    # RULE-BASED RESPONSES
    # =========================
    if "halo" in text or "hai" in text:
        bot_reply = random.choice([
            "Halo juga!",
            "Hai! Apa kabar?",
            "Senang bertemu denganmu!"
        ])

    elif "nama" in text:
        bot_reply = "Namaku MiniBot 🤖"

    elif "umur" in text:
        bot_reply = "Aku tidak punya umur, aku adalah program komputer."

    elif "robot" in text:
        bot_reply = "Robot adalah mesin yang bisa diprogram untuk melakukan tugas tertentu."

    elif "python" in text:
        bot_reply = "Python adalah bahasa pemrograman yang mudah dipelajari."

    elif "sekolah" in text:
        bot_reply = "Belajar di sekolah itu penting dan menyenangkan."

    elif "hobi" in text:
        bot_reply = "Hobiku membantu manusia belajar coding!"

    elif "bye" in text or "dadah" in text:
        bot_reply = "Sampai jumpa lagi!"

    else:
        bot_reply = random.choice([
            "Menarik sekali!",
            "Coba ceritakan lebih banyak.",
            "Aku masih belajar memahami itu.",
            "Wah, seru juga!",
            "Bisa jelaskan lagi?"
        ])

    # =========================
    # SAVE BOT RESPONSE
    # =========================
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_reply
    })

    # =========================
    # DISPLAY BOT RESPONSE
    # =========================
    with st.chat_message("assistant"):
        st.write(bot_reply)

# =========================
# SIDEBAR
# =========================
with st.sidebar:

    st.header("Tentang App")

    st.write("Mini chatbot sederhana menggunakan Streamlit")

    if st.button("Hapus Chat"):

        st.session_state.messages = []

        st.rerun()