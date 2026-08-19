# Instalasi Dependency - Chatbot Week 1

## Dependency

Week 1 hanya butuh:

- `streamlit`
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
pip install streamlit
```

Jika memakai `python3`:

```bash
python3 -m pip install streamlit
```

## Opsi 2 - Pakai virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install streamlit
```

Untuk Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install streamlit
```

## Cek Instalasi

```bash
python3 --version
python3 -m pip show streamlit
```

Cek VS Code:

- pastikan VS Code bisa dibuka
- pastikan folder project berhasil dibuka
- pastikan file `chatbot/week-1/app.py` bisa diedit

## Menjalankan App

```bash
streamlit run chatbot/week-1/app.py
```

## File Requirements

Jika ingin install dari file:

```bash
pip install -r chatbot/week-1/requirements.txt
```
