# Tutor Flow Week 2 - Read Pixels and Basic Image Processing

Durasi: `60 menit`

File utama:

- `app.py`

Tujuan:

- siswa memahami bahwa gambar digital tersusun dari pixel
- siswa mengenal nilai warna `RGB`
- siswa membuat app yang membaca satu pixel dan memberi efek gambar sederhana

## Persiapan Tutor

IDE yang dipakai:

- `Visual Studio Code (VS Code)`

Siswa membuat folder kerja sendiri, misalnya `computer-vision-week-2`, lalu membuat satu file bernama `app.py`.

Jalankan dari terminal pada folder tersebut:

```bash
streamlit run app.py
```

Saat mengajar, file yang dibahas tetap `satu file yang sama`, tetapi ditulis bertahap.

## Alur 1 Jam

### 0-10 menit: Cek instalasi dan review Week 1

Langkah tutor:

1. Pastikan VS Code, Python, Streamlit, Pillow, dan NumPy sudah terpasang.
2. Minta siswa membuat folder `computer-vision-week-2` dan membukanya di VS Code.
3. Buat file `app.py`.
4. Review: Week 1 menunjukkan gambar dapat di-upload dan dibaca menjadi array.
5. Jelaskan target hari ini: melihat isi pixel dan mengubah semua pixel untuk membuat efek visual.

Perintah cek:

```bash
python3 --version
python3 -m pip show streamlit pillow numpy
```

Jika belum terpasang:

```bash
python3 -m pip install streamlit pillow numpy
```

### 10-20 menit: Bagian 1 - Kerangka app dan upload gambar

Tulis bagian awal sampai upload file:

```python
import numpy as np
from PIL import Image
import streamlit as st

st.title("Pixel Playground")
st.write("Lihat bagaimana gambar dibaca sebagai angka RGB.")

uploaded_file = st.file_uploader("Upload gambar", type=["png", "jpg", "jpeg"])
```

Jelaskan:

- `Pillow` membuka gambar.
- `NumPy` membantu membaca gambar sebagai angka.
- gambar adalah input untuk project computer vision.

### 20-30 menit: Bagian 2 - Membaca gambar sebagai pixel RGB

Tambahkan:

```python
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    pixels = np.array(image)
    red, green, blue = pixels[0, 0]
```

Jelaskan:

- pixel adalah titik warna paling kecil pada gambar.
- `pixels[0, 0]` berarti pixel pada pojok kiri atas.
- setiap pixel RGB memiliki tiga angka: merah, hijau, dan biru.
- nilai `0` berarti tidak ada warna tersebut; `255` berarti sangat kuat.

Latihan cepat:

- upload dua gambar berbeda dan amati apakah nilai RGB pixel pojoknya berubah.

### 30-40 menit: Bagian 3 - Memilih efek visual

Tambahkan:

```python
effect = st.selectbox("Pilih efek", ["Grayscale", "Inverse Color", "Brightness"])
```

Jelaskan:

- satu app dapat memberi beberapa pilihan pengolahan gambar.
- variable `effect` menyimpan pilihan pengguna.
- setelah ini kode memakai `if-elif-else` untuk memilih proses yang tepat.

### 40-52 menit: Bagian 4 - Mengolah semua pixel

Tambahkan:

```python
if effect == "Grayscale":
    result = np.mean(pixels, axis=2).astype(np.uint8)
elif effect == "Inverse Color":
    result = 255 - pixels
else:
    result = np.clip(pixels.astype(int) + 40, 0, 255).astype(np.uint8)
```

Jelaskan secara visual, tanpa matematika berat:

- grayscale: tiga angka RGB dirata-rata sehingga menjadi abu-abu.
- inverse: setiap warna dibalik dari `255`.
- brightness: setiap nilai warna ditambah agar gambar lebih terang.
- `np.clip(..., 0, 255)` menjaga nilai warna tetap valid.

### 52-58 menit: Bagian 5 - Menampilkan hasil

Tambahkan:

```python
left, right = st.columns(2)
left.image(image, caption="Gambar asli", width="stretch")
right.image(result, caption=effect, width="stretch")
st.write(f"Pixel kiri atas: R={red}, G={green}, B={blue}")
```

Target hasil:

- gambar asli dan hasil tampil berdampingan.
- siswa dapat memilih efek berbeda.
- app menunjukkan nilai satu pixel RGB.

### 58-60 menit: Variasi dan penutup

Latihan:

- ubah `+ 40` menjadi `+ 80` dan bandingkan brightness.
- ganti caption gambar.
- pilih foto dengan warna cerah dan foto dengan warna gelap, lalu bandingkan efeknya.

Pengantar Week 3:

- setelah semua pixel dapat diolah, gambar dapat dipotong, diputar, diubah ukuran, dan disimpan.

## Catatan Tutor

- Gunakan gambar dengan objek dan warna jelas agar efek mudah terlihat.
- Hindari teori matriks; cukup tekankan bahwa array adalah kumpulan angka pixel.
- Jika waktu terbatas, prioritaskan grayscale dan inverse color; brightness dapat menjadi latihan tambahan.
