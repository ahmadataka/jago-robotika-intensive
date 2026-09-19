# Tutor Flow Week 5 - Drawing and Visual Annotation

Durasi: `60 menit`

File utama:

- `app.py`

Tujuan:

- siswa menggambar garis, rectangle, circle, dan teks pada gambar
- siswa memahami koordinat sederhana pada gambar digital
- siswa mengatur warna, ketebalan anotasi, dan ukuran teks
- siswa membandingkan gambar asli dengan hasil anotasi dan mendownload hasilnya

## Persiapan Tutor

IDE yang dipakai:

- `Visual Studio Code (VS Code)`

Siswa membuat folder kerja sendiri, misalnya `computer-vision-week-5`, lalu membuat satu file bernama `app.py`.

Jalankan dari terminal pada folder tersebut:

```bash
streamlit run app.py
```

Saat mengajar, file yang dibahas tetap `satu file yang sama`, tetapi ditulis bertahap.

## Alur 1 Jam

### 0-10 menit: Cek instalasi dan review Week 4

Langkah tutor:

1. Pastikan VS Code, Python, Streamlit, dan Pillow sudah terpasang.
2. Minta siswa membuat folder `computer-vision-week-5` dan file `app.py`.
3. Review Week 4: filter mengubah warna dan ketajaman pixel.
4. Jelaskan bahwa anotasi menambahkan informasi visual tanpa mengubah file asli.

Perintah cek:

```bash
python3 --version
python3 -m pip show streamlit pillow
```

Jika belum terpasang:

```bash
python3 -m pip install streamlit pillow
```

### 10-20 menit: Bagian 1 - Kerangka app dan kanvas gambar

Tulis bagian awal:

```python
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
import streamlit as st

st.title("Image Annotation Studio")
st.write("Tambahkan garis, kotak, lingkaran, atau teks pada gambar.")

uploaded_file = st.file_uploader("Upload gambar", type=["png", "jpg", "jpeg"])
```

Lanjutkan setelah gambar tersedia:

```python
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    result = image.copy()
    draw = ImageDraw.Draw(result)
    width, height = result.size
```

Jelaskan:

- `image.copy()` menjaga gambar asli tetap aman.
- `ImageDraw.Draw(result)` membuat kanvas gambar yang dapat diberi anotasi.
- `width` dan `height` dipakai untuk menentukan posisi relatif.

### 20-28 menit: Bagian 2 - Kontrol anotasi

Tambahkan:

```python
shape = st.selectbox("Pilih anotasi", ["Rectangle", "Circle", "Line", "Text"])
color = st.color_picker("Pilih warna", "#FF0000")
thickness = st.slider("Ketebalan garis", 1, 10, 5)
```

Jelaskan:

- `selectbox` memilih jenis anotasi.
- `color_picker` menghasilkan kode warna.
- `slider` mengatur ketebalan garis.

### 28-40 menit: Bagian 3 - Rectangle dan circle

Tambahkan:

```python
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
```

Jelaskan:

- koordinat ditulis sebagai `(kiri, atas, kanan, bawah)`.
- `width // 4` dan `height // 4` menempatkan bentuk di bagian tengah.
- circle dibuat dengan menggambar ellipse di dalam kotak koordinat.

### 40-49 menit: Bagian 4 - Line dan text

Tambahkan:

```python
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
```

Jelaskan:

- line memakai titik awal dan titik akhir.
- text memakai satu titik sebagai posisi awal tulisan.
- `ImageFont` membuat ukuran teks dapat diatur dengan slider.
- ukuran stroke mengikuti ukuran font agar tulisan tetap jelas.
- garis putih di sekitar teks membantu tulisan tetap terlihat pada gambar gelap.

### 49-56 menit: Bagian 5 - Tampilkan dan download hasil

Tambahkan:

```python
left, right = st.columns(2)
left.image(image, caption="Gambar asli", width="stretch")
right.image(result, caption=shape, width="stretch")

buffer = BytesIO()
result.save(buffer, format="PNG")
st.download_button("Download hasil", buffer.getvalue(), "hasil_anotasi.png", "image/png")
```

Target hasil:

- gambar asli dan hasil anotasi tampil berdampingan.
- siswa dapat memilih empat jenis anotasi.
- warna dan ketebalan dapat diubah.
- ukuran teks dapat diubah dari 12 sampai 80 pixel.
- hasil dapat didownload sebagai PNG.

### 56-60 menit: Variasi dan penutup

Latihan:

- ubah posisi rectangle agar berada di pojok gambar.
- buat line dari kiri bawah menuju kanan atas.
- gunakan teks untuk memberi nama objek pada foto.
- tentukan kombinasi warna dan ketebalan yang paling mudah terlihat.

Pengantar Week 6:

- setelah bekerja dengan gambar statis, siswa akan membaca input kamera sebagai rangkaian frame.

## Catatan Tutor

- Gunakan gambar dengan objek jelas agar fungsi anotasi terasa nyata.
- Gambar koordinat sederhana di papan sebelum menjelaskan empat angka pada rectangle.
- Jika waktu terbatas, prioritaskan rectangle, line, dan text; circle dapat menjadi latihan tambahan.
