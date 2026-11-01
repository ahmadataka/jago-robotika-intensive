import os

from google import genai
from google.genai import errors
import streamlit as st

MODEL_NAME = "gemini-3.5-flash-lite"

st.title("My First Gemini App")
st.caption("Kirim satu prompt ke Gemini dan tampilkan responsenya.")

model_name = st.sidebar.selectbox(
    "Model Gemini",
    [MODEL_NAME, "gemini-3.8-flash", "gemini-3.1-flash-lite"],
)


def get_api_key():
    try:
        return st.secrets.get("GEMINI_API_KEY", "") or os.getenv("GEMINI_API_KEY", "")
    except FileNotFoundError:
        return os.getenv("GEMINI_API_KEY", "")


api_key = get_api_key()

if not api_key:
    st.error("GEMINI_API_KEY belum ditemukan.")
    st.code('GEMINI_API_KEY = "PASTE_API_KEY_DI_SINI"', language="toml")
    st.info("Simpan baris tersebut di file .streamlit/secrets.toml, bukan di app.py.")
    st.stop()

client = genai.Client(api_key=api_key, http_options={"timeout": 30000})

role = st.selectbox(
    "Peran Gemini",
    ["Tutor sains", "Tutor Python", "Pemandu museum"],
)
question = st.text_area("Pertanyaan", placeholder="Contoh: Jelaskan cara kerja sensor ultrasonik.")
safe_to_send = st.checkbox("Saya tidak memasukkan password, alamat, atau data pribadi.")

if st.button("Tanya Gemini"):
    if not question.strip():
        st.warning("Tulis pertanyaan terlebih dahulu.")
    elif not safe_to_send:
        st.error("Periksa safety sebelum mengirim prompt.")
    else:
        prompt = f"""Kamu adalah {role.lower()}.
Jawab dengan bahasa Indonesia yang mudah dipahami siswa.
Berikan jawaban singkat dan jelas.
Pertanyaan: {question.strip()}"""

        with st.spinner("Gemini sedang berpikir..."):
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt,
                )
                answer = response.text or "Gemini belum memberikan jawaban."
                st.subheader("Jawaban Gemini")
                st.write(answer)
            except errors.APIError as error:
                if error.code == 503:
                    st.error("Gemini sedang sibuk (503). Coba lagi nanti atau pilih model lain di sidebar.")
                elif error.code == 429:
                    st.error("Batas request atau kuota tercapai (429). Periksa Usage di Google AI Studio.")
                elif error.code in (401, 403):
                    st.error("Akses ditolak. Periksa status API key dan izin project di Google AI Studio.")
                elif error.code == 404:
                    st.error("Model tidak ditemukan (404). Pilih model lain di sidebar.")
                else:
                    st.error(f"Gemini menolak request (kode {error.code}). Periksa key, model, dan status project.")
            except Exception:
                st.error("Request gagal tersambung. Periksa koneksi internet lalu coba lagi.")

st.caption(f"Model: {model_name}")
