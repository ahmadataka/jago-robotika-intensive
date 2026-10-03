# Tutor Flow Week 7 - Color Detection

Durasi: `60 menit`

File utama:

- `app.py`

Tujuan:

- siswa memahami perbedaan praktis RGB dan HSV
- siswa membuat threshold untuk memilih kelompok warna
- siswa membuat mask hitam-putih
- siswa menemukan titik pusat warna yang terdeteksi
- siswa menghasilkan mini project Color Tracker

## Persiapan Tutor

IDE yang dipakai:

- `Visual Studio Code (VS Code)`

Siswa membuat folder kerja sendiri, misalnya `computer-vision-week-7`, lalu membuat satu file bernama `app.py`.

Jalankan dari terminal pada folder tersebut:

```bash
streamlit run app.py
```

Siapkan benda merah, hijau, dan biru atau beberapa gambar uji dengan warna yang jelas. Webcam tidak wajib karena aplikasi memiliki pilihan upload.

## Alur 1 Jam

### 0-10 menit: Cek instalasi dan review frame

Langkah tutor:

1. Pastikan VS Code, Python, Streamlit, Pillow, dan NumPy sudah terpasang.
2. Minta siswa membuat folder `computer-vision-week-7` dan file `app.py`.
3. Review Week 6: satu tangkapan kamera adalah satu frame yang berisi pixel.
4. Tunjukkan benda merah, hijau, dan biru pada kondisi terang dan gelap.
5. Jelaskan tujuan: komputer memilih pixel dengan warna target.

Perintah cek:

```bash
python3 --version
python3 -m pip show streamlit pillow numpy
```

Jika belum terpasang:

```bash
python3 -m pip install streamlit pillow numpy
```

### 10-18 menit: Bagian 1 - Tampilan dan pilihan input

Tulis bagian awal:

```python
import numpy as np
from PIL import Image, ImageDraw
import streamlit as st

st.title("Color Tracker")
st.write("Pilih warna, lalu cari benda dengan warna tersebut pada gambar.")

target_color = st.sidebar.selectbox("Warna target", ["Merah", "Hijau", "Biru"])
input_mode = st.sidebar.radio("Sumber gambar", ["Kamera", "Upload"])
```

Jelaskan:

- pengguna memilih warna yang akan dicari.
- kamera dipakai untuk mengambil satu frame.
- upload menjadi pilihan jika webcam tidak tersedia atau error.

### 18-25 menit: Bagian 2 - Kamera atau upload

Tambahkan:

```python
if input_mode == "Kamera":
    input_file = st.camera_input("Ambil satu frame")
else:
    input_file = st.file_uploader("Upload gambar", type=["png", "jpg", "jpeg"])
```

Jelaskan bahwa kedua widget menghasilkan file gambar yang dapat dibuka menggunakan kode yang sama.

### 25-33 menit: Bagian 3 - Dari RGB ke HSV

Di dalam `if input_file:`, tambahkan:

```python
image = Image.open(input_file).convert("RGB")
hsv = np.array(image.convert("HSV"))
hue = hsv[:, :, 0]
saturation = hsv[:, :, 1]
brightness = hsv[:, :, 2]
```

Penjelasan praktis:

- RGB menyimpan banyaknya cahaya merah, hijau, dan biru.
- HSV memisahkan jenis warna, kekuatan warna, dan terang-gelap.
- `hue` membantu memilih warna meskipun nilai RGB tidak persis sama.
- pada Pillow, nilai H, S, dan V berada pada rentang 0 sampai 255.

Gunakan ilustrasi roda warna; tidak perlu membahas rumus konversi.

### 33-42 menit: Bagian 4 - Threshold warna

Tambahkan:

```python
if target_color == "Merah":
    hue_match = (hue < 15) | (hue > 235)
elif target_color == "Hijau":
    hue_match = (hue > 45) & (hue < 105)
else:
    hue_match = (hue > 145) & (hue < 195)

mask = hue_match & (saturation > 80) & (brightness > 60)
```

Jelaskan:

- threshold adalah batas nilai yang diterima.
- `|` berarti salah satu kondisi boleh benar.
- `&` berarti semua kondisi harus benar.
- batas saturation mengurangi pixel abu-abu atau putih.
- batas brightness mengurangi pixel yang terlalu gelap.

### 42-49 menit: Bagian 5 - Tampilkan mask dan hasil deteksi

Tambahkan:

```python
mask_image = Image.fromarray((mask * 255).astype(np.uint8))

result_array = np.array(image)
result_array[~mask] = result_array[~mask] // 4
result = Image.fromarray(result_array)
```

Jelaskan:

- `mask` berisi True dan False untuk setiap pixel.
- True dibuat putih dan False dibuat hitam.
- pixel di luar mask dibuat lebih gelap agar warna target menonjol.

### 49-56 menit: Bagian 6 - Cari titik pusat warna

Tambahkan:

```python
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
```

Jelaskan:

- `np.where(mask)` mengambil posisi semua pixel putih.
- rata-rata posisi menghasilkan perkiraan titik pusat warna.
- lingkaran putih menunjukkan posisi yang sedang dilacak.
- tracker ini memproses satu frame, belum video real-time.

Tambahkan pesan berhasil/gagal dan tampilkan gambar asli, hasil tracker, serta mask mengikuti kode lengkap.

### 56-60 menit: Pengujian dan penutup

Pengujian wajib:

1. Coba benda merah, hijau, dan biru secara bergantian.
2. Ubah pilihan warna target dan perhatikan mask.
3. Coba gambar tanpa warna target.
4. Bandingkan hasil pada kondisi terang dan gelap.
5. Uji pilihan Upload agar semua siswa mempunyai jalur cadangan.

Pengantar Week 8:

- siswa akan membandingkan dua frame untuk mendeteksi gerakan.

## Catatan Tutor

- Gunakan benda dengan warna solid dan latar sederhana saat demonstrasi awal.
- Deteksi dapat terganggu cahaya, bayangan, dan warna latar; hal tersebut adalah bagian dari eksperimen.
- Jangan mengejar threshold sempurna untuk semua kondisi. Fokus pada hubungan warna, batas nilai, dan mask.
- Jika kamera error, pilih Upload tanpa mengubah kode lainnya.
- Jika waktu terbatas, prioritaskan deteksi satu warna, mask, dan tampilan hasil; titik pusat dapat didemonstrasikan tutor.
