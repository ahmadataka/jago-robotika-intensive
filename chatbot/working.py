import streamlit as st
from google import genai
from google.genai import errors
import os

model_name = "gemini-3.5-flash-lite"

def get_api_key():
    try:
        return st.secrets.get("GEMINI_API_KEY", "") or os.getenv("GEMINI_API_KEY", "")
    except FileNotFoundError:
        return os.getenv("GEMINI_API_KEY", "")

api_key = get_api_key()
client = genai.Client(api_key=api_key)

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
        prompt = f"""Peran: Kamu adalah {role.lower()}.
        Format: {response_style.lower()}.
        Pertanyaan: {question.strip()}.
        Jawab pertanyaan dengan baik dan mudah dipahami oleh siswa."""

        with st.spinner("Gemini sedang berpikir..."):
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt,
                )
                answer = response.text or "Gemini belum memberikan jawaban."
                st.subheader("Jawaban Gemini")
                st.write(answer)
            except Exception:
                st.error("Request gagal tersambung. Periksa koneksi internet lalu coba lagi.")