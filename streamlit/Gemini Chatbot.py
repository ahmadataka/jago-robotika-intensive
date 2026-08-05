import streamlit as st
from google import genai

DEFAULT_MODEL = "gemini-3.6-flash"


st.set_page_config(
    page_title="Gemini Chatbot",
    page_icon="🤖",
    layout="centered",
)

st.title("Gemini Chatbot")
st.write("Chat dengan AI Gemini menggunakan Streamlit.")


def get_api_key() -> str:
    return st.secrets.get("GEMINI_API_KEY", "")


def build_client() -> genai.Client | None:
    api_key = get_api_key()
    if not api_key:
        return None
    return genai.Client(api_key=api_key)


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


client = build_client()

if client is None:
    st.error("GEMINI_API_KEY belum ditemukan di secrets Streamlit.")
    st.stop()


if "model_name" not in st.session_state:
    st.session_state.model_name = DEFAULT_MODEL


user_input = st.chat_input("Ketik pesan di sini...")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
    })

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Gemini sedang berpikir..."):
            try:
                history_text = "\n".join(
                    f"{message['role']}: {message['content']}"
                    for message in st.session_state.messages
                )
                response = client.models.generate_content(
                    model=st.session_state.model_name,
                    contents=history_text,
                )
                bot_reply = response.text or "Maaf, belum ada jawaban."
            except Exception as error:
                bot_reply = f"Terjadi error: {error}"

        st.write(bot_reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_reply,
    })


with st.sidebar:
    st.header("Tentang App")
    st.write("Chatbot AI sederhana menggunakan Gemini API.")
    st.session_state.model_name = st.text_input(
        "Model Gemini",
        value=st.session_state.model_name,
        help="Contoh: gemini-3.6-flash",
    ).strip() or DEFAULT_MODEL
    st.caption(f"Model aktif: {st.session_state.model_name}")

    if st.button("Hapus Chat"):
        st.session_state.messages = []
        st.rerun()
