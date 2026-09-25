# Tutor Flow Week 6 - Chat History with Session State

Durasi: `60 menit`

File utama:

- `app.py`

Tujuan:

- siswa memahami alasan Streamlit kehilangan data saat app dijalankan ulang
- siswa memakai `st.session_state` untuk menyimpan percakapan
- siswa menampilkan kembali semua pesan dengan loop
- siswa membuat tombol clear chat

## Persiapan Tutor

IDE yang dipakai:

- `Visual Studio Code (VS Code)`

Siswa membuat folder kerja sendiri, misalnya `chatbot-week-6`, lalu membuat satu file bernama `app.py`.

Jalankan dari terminal pada folder tersebut:

```bash
streamlit run app.py
```

Saat mengajar, file yang dibahas tetap `satu file yang sama`, tetapi ditulis bertahap.

## Alur 1 Jam

### 0-10 menit: Cek instalasi dan review masalah Week 5

Langkah tutor:

1. Pastikan VS Code, Python, dan Streamlit sudah terpasang.
2. Minta siswa membuat folder `chatbot-week-6` dan file `app.py`.
3. Review Week 5: setiap pesan baru membuat pesan sebelumnya hilang.
4. Jelaskan bahwa Streamlit menjalankan ulang file saat pengguna berinteraksi.
5. Perkenalkan `st.session_state` sebagai tempat menyimpan data sementara.

Perintah cek:

```bash
python3 --version
python3 -m pip show streamlit
```

Jika belum terpasang:

```bash
python3 -m pip install streamlit
```

### 10-20 menit: Bagian 1 - Kerangka app dan tempat penyimpanan pesan

Tulis bagian awal:

```python
import random

import streamlit as st

st.title("Chatbot with Memory")
st.caption("Chatbot sekarang mengingat percakapan selama app masih terbuka.")

bot_name = st.sidebar.selectbox("Pilih nama chatbot", ["Robo", "Milo", "Luna"])
```

Tambahkan penyimpanan awal:

```python
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": f"Halo! Aku {bot_name}. Ada yang ingin kamu tanyakan?"}
    ]
```

Jelaskan:

- `messages` adalah nama tempat penyimpanan percakapan.
- list menyimpan banyak pesan secara berurutan.
- setiap pesan mempunyai `role` dan `content`.
- kondisi `if` mencegah list dibuat ulang setiap kali app rerun.

### 20-30 menit: Bagian 2 - Tampilkan seluruh history

Tambahkan:

```python
for item in st.session_state.messages:
    with st.chat_message(item["role"]):
        st.write(item["content"])
```

Jelaskan:

- loop membaca setiap pesan dari awal sampai akhir.
- `item["role"]` menentukan bubble user atau assistant.
- `item["content"]` adalah teks yang ditampilkan.

Target sementara:

- pesan pembuka bot tetap terlihat setelah app rerun.

### 30-40 menit: Bagian 3 - Simpan pesan pengguna

Tambahkan:

```python
message = st.chat_input("Ketik pesan di sini...")

if message:
    st.session_state.messages.append({"role": "user", "content": message})

    with st.chat_message("user"):
        st.write(message)
```

Jelaskan:

- `.append()` menambahkan satu pesan baru ke bagian akhir list.
- pesan disimpan dahulu, kemudian ditampilkan.
- setelah rerun berikutnya, loop akan menampilkan pesan itu lagi.

### 40-50 menit: Bagian 4 - Buat dan simpan jawaban bot

Gunakan kembali logika keyword Week 5 untuk menghasilkan variable `answer`, lalu tambahkan:

```python
answer = random.choice(answers)
bot_message = f"**{bot_name}:** {answer}"
st.session_state.messages.append({"role": "assistant", "content": bot_message})

with st.chat_message("assistant"):
    st.write(bot_message)
```

Jelaskan:

- pesan bot juga harus dimasukkan ke list.
- urutan append menjaga percakapan tetap user lalu assistant.
- semua pesan akan tetap terlihat selama tab dan sesi Streamlit masih aktif.

### 50-56 menit: Bagian 5 - Tombol clear chat

Letakkan sebelum loop history:

```python
if st.sidebar.button("Clear Chat"):
    st.session_state.messages = [
        {"role": "assistant", "content": f"Halo! Aku {bot_name}. Mari mulai percakapan baru!"}
    ]
    st.rerun()
```

Jelaskan:

- tombol mengganti history lama dengan satu pesan pembuka baru.
- `st.rerun()` langsung menggambar ulang tampilan setelah data dibersihkan.

### 56-60 menit: Pengujian dan penutup

Pengujian wajib:

- kirim minimal tiga pesan dan pastikan semuanya tetap terlihat.
- ubah keyword pertanyaan dan periksa urutan bubble.
- tekan clear chat dan pastikan history lama hilang.

Latihan tambahan:

- ubah pesan setelah clear chat.
- tampilkan jumlah pesan dengan `len(st.session_state.messages)`.

Pengantar Week 7:

- siswa akan memilih tema chatbot sendiri dan menyusun daftar pertanyaan serta jawaban untuk mini project.

## Catatan Tutor

- Gunakan gambar list sederhana di papan untuk menjelaskan urutan pesan.
- Jangan terlalu lama membahas dictionary; cukup jelaskan bahwa setiap pesan punya role dan content.
- Jika waktu terbatas, prioritaskan penyimpanan history dan clear chat; variasi respons dapat disederhanakan.
