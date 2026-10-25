# Tutor Flow Week 10 - Fun Interactive Vision Projects

Durasi: `60 menit`

File utama:

- `app.py`
- `starter.py` sebagai template awal opsional

Tujuan:

- siswa menggabungkan input kamera atau upload dengan teknik yang sudah dipelajari
- siswa membuat grayscale dan edge filter
- siswa mendeteksi warna menggunakan HSV dan mask
- siswa menghitung beberapa objek dengan connected components
- siswa memilih arah mini project untuk dikembangkan pada Week 11

## Persiapan Tutor

IDE yang dipakai:

- `Visual Studio Code (VS Code)`

Siswa membuat folder kerja sendiri, misalnya `computer-vision-week-10`, lalu membuat satu file bernama `app.py`.

Jalankan dari terminal pada folder tersebut:

```bash
streamlit run app.py
```

Siapkan gambar dengan detail jelas dan beberapa benda merah, hijau, atau biru yang terpisah. Webcam tidak wajib karena aplikasi memiliki pilihan upload.

Untuk menghemat waktu mengetik, tutor dapat membagikan isi `starter.py` sebelum kelas. Siswa menyalin template tersebut ke file `app.py`. Template sudah berisi import, pilihan project, camera/upload, dan pembacaan gambar; siswa fokus menambahkan pemrosesan vision. `app.py` di materi tutor adalah kode final untuk pengecekan.

## Alur 1 Jam

### 0-8 menit: Cek instalasi dan pilih mini project

Langkah tutor:

1. Pastikan VS Code, Python, Streamlit, Pillow, NumPy, dan OpenCV sudah terpasang.
2. Minta siswa membuat folder `computer-vision-week-10` dan file `app.py`.
3. Review grayscale, mask warna, bounding box, dan input kamera.
4. Perkenalkan tiga pilihan: Color Object Counter, Grayscale Filter, dan Edge Filter.
5. Jelaskan bahwa satu app dapat memiliki beberapa mode project.

Perintah cek:

```bash
python3 --version
python3 -m pip show streamlit pillow numpy opencv-python-headless
```

Jika belum terpasang:

```bash
python3 -m pip install streamlit pillow numpy "opencv-python-headless<5"
```

### 8-16 menit: Bagian 1 - Buka template dan review input

Jika memakai `starter.py`, bagian awal berikut tidak perlu diketik ulang. Tutor membacanya bersama siswa:

```python
import cv2
import numpy as np
from PIL import Image
import streamlit as st

st.title("Vision Playground")
st.write("Pilih mini project untuk bereksperimen dengan gambar.")

project = st.sidebar.selectbox(
    "Pilih project",
    ["Color Object Counter", "Grayscale Filter", "Edge Filter"],
)
input_mode = st.sidebar.radio("Sumber gambar", ["Kamera", "Upload"])
```

Template juga sudah memuat pengaturan warna, ukuran minimum, camera input, upload, serta pembacaan gambar. Jika tidak memakai template, tulis bagian tersebut secara bertahap mengikuti kode lengkap.

### 16-25 menit: Bagian 2 - Baca gambar dan buat dua filter

Template sudah membaca gambar di dalam `if input_file:`. Mulai penulisan materi dari pemrosesan filter berikut:

```python
image = Image.open(input_file).convert("RGB")
image_array = np.array(image)
```

Grayscale Filter:

```python
result = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
```

Edge Filter:

```python
grayscale = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
result = cv2.Canny(grayscale, 80, 160)
```

Jelaskan:

- grayscale menyederhanakan warna menjadi terang-gelap.
- Canny mencari perubahan terang-gelap yang tajam sebagai tepi.
- kedua filter dapat menjadi dasar project foto yang lebih kreatif.

### 25-36 menit: Bagian 3 - Buat color mask

Untuk Color Object Counter, ubah gambar ke HSV:

```python
hsv = cv2.cvtColor(image_array, cv2.COLOR_RGB2HSV)
```

Tambahkan threshold merah, hijau, dan biru mengikuti kode lengkap. Ingatkan siswa bahwa OpenCV memakai nilai Hue 0 sampai 179.

Setelah mask dibuat, tambahkan:

```python
mask = cv2.medianBlur(mask, 7)
```

Jelaskan bahwa median blur membersihkan titik noise kecil agar objek lebih mudah dihitung.

### 36-48 menit: Bagian 4 - Hitung objek

Tambahkan:

```python
total_labels, labels, stats, centers = cv2.connectedComponentsWithStats(mask)
result = image_array.copy()
object_count = 0
```

Lalu loop setiap label:

```python
for label in range(1, total_labels):
    x, y, width, height, area = stats[label]
    if area >= minimum_area:
        object_count += 1
        cv2.rectangle(result, (x, y), (x + width, y + height), (255, 80, 40), 4)
```

Jelaskan:

- connected components mengelompokkan pixel putih yang saling terhubung.
- label 0 adalah background sehingga loop dimulai dari 1.
- area kecil diabaikan sebagai noise.
- setiap objek yang lolos diberi kotak dan nomor.

### 48-55 menit: Tampilkan dan uji project

Tampilkan gambar asli, hasil, mask, dan jumlah objek mengikuti kode lengkap.

Pengujian wajib:

1. Coba ketiga mode project.
2. Ubah warna target.
3. Dekatkan dua benda sampai dianggap satu objek.
4. Ubah ukuran objek minimum.
5. Coba latar atau pencahayaan berbeda.

### 55-60 menit: Personalisasi dan rencana final project

Siswa memilih satu arah pengembangan:

- Color Counter: tambah skor atau target jumlah benda.
- Object Finder: tampilkan pesan ketika warna target ditemukan.
- Photo Filter: tambah pilihan blur atau efek lain.
- Edge Art: buat tampilan garis dengan warna berbeda.

Tutor dapat meminta satu siswa screen sharing untuk demo. Siswa lain tetap menjalankan dan menguji app masing-masing.

Pengantar Week 11:

- siswa akan memilih ide final project, menggabungkan teknik yang sesuai, dan memperbaiki tampilan serta alur demo.

## Catatan Tutor

- Fokus utama adalah menggabungkan konsep lama, bukan menghafal semua fungsi OpenCV.
- Benda yang saling menempel dapat dihitung sebagai satu objek; gunakan ini untuk menjelaskan keterbatasan.
- Jika kamera error, gunakan Upload tanpa mengubah bagian pemrosesan.
- Tidak semua siswa harus memilih project yang sama untuk dikembangkan pada Week 11.
- Jika waktu terbatas, prioritaskan Color Object Counter; dua filter dapat didemonstrasikan dari kode lengkap.
