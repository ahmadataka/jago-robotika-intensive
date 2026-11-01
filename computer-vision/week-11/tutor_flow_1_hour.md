# Tutor Flow Week 11 - Final Project Build

Durasi: `60 menit`

File utama:

- `app.py`

Tujuan:

- siswa memilih ide final project Computer Vision
- siswa menggabungkan teknik dari minggu sebelumnya
- siswa menambahkan tujuan, instruksi, dan feedback pengguna
- siswa menguji project secara mandiri dan bersama tutor
- siswa menghasilkan final project yang hampir siap dipresentasikan

## Persiapan Tutor

IDE yang dipakai:

- `Visual Studio Code (VS Code)`

Siswa membuat folder kerja sendiri, misalnya `computer-vision-week-11`, lalu membuat satu file bernama `app.py`.

Jalankan dari terminal pada folder tersebut:

```bash
streamlit run app.py
```

Kode materi menggunakan `Color Hunt Challenge` sebagai reference project. Siswa boleh memilih alternatif:

- Color Hunt Challenge dari Week 10 Color Counter
- Face Detector dari Week 9
- Filter Studio dari Week 10
- Motion Alarm dari Week 8

Jika siswa memilih alternatif, gunakan kode minggu terkait sebagai starting point dan ikuti checklist project yang sama.

Untuk siswa yang melanjutkan Face Detector Week 9, tersedia dua contoh tambahan:

- `expression_detector.py`: mendeteksi pola senyum pada area mulut.
- `video_face_tracker.py`: menampilkan live webcam dengan kotak dan titik pusat wajah, memakai pipeline Week 9 pada setiap frame.

Saran, prinsip kerja, cara menjalankan, keterbatasan, dan alur tutor masing-masing project tersedia di [face_project_extensions.md](face_project_extensions.md).

## Alur 1 Jam

### 0-10 menit: Cek instalasi dan pilih project

Langkah tutor:

1. Pastikan VS Code, Python, Streamlit, Pillow, NumPy, dan OpenCV sudah terpasang.
2. Minta siswa membuat folder `computer-vision-week-11` dan file `app.py`.
3. Tampilkan kembali project Week 8-10.
4. Minta siswa memilih satu project yang realistis diselesaikan.
5. Isi rencana singkat sebelum coding.

Rencana project:

- nama project
- input: kamera atau upload
- teknik vision yang dipakai
- output yang ditampilkan
- kondisi berhasil atau pesan feedback

Perintah cek:

```bash
python3 --version
python3 -m pip show streamlit pillow numpy opencv-python-headless
```

Jika belum terpasang:

```bash
python3 -m pip install streamlit pillow numpy "opencv-python-headless<5"
```

### 10-18 menit: Bagian 1 - Identitas dan tujuan project

Untuk reference project, tulis:

```python
import cv2
import numpy as np
from PIL import Image
import streamlit as st

st.title("Color Hunt Challenge")
st.write("Temukan sejumlah benda dengan warna target untuk menyelesaikan tantangan.")
```

Tambahkan pengaturan warna, target jumlah benda, ukuran minimum, dan sumber gambar mengikuti kode lengkap.

Jelaskan bahwa project final harus memiliki tujuan yang dapat dipahami pengguna, bukan hanya menampilkan hasil filter.

### 18-30 menit: Bagian 2 - Gunakan kembali vision pipeline

Gunakan kembali pipeline Week 10:

1. Baca gambar dengan Pillow.
2. Ubah gambar menjadi array NumPy.
3. Konversi RGB ke HSV.
4. Buat mask warna merah, hijau, atau biru.
5. Bersihkan mask dengan median blur.

Siswa tidak perlu mengetik ulang dari ingatan. Mereka boleh melihat kode Week 10 dan menjelaskan fungsi setiap bagian yang dipakai.

### 30-40 menit: Bagian 3 - Hitung dan tandai objek

Gunakan `connectedComponentsWithStats` untuk mendapatkan setiap objek, lalu:

```python
for label in range(1, total_labels):
    x, y, width, height, area = stats[label]
    if area >= minimum_area:
        object_count += 1
        cv2.rectangle(result, (x, y), (x + width, y + height), (255, 80, 40), 4)
```

Tambahkan nomor pada objek mengikuti kode lengkap.

Tekankan bahwa bagian vision berasal dari materi sebelumnya. Fokus Week 11 adalah mengubahnya menjadi project dengan tujuan dan feedback.

### 40-50 menit: Bagian 4 - Tambahkan game logic dan feedback

Tampilkan jumlah objek dan target:

```python
count_col, goal_col = st.columns(2)
count_col.metric("Objek ditemukan", object_count)
goal_col.metric("Target", target_count)

progress = min(object_count / target_count, 1.0)
st.progress(progress)
```

Tambahkan kondisi berhasil:

```python
if object_count >= target_count:
    st.success("Tantangan berhasil! Target warna sudah ditemukan.")
else:
    remaining = target_count - object_count
    st.info(f"Cari {remaining} benda {target_color.lower()} lagi untuk menang.")
```

Jelaskan bahwa feedback membuat project terasa interaktif dan siap didemokan.

### 50-57 menit: Pengujian online dan perbaikan

Checklist pengujian:

1. Coba gambar tanpa objek target.
2. Coba jumlah objek di bawah target.
3. Coba jumlah objek sama atau lebih dari target.
4. Ubah warna target.
5. Ubah ukuran minimum.
6. Periksa petunjuk saat belum ada input.

Tutor memberi satu skenario pengujian melalui meeting chat atau screen sharing. Siswa menguji app masing-masing dan memperbaiki satu masalah paling penting.

### 57-60 menit: Persiapan Week 12

Siswa mencatat hal yang belum selesai:

- bug atau kondisi yang belum bekerja
- tampilan yang ingin diperbaiki
- gambar atau benda untuk demo
- penjelasan singkat cara kerja

Pengantar Week 12:

- final testing, perbaikan terakhir, dan presentasi project.

## Catatan Tutor

- Jangan memaksa semua siswa memilih Color Hunt; reference project hanya contoh lengkap.
- Batasi scope agar satu fitur utama benar-benar bekerja.
- Siswa boleh menyalin bagian pipeline dari kode minggu sebelumnya jika dapat menjelaskan fungsinya.
- Jika kamera error, gunakan Upload agar pembangunan project tetap berjalan.
- Jika waktu terbatas, prioritaskan project bekerja, feedback jelas, dan checklist demo Week 12.
