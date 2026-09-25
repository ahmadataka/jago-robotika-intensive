# Persiapan Komputer - Computer Vision Week 6

Panduan ini dikerjakan di komputer masing-masing. Siswa membuat file Python sendiri dari nol, sehingga tidak perlu membuka atau mengunduh folder repo Jago Robotika.

## Yang Perlu Disiapkan

- komputer atau laptop dengan kamera
- browser yang mendapat izin menggunakan kamera
- `Python`
- `Visual Studio Code (VS Code)` sebagai editor
- `streamlit`
- `pillow`
- `numpy`

## Install VS Code

1. Download `Visual Studio Code` dari [code.visualstudio.com](https://code.visualstudio.com/).
2. Install seperti aplikasi biasa.
3. Buat folder baru, misalnya `computer-vision-week-6`, di lokasi yang mudah ditemukan.
4. Buka VS Code, lalu pilih **File > Open Folder** dan pilih folder `computer-vision-week-6`.

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

```bash
python3 --version
python3 -m pip show streamlit pillow numpy
```

## Membuat dan Menjalankan App

1. Di panel Explorer VS Code, klik ikon **New File**.
2. Beri nama file: `app.py`.
3. Ketik kode yang diberikan tutor.
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

## Izin Kamera

Saat browser meminta izin kamera, pilih **Allow** atau **Izinkan**. Jika kamera tidak muncul:

- periksa izin kamera pada browser
- tutup aplikasi lain yang sedang memakai kamera
- refresh halaman Streamlit
- pastikan alamat yang dibuka adalah `localhost`

Untuk menghentikan app, kembali ke terminal lalu tekan `Ctrl+C`.
