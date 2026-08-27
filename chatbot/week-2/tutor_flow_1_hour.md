# Tutor Flow Week 2 - First Chatbot Flow

Durasi: `60 menit`

File utama:

- `app.py`

Tujuan:

- siswa memahami alur dasar chatbot: pesan pengguna -> proses program -> jawaban bot
- siswa membuat chatbot pertama yang dapat menerima satu pesan dan memberi satu respons
- siswa memahami bahwa chatbot belum harus memakai AI

## Persiapan Tutor

IDE yang dipakai:

- `Visual Studio Code (VS Code)`

Siswa membuat folder kerja sendiri, misalnya `chatbot-week-2`, lalu membuat satu file bernama `app.py`.

Jalankan dari terminal pada folder tersebut:

```bash
streamlit run app.py
```

Saat mengajar, file yang dibahas tetap `satu file yang sama`, tetapi ditulis bertahap.

## Alur 1 Jam

### 0-10 menit: Cek instalasi dan review Week 1

Langkah tutor:

1. Pastikan VS Code, Python, dan Streamlit sudah terpasang.
2. Minta siswa membuat folder `chatbot-week-2` dan membukanya di VS Code.
3. Buat file `app.py`.
4. Review singkat: Streamlit membuat tampilan app dari kode Python.
5. Jelaskan perbedaan app Week 1 dan chatbot: chatbot menerima pesan lalu memberi respons.

Perintah cek:

```bash
python3 --version
python3 -m pip show streamlit
```

Jika belum terpasang:

```bash
python3 -m pip install streamlit
```

### 10-20 menit: Bagian 1 - Judul dan tujuan chatbot

Tulis bagian awal:

```python
import streamlit as st

st.title("My First Chatbot")
st.write("Tulis pesan untuk memulai percakapan dengan chatbot.")
```

Jelaskan:

- `import` mengambil kemampuan Streamlit.
- judul memberi tahu pengguna fungsi app.
- chatbot selalu membutuhkan tempat bagi pengguna untuk memulai percakapan.

Target hasil sementara:

- app menampilkan judul dan instruksi singkat.

### 20-30 menit: Bagian 2 - Memberi identitas pada bot

Tambahkan bagian sidebar:

```python
bot_name = st.sidebar.selectbox("Pilih nama chatbot", ["Robo", "Milo", "Luna"])
st.sidebar.write("Chatbot ini masih belajar.")
```

Jelaskan:

- chatbot dapat memiliki nama atau karakter.
- `selectbox` menyimpan pilihan pengguna ke variable `bot_name`.
- pilihan itu nanti dipakai di jawaban chatbot.

Latihan cepat:

- tambahkan satu nama chatbot buatan siswa.

### 30-40 menit: Bagian 3 - Pesan dari pengguna

Tambahkan:

```python
message = st.text_input("Kamu:", placeholder="Contoh: Halo, aku suka robot!")
```

Jelaskan alur data:

```text
Pengguna mengetik pesan -> pesan disimpan di variable message -> chatbot memakai message
```

Tekankan bahwa pada tahap ini chatbot belum memahami isi pesan. Ia baru berhasil menerima pesan.

### 40-55 menit: Bagian 4 - Kirim pesan dan respons bot

Tambahkan bagian akhir:

```python
if st.button("Kirim Pesan"):
    if message:
        st.write(f"**Kamu:** {message}")
        st.success(f"**{bot_name}:** Halo! Aku menerima pesanmu.")
    else:
        st.warning("Tulis pesan dulu ya.")
```

Jelaskan:

- tombol menjadi pemicu percakapan.
- `if message:` mengecek apakah pengguna sudah menulis pesan.
- `f"..."` memasukkan isi variable ke dalam kalimat.
- respons bot masih tetap, karena logika memahami kata kunci baru dibuat pada Week 3.

Target hasil:

- siswa mengetik pesan.
- app menampilkan pesan tersebut dan respons dari chatbot.

### 55-60 menit: Variasi dan penutup

Latihan:

- ganti nama bot.
- ganti kalimat respons chatbot.
- buat respons bot bertema robot, sekolah, atau game.

Diskusi penutup:

- apa yang sudah bisa dilakukan chatbot ini?
- apa yang belum bisa dilakukan?
- bagaimana agar bot menjawab berbeda saat diberi pesan `halo` atau `robot`?

Jawaban terakhir menjadi pengantar Week 3: chatbot rule-based dengan `if-elif-else`.

## Catatan Tutor

- Jangan langsung memakai `st.chat_input`; tampilan chat dipelajari pada Week 5.
- Jangan langsung memakai Gemini atau API.
- Pastikan setiap siswa mencoba mengirim pesan kosong agar melihat fungsi validasi.
