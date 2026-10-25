import cv2
import numpy as np
from PIL import Image
import streamlit as st

st.title("Vision Playground")
st.write("Pilih mini project untuk bereksperimen dengan gambar.")

project = st.sidebar.selectbox(
    "Pilih project",
    ["Color Object Counter", "Grayscale Filter", "Edge Filter"],
)
input_mode = st.sidebar.radio("Sumber gambar", ["Kamera", "Upload"])

if project == "Color Object Counter":
    target_color = st.sidebar.selectbox("Warna target", ["Merah", "Hijau", "Biru"])
    minimum_area = st.sidebar.slider("Ukuran objek minimum", 100, 5000, 500, 100)

if input_mode == "Kamera":
    input_file = st.camera_input("Ambil satu frame")
else:
    input_file = st.file_uploader("Upload gambar", type=["png", "jpg", "jpeg"])

if input_file:
    image = Image.open(input_file).convert("RGB")
    image_array = np.array(image)

    st.image(image, caption="Gambar asli", width="stretch")
    st.info("Lanjutkan dengan filter atau Color Object Counter.")
else:
    st.info("Gunakan kamera atau upload gambar untuk memulai mini project.")
