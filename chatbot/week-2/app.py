import streamlit as st

st.title("My First Chatbot")
st.write("Tulis pesan untuk memulai percakapan dengan chatbot.")

bot_name = st.sidebar.selectbox("Pilih nama chatbot", ["Robo", "Milo", "Luna"])
st.sidebar.write("Chatbot ini masih belajar. Minggu depan ia akan belajar menjawab berdasarkan kata kunci.")

message = st.text_input("Kamu:", placeholder="Contoh: Halo, aku suka robot!")

if st.button("Kirim Pesan"):
    if message:
        st.write(f"**Kamu:** {message}")
        st.success(f"**{bot_name}:** Halo! Aku menerima pesanmu. Senang bisa ngobrol denganmu!")
    else:
        st.warning("Tulis pesan dulu ya.")
