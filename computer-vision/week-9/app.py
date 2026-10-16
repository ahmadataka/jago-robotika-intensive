import cv2
import numpy as np
from PIL import Image
import streamlit as st

st.title("Face Detector")
st.write("Gunakan model siap pakai untuk menemukan wajah pada gambar.")

input_mode = st.sidebar.radio("Sumber gambar", ["Kamera", "Upload"])
minimum_size = st.sidebar.slider("Ukuran wajah minimum", 30, 150, 50, 10)
st.sidebar.info("Face detection menemukan posisi wajah, bukan mengenali identitas orang.")

if input_mode == "Kamera":
    input_file = st.camera_input("Ambil satu frame")
else:
    input_file = st.file_uploader("Upload gambar", type=["png", "jpg", "jpeg"])

if input_file:
    image = Image.open(input_file).convert("RGB")
    image_array = np.array(image)
    grayscale = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)

    model_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    face_detector = cv2.CascadeClassifier(model_path)
    faces = face_detector.detectMultiScale(
        grayscale,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(minimum_size, minimum_size),
    )

    result = image_array.copy()
    for x, y, width, height in faces:
        cv2.rectangle(result, (x, y), (x + width, y + height), (255, 80, 40), 5)

    left, right = st.columns(2)
    left.image(image, caption="Gambar asli", width="stretch")
    right.image(result, caption="Hasil face detection", width="stretch")

    st.metric("Jumlah wajah", len(faces))

    if len(faces) > 0:
        st.success("Wajah terdeteksi. Coba ubah jarak atau sudut kamera.")
    else:
        st.warning("Wajah belum terdeteksi. Coba posisi lebih dekat dan cahaya lebih terang.")
else:
    st.info("Gunakan kamera atau upload gambar yang menampilkan wajah dari arah depan.")
