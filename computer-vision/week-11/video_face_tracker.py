import time

import cv2
import streamlit as st

st.title("Live Face Tracker")
st.write("Kotak dan titik pusat mengikuti wajah saat kamera berjalan.")

minimum_size = st.sidebar.slider("Ukuran wajah minimum", 30, 150, 50, 10)
st.sidebar.info("Jalankan di laptop sendiri. OpenCV membuka kamera pada komputer yang menjalankan Python.")
run_camera = st.checkbox("Jalankan kamera")

model_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_detector = cv2.CascadeClassifier(model_path)
preview = st.empty()
status = st.empty()

if run_camera:
    camera = cv2.VideoCapture(0)
    try:
        if not camera.isOpened():
            st.error("Kamera tidak dapat dibuka. Periksa izin kamera dan tutup aplikasi kamera lain.")
        else:
            while run_camera:
                success, frame = camera.read()
                if not success:
                    st.warning("Frame kamera tidak terbaca. Matikan checkbox lalu coba lagi.")
                    break

                image_array = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                grayscale = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
                faces = face_detector.detectMultiScale(
                    grayscale,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(minimum_size, minimum_size),
                )

                result = image_array.copy()
                for x, y, width, height in faces:
                    cv2.rectangle(result, (x, y), (x + width, y + height), (255, 80, 40), 5)
                    center_x = x + width // 2
                    center_y = y + height // 2
                    cv2.circle(result, (center_x, center_y), 5, (0, 200, 80), -1)

                preview.image(result, caption="Live face detection", width="stretch")
                status.write(f"Jumlah wajah: {len(faces)}")
                time.sleep(0.05)
    finally:
        camera.release()
else:
    st.info("Centang Jalankan kamera untuk mulai. Hilangkan centang untuk berhenti.")
