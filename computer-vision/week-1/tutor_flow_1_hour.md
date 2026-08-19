# Tutor Flow Week 1 - Computer Vision

Durasi: `60 menit`

File utama:

- `computer-vision/week-1/app.py`

Tujuan:

- siswa mengenal apa itu `computer vision`
- siswa melihat hubungan antara `gambar` dan `pixel`
- siswa membuat app sederhana untuk upload dan membaca gambar

## Persiapan Tutor

IDE yang dipakai:

- `Visual Studio Code (VS Code)`

Jalankan:

```bash
streamlit run computer-vision/week-1/app.py
```

Saat mengajar, file yang dibahas tetap `satu file yang sama`, tetapi dibuat bertahap.

## Alur 1 Jam

### 0-10 menit: Cek instalasi dan buka project

Langkah tutor:

1. Pastikan `VS Code` sudah terinstall
2. Jika belum, install `VS Code` dulu
3. Buka folder project di `VS Code`
4. Cek apakah `Python`, `Streamlit`, `Pillow`, dan `NumPy` sudah ada
5. Jika belum, install dulu
6. Jalankan app pertama kali

Langkah install VS Code:

- download `Visual Studio Code`
- install seperti aplikasi biasa
- buka folder `jago-robotika-intensive`
- pastikan file `computer-vision/week-1/app.py` terlihat di sidebar

Perintah cek:

```bash
python3 --version
python3 -m pip show streamlit pillow numpy
```

Jika belum terpasang:

```bash
python3 -m pip install streamlit pillow numpy
```

### 10-20 menit: Bagian 1 - Pembuka app

Fokus baris awal:

- `import numpy as np`
- `from PIL import Image`
- `import streamlit as st`
- `st.title(...)`
- `st.write(...)`

Tujuan penjelasan:

- computer vision memakai gambar sebagai input
- kita butuh library untuk app, gambar, dan array angka

Target hasil sementara:

- siswa melihat judul dan deskripsi singkat

### 20-30 menit: Bagian 2 - Upload gambar

Lanjutkan ke bagian:

- `uploaded_file = st.file_uploader(...)`
- `if uploaded_file is not None:`
- `else:`

Tujuan penjelasan:

- gambar menjadi input untuk computer vision
- kondisi berbeda saat gambar belum ada dan sudah ada

Target hasil sementara:

- app bisa meminta user upload gambar

### 30-45 menit: Bagian 3 - Membaca dan menampilkan gambar

Lanjutkan ke bagian:

- `Image.open(uploaded_file).convert("RGB")`
- `np.array(image)`
- `st.image(...)`

Tujuan penjelasan:

- gambar bisa dibuka sebagai data
- komputer membaca gambar sebagai array

Target hasil sementara:

- gambar asli tampil di app

### 45-55 menit: Bagian 4 - Info gambar

Lanjutkan ke bagian:

- `image.width`
- `image.height`
- `image_array.shape`
- `image_array.shape[2]`
- `st.write(...)`

Tujuan penjelasan:

- gambar punya lebar, tinggi, dan channel
- array adalah cara komputer menyimpan gambar

### 55-60 menit: Penutup

Diskusi:

- apa itu pixel?
- kenapa komputer membaca gambar sebagai angka?
- apa yang ingin mereka coba di minggu berikutnya?

## Catatan Tutor

- Tidak perlu membuat beberapa file terpisah.
- Tulis dan jelaskan file yang sama secara bertahap.
- Jika waktu terbatas, prioritas minimum:
  - upload gambar
  - tampilkan gambar
  - tunjukkan ukuran gambar
  - tunjukkan bentuk array
