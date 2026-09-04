# Tutor Flow Week 3 - Image Editing Basics

Durasi: `60 menit`

File utama:

- `app.py`

Tujuan:

- siswa dapat mengubah gambar dengan crop, resize, rotate, dan flip
- siswa memahami bahwa satu gambar dapat menghasilkan gambar baru
- siswa dapat mengunduh hasil edit dari aplikasi Streamlit

## Persiapan Tutor

IDE yang dipakai:

- `Visual Studio Code (VS Code)`

Siswa membuat folder kerja sendiri, misalnya `computer-vision-week-3`, lalu membuat satu file bernama `app.py`.

Jalankan dari terminal pada folder tersebut:

```bash
streamlit run app.py
```

Saat mengajar, file yang dibahas tetap `satu file yang sama`, tetapi ditulis bertahap.

## Alur 1 Jam

### 0-10 menit: Cek instalasi dan review Week 2

Langkah tutor:

1. Pastikan VS Code, Python, Streamlit, dan Pillow sudah terpasang.
2. Minta siswa membuat folder `computer-vision-week-3` dan file `app.py`.
3. Review Week 2: gambar tersusun dari pixel dan semua pixel dapat diberi efek.
4. Jelaskan target hari ini: mengubah posisi, ukuran, atau arah gambar.

Perintah cek:

```bash
python3 --version
python3 -m pip show streamlit pillow
```

Jika belum terpasang:

```bash
python3 -m pip install streamlit pillow
```

### 10-20 menit: Bagian 1 - Kerangka app dan upload gambar

Tulis bagian awal sampai upload file:

```python
from io import BytesIO

from PIL import Image
import streamlit as st

st.title("Mini Image Editor")
st.write("Upload gambar, pilih edit, lalu download hasilnya.")

uploaded_file = st.file_uploader("Upload gambar", type=["png", "jpg", "jpeg"])
```

Jelaskan:

- `Pillow` membantu membuka dan mengubah gambar.
- `BytesIO` menyimpan hasil sementara di memori agar dapat didownload.
- app membutuhkan gambar dari pengguna sebagai input.

### 20-30 menit: Bagian 2 - Memilih jenis edit

Tambahkan:

```python
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    edit = st.selectbox(
        "Pilih edit",
        ["Crop Tengah", "Resize 50%", "Rotate 90 Derajat", "Flip Horizontal"],
    )
```

Jelaskan:

- `image` adalah gambar asli.
- `edit` menyimpan pilihan pengguna.
- hasil pengolahan nanti disimpan di variable baru bernama `result`.

### 30-45 menit: Bagian 3 - Crop dan resize

Tambahkan dua kondisi pertama:

```python
if edit == "Crop Tengah":
    width, height = image.size
    result = image.crop((width // 4, height // 4, width * 3 // 4, height * 3 // 4))
elif edit == "Resize 50%":
    width, height = image.size
    result = image.resize((width // 2, height // 2))
```

Jelaskan:

- `image.size` memberi lebar dan tinggi gambar.
- crop memilih sebagian area gambar, di sini bagian tengah.
- resize membuat gambar menjadi setengah dari ukuran awal.
- `//` berarti pembagian yang menghasilkan angka bulat.

### 45-52 menit: Bagian 4 - Rotate dan flip

Tambahkan kondisi berikut:

```python
elif edit == "Rotate 90 Derajat":
    result = image.rotate(90, expand=True)
else:
    result = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
```

Jelaskan:

- rotate memutar gambar 90 derajat.
- `expand=True` membuat kanvas gambar ikut menyesuaikan setelah diputar.
- flip horizontal membuat gambar seperti bercermin.

### 52-58 menit: Bagian 5 - Tampilkan dan download hasil

Tambahkan:

```python
left, right = st.columns(2)
left.image(image, caption="Gambar asli", width="stretch")
right.image(result, caption=edit, width="stretch")

buffer = BytesIO()
result.save(buffer, format="PNG")
st.download_button("Download hasil", buffer.getvalue(), "hasil_edit.png", "image/png")
```

Target hasil:

- gambar asli dan hasil edit tampil berdampingan.
- siswa dapat memilih empat edit berbeda.
- tombol download menghasilkan file PNG.

### 58-60 menit: Variasi dan penutup

Latihan:

- ubah `Resize 50%` menjadi `Resize 75%`.
- coba foto portrait dan landscape.
- ubah nama file download menjadi nama karya siswa.

Pengantar Week 4:

- setelah bentuk gambar dapat diubah, siswa akan memberi filter warna seperti brightness, contrast, blur, dan sharpen.

## Catatan Tutor

- Gunakan foto dengan objek utama di tengah agar hasil crop mudah dipahami.
- Jika waktu terbatas, prioritaskan crop, rotate, dan flip; resize serta download dapat menjadi latihan tambahan.
- Tekankan bahwa file asli tidak berubah; hasil edit disimpan sebagai gambar baru.
