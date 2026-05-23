import streamlit as st

st.title("My Multi Page App")


col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Home"):
        st.session_state.page = "Home"
        
with col2:
    if st.button("Profile"):
        st.session_state.page = "Profile"

with col3:
    if st.button("Settings"):
        st.session_state.page = "Settings"

with col4:
    if st.button("Calculator"):
        st.session_state.page = "Calculator"

st.write("---")

# st.write("Page = ", st.session_state.page)


if st.session_state.page == "Home":
    st.header("Home Page")
    st.write("Selamat datang di aplikasi.")

elif st.session_state.page == "Profile":
    st.header("Profile Page")
    name = st.text_input("Nama:")
    if name:
        st.success(f"Halo {name}")

elif st.session_state.page == "Settings":
    st.header("Settings Page")
    theme = st.selectbox("Pilih tema:", ["Light", "Dark"])
    st.write("Tema yang dipilih:", theme)

else:
    st.header("Calculator Page")
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
        st.success(f"Hasil: {result}")

# if "page" not in st.session_state:
#     st.session_state.page = "Home"
