# Persiapan Komputer - Computer Vision Week 10

Panduan ini dikerjakan di komputer masing-masing. Siswa membuat file Python sendiri dari nol, sehingga tidak perlu membuka atau mengunduh folder repo Jago Robotika.

## Yang Perlu Disiapkan

- `Python`
- `Visual Studio Code (VS Code)` sebagai editor
- `streamlit`
- `pillow`
- `numpy`
- `opencv-python-headless` versi 4
- kamera laptop atau gambar uji

Webcam tidak wajib. Jika kamera tidak tersedia atau error, gunakan pilihan **Upload** pada aplikasi.

## Install VS Code

1. Download `Visual Studio Code` dari [code.visualstudio.com](https://code.visualstudio.com/).
2. Install seperti aplikasi biasa.
3. Buat folder baru, misalnya `computer-vision-week-10`, di lokasi yang mudah ditemukan.
4. Buka VS Code, lalu pilih **File > Open Folder** dan pilih folder `computer-vision-week-10`.

Extension opsional yang membantu:

- `Python`
- `Pylance`

## Install Library Python

Buka terminal di VS Code melalui **Terminal > New Terminal**, lalu jalankan:

```bash
pip install streamlit pillow numpy "opencv-python-headless<5"
```

Jika komputer memakai perintah `python3`:

```bash
python3 -m pip install streamlit pillow numpy "opencv-python-headless<5"
```

## Cek Instalasi

Mac atau Linux:

```bash
python3 --version
python3 -m pip show streamlit pillow numpy opencv-python-headless
```

Windows:

```bash
python --version
python -m pip show streamlit pillow numpy opencv-python-headless
```

## Membuat dan Menjalankan App

1. Di panel Explorer VS Code, klik ikon **New File**.
2. Beri nama file: `app.py`.
3. Ketik kode yang diberikan tutor secara bertahap.
4. Simpan dengan `Ctrl+S` (Windows) atau `Cmd+S` (Mac).
5. Di terminal VS Code, pastikan posisinya berada di folder yang sama dengan `app.py`.
6. Jalankan:

```bash
streamlit run app.py
```

Jika perintah `streamlit` tidak dikenali, gunakan:

```bash
python3 -m streamlit run app.py
```

Di Windows, gunakan:

```bash
python -m streamlit run app.py
```

## Menyiapkan Gambar Uji

Untuk filter:

- gunakan gambar dengan detail yang cukup jelas
- bandingkan hasil Grayscale dan Edge Filter

Untuk Color Object Counter:

- gunakan beberapa benda merah, hijau, atau biru
- beri jarak antar benda agar tidak dianggap sebagai satu objek
- gunakan latar dengan warna berbeda
- naikkan ukuran minimum jika noise ikut terhitung

Minta izin sebelum memotret atau menggunakan gambar orang lain. Untuk menghentikan app, kembali ke terminal lalu tekan `Ctrl+C`.
