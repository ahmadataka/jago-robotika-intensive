import streamlit as st

BOT_NAME = "Nova"

st.title("Smart Space Bot")
st.caption("Chatbot bertopik dengan kombinasi beberapa keyword.")

topic = st.sidebar.selectbox("Pilih topik", ["Tata Surya", "Penjelajahan"])
st.sidebar.write("Coba pertanyaan berikut:")

if topic == "Tata Surya":
    st.sidebar.write("- Apa planet terbesar?")
    st.sidebar.write("- Apa planet merah?")
    rules = [
        (["planet", "terbesar"], "Jupiter adalah planet terbesar di tata surya."),
        (["planet", "merah"], "Mars disebut planet merah karena permukaannya kaya zat besi."),
        (["planet"], "Tata surya kita memiliki delapan planet."),
        (["matahari"], "Matahari adalah bintang di pusat tata surya."),
    ]
else:
    st.sidebar.write("- Siapa manusia pertama di Bulan?")
    st.sidebar.write("- Apa tugas rover Mars?")
    rules = [
        (["manusia", "bulan"], "Neil Armstrong menjadi manusia pertama yang berjalan di Bulan."),
        (["rover", "mars"], "Rover Mars menjelajah permukaan dan mengirim data ke Bumi."),
        (["rover"], "Rover adalah robot penjelajah yang bekerja dari jarak jauh."),
        (["astronaut"], "Astronaut dilatih untuk bekerja di luar angkasa."),
    ]

if "topic" not in st.session_state or st.session_state.topic != topic:
    st.session_state.topic = topic
    st.session_state.messages = [
        {"role": "assistant", "content": f"Halo! Aku {BOT_NAME}. Mari bahas {topic.lower()}!"}
    ]

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = [
        {"role": "assistant", "content": f"Chat dibersihkan. Tanyakan tentang {topic.lower()}, ya!"}
    ]
    st.rerun()

for item in st.session_state.messages:
    with st.chat_message(item["role"]):
        st.write(item["content"])

message = st.chat_input(f"Tanyakan tentang {topic.lower()}...")

if message:
    st.session_state.messages.append({"role": "user", "content": message})
    with st.chat_message("user"):
        st.write(message)

    clean_message = message.lower().strip()
    answer = f"Aku belum memahami pertanyaan itu. Coba lihat contoh topik {topic.lower()} di sidebar."

    for keywords, response in rules:
        if all(keyword in clean_message for keyword in keywords):
            answer = response
            break

    bot_message = f"**{BOT_NAME}:** {answer}"
    st.session_state.messages.append({"role": "assistant", "content": bot_message})

    with st.chat_message("assistant"):
        st.write(bot_message)
