# Persiapan Komputer - Computer Vision Week 8

Panduan ini dikerjakan di komputer masing-masing. Siswa membuat file Python sendiri dari nol, sehingga tidak perlu membuka atau mengunduh folder repo Jago Robotika.

## Yang Perlu Disiapkan

- `Python`
- `Visual Studio Code (VS Code)` sebagai editor
- `streamlit`
- `pillow`
- `numpy`
- kamera laptop atau dua gambar dari posisi yang sama

Webcam tidak wajib. Jika kamera tidak tersedia atau error, gunakan pilihan **Upload** pada aplikasi.

## Install VS Code

1. Download `Visual Studio Code` dari [code.visualstudio.com](https://code.visualstudio.com/).
2. Install seperti aplikasi biasa.
3. Buat folder baru, misalnya `computer-vision-week-8`, di lokasi yang mudah ditemukan.
4. Buka VS Code, lalu pilih **File > Open Folder** dan pilih folder `computer-vision-week-8`.

Extension opsional yang membantu:

- `Python`
- `Pylance`

## Install Library Python

Buka terminal di VS Code melalui **Terminal > New Terminal**, lalu jalankan:

```bash
pip install streamlit pillow numpy
```

Jika komputer memakai perintah `python3`:

```bash
python3 -m pip install streamlit pillow numpy
```

## Cek Instalasi

Mac atau Linux:

```bash
python3 --version
python3 -m pip show streamlit pillow numpy
```

Windows:

```bash
python --version
python -m pip show streamlit pillow numpy
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

## Menyiapkan Dua Frame

Jika memakai kamera:

1. Letakkan laptop di meja agar kamera tidak berpindah.
2. Ambil Frame 1 saat kondisi masih diam.
3. Gerakkan satu benda tanpa menggeser laptop.
4. Ambil Frame 2.

Jika kamera tidak tersedia atau error:

1. Pilih **Upload** pada sidebar.
2. Gunakan dua gambar dengan ukuran dan posisi kamera yang hampir sama.
3. Pastikan ada satu benda yang berpindah atau muncul pada gambar kedua.

Jika seluruh gambar dianggap bergerak, posisi kamera kemungkinan berubah. Ulangi pengambilan frame atau naikkan nilai **Batas perbedaan pixel**.

Untuk menghentikan app, kembali ke terminal lalu tekan `Ctrl+C`.
