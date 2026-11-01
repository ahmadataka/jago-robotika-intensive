# Tutor Flow Week 11 - Intro to Gemini with Streamlit

Durasi: `60 menit`

File utama:

- `app.py`

Tujuan:

- siswa menggunakan library `google-genai`
- siswa menyimpan API key di Streamlit Secrets
- siswa membuat client Gemini
- siswa mengirim satu prompt dan menampilkan response
- siswa mempertahankan safety saat menggunakan AI

## Persiapan Tutor

IDE yang dipakai:

- `Visual Studio Code (VS Code)`

Siswa membuat folder kerja sendiri, misalnya `chatbot-week-11`, lalu membuat satu file bernama `app.py`.

Jalankan dari terminal pada folder tersebut:

```bash
streamlit run app.py
```

Sebelum kelas:

- pastikan `streamlit` dan `google-genai` dapat di-install
- pastikan model `gemini-3.5-flash-lite` tersedia; gunakan pilihan model di sidebar bila layanan model tertentu sedang sibuk
- siapkan API key untuk demonstrasi tutor
- kirim instruksi pembuatan key kepada siswa lebih awal jika mereka memakai key sendiri
- jangan pernah mengirim atau menampilkan key melalui meeting chat atau screen sharing

Jika siswa belum memiliki API key, gunakan satu demonstrasi tutor. Jangan membagikan key tutor kepada peserta.

## Alur 1 Jam

### 0-10 menit: Cek instalasi, API key, dan safety

Langkah tutor:

1. Pastikan VS Code, Python, Streamlit, dan `google-genai` sudah terpasang.
2. Minta siswa membuat folder `chatbot-week-11` dan file `app.py`.
3. Review alur Week 10: prompt, request, model, dan response.
4. Pastikan siswa membuat `.streamlit/secrets.toml` tanpa screen sharing isi key.
5. Ulangi larangan memasukkan data pribadi ke prompt.

Perintah cek:

```bash
python3 --version
python3 -m pip show streamlit google-genai
```

Jika belum terpasang:

```bash
python3 -m pip install streamlit google-genai
```

Isi `.streamlit/secrets.toml`:

```toml
GEMINI_API_KEY = "PASTE_API_KEY_DI_SINI"
```

Pastikan file tersebut tidak dimasukkan ke Git.

### 10-18 menit: Bagian 1 - Import dan tampilan app

Tulis:

```python
import os

from google import genai
import streamlit as st

MODEL_NAME = "gemini-3.5-flash-lite"

st.title("My First Gemini App")
st.caption("Kirim satu prompt ke Gemini dan tampilkan responsenya.")
```

Jelaskan:

- `google-genai` adalah SDK untuk berkomunikasi dengan Gemini.
- nama model menentukan model yang menerima prompt.
- model dapat berubah pada masa depan sehingga tutor perlu memeriksa dokumentasi resmi.

### 18-27 menit: Bagian 2 - Baca key dan buat client

Tambahkan fungsi `get_api_key()` mengikuti kode lengkap, lalu:

```python
api_key = get_api_key()

if not api_key:
    st.error("GEMINI_API_KEY belum ditemukan.")
    st.stop()

client = genai.Client(api_key=api_key, http_options={"timeout": 30000})
```

Jelaskan:

- API key membuktikan bahwa request berasal dari project yang diizinkan.
- key dibaca saat app berjalan dan tidak ditulis dalam source code.
- `client` menjadi penghubung antara app dan Gemini API.

### 27-36 menit: Bagian 3 - Input dan safety

Tambahkan:

```python
role = st.selectbox(
    "Peran Gemini",
    ["Tutor sains", "Tutor Python", "Pemandu museum"],
)
question = st.text_area("Pertanyaan", placeholder="Contoh: Jelaskan cara kerja sensor ultrasonik.")
safe_to_send = st.checkbox("Saya tidak memasukkan password, alamat, atau data pribadi.")
```

Tambahkan validasi pertanyaan kosong dan checkbox safety mengikuti kode lengkap.

### 36-45 menit: Bagian 4 - Susun prompt

Di dalam bagian `else`, tambahkan:

```python
prompt = f"""Kamu adalah {role.lower()}.
Jawab dengan bahasa Indonesia yang mudah dipahami siswa.
Berikan jawaban singkat dan jelas.
Pertanyaan: {question.strip()}"""
```

Hubungkan dengan Week 10:

- peran menentukan cara Gemini menjawab
- instruksi bahasa menentukan target pengguna
- format singkat mengurangi jawaban yang terlalu panjang
- pertanyaan pengguna ditempatkan pada bagian akhir

### 45-53 menit: Bagian 5 - Request Gemini dan tampilkan response

Tambahkan:

```python
response = client.models.generate_content(
    model=model_name,
    contents=prompt,
)
answer = response.text or "Gemini belum memberikan jawaban."

st.subheader("Jawaban Gemini")
st.write(answer)
```

Bungkus request dengan spinner dan `try-except` mengikuti kode lengkap.

Tambahkan pilihan `model_name` di sidebar seperti kode lengkap. Jika muncul 503, model sedang sibuk; pilih model lain atau coba lagi nanti. Error ini tidak berarti API key salah.

Jelaskan:

- `generate_content` mengirim prompt melalui internet.
- `response.text` berisi teks jawaban dari Gemini.
- `try-except` mencegah app berhenti total saat key, koneksi, quota, atau model bermasalah.

### 53-58 menit: Pengujian online

Siswa mencoba:

1. Pertanyaan yang sama dengan dua pilihan peran.
2. Pertanyaan kosong.
3. Checkbox safety belum dicentang.
4. Satu pertanyaan tentang materi sekolah.
5. Memeriksa satu fakta dari jawaban Gemini menggunakan sumber lain.

Tutor dapat meminta satu siswa screen sharing hasil app, tetapi jangan membuka `secrets.toml` saat screen sharing.

### 58-60 menit: Penutup

Minta siswa menjelaskan kembali:

- lokasi API key
- fungsi `genai.Client`
- fungsi `generate_content`
- alasan jawaban AI perlu diperiksa

Pengantar Week 12:

- siswa akan menggabungkan Gemini dengan chat UI, history, tema khusus, dan persiapan presentasi final.

## Catatan Tutor

- Jangan menulis API key pada `app.py`, slide, meeting chat, atau screenshot.
- Jangan menampilkan isi `secrets.toml` saat screen sharing.
- Gunakan pertanyaan pendek agar penggunaan quota tetap terkendali.
- Jika API tidak dapat digunakan, tetap ajarkan struktur kode dan lakukan satu demonstrasi dari komputer tutor.
- Jika waktu terbatas, prioritaskan client, satu request berhasil, safety, dan verifikasi jawaban.
