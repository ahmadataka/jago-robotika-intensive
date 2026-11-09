import streamlit as st
from google import genai
from google.genai import errors, types
import os

model_name = "gemini-3.5-flash-lite"

def get_api_key():
    try:
        return st.secrets.get("GEMINI_API_KEY", "") or os.getenv("GEMINI_API_KEY", "")
    except FileNotFoundError:
        return os.getenv("GEMINI_API_KEY", "")

api_key = get_api_key()
client = genai.Client(api_key=api_key)

st.title("AI Chatbot")

st.sidebar.header("Alur AI Chatbot")
st.sidebar.write("Pertanyaan -> Prompt -> Request -> Response")

role = st.sidebar.selectbox(
    "Peran AI",
    ["Tutor sains", "Tutor Python", "Pemandu museum"],
)
response_style = st.sidebar.selectbox(
    "Format jawaban",
    ["Jawaban singkat", "Daftar 3 poin", "Kuis 1 soal"],
)

safe_to_send = st.sidebar.checkbox("Saya tidak memasukkan password, alamat, atau data pribadi.")

def clear_chat():
    st.session_state.messages = []

if st.sidebar.button("Hapus Chat"):
    clear_chat()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["text"])

question = st.chat_input("Tulis pertanyaan...", disabled= not safe_to_send)

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
                st.write(answer)
                st.session_state.messages.append({"role": "user", "text": question})
                st.session_state.messages.append({"role": "assistant", "text": answer})
            except Exception:
                st.error("Request gagal tersambung. Periksa koneksi internet lalu coba lagi.")