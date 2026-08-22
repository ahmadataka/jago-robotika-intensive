# Persiapan Komputer - Computer Vision Week 1

Panduan ini dikerjakan di komputer masing-masing. Siswa membuat file Python sendiri dari nol, sehingga tidak perlu membuka atau mengunduh folder repo Jago Robotika.

## Dependency

Week 1 butuh:

- `streamlit`
- `pillow`
- `numpy`
- `Visual Studio Code (VS Code)` sebagai editor

## Install VS Code

1. Download `Visual Studio Code`
2. Install seperti aplikasi biasa
3. Buat folder baru, misalnya `computer-vision-week-1`, di lokasi yang mudah ditemukan
4. Buka VS Code, lalu pilih **File > Open Folder** dan pilih folder `computer-vision-week-1`

Opsional extension yang membantu:

- `Python`
- `Pylance`

## Opsi 1 - Install global

```bash
pip install streamlit pillow numpy
```

Jika memakai `python3`:

```bash
python3 -m pip install streamlit pillow numpy
```

## Opsi 2 - Pakai virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install streamlit pillow numpy
```

Untuk Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install streamlit pillow numpy
```

## Cek Instalasi

```bash
python3 --version
python3 -m pip show streamlit pillow numpy
```

Cek VS Code:

- pastikan VS Code bisa dibuka
- pastikan folder `computer-vision-week-1` berhasil dibuka

## Membuat File Python

1. Di panel Explorer VS Code, klik ikon **New File**.
2. Beri nama file: `app.py`.
3. Ketik kode yang diberikan tutor ke dalam file tersebut.
4. Simpan dengan `Ctrl+S` (Windows) atau `Cmd+S` (Mac).

## Menjalankan App

1. Buka terminal di VS Code melalui menu **Terminal > New Terminal**.
2. Pastikan terminal berada di folder yang sama dengan file `app.py`.
3. Jalankan:

```bash
streamlit run app.py
```

Browser akan membuka aplikasi Streamlit secara otomatis. Jika tidak, buka alamat yang muncul di terminal, biasanya `http://localhost:8501`.

Untuk menghentikan aplikasi, kembali ke terminal lalu tekan `Ctrl+C`.

## Jika Perintah Tidak Dikenali

```bash
python3 -m streamlit run app.py
```

Di Windows, gunakan:

```bash
python -m streamlit run app.py
```

## Catatan

`opencv-python` belum wajib untuk Week 1. Itu bisa mulai dipakai di minggu-minggu berikutnya saat masuk materi webcam atau image processing yang lebih lanjut.
