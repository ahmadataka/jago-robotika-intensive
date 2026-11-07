import os

from google import genai
from google.genai import errors, types
import streamlit as st

MODEL_NAME = "gemini-3.5-flash-lite"
THEMES = {
    "Tutor Python": "Bantu siswa memahami Python dengan contoh kecil dan petunjuk bertahap.",
    "Asisten Robotika": "Jelaskan robot, sensor, dan cara kerja program dengan contoh sederhana.",
    "Pembuat Cerita": "Bantu siswa membuat cerita pendek yang sesuai untuk anak sekolah.",
}


def get_api_key():
    try:
        return st.secrets.get("GEMINI_API_KEY", "") or os.getenv("GEMINI_API_KEY", "")
    except FileNotFoundError:
        return os.getenv("GEMINI_API_KEY", "")


def clear_chat():
    st.session_state.messages = []


st.title("Gemini Project Chatbot")
st.caption("Pilih tema, kirim pesan, lalu ajukan pertanyaan lanjutan.")

if "messages" not in st.session_state:
    st.session_state.messages = []

theme = st.sidebar.selectbox("Tema chatbot", list(THEMES), on_change=clear_chat)
model_name = st.sidebar.selectbox(
    "Model Gemini", [MODEL_NAME, "gemini-3.8-flash", "gemini-3.1-flash-lite"]
)
st.sidebar.button("Hapus chat", on_click=clear_chat)
st.sidebar.caption("Mengganti tema memulai percakapan baru.")
safe_to_send = st.sidebar.checkbox("Saya tidak akan memasukkan data pribadi.")
st.sidebar.caption("Pesan terbaru dan sebagian riwayat dikirim ke Gemini.")

api_key = get_api_key()
if not api_key:
    st.error("GEMINI_API_KEY belum ditemukan.")
    st.info("Gunakan .streamlit/secrets.toml seperti pada Week 11.")
    st.stop()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["text"])

if not safe_to_send:
    st.info("Centang konfirmasi di sidebar untuk mulai chat.")

question = st.chat_input(
    "Ketik pertanyaan...", disabled=not safe_to_send, max_chars=1000
)

if question and question.strip():
    question = question.strip()
    with st.chat_message("user"):
        st.write(question)

    # Streamlit uses "assistant"; Gemini uses "model" for bot replies.
    contents = []
    for message in st.session_state.messages[-10:]:
        role = "model" if message["role"] == "assistant" else "user"
        contents.append(
            types.Content(role=role, parts=[types.Part.from_text(text=message["text"])])
        )
    contents.append(
        types.Content(role="user", parts=[types.Part.from_text(text=question)])
    )

    with st.chat_message("assistant"):
        with st.spinner("Gemini sedang berpikir..."):
            try:
                with genai.Client(api_key=api_key, http_options={"timeout": 30000}) as client:
                    response = client.models.generate_content(
                        model=model_name,
                        contents=contents,
                        config=types.GenerateContentConfig(
                            system_instruction=(
                                THEMES[theme] + " Jawab singkat dalam bahasa Indonesia."
                            ),
                        ),
                    )
                answer = (response.text or "").strip()
                if answer:
                    st.write(answer)
                    st.session_state.messages.append({"role": "user", "text": question})
                    st.session_state.messages.append({"role": "assistant", "text": answer})
                else:
                    st.warning("Gemini tidak mengembalikan teks. Coba ubah pertanyaan.")
            except errors.APIError as error:
                if error.code == 503:
                    st.error("Gemini sedang sibuk (503). Pilih model lain dan kirim ulang pesan.")
                elif error.code == 429:
                    st.error("Batas request atau kuota tercapai (429). Periksa Google AI Studio.")
                elif error.code in (401, 403):
                    st.error("Akses ditolak. Periksa API key dan izin project.")
                elif error.code == 404:
                    st.error("Model tidak tersedia (404). Pilih model lain dan kirim ulang pesan.")
                else:
                    st.error(f"Request Gemini gagal (kode {error.code}).")
            except Exception:
                st.error("Request gagal. Periksa koneksi, lalu kirim ulang pesan.")
