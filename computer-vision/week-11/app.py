import cv2
import numpy as np
from PIL import Image
import streamlit as st

st.title("Color Hunt Challenge")
st.write("Temukan sejumlah benda dengan warna target untuk menyelesaikan tantangan.")

target_color = st.sidebar.selectbox("Warna target", ["Merah", "Hijau", "Biru"])
target_count = st.sidebar.slider("Target jumlah benda", 1, 5, 2)
minimum_area = st.sidebar.slider("Ukuran objek minimum", 100, 5000, 500, 100)
input_mode = st.sidebar.radio("Sumber gambar", ["Kamera", "Upload"])

st.sidebar.info("Pisahkan setiap benda agar dapat dihitung sebagai objek berbeda.")

if input_mode == "Kamera":
    input_file = st.camera_input("Ambil satu frame")
else:
    input_file = st.file_uploader("Upload gambar", type=["png", "jpg", "jpeg"])

if input_file:
    image = Image.open(input_file).convert("RGB")
    image_array = np.array(image)
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
    right.image(result, caption="Hasil Color Hunt", width="stretch")

    count_col, goal_col = st.columns(2)
    count_col.metric("Objek ditemukan", object_count)
    goal_col.metric("Target", target_count)

    progress = min(object_count / target_count, 1.0)
    st.progress(progress)

    if object_count >= target_count:
        st.success("Tantangan berhasil! Target warna sudah ditemukan.")
    else:
        remaining = target_count - object_count
        st.info(f"Cari {remaining} benda {target_color.lower()} lagi untuk menang.")

    with st.expander("Lihat color mask"):
        st.image(mask, width="stretch")
else:
    st.info("Gunakan kamera atau upload gambar untuk memulai tantangan.")
