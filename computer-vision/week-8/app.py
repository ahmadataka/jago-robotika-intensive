import numpy as np
from PIL import Image
import streamlit as st

st.title("Motion Detector")
st.write("Bandingkan dua frame untuk menemukan bagian gambar yang bergerak.")

input_mode = st.sidebar.radio("Sumber frame", ["Kamera", "Upload"])
threshold = st.sidebar.slider("Batas perbedaan pixel", 10, 100, 30)
alarm_limit = st.sidebar.slider("Batas alarm (%)", 1.0, 20.0, 3.0)

if input_mode == "Kamera":
    frame_1_file = st.camera_input("Frame 1: ambil gambar awal", key="camera_1")
    frame_2_file = st.camera_input("Frame 2: bergerak lalu ambil gambar kedua", key="camera_2")
else:
    frame_1_file = st.file_uploader("Upload frame pertama", type=["png", "jpg", "jpeg"])
    frame_2_file = st.file_uploader("Upload frame kedua", type=["png", "jpg", "jpeg"])

if frame_1_file and frame_2_file:
    frame_1 = Image.open(frame_1_file).convert("RGB")
    frame_2 = Image.open(frame_2_file).convert("RGB").resize(frame_1.size)

    gray_1 = np.array(frame_1.convert("L"), dtype=np.int16)
    gray_2 = np.array(frame_2.convert("L"), dtype=np.int16)

    difference = np.abs(gray_2 - gray_1)
    motion_mask = difference > threshold
    motion_percent = float(motion_mask.mean() * 100)

    mask_image = Image.fromarray((motion_mask * 255).astype(np.uint8))
    result_array = np.array(frame_2)
    result_array[~motion_mask] = result_array[~motion_mask] // 4
    result = Image.fromarray(result_array)

    first, second = st.columns(2)
    first.image(frame_1, caption="Frame 1", width="stretch")
    second.image(frame_2, caption="Frame 2", width="stretch")

    result_col, mask_col = st.columns(2)
    result_col.image(result, caption="Bagian yang bergerak", width="stretch")
    mask_col.image(mask_image, caption="Motion mask", width="stretch")

    st.metric("Perubahan gambar", f"{motion_percent:.1f}%")

    if motion_percent >= alarm_limit:
        st.error("ALARM: Gerakan terdeteksi!")
    else:
        st.success("Aman: belum ada gerakan besar.")
else:
    st.info("Siapkan dua frame dengan posisi kamera yang sama, lalu gerakkan satu benda.")
