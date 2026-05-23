import streamlit as st
import time

st.title("Greeting App")

name = st.text_input("Masukkan nama kamu:")

if name:
    st.success(f"Halo, {name}! Selamat idul fitri.")

num1 = st.number_input("Angka pertama:", value=0)

num2 = st.number_input("Angka kedua:", value=0)

operation = st.selectbox(
    "Pilih operasi:",
    ["Tambah", "Kurang", "Kali", "Bagi"]
)

tombol = st.button("Hitung")
if tombol:
    if operation == "Tambah":
        result = num1 + num2
    elif operation == "Kurang":
        result = num1 - num2
    elif operation == "Bagi":
        result = num1 / num2
    else:
        result = num1 * num2
    time.sleep(5)
    st.error(f"Hasil: {result}")