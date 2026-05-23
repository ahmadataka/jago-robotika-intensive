import streamlit as st

st.set_page_config(page_title="Pembuat Caption gambar Otomatis", layout="centered")

st.title("Pembuat Caption Gambar")

st.write("Selamat datang di website untuk membuat caption pada gambar secara otomatis!")

uploaded_file = st.file_uploader("Upload gambarmu!", type=["jpg","jpeg", "png"])

jenis = st.selectbox("Pilih jenis gambarmu", ["hewan", "orang", "makanan", "tempat", "lain-lain"])

style = st.selectbox("Pilih style caption-mu", ["serius", "lucu", "simpel", "gaul", "aneh"])

if uploaded_file:
    st.image(uploaded_file)
    
tombol=st.button("Buat caption-mu!")

captions = {
    "hewan": {
        "lucu": 
            "Hewan ini sepertinya sedang merencanakan sesuatu."
        ,
        "serius": 
            "Ini adalah kingdom animalia"
        ,
        "simpel": 
            "Ini hewan"
        ,
        "gaul": 
            "gue hewan lho"
        ,
        "aneh": 
            "aku lapar"
    },
    "orang": {
        "lucu": 
            "Orang ini sepertinya sedang merencanakan sesuatu."
        ,
        "serius": 
            "Ini adalah homo sapiens"
        ,
        "simpel": 
            "Ini orang"
        ,
        "gaul": 
            "gue orang lho"
        ,
        "aneh": 
            "aku lapar"
    },
    "makanan": {
        "lucu": 
            "Makanan ini sepertinya sedang merencanakan sesuatu."
        ,
        "serius": 
            "Ini adalah makanan yang enak"
        ,
        "simpel": 
            "Ini makanan, bukan hewan"
        ,
        "gaul": 
            "ayo makan gue"
        ,
        "aneh": 
            "kamu lapar?"
    },
    "tempat": {
        "lucu": 
            "Hewan ini sepertinya sedang merencanakan sesuatu."
        ,
        "serius": 
            "Ini adalah kingdom animalia"
        ,
        "simpel": 
            "Ini hewan"
        ,
        "gaul": 
            "gue hewan lho"
        ,
        "aneh": 
            "aku lapar"
    },
    "lain-lain": {
        "lucu": 
            "Hewan ini sepertinya sedang merencanakan sesuatu."
        ,
        "serius": 
            "Ini adalah kingdom animalia"
        ,
        "simpel": 
            "Ini hewan"
        ,
        "gaul": 
            "gue hewan lho"
        ,
        "aneh": 
            "aku lapar"
    }
    }
if tombol and uploaded_file:
    caption = captions[jenis][style]
    st.success(caption)
elif tombol and not uploaded_file:
    st.warning("Upload dulu file-mu!")