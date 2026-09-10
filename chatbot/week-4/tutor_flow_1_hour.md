# Tutor Flow Week 4 - Better Chatbot Responses

Durasi: `60 menit`

File utama:

- `app.py`

Tujuan:

- siswa membuat jawaban chatbot yang lebih bervariasi dengan list dan `random.choice`
- siswa menggunakan `or` untuk mengenali beberapa keyword
- siswa memahami kondisi bertingkat untuk memberi respons yang lebih sesuai
- siswa memperbaiki fallback response agar lebih ramah

## Persiapan Tutor

IDE yang dipakai:

- `Visual Studio Code (VS Code)`

Siswa membuat folder kerja sendiri, misalnya `chatbot-week-4`, lalu membuat satu file bernama `app.py`.

Jalankan dari terminal pada folder tersebut:

```bash
streamlit run app.py
```

Saat mengajar, file yang dibahas tetap `satu file yang sama`, tetapi ditulis bertahap.

## Alur 1 Jam

### 0-10 menit: Cek instalasi dan review Week 3

Langkah tutor:

1. Pastikan VS Code, Python, dan Streamlit sudah terpasang.
2. Minta siswa membuat folder `chatbot-week-4` dan file `app.py`.
3. Review Week 3: keyword dipilih dengan `if-elif-else`, tetapi setiap keyword selalu menghasilkan jawaban yang sama.
4. Tanyakan bagaimana membuat bot terasa tidak monoton.

Perintah cek:

```bash
python3 --version
python3 -m pip show streamlit
```

Jika belum terpasang:

```bash
python3 -m pip install streamlit
```

### 10-20 menit: Bagian 1 - Kerangka chatbot dan library random

Tulis bagian awal sampai input pesan:

```python
import random

import streamlit as st

st.title("Friendly Rule-Based Chatbot")
st.write("Chatbot ini punya beberapa variasi jawaban.")

bot_name = st.sidebar.selectbox("Pilih nama chatbot", ["Robo", "Milo", "Luna"])
message = st.text_input("Kamu:")
```

Jelaskan:

- struktur app melanjutkan chatbot Week 3.
- `random` adalah library bawaan Python untuk memilih secara acak.
- library bawaan Python tidak perlu di-install dengan `pip`.

### 20-30 menit: Bagian 2 - List jawaban dan random.choice

Mulai blok tombol dan respons sapaan:

```python
if st.button("Kirim Pesan"):
    if message:
        clean_message = message.lower().strip()

        if "halo" in clean_message or "hai" in clean_message:
            answers = [
                "Halo juga! Senang bertemu denganmu.",
                "Hai! Ada yang ingin kamu tanyakan?",
                "Halo! Aku siap mengobrol denganmu.",
            ]
```

Jelaskan:

- list menyimpan beberapa jawaban di dalam satu variable.
- `or` membuat bot menerima kata `halo` maupun `hai`.
- nanti `random.choice(answers)` memilih satu jawaban dari list.

Uji sementara dengan mengganti isi list dan melihat hasil yang berbeda.

### 30-43 menit: Bagian 3 - Kondisi bertingkat untuk topik robot

Tambahkan:

```python
elif "robot" in clean_message:
    if "suka" in clean_message or "membuat" in clean_message:
        answers = [
            "Keren! Membuat robot melatih kreativitas dan logika.",
            "Aku juga suka robot. Robot apa yang ingin kamu buat?",
        ]
    else:
        answers = [
            "Robot adalah mesin yang dapat diprogram.",
            "Robot memakai sensor, program, dan bagian yang bisa bergerak.",
        ]
```

Jelaskan:

- kondisi pertama menemukan topik `robot`.
- kondisi di dalamnya memeriksa maksud yang lebih khusus, yaitu `suka` atau `membuat`.
- pesan `Apa itu robot?` dan `Aku suka membuat robot` dapat menerima jenis jawaban berbeda.

### 43-50 menit: Bagian 4 - Respons Python dan fallback

Tambahkan:

```python
elif "python" in clean_message:
    answers = [
        "Python adalah bahasa yang ramah untuk belajar coding.",
        "Kita memakai Python untuk membuat chatbot ini.",
    ]
else:
    answers = [
        "Aku belum memahami pesan itu. Coba tanyakan tentang robot atau Python.",
        "Hmm, aku masih belajar. Coba gunakan kata halo, robot, atau Python.",
    ]
```

Jelaskan bahwa fallback tetap perlu membantu pengguna, bukan hanya mengatakan `tidak tahu`.

### 50-56 menit: Bagian 5 - Pilih dan tampilkan jawaban

Tambahkan:

```python
answer = random.choice(answers)
st.write(f"**Kamu:** {message}")
st.success(f"**{bot_name}:** {answer}")
```

Pengujian wajib:

- kirim `halo` beberapa kali dan amati variasinya.
- coba `Apa itu robot?`.
- coba `Aku suka membuat robot`.
- coba pesan yang tidak memiliki keyword.

### 56-60 menit: Variasi dan penutup

Latihan:

- tambahkan satu jawaban pada list sapaan.
- tambahkan keyword alternatif, misalnya `coding` untuk topik Python.
- buat kondisi bertingkat untuk topik pilihan siswa.

Pengantar Week 5:

- logika bot sudah lebih menarik; berikutnya tampilannya diubah menjadi bubble percakapan memakai `st.chat_input` dan `st.chat_message`.

## Catatan Tutor

- Mulai dengan satu list jawaban sebelum menulis semua kondisi.
- Tekankan bahwa respons tetap mengikuti aturan; bot belum memakai AI.
- Jika waktu terbatas, prioritaskan sapaan, topik robot, dan fallback.
