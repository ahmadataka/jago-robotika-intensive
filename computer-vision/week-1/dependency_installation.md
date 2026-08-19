# Instalasi Dependency - Computer Vision Week 1

## Dependency

Week 1 butuh:

- `streamlit`
- `pillow`
- `numpy`
- `Visual Studio Code (VS Code)` sebagai editor

## Install VS Code

1. Download `Visual Studio Code`
2. Install seperti aplikasi biasa
3. Buka folder project `jago-robotika-intensive` di VS Code

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
- pastikan folder project berhasil dibuka
- pastikan file `computer-vision/week-1/app.py` bisa diedit

## Menjalankan App

```bash
streamlit run computer-vision/week-1/app.py
```

## File Requirements

```bash
pip install -r computer-vision/week-1/requirements.txt
```

## Catatan

`opencv-python` belum wajib untuk Week 1. Itu bisa mulai dipakai di minggu-minggu berikutnya saat masuk materi webcam atau image processing yang lebih lanjut.
