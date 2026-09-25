# Tutor Flow Week 6 - Intro to Webcam Input

Durasi: `60 menit`

File utama:

- `app.py`

Tujuan:

- siswa mengambil input gambar langsung dari kamera
- siswa memahami bahwa satu tangkapan kamera adalah satu frame
- siswa mengubah frame menjadi array pixel dan grayscale
- siswa memahami bahwa video adalah rangkaian frame yang tampil cepat

## Persiapan Tutor

IDE yang dipakai:

- `Visual Studio Code (VS Code)`

Siswa membuat folder kerja sendiri, misalnya `computer-vision-week-6`, lalu membuat satu file bernama `app.py`.

Jalankan dari terminal pada folder tersebut:

```bash
streamlit run app.py
```

Saat mengajar, file yang dibahas tetap `satu file yang sama`, tetapi ditulis bertahap.

## Alur 1 Jam

### 0-10 menit: Cek instalasi, kamera, dan review Week 5

Langkah tutor:

1. Pastikan VS Code, Python, Streamlit, Pillow, dan NumPy sudah terpasang.
2. Minta siswa membuat folder `computer-vision-week-6` dan file `app.py`.
3. Pastikan kamera laptop berfungsi dan browser mendapat izin kamera.
4. Review Week 5: gambar statis dapat diberi anotasi.
5. Jelaskan bahwa kamera memberi banyak gambar berurutan yang disebut frame.

Jika laptop tidak memiliki kamera atau camera input error, siswa tetap dapat mengikuti materi dengan upload gambar. Ganti sementara:

```python
camera_frame = st.camera_input("Ambil gambar dari kamera")
```

menjadi:

```python
camera_frame = st.file_uploader("Upload satu frame", type=["png", "jpg", "jpeg"])
```

Baris berikutnya tidak perlu diubah karena hasil camera input dan file uploader sama-sama dapat dibuka menggunakan `Image.open()`.

Perintah cek:

```bash
python3 --version
python3 -m pip show streamlit pillow numpy
```

Jika belum terpasang:

```bash
python3 -m pip install streamlit pillow numpy
```

### 10-20 menit: Bagian 1 - Kerangka app dan camera input

Tulis bagian awal:

```python
import numpy as np
from PIL import Image, ImageOps
import streamlit as st

st.title("Webcam Frame Explorer")
st.write("Ambil satu frame dari kamera, lalu lihat bagaimana komputer memprosesnya.")

camera_frame = st.camera_input("Ambil gambar dari kamera")
```

Jelaskan:

- `st.camera_input` membuka kamera melalui browser.
- preview kamera terlihat bergerak, tetapi tombol kamera mengambil satu frame.
- hasil tangkapan disimpan ke variable `camera_frame`.

### 20-30 menit: Bagian 2 - Baca frame sebagai gambar dan array

Tambahkan:

```python
if camera_frame:
    image = Image.open(camera_frame).convert("RGB")
    frame = np.array(image)
```

Jelaskan:

- Pillow membuka frame seperti file gambar biasa.
- NumPy mengubah frame menjadi kumpulan angka pixel.
- bentuk array adalah `(tinggi, lebar, channel warna)`.

Hubungkan dengan materi Week 1 dan Week 2: gambar upload dan frame kamera sama-sama dapat dibaca sebagai array.

### 30-40 menit: Bagian 3 - Proses satu frame

Tambahkan:

```python
grayscale = ImageOps.grayscale(image)

left, right = st.columns(2)
left.image(image, caption="Frame asli", width="stretch")
right.image(grayscale, caption="Frame grayscale", width="stretch")
```

Jelaskan:

- frame asli mempunyai channel RGB.
- grayscale menghasilkan satu tingkat terang untuk setiap pixel.
- proses yang sama dapat diterapkan pada setiap frame dalam sebuah video.

### 40-50 menit: Bagian 4 - Baca informasi frame

Tambahkan:

```python
red, green, blue = frame[0, 0]
st.write("Ukuran frame:", image.width, "x", image.height)
st.write("Bentuk array:", frame.shape)
st.write(f"Pixel kiri atas: R={red}, G={green}, B={blue}")
```

Jelaskan:

- resolusi menunjukkan jumlah pixel secara horizontal dan vertikal.
- pixel kiri atas tetap mempunyai nilai RGB seperti gambar upload.
- frame hanyalah gambar yang berasal dari kamera.

### 50-56 menit: Bagian 5 - Konsep frame-by-frame

Tambahkan:

```python
st.success("Satu foto kamera adalah satu frame. Banyak frame yang tampil cepat akan menjadi video.")
```

Demonstrasi:

1. Ambil frame pertama dengan posisi tangan di bawah.
2. Ambil ulang frame dengan posisi tangan berbeda.
3. Jelaskan bahwa video melakukan proses tersebut berkali-kali setiap detik.

Tekankan bahwa Week 6 baru memproses satu frame agar konsepnya jelas dan app tetap ringan.

### 56-60 menit: Variasi dan penutup

Latihan:

- ambil frame pada kondisi terang dan gelap, lalu bandingkan nilai RGB.
- ambil gambar benda berwarna merah atau biru.
- ganti efek grayscale dengan efek Week 4 jika waktu cukup.

Pengantar Week 7:

- siswa akan memakai warna pixel untuk mendeteksi benda dengan warna tertentu.

## Catatan Tutor

- Minta izin sebelum siswa mengarahkan kamera kepada teman.
- Jika kamera tidak berfungsi, cek permission browser dan pastikan aplikasi kamera lain sudah ditutup.
- Jika kamera tetap gagal atau perangkat tidak memiliki webcam, gunakan versi `st.file_uploader` pada bagian persiapan. Siswa dapat memakai foto yang sudah tersimpan sebagai satu frame pengganti.
- Jelaskan bahwa mode upload hanya cadangan. Konsep pixel, array, RGB, dan grayscale yang dipelajari tetap sama.
- Jangan masuk ke loop webcam OpenCV pada Week 6; fokus pada konsep satu frame dahulu.
- Jika waktu terbatas, prioritaskan camera input, array shape, dan grayscale.
