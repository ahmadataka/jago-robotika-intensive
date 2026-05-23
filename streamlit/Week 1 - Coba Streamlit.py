import streamlit as st

st.title("Counter App")

if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Tambah"):
    st.session_state.count += 1

if st.button("Reset"):
    st.session_state.count = 0

st.write("Nilai sekarang:", st.session_state.count)

if st.session_state.count > 10:
    st.success("Sukses")