import cv2
import numpy as np
from PIL import Image
import streamlit as st

st.title("Smile / Expression Detector")
st.write("Temukan wajah, lalu cari pola senyum pada area mulut.")

input_mode = st.sidebar.radio("Sumber gambar", ["Kamera", "Upload"])
minimum_size = st.sidebar.slider("Ukuran wajah minimum", 30, 150, 50, 10)
smile_neighbors = st.sidebar.slider("Ketatnya deteksi senyum", 5, 40, 20)
st.sidebar.info("Pola senyum pada gambar tidak menentukan perasaan seseorang.")

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
    smile_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")
    faces = face_detector.detectMultiScale(
        grayscale,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(minimum_size, minimum_size),
    )

    result = image_array.copy()
    smile_count = 0
    for x, y, width, height in faces:
        mouth_y = y + height // 2
        mouth = grayscale[mouth_y:y + height, x:x + width]
        smiles = smile_detector.detectMultiScale(
            mouth, scaleFactor=1.7, minNeighbors=smile_neighbors, minSize=(20, 10)
        )
        if len(smiles) > 0:
            label = "Senyum terdeteksi"
            smile_count += 1
        else:
            label = "Senyum belum terdeteksi"

        cv2.rectangle(result, (x, y), (x + width, y + height), (255, 80, 40), 5)
        cv2.putText(result, label, (x, max(20, y - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 80, 40), 2)

    left, right = st.columns(2)
    left.image(image, caption="Gambar asli", width="stretch")
    right.image(result, caption="Hasil deteksi ekspresi", width="stretch")
    st.metric("Jumlah wajah", len(faces))
    st.metric("Senyum terdeteksi", smile_count)
else:
    st.info("Gunakan kamera atau upload gambar wajah dari arah depan.")
