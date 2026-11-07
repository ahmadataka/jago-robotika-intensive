# Persiapan Komputer - Chatbot Week 12

Gunakan Python, VS Code, Streamlit, dan `google-genai` dari Week 11. Siswa bisa bekerja di folder sendiri tanpa mengunduh repo.

## Install dan jalankan

1. Buat folder `chatbot-week-12` dan buka di VS Code.
2. Salin `app.py` Week 11 ke folder tersebut sebagai titik awal.
3. Jika library belum terpasang, jalankan:

```bash
python -m pip install streamlit google-genai
```

4. Jika memakai key yang disimpan per project, buat `.streamlit/secrets.toml` di folder Week 12 dan gunakan key Week 11. Jika memakai global secrets atau environment variable `GEMINI_API_KEY`, tidak perlu membuat file baru.

```toml
GEMINI_API_KEY = "ISI_KEY_LOKAL_DI_SINI"
```

5. Dari folder yang berisi `app.py`, jalankan:

```bash
streamlit run app.py
```

Jika perintah Streamlit tidak dikenali, jalankan `python -m streamlit run app.py`. Di macOS, gunakan `python3` jika perintah `python` tidak tersedia.

## Cek sebelum demo

- Setelah mengubah secrets, hentikan server dengan `Ctrl+C` dan jalankan kembali.
- Jangan tampilkan secrets saat screen sharing atau memasukkan file tersebut ke Git.
- Centang konfirmasi di sidebar, lalu kirim satu pertanyaan pendek.
- Jika model sibuk (503), pilih model lain dan kirim ulang pesan. Jika kuota tercapai (429), periksa project di Google AI Studio.
- Jika belum punya key, tutor dapat mendemonstrasikan app dari laptopnya.
