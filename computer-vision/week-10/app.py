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

    if project == "Grayscale Filter":
        result = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
        st.image(result, caption="Grayscale Filter", width="stretch")

    elif project == "Edge Filter":
        grayscale = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
        result = cv2.Canny(grayscale, 80, 160)
        st.image(result, caption="Edge Filter", width="stretch")

    else:
        hsv = cv2.cvtColor(image_array, cv2.COLOR_RGB2HSV)

        if target_color == "Merah":
            mask_1 = cv2.inRange(hsv, (0, 100, 70), (10, 255, 255))
            mask_2 = cv2.inRange(hsv, (170, 100, 70), (179, 255, 255))
            mask = mask_1 | mask_2
        elif target_color == "Hijau":
            mask = cv2.inRange(hsv, (40, 70, 50), (85, 255, 255))
        else:
            mask = cv2.inRange(hsv, (95, 70, 50), (135, 255, 255))

        mask = cv2.medianBlur(mask, 7)
        total_labels, labels, stats, centers = cv2.connectedComponentsWithStats(mask)

        result = image_array.copy()
        object_count = 0

        for label in range(1, total_labels):
            x, y, width, height, area = stats[label]
            if area >= minimum_area:
                object_count += 1
                cv2.rectangle(result, (x, y), (x + width, y + height), (255, 80, 40), 4)
                cv2.putText(
                    result,
                    str(object_count),
                    (x, max(25, y - 8)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (255, 80, 40),
                    2,
                )

        left, right = st.columns(2)
        left.image(image, caption="Gambar asli", width="stretch")
        right.image(result, caption="Objek yang dihitung", width="stretch")
        st.image(mask, caption="Color mask", width="stretch")
        st.metric(f"Jumlah objek {target_color.lower()}", object_count)
else:
    st.info("Gunakan kamera atau upload gambar untuk memulai mini project.")
