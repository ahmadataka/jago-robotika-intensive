import streamlit as st

st.title("My First Chatbot App")
st.write("Hari ini kita belajar membuat app chatbot sederhana dengan Streamlit.")

st.sidebar.title("Menu")
topic = st.sidebar.selectbox("Pilih topik", ["Robot", "Game", "Sekolah"])
st.sidebar.write("Pilih topik lalu isi nama kamu.")

name = st.text_input("Siapa namamu?")
mood = st.radio("Bagaimana perasaanmu hari ini?", ["Senang", "Semangat", "Penasaran"])

if st.button("Sapa Aku"):
    if name:
        st.success(f"Halo {name}!")
        st.write(f"Hari ini kamu merasa {mood.lower()}.")
        st.write(f"Aku siap ngobrol tentang {topic.lower()}.")
    else:
        st.warning("Tulis nama dulu ya.")
