import numpy as np
from PIL import Image
import streamlit as st

st.title("My First Computer Vision App")
st.write("Hari ini kita belajar bagaimana komputer membaca gambar.")

uploaded_file = st.file_uploader("Upload gambar", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    image_array = np.array(image)

    st.image(image, width="stretch")
    st.write("Ukuran gambar:", image.width, "x", image.height)
    st.write("Bentuk array:", image_array.shape)
    st.write("Jumlah channel warna:", image_array.shape[2])
else:
    st.info("Upload gambar dulu ya.")
