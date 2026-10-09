# Tutor Flow Week 8 - Motion Detection

Durasi: `60 menit`

File utama:

- `app.py`

Tujuan:

- siswa memahami gerakan sebagai perubahan antara dua frame
- siswa membandingkan nilai grayscale pixel
- siswa membuat threshold dan motion mask
- siswa menghitung persentase perubahan gambar
- siswa membuat alarm gerakan sederhana

## Persiapan Tutor

IDE yang dipakai:

- `Visual Studio Code (VS Code)`

Siswa membuat folder kerja sendiri, misalnya `computer-vision-week-8`, lalu membuat satu file bernama `app.py`.

Jalankan dari terminal pada folder tersebut:

```bash
streamlit run app.py
```

Siapkan kamera yang dapat diletakkan stabil atau dua gambar dari posisi yang sama. Webcam tidak wajib karena aplikasi memiliki pilihan upload.

## Alur 1 Jam

### 0-10 menit: Cek instalasi dan demonstrasi gerakan

Langkah tutor:

1. Pastikan VS Code, Python, Streamlit, Pillow, dan NumPy sudah terpasang.
2. Minta siswa membuat folder `computer-vision-week-8` dan file `app.py`.
3. Review Week 7: mask memilih pixel yang memenuhi suatu kondisi.
4. Tampilkan dua gambar: latar sama, tetapi satu benda berpindah.
5. Jelaskan bahwa komputer mendeteksi gerakan dengan mencari pixel yang berubah.

Perintah cek:

```bash
python3 --version
python3 -m pip show streamlit pillow numpy
```

Jika belum terpasang:

```bash
python3 -m pip install streamlit pillow numpy
```

### 10-18 menit: Bagian 1 - Tampilan dan pengaturan

Tulis bagian awal:

```python
import numpy as np
from PIL import Image
import streamlit as st

st.title("Motion Detector")
st.write("Bandingkan dua frame untuk menemukan bagian gambar yang bergerak.")

input_mode = st.sidebar.radio("Sumber frame", ["Kamera", "Upload"])
threshold = st.sidebar.slider("Batas perbedaan pixel", 10, 100, 30)
alarm_limit = st.sidebar.slider("Batas alarm (%)", 1.0, 20.0, 3.0)
```

Jelaskan:

- threshold menentukan seberapa besar perubahan pixel yang dianggap gerakan.
- batas alarm menentukan berapa persen gambar harus berubah sebelum alarm aktif.
- nilai ini dapat disesuaikan dengan kondisi kelas dan pencahayaan.

### 18-26 menit: Bagian 2 - Ambil dua frame

Tambahkan:

```python
if input_mode == "Kamera":
    frame_1_file = st.camera_input("Frame 1: ambil gambar awal", key="camera_1")
    frame_2_file = st.camera_input("Frame 2: bergerak lalu ambil gambar kedua", key="camera_2")
else:
    frame_1_file = st.file_uploader("Upload frame pertama", type=["png", "jpg", "jpeg"])
    frame_2_file = st.file_uploader("Upload frame kedua", type=["png", "jpg", "jpeg"])
```

Demonstrasi kamera:

1. Jangan menggeser laptop.
2. Ambil frame pertama.
3. Gerakkan satu benda.
4. Ambil frame kedua.

Jika webcam tidak tersedia atau kedua camera input bermasalah, pilih Upload dan lanjutkan materi tanpa mengubah kode.

### 26-35 menit: Bagian 3 - Samakan ukuran dan ubah ke grayscale

Di dalam `if frame_1_file and frame_2_file:`, tambahkan:

```python
frame_1 = Image.open(frame_1_file).convert("RGB")
frame_2 = Image.open(frame_2_file).convert("RGB").resize(frame_1.size)

gray_1 = np.array(frame_1.convert("L"), dtype=np.int16)
gray_2 = np.array(frame_2.convert("L"), dtype=np.int16)
```

Jelaskan:

- dua gambar harus memiliki ukuran yang sama agar setiap pixel dapat dibandingkan.
- grayscale menyederhanakan satu pixel menjadi satu nilai terang-gelap.
- `int16` mencegah kesalahan saat nilai pixel dikurangkan.

### 35-43 menit: Bagian 4 - Hitung perbedaan dan buat mask

Tambahkan:

```python
difference = np.abs(gray_2 - gray_1)
motion_mask = difference > threshold
motion_percent = float(motion_mask.mean() * 100)
```

Jelaskan:

- pengurangan menunjukkan perubahan antara frame pertama dan kedua.
- `np.abs` membuat semua perbedaan menjadi nilai positif.
- pixel di atas threshold dianggap bergerak.
- rata-rata mask menjadi persentase pixel yang berubah.

### 43-50 menit: Bagian 5 - Visualisasikan gerakan

Tambahkan:

```python
mask_image = Image.fromarray((motion_mask * 255).astype(np.uint8))
result_array = np.array(frame_2)
result_array[~motion_mask] = result_array[~motion_mask] // 4
result = Image.fromarray(result_array)
```

Jelaskan:

- mask putih menunjukkan pixel yang berubah.
- bagian yang tidak bergerak dibuat lebih gelap.
- hasil ini membantu melihat lokasi gerakan, bukan hanya jumlahnya.

Tampilkan dua frame, hasil deteksi, dan mask mengikuti kode lengkap.

### 50-56 menit: Bagian 6 - Buat alarm gerakan

Tambahkan:

```python
st.metric("Perubahan gambar", f"{motion_percent:.1f}%")

if motion_percent >= alarm_limit:
    st.error("ALARM: Gerakan terdeteksi!")
else:
    st.success("Aman: belum ada gerakan besar.")
```

Jelaskan:

- alarm tidak hanya melihat satu pixel, tetapi persentase seluruh perubahan.
- batas terlalu rendah mudah menghasilkan alarm palsu.
- batas terlalu tinggi dapat melewatkan gerakan kecil.

### 56-60 menit: Tantangan dan penutup

Pengujian wajib:

1. Bandingkan dua frame yang hampir sama.
2. Gerakkan satu benda dan lihat motion mask.
3. Ubah threshold dari rendah ke tinggi.
4. Ubah batas alarm dan amati status.
5. Geser kamera sedikit untuk melihat mengapa kamera harus stabil.

Pilihan tantangan:

- Security Alarm: cari batas yang mendeteksi orang lewat.
- Motion Game: pemain menang jika perubahan gambar melewati angka tertentu.
- Quiet Monitor: alarm aktif jika ada gerakan saat seharusnya diam.

Pengantar Week 9:

- siswa akan memakai model siap pakai untuk mendeteksi dan menandai wajah.

## Catatan Tutor

- Cahaya yang berubah juga dapat dianggap sebagai gerakan. Gunakan ini untuk menjelaskan keterbatasan sistem.
- Kamera harus stabil; perpindahan kecil dapat membuat hampir seluruh frame berubah.
- Tidak perlu membuat video real-time pada Week 8. Dua frame cukup untuk memahami prinsip motion detection.
- Jika dua camera input sulit digunakan pada perangkat tertentu, pilih Upload sebagai jalur utama.
- Jika waktu terbatas, prioritaskan difference, threshold, mask, dan indikator alarm.
