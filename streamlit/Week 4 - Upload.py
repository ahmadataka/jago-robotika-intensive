import streamlit as st

st.set_page_config(page_title="Upload Your Photo", layout="centered")

st.title("Image Upload App")
st.write("Upload gambar kamu dan lihat hasilnya di bawah")

uploaded_file = st.file_uploader(
    "Pilih file gambar",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    if uploaded_file.size > 3000000:
        st.error("File terlalu besar")
    else:
        st.success("Gambar berhasil diupload")
        lebar = st.slider("Lebar gambar", 100, 900, 500)      
        st.image(uploaded_file, width = lebar)
        st.write("Tipe Data: ", uploaded_file.type)
        st.write("Nama File: ", uploaded_file.name)
        st.write("Ukuran File: ", uploaded_file.size)
else:
    st.warning("Gambar belum diupload")














# if uploaded_file is not None:
#     
#     st.success("Gambar berhasil diupload")
# 
#     st.subheader("Preview Gambar")
# 
#     width = st.slider("Atur ukuran gambar", 100, 800, 400)
# 
#     st.image(uploaded_file, width=width)
# 
#     st.subheader("Informasi File")
# 
#     st.write("Nama file:", uploaded_file.name)
#     st.write("Tipe file:", uploaded_file.type)
#     st.write("Ukuran file (bytes):", uploaded_file.size)
# 
# else:
#     st.warning("Silakan upload gambar terlebih dahulu")