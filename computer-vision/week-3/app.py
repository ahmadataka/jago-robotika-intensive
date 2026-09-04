from io import BytesIO

from PIL import Image
import streamlit as st

st.title("Mini Image Editor")
st.write("Upload gambar, pilih edit, lalu download hasilnya.")

uploaded_file = st.file_uploader("Upload gambar", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    edit = st.selectbox("Pilih edit", ["Crop Tengah", "Resize 50%", "Rotate 90 Derajat", "Flip Horizontal"])

    if edit == "Crop Tengah":
        width, height = image.size
        result = image.crop((width // 4, height // 4, width * 3 // 4, height * 3 // 4))
    elif edit == "Resize 50%":
        width, height = image.size
        result = image.resize((width // 2, height // 2))
    elif edit == "Rotate 90 Derajat":
        result = image.rotate(90, expand=True)
    else:
        result = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

    left, right = st.columns(2)
    left.image(image, caption="Gambar asli", width="stretch")
    right.image(result, caption=edit, width="stretch")

    buffer = BytesIO()
    result.save(buffer, format="PNG")
    st.download_button("Download hasil", buffer.getvalue(), "hasil_edit.png", "image/png")
else:
    st.info("Upload gambar dulu ya.")
