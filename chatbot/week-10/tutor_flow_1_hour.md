# Tutor Flow Week 10 - Prepare for AI Chatbot

Durasi: `60 menit`

File utama:

- `app.py`
- `starter.py` sebagai template awal opsional

Tujuan:

- siswa membedakan chatbot rule-based dan chatbot AI
- siswa memahami alur sederhana prompt, request, API, dan response
- siswa menyusun prompt dengan peran, tugas, format, dan pertanyaan
- siswa memahami safety dasar sebelum mengirim data ke layanan AI
- siswa menjalankan simulasi tanpa API key atau AI sungguhan

## Persiapan Tutor

IDE yang dipakai:

- `Visual Studio Code (VS Code)`

Siswa membuat folder kerja sendiri, misalnya `chatbot-week-10`, lalu membuat satu file bernama `app.py`.

Jalankan dari terminal pada folder tersebut:

```bash
streamlit run app.py
```

Week 10 tidak membutuhkan akun Gemini atau API key. Tegaskan bahwa output yang ditampilkan masih simulasi.

Untuk menghemat waktu mengetik, tutor dapat membagikan isi `starter.py` sebelum kelas. Siswa menyalin template tersebut ke file `app.py`, lalu hanya melengkapi bagian prompt, request, dan response selama kelas. `app.py` di materi tutor adalah kode final untuk pengecekan.

## Alur 1 Jam

### 0-10 menit: Cek instalasi dan bandingkan dua chatbot

Langkah tutor:

1. Pastikan VS Code, Python, dan Streamlit sudah terpasang.
2. Minta siswa membuat folder `chatbot-week-10` dan file `app.py`.
3. Tunjukkan chatbot Week 9 dan tanyakan sesuatu di luar rules.
4. Jelaskan bahwa chatbot rule-based hanya mengikuti aturan yang ditulis programmer.
5. Jelaskan bahwa AI dapat menghasilkan jawaban baru, tetapi jawabannya tetap dapat salah.

Perintah cek:

```bash
python3 --version
python3 -m pip show streamlit
```

Jika belum terpasang:

```bash
python3 -m pip install streamlit
```

Perbandingan sederhana:

| Rule-based | AI chatbot |
| --- | --- |
| mencari keyword | memahami prompt secara lebih fleksibel |
| jawaban ditulis programmer | jawaban dibuat model |
| hasil lebih mudah diprediksi | hasil dapat berbeda atau keliru |
| tidak memerlukan API | biasanya memakai API dan layanan model |

### 10-18 menit: Konsep API dengan analogi sederhana

Gunakan analogi restoran:

- pengguna adalah pelanggan
- app adalah pelayan
- API adalah jalur pemesanan
- model AI adalah dapur
- prompt adalah pesanan
- response adalah makanan yang dikirim kembali

Gambar alur berikut di layar atau papan digital:

```text
Pertanyaan -> Prompt -> Request API -> Model AI -> Response -> App
```

Jelaskan bahwa Week 10 hanya mensimulasikan alur tersebut di dalam satu file Python.

### 18-26 menit: Bagian 1 - Buka template dan review tampilan

Jika memakai `starter.py`, bagian tampilan, sidebar, input, dan validasi safety sudah tersedia. Tutor cukup membacanya bersama siswa, bukan mengetik ulang semua baris.

Bagian awal template:

```python
import streamlit as st

st.title("AI Request Simulator")
st.caption("Pelajari prompt, request, dan response sebelum memakai Gemini sungguhan.")
st.warning("Mode simulasi: app ini belum mengirim data ke AI atau internet.")

st.sidebar.header("Alur AI Chatbot")
st.sidebar.write("1. Pengguna menulis pertanyaan")
st.sidebar.write("2. App menyusun prompt")
st.sidebar.write("3. API menerima request")
st.sidebar.write("4. Model mengirim response")
```

Pastikan siswa dapat menjelaskan kembali arti empat langkah tersebut. Jika tidak memakai template, tulis bagian ini secara bertahap seperti biasa.

### 26-36 menit: Bagian 2 - Review input untuk menyusun prompt

Bagian berikut sudah tersedia dalam template dan digunakan untuk menjelaskan input prompt:

```python
role = st.selectbox(
    "Peran AI",
    ["Tutor sains", "Tutor Python", "Pemandu museum"],
)
response_style = st.selectbox(
    "Format jawaban",
    ["Jawaban singkat", "Daftar 3 poin", "Kuis 1 soal"],
)
question = st.text_area("Pertanyaan", placeholder="Contoh: Mengapa langit berwarna biru?")
safe_to_send = st.checkbox("Saya tidak memasukkan password, alamat, atau data pribadi.")
```

Jelaskan empat bagian prompt:

- peran: AI diminta bertindak sebagai siapa
- tugas: apa yang harus dilakukan
- format: bentuk jawaban yang diinginkan
- pertanyaan: informasi yang ingin diketahui pengguna

### 36-44 menit: Bagian 3 - Review safety sebelum request

Tombol dan validasi berikut juga sudah tersedia dalam template:

```python
if st.button("Kirim Simulasi"):
    if not question.strip():
        st.warning("Tulis pertanyaan terlebih dahulu.")
    elif not safe_to_send:
        st.error("Periksa safety terlebih dahulu sebelum mengirim prompt.")
```

Diskusikan data yang tidak boleh dimasukkan:

- password
- alamat rumah lengkap
- nomor telepon pribadi
- nomor identitas
- rahasia milik orang lain

Tekankan bahwa AI dapat menghasilkan informasi yang salah sehingga jawaban penting harus diperiksa kembali.

### 44-53 menit: Bagian 4 - Susun prompt, request, dan response

Di dalam bagian `else`, susun prompt:

```python
prompt = f"""Peran: Kamu adalah {role.lower()}.
Tugas: Jawab pertanyaan pengguna dengan bahasa yang mudah dipahami siswa.
Format: {response_style}.
Pertanyaan: {question.strip()}"""
```

Lalu buat dictionary request dan response mengikuti kode lengkap.

Jelaskan:

- request adalah data yang dikirim app menuju API.
- model menunjukkan AI yang ingin digunakan.
- response adalah data balasan dari API.
- pada Week 10, kedua dictionary dibuat secara lokal dan tidak dikirim ke internet.

### 53-58 menit: Eksperimen prompt

Siswa menjalankan minimal tiga percobaan:

1. Pertanyaan sama dengan peran berbeda.
2. Pertanyaan sama dengan format berbeda.
3. Pertanyaan kosong atau checkbox safety belum dicentang.

Tutor meminta satu atau dua siswa menunjukkan hasil melalui screen sharing. Siswa lain tetap menjalankan app masing-masing.

### 58-60 menit: Penutup

Minta siswa menyebutkan kembali:

- apa itu prompt
- apa itu API request
- apa itu response
- mengapa data pribadi tidak boleh dikirim
- mengapa jawaban AI perlu diperiksa

Pengantar Week 11:

- response simulasi akan diganti dengan response Gemini sungguhan menggunakan `google-genai` dan API key yang disiapkan secara aman.

## Catatan Tutor

- Jangan memasukkan API key pada Week 10.
- Jangan menyebut output simulasi sebagai jawaban AI sungguhan.
- Fokus pada alur dan kualitas prompt, bukan detail jaringan atau JSON yang rumit.
- Jika waktu terbatas, prioritaskan diagram alur, prompt builder, safety, dan satu simulasi lengkap.
