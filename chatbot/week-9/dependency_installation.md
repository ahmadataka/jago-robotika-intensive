# Persiapan Komputer - Chatbot Week 9

Panduan ini dikerjakan di komputer masing-masing. Siswa membuat file Python sendiri dari nol, sehingga tidak perlu membuka atau mengunduh folder repo Jago Robotika.

## Yang Perlu Disiapkan

- `Python`
- `Visual Studio Code (VS Code)` sebagai editor
- `streamlit`

## Install VS Code

1. Download `Visual Studio Code` dari [code.visualstudio.com](https://code.visualstudio.com/).
2. Install seperti aplikasi biasa.
3. Buat folder baru, misalnya `chatbot-week-9`, di lokasi yang mudah ditemukan.
4. Buka VS Code, lalu pilih **File > Open Folder** dan pilih folder `chatbot-week-9`.

Extension opsional yang membantu:

- `Python`
- `Pylance`

## Install Streamlit

Buka terminal di VS Code melalui **Terminal > New Terminal**, lalu jalankan:

```bash
pip install streamlit
```

Jika komputer memakai perintah `python3`:

```bash
python3 -m pip install streamlit
```

## Cek Instalasi

Mac atau Linux:

```bash
python3 --version
python3 -m pip show streamlit
```

Windows:

```bash
python --version
python -m pip show streamlit
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

Browser biasanya membuka app secara otomatis di `http://localhost:8501`. Untuk menghentikan app, kembali ke terminal lalu tekan `Ctrl+C`.
