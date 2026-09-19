from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
import streamlit as st

st.title("Image Annotation Studio")
st.write("Tambahkan garis, kotak, lingkaran, atau teks pada gambar.")

uploaded_file = st.file_uploader("Upload gambar", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    result = image.copy()
    draw = ImageDraw.Draw(result)
    width, height = result.size

    shape = st.selectbox("Pilih anotasi", ["Rectangle", "Circle", "Line", "Text"])
    color = st.color_picker("Pilih warna", "#FF0000")
    thickness = st.slider("Ketebalan garis", 1, 10, 5)

    if shape == "Rectangle":
        draw.rectangle(
            (width // 4, height // 4, width * 3 // 4, height * 3 // 4),
            outline=color,
            width=thickness,
        )
    elif shape == "Circle":
        draw.ellipse(
            (width // 4, height // 4, width * 3 // 4, height * 3 // 4),
            outline=color,
            width=thickness,
        )
    elif shape == "Line":
        draw.line(
            (width // 5, height // 5, width * 4 // 5, height * 4 // 5),
            fill=color,
            width=thickness,
        )
    else:
        label = st.text_input("Tulis teks", "Objek")
        font_size = st.slider("Ukuran teks", 12, 80, 32)
        font = ImageFont.load_default(size=font_size)
        draw.text(
            (width // 10, height // 10),
            label,
            fill=color,
            font=font,
            stroke_width=max(1, font_size // 20),
            stroke_fill="white",
        )

    left, right = st.columns(2)
    left.image(image, caption="Gambar asli", width="stretch")
    right.image(result, caption=shape, width="stretch")

    buffer = BytesIO()
    result.save(buffer, format="PNG")
    st.download_button("Download hasil", buffer.getvalue(), "hasil_anotasi.png", "image/png")
else:
    st.info("Upload gambar dulu ya.")
