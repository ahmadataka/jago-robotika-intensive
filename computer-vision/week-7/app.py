import numpy as np
from PIL import Image, ImageDraw
import streamlit as st

st.title("Color Tracker")
st.write("Pilih warna, lalu cari benda dengan warna tersebut pada gambar.")

target_color = st.sidebar.selectbox("Warna target", ["Merah", "Hijau", "Biru"])
input_mode = st.sidebar.radio("Sumber gambar", ["Kamera", "Upload"])

if input_mode == "Kamera":
    input_file = st.camera_input("Ambil satu frame")
else:
    input_file = st.file_uploader("Upload gambar", type=["png", "jpg", "jpeg"])

if input_file:
    image = Image.open(input_file).convert("RGB")
    hsv = np.array(image.convert("HSV"))
    hue = hsv[:, :, 0]
    saturation = hsv[:, :, 1]
    brightness = hsv[:, :, 2]

    if target_color == "Merah":
        hue_match = (hue < 15) | (hue > 235)
    elif target_color == "Hijau":
        hue_match = (hue > 45) & (hue < 105)
    else:
        hue_match = (hue > 145) & (hue < 195)

    mask = hue_match & (saturation > 80) & (brightness > 60)
    mask_image = Image.fromarray((mask * 255).astype(np.uint8))

    result_array = np.array(image)
    result_array[~mask] = result_array[~mask] // 4
    result = Image.fromarray(result_array)

    y_points, x_points = np.where(mask)
    if len(x_points) > 0:
        center_x = int(x_points.mean())
        center_y = int(y_points.mean())
        draw = ImageDraw.Draw(result)
        draw.ellipse(
            (center_x - 15, center_y - 15, center_x + 15, center_y + 15),
            outline="white",
            width=5,
        )
        st.success(f"Warna {target_color.lower()} terdeteksi di ({center_x}, {center_y}).")
    else:
        st.warning(f"Warna {target_color.lower()} belum terdeteksi.")

    left, right = st.columns(2)
    left.image(image, caption="Gambar asli", width="stretch")
    right.image(result, caption=f"Tracker {target_color}", width="stretch")
    st.image(mask_image, caption="Mask: putih = pixel yang terdeteksi", width="stretch")
else:
    st.info("Gunakan kamera atau upload gambar yang memiliki warna merah, hijau, atau biru.")
