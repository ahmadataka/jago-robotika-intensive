import streamlit as st

st.title("AI Request Simulator")
st.caption("Pelajari prompt, request, dan response sebelum memakai Gemini sungguhan.")
st.warning("Mode simulasi: app ini belum mengirim data ke AI atau internet.")

st.sidebar.header("Alur AI Chatbot")
st.sidebar.write("Pertanyaan -> Prompt -> Request -> Response")

role = st.selectbox(
    "Peran AI",
    ["Tutor sains", "Tutor Python", "Pemandu museum"],
)
response_style = st.selectbox(
    "Format jawaban",
    ["Jawaban singkat", "Daftar 3 poin", "Kuis 1 soal"],
)
question = st.text_area("Pertanyaan", placeholder="Contoh: Mengapa langit berwarna biru?")
safe_to_send = st.checkbox("Saya tidak memasukkan password, alamat, atau data pribadi.")

if st.button("Kirim Simulasi"):
    if not question.strip():
        st.warning("Tulis pertanyaan terlebih dahulu.")
    elif not safe_to_send:
        st.error("Periksa safety terlebih dahulu sebelum mengirim prompt.")
    else:
        st.info("Lanjutkan dengan menyusun prompt, request, dan response simulasi.")
