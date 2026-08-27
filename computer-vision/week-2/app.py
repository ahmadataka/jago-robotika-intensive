import numpy as np
from PIL import Image
import streamlit as st

st.title("Pixel Playground")
st.write("Lihat bagaimana gambar dibaca sebagai angka RGB, lalu coba efek sederhana.")

uploaded_file = st.file_uploader("Upload gambar", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    pixels = np.array(image)
    red, green, blue = pixels[0, 0]

    effect = st.selectbox("Pilih efek", ["Grayscale", "Inverse Color", "Brightness"])

    if effect == "Grayscale":
        result = np.mean(pixels, axis=2).astype(np.uint8)
    elif effect == "Inverse Color":
        result = 255 - pixels
    else:
        result = np.clip(pixels.astype(int) + 40, 0, 255).astype(np.uint8)

    left, right = st.columns(2)
    left.image(image, caption="Gambar asli", width="stretch")
    right.image(result, caption=effect, width="stretch")
    st.write(f"Pixel kiri atas: R={red}, G={green}, B={blue}")
else:
    st.info("Upload gambar dulu ya.")
