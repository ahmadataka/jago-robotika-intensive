from io import BytesIO

from PIL import Image, ImageEnhance, ImageFilter
import streamlit as st

st.title("Image Filter Lab")
st.write("Atur warna dan ketajaman gambar dengan beberapa filter sederhana.")

uploaded_file = st.file_uploader("Upload gambar", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    effect = st.selectbox(
        "Pilih filter",
        ["Brightness", "Contrast", "Blur", "Sharpen", "Red Channel", "Green Channel", "Blue Channel"],
    )
    strength = st.slider("Kekuatan filter", 1, 3, 2)

    if effect == "Brightness":
        result = ImageEnhance.Brightness(image).enhance(1 + strength * 0.3)
    elif effect == "Contrast":
        result = ImageEnhance.Contrast(image).enhance(1 + strength * 0.4)
    elif effect == "Blur":
        result = image.filter(ImageFilter.GaussianBlur(radius=strength))
    elif effect == "Sharpen":
        result = ImageEnhance.Sharpness(image).enhance(1 + strength)
    else:
        red, green, blue = image.split()
        empty = Image.new("L", image.size, 0)

        if effect == "Red Channel":
            result = Image.merge("RGB", (red, empty, empty))
        elif effect == "Green Channel":
            result = Image.merge("RGB", (empty, green, empty))
        else:
            result = Image.merge("RGB", (empty, empty, blue))

    left, right = st.columns(2)
    left.image(image, caption="Gambar asli", width="stretch")
    right.image(result, caption=effect, width="stretch")

    buffer = BytesIO()
    result.save(buffer, format="PNG")
    st.download_button("Download hasil", buffer.getvalue(), "hasil_filter.png", "image/png")
else:
    st.info("Upload gambar dulu ya.")
