# Persiapan Komputer - Chatbot Week 11

Panduan ini dikerjakan di komputer masing-masing. Siswa membuat file Python sendiri dari nol, sehingga tidak perlu membuka atau mengunduh folder repo Jago Robotika.

## Yang Perlu Disiapkan

- `Python`
- `Visual Studio Code (VS Code)` sebagai editor
- `streamlit`
- `google-genai`
- koneksi internet
- Gemini API key dari Google AI Studio

## Install VS Code

1. Download `Visual Studio Code` dari [code.visualstudio.com](https://code.visualstudio.com/).
2. Install seperti aplikasi biasa.
3. Buat folder baru, misalnya `chatbot-week-11`, di lokasi yang mudah ditemukan.
4. Buka VS Code, lalu pilih **File > Open Folder** dan pilih folder `chatbot-week-11`.

Extension opsional yang membantu:

- `Python`
- `Pylance`

## Install Library Python

Buka terminal di VS Code melalui **Terminal > New Terminal**, lalu jalankan:

```bash
pip install streamlit google-genai
```

Jika komputer memakai perintah `python3`:

```bash
python3 -m pip install streamlit google-genai
```

## Cek Instalasi

Mac atau Linux:

```bash
python3 --version
python3 -m pip show streamlit google-genai
```

Windows:

```bash
python --version
python -m pip show streamlit google-genai
```

## Menyiapkan Gemini API Key

1. Buka [Google AI Studio](https://aistudio.google.com/apikey).
2. Buat atau pilih API key yang akan digunakan untuk kelas.
3. Jangan kirim API key melalui meeting chat, screenshot, atau source code.
4. Di dalam folder `chatbot-week-11`, buat folder baru bernama `.streamlit`.
5. Di dalam folder tersebut, buat file `secrets.toml`.
6. Isi file:

```toml
GEMINI_API_KEY = "PASTE_API_KEY_DI_SINI"
```

Ganti teks contoh dengan API key milik pengguna. Jangan menambahkan `secrets.toml` ke GitHub. Jika project memakai Git, masukkan `.streamlit/` ke `.gitignore`.

Jika siswa belum dapat membuat API key, tutor dapat melakukan demonstrasi melalui screen sharing. Siswa tetap dapat menulis bagian UI dan mempelajari alur request tanpa membagikan key tutor.

## Membuat dan Menjalankan App

1. Di panel Explorer VS Code, klik ikon **New File**.
2. Beri nama file: `app.py`.
3. Ketik kode yang diberikan tutor secara bertahap.
4. Simpan dengan `Ctrl+S` (Windows) atau `Cmd+S` (Mac).
5. Pastikan terminal berada di folder yang sama dengan `app.py`.
6. Jalankan:

```bash
streamlit run app.py
```

Jika perintah `streamlit` tidak dikenali:

```bash
python3 -m streamlit run app.py
```

Di Windows:

```bash
python -m streamlit run app.py
```

## Troubleshooting

- `GEMINI_API_KEY belum ditemukan`: periksa nama folder `.streamlit`, nama file `secrets.toml`, dan nama key.
- Request gagal: periksa koneksi internet, status API key, quota akun, dan nama model.
- `503`: model sedang sibuk. Coba lagi nanti atau pilih model lain di sidebar. Pilihan awal app adalah `gemini-3.5-flash-lite`.
- `429`: batas request atau kuota project tercapai; periksa Usage di Google AI Studio.
- `401` atau `403`: periksa status key dan izin project.
- `404`: model tidak tersedia; pilih model lain.
- Setelah membuat atau mengubah `secrets.toml`, hentikan app dengan `Ctrl+C`, lalu jalankan kembali.

Untuk menghentikan app, kembali ke terminal lalu tekan `Ctrl+C`.
