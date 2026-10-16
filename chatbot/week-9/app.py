import streamlit as st

BOT_NAME = "Nova"

st.title("Nova Space Bot")
st.caption("Chatbot bertema luar angkasa yang siap diuji dan didemokan.")

topic = st.sidebar.selectbox("Pilih topik", ["Tata Surya", "Penjelajahan"])
st.sidebar.subheader("Kemampuan")
st.sidebar.write("Menjawab pertanyaan sederhana sesuai contoh keyword.")
st.sidebar.warning("Batasan: Nova belum memakai AI dan tidak memahami semua pertanyaan.")

if topic == "Tata Surya":
    st.sidebar.write("Coba: planet terbesar, planet merah, atau matahari.")
    rules = [
        (["planet", "terbesar"], "Jupiter adalah planet terbesar di tata surya."),
        (["planet", "merah"], "Mars disebut planet merah karena permukaannya kaya zat besi."),
        (["planet"], "Tata surya kita memiliki delapan planet."),
        (["matahari"], "Matahari adalah bintang di pusat tata surya."),
    ]
else:
    st.sidebar.write("Coba: manusia di Bulan, rover Mars, atau astronaut.")
    rules = [
        (["manusia", "bulan"], "Neil Armstrong menjadi manusia pertama yang berjalan di Bulan."),
        (["rover", "mars"], "Rover Mars menjelajah permukaan dan mengirim data ke Bumi."),
        (["rover"], "Rover adalah robot penjelajah yang bekerja dari jarak jauh."),
        (["astronaut"], "Astronaut dilatih untuk bekerja di luar angkasa."),
    ]

if "unknown_questions" not in st.session_state:
    st.session_state.unknown_questions = []

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
    answer = "Maaf, pertanyaan itu belum ada dalam pengetahuanku."
    found = False

    for keywords, response in rules:
        if all(keyword in clean_message for keyword in keywords):
            answer = response
            found = True
            break

    if not found:
        st.session_state.unknown_questions.append(f"[{topic}] {message}")

    bot_message = f"**{BOT_NAME}:** {answer}"
    st.session_state.messages.append({"role": "assistant", "content": bot_message})

    with st.chat_message("assistant"):
        st.write(bot_message)

with st.sidebar.expander(f"Catatan pengujian ({len(st.session_state.unknown_questions)})"):
    if st.session_state.unknown_questions:
        for question in st.session_state.unknown_questions:
            st.write("-", question)
    else:
        st.write("Belum ada pertanyaan yang gagal dijawab.")

    if st.button("Hapus Catatan"):
        st.session_state.unknown_questions = []
        st.rerun()
