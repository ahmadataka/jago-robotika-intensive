import streamlit as st

st.title("AI Request Simulator")
st.caption("Pelajari prompt, request, dan response sebelum memakai Gemini sungguhan.")
st.warning("Mode simulasi: app ini belum mengirim data ke AI atau internet.")

st.sidebar.header("Alur AI Chatbot")
st.sidebar.write("1. Pengguna menulis pertanyaan")
st.sidebar.write("2. App menyusun prompt")
st.sidebar.write("3. API menerima request")
st.sidebar.write("4. Model mengirim response")

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
        prompt = f"""Peran: Kamu adalah {role.lower()}.
Tugas: Jawab pertanyaan pengguna dengan bahasa yang mudah dipahami siswa.
Format: {response_style}.
Pertanyaan: {question.strip()}"""

        request_data = {
            "model": "gemini-simulation",
            "prompt": prompt,
        }
        response_data = {
            "status": "success",
            "text": f"[SIMULASI] AI akan membuat {response_style.lower()} untuk: {question.strip()}",
        }

        st.subheader("1. Prompt")
        st.code(prompt)

        request_col, response_col = st.columns(2)
        request_col.subheader("2. Request")
        request_col.json(request_data)
        response_col.subheader("3. Response")
        response_col.json(response_data)

        with st.chat_message("assistant"):
            st.write(response_data["text"])

        st.info("Pada Week 11, response simulasi ini akan diganti dengan jawaban Gemini sungguhan.")
