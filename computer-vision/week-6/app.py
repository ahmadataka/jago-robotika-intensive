import numpy as np
from PIL import Image, ImageOps
import streamlit as st

st.title("Webcam Frame Explorer")
st.write("Ambil satu frame dari kamera, lalu lihat bagaimana komputer memprosesnya.")

camera_frame = st.camera_input("Ambil gambar dari kamera")

if camera_frame:
    image = Image.open(camera_frame).convert("RGB")
    frame = np.array(image)
    grayscale = ImageOps.grayscale(image)

    left, right = st.columns(2)
    left.image(image, caption="Frame asli", width="stretch")
    right.image(grayscale, caption="Frame grayscale", width="stretch")

    red, green, blue = frame[0, 0]
    st.write("Ukuran frame:", image.width, "x", image.height)
    st.write("Bentuk array:", frame.shape)
    st.write(f"Pixel kiri atas: R={red}, G={green}, B={blue}")
    st.success("Satu foto kamera adalah satu frame. Banyak frame yang tampil cepat akan menjadi video.")
else:
    st.info("Izinkan akses kamera, lalu tekan tombol untuk mengambil satu frame.")
