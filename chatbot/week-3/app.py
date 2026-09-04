import streamlit as st

st.title("Rule-Based Chatbot")
st.write("Chatbot ini mulai menjawab berdasarkan kata yang kamu tulis.")

bot_name = st.sidebar.selectbox("Pilih nama chatbot", ["Robo", "Milo", "Luna"])
st.sidebar.write("Coba tulis: halo, nama, robot, atau python.")

message = st.text_input("Kamu:", placeholder="Contoh: Halo, Robo!")

if st.button("Kirim Pesan"):
    if message:
        clean_message = message.lower().strip()

        if "halo" in clean_message:
            answer = "Halo juga! Senang bisa ngobrol denganmu."
        elif "nama" in clean_message:
            answer = f"Namaku {bot_name}. Aku chatbot buatanmu!"
        elif "robot" in clean_message:
            answer = "Robot adalah mesin yang dapat diprogram untuk melakukan tugas."
        elif "python" in clean_message:
            answer = "Python adalah bahasa pemrograman yang kita pakai untuk membuat app ini."
        else:
            answer = "Maaf, aku belum memahami pesan itu. Coba tulis halo, nama, robot, atau python."

        st.write(f"**Kamu:** {message}")
        st.success(f"**{bot_name}:** {answer}")
    else:
        st.warning("Tulis pesan dulu ya.")
