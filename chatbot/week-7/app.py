import streamlit as st

BOT_NAME = "Nova"

st.title("Space Explorer Bot")
st.caption("Tanyakan fakta sederhana tentang luar angkasa.")

st.sidebar.header("Tentang Chatbot")
st.sidebar.write("Nova adalah chatbot bertema luar angkasa.")
st.sidebar.write("Coba gunakan kata: planet, matahari, bulan, atau astronaut.")

responses = {
    "planet": "Planet adalah benda langit yang mengelilingi sebuah bintang.",
    "matahari": "Matahari adalah bintang yang menjadi pusat tata surya kita.",
    "bulan": "Bulan adalah satelit alami Bumi.",
    "astronaut": "Astronaut adalah orang yang dilatih untuk pergi ke luar angkasa.",
}

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": f"Halo! Aku {BOT_NAME}. Ayo belajar luar angkasa!"}
    ]

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = [
        {"role": "assistant", "content": f"Halo! Aku {BOT_NAME}. Mulai lagi, yuk!"}
    ]
    st.rerun()

for item in st.session_state.messages:
    with st.chat_message(item["role"]):
        st.write(item["content"])

message = st.chat_input("Tulis pertanyaan tentang luar angkasa...")

if message:
    st.session_state.messages.append({"role": "user", "content": message})

    with st.chat_message("user"):
        st.write(message)

    answer = "Maaf, aku belum tahu. Coba tanyakan planet, matahari, bulan, atau astronaut."
    clean_message = message.lower().strip()

    for keyword, response in responses.items():
        if keyword in clean_message:
            answer = response
            break

    bot_message = f"**{BOT_NAME}:** {answer}"
    st.session_state.messages.append({"role": "assistant", "content": bot_message})

    with st.chat_message("assistant"):
        st.write(bot_message)
