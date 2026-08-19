# Instalasi Dependency - Chatbot Week 1

## Dependency

Week 1 hanya butuh:

- `streamlit`
- `Visual Studio Code (VS Code)` sebagai editor

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

## Menjalankan App

```bash
streamlit run chatbot/week-1/app.py
```

## File Requirements

Jika ingin install dari file:

```bash
pip install -r chatbot/week-1/requirements.txt
```
