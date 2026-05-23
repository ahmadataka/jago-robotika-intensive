import streamlit as st

st.title("My Music Player")

if "playlist" not in st.session_state:
    st.session_state.playlist = []

uploaded_file = st.file_uploader("Upload lagu", type=["mp3"])

if uploaded_file:
    if st.button("Tambah ke Playlist"):
        st.session_state.playlist.append(uploaded_file)

st.subheader("Playlist")

if st.session_state.playlist:
    song_names = [file.name for file in st.session_state.playlist]
    selected = st.selectbox("Pilih lagu", song_names)

    for file in st.session_state.playlist:
        if file.name == selected:
            st.audio(file)