# Tutor Flow Week 5 - Chat UI with Streamlit

Durasi: `60 menit`

File utama:

- `app.py`

Tujuan:

- siswa mengenal `st.chat_input` dan `st.chat_message`
- siswa mengubah chatbot berbasis form menjadi tampilan percakapan
- siswa menampilkan pesan pengguna dan jawaban bot dalam bubble yang berbeda
- siswa memahami bahwa riwayat percakapan belum disimpan pada Week 5

## Persiapan Tutor

IDE yang dipakai:

- `Visual Studio Code (VS Code)`

Siswa membuat folder kerja sendiri, misalnya `chatbot-week-5`, lalu membuat satu file bernama `app.py`.

Jalankan dari terminal pada folder tersebut:

```bash
streamlit run app.py
```

Saat mengajar, file yang dibahas tetap `satu file yang sama`, tetapi ditulis bertahap.

## Alur 1 Jam

### 0-10 menit: Cek instalasi dan review Week 4

Langkah tutor:

1. Pastikan VS Code, Python, dan Streamlit sudah terpasang.
2. Minta siswa membuat folder `chatbot-week-5` dan file `app.py`.
3. Review Week 4: chatbot memilih jawaban menggunakan keyword dan `random.choice`.
4. Bandingkan tampilan `text_input` + button dengan tampilan aplikasi chat yang biasa dipakai siswa.

Perintah cek:

```bash
python3 --version
python3 -m pip show streamlit
```

Jika belum terpasang:

```bash
python3 -m pip install streamlit
```

### 10-20 menit: Bagian 1 - Kerangka app dan pesan pembuka bot

Tulis bagian awal:

```python
import random

import streamlit as st

st.title("Chat UI Bot")
st.caption("Sekarang chatbot tampil seperti aplikasi percakapan.")

bot_name = st.sidebar.selectbox("Pilih nama chatbot", ["Robo", "Milo", "Luna"])

with st.chat_message("assistant"):
    st.write(f"Halo! Aku {bot_name}. Ada yang ingin kamu tanyakan?")
```

Jelaskan:

- `st.chat_message("assistant")` membuat bubble untuk pesan bot.
- semua perintah di dalam blok `with` tampil sebagai bagian dari bubble tersebut.
- pesan pembuka membantu pengguna mengetahui bahwa bot siap menerima pertanyaan.

### 20-30 menit: Bagian 2 - Input dan bubble pengguna

Tambahkan:

```python
message = st.chat_input("Ketik pesan di sini...")

if message:
    with st.chat_message("user"):
        st.write(message)
```

Jelaskan:

- `st.chat_input` selalu berada di bagian bawah halaman.
- saat pengguna menekan Enter, teks disimpan ke variable `message`.
- `st.chat_message("user")` membuat bubble khusus pengguna.
- tidak dibutuhkan button terpisah karena Enter langsung mengirim pesan.

### 30-43 menit: Bagian 3 - Gunakan kembali logika chatbot

Tambahkan logika di dalam `if message:`:

```python
clean_message = message.lower().strip()

if "halo" in clean_message or "hai" in clean_message:
    answers = ["Halo juga!", "Hai! Senang bertemu denganmu."]
elif "robot" in clean_message:
    answers = [
        "Robot adalah mesin yang dapat diprogram untuk melakukan tugas.",
        "Robot dapat memakai sensor untuk memahami lingkungan.",
    ]
elif "python" in clean_message:
    answers = [
        "Python adalah bahasa pemrograman yang mudah dipelajari.",
        "Kita memakai Python untuk membuat chatbot ini.",
    ]
else:
    answers = [
        "Aku belum memahami pesan itu. Coba tanyakan tentang robot atau Python.",
        "Aku masih belajar. Coba gunakan kata halo, robot, atau Python.",
    ]
```

Jelaskan bahwa logika chatbot tidak berubah; yang berubah adalah cara pesan ditampilkan.

### 43-52 menit: Bagian 4 - Bubble jawaban chatbot

Tambahkan:

```python
answer = random.choice(answers)

with st.chat_message("assistant"):
    st.write(f"**{bot_name}:** {answer}")
```

Target hasil:

- pengguna menulis pesan di bagian bawah app.
- pesan pengguna tampil dalam bubble user.
- jawaban chatbot tampil dalam bubble assistant.
- chatbot tetap mengenali keyword dari minggu sebelumnya.

### 52-57 menit: Uji perbedaan form dan chat UI

Pengujian wajib:

- kirim `Halo`.
- kirim pertanyaan tentang robot.
- kirim pertanyaan tentang Python.
- kirim pesan tanpa keyword.

Diskusikan:

- tampilan chat lebih mudah dibaca daripada output `st.success`.
- setelah pesan baru dikirim, pesan sebelumnya belum tersimpan.
- kekurangan tersebut sengaja menjadi topik Week 6.

### 57-60 menit: Variasi dan penutup

Latihan:

- ubah pesan pembuka bot.
- tambahkan satu keyword dan dua variasi jawaban.
- ubah nama chatbot di sidebar.

Pengantar Week 6:

- siswa akan memakai `st.session_state` untuk menyimpan seluruh percakapan dan membuat tombol clear chat.

## Catatan Tutor

- Jangan menambahkan `session_state` pada Week 5; biarkan siswa melihat masalah hilangnya riwayat chat.
- Pastikan indentasi di dalam setiap blok `with` benar.
- Jika waktu terbatas, gunakan dua keyword saja, lalu fokuskan kelas pada `chat_input` dan `chat_message`.
