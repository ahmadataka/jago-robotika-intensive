# Tutor Flow Week 7 - Topic-Based Chatbot Project

Durasi: `60 menit`

File utama:

- `app.py`

Tujuan:

- siswa memilih satu tema chatbot yang jelas
- siswa menyusun keyword dan jawaban yang sesuai tema
- siswa menyimpan pengetahuan chatbot dalam dictionary
- siswa membuat sidebar informasi dan petunjuk penggunaan
- siswa menghasilkan mini project chatbot bertema

## Persiapan Tutor

IDE yang dipakai:

- `Visual Studio Code (VS Code)`

Siswa membuat folder kerja sendiri, misalnya `chatbot-week-7`, lalu membuat satu file bernama `app.py`.

Jalankan dari terminal pada folder tersebut:

```bash
streamlit run app.py
```

Saat mengajar, file yang dibahas tetap `satu file yang sama`, tetapi ditulis bertahap.

## Alur 1 Jam

### 0-10 menit: Cek instalasi dan rencanakan tema

Langkah tutor:

1. Pastikan VS Code, Python, dan Streamlit sudah terpasang.
2. Minta siswa membuat folder `chatbot-week-7` dan file `app.py`.
3. Review Week 6: history disimpan dengan `st.session_state`.
4. Tunjukkan contoh tema: luar angkasa, hewan, olahraga, sekolah, atau robotika.
5. Minta setiap siswa memilih satu tema dan menulis minimal empat keyword beserta jawabannya.

Perintah cek:

```bash
python3 --version
python3 -m pip show streamlit
```

Jika belum terpasang:

```bash
python3 -m pip install streamlit
```

Contoh perencanaan:

| Keyword | Jawaban singkat |
| --- | --- |
| planet | Planet mengelilingi sebuah bintang. |
| matahari | Matahari adalah pusat tata surya. |
| bulan | Bulan adalah satelit alami Bumi. |
| astronaut | Astronaut pergi ke luar angkasa. |

### 10-18 menit: Bagian 1 - Identitas mini project

Tulis bagian awal:

```python
import streamlit as st

BOT_NAME = "Nova"

st.title("Space Explorer Bot")
st.caption("Tanyakan fakta sederhana tentang luar angkasa.")
```

Jelaskan:

- nama, judul, dan deskripsi harus sesuai dengan tema.
- `BOT_NAME` ditulis sekali agar mudah diganti.
- siswa boleh langsung mengganti contoh luar angkasa dengan temanya sendiri.

### 18-25 menit: Bagian 2 - Sidebar informasi

Tambahkan:

```python
st.sidebar.header("Tentang Chatbot")
st.sidebar.write("Nova adalah chatbot bertema luar angkasa.")
st.sidebar.write("Coba gunakan kata: planet, matahari, bulan, atau astronaut.")
```

Jelaskan:

- sidebar memberi tahu pengguna kemampuan chatbot.
- petunjuk keyword membantu pengguna mencoba app.
- jangan menjanjikan bahwa chatbot dapat menjawab semua pertanyaan.

### 25-35 menit: Bagian 3 - Daftar pengetahuan chatbot

Tambahkan dictionary:

```python
responses = {
    "planet": "Planet adalah benda langit yang mengelilingi sebuah bintang.",
    "matahari": "Matahari adalah bintang yang menjadi pusat tata surya kita.",
    "bulan": "Bulan adalah satelit alami Bumi.",
    "astronaut": "Astronaut adalah orang yang dilatih untuk pergi ke luar angkasa.",
}
```

Jelaskan:

- bagian kiri adalah keyword.
- bagian kanan adalah jawaban untuk keyword tersebut.
- satu pasangan keyword dan jawaban dipisahkan dengan koma.
- siswa dapat menambah pengetahuan tanpa membuat banyak blok `elif`.

### 35-43 menit: Bagian 4 - Gunakan kembali chat history

Salin dan sesuaikan pola Week 6:

```python
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": f"Halo! Aku {BOT_NAME}. Ayo belajar luar angkasa!"}
    ]

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = [
        {"role": "assistant", "content": f"Halo! Aku {BOT_NAME}. Mulai lagi, yuk!"}
    ]
    st.rerun()

for item in st.session_state.messages:
    with st.chat_message(item["role"]):
        st.write(item["content"])
```

Tekankan bahwa siswa tidak harus mempelajari ulang seluruh bagian Week 6. Fokus Week 7 adalah isi dan identitas project.

### 43-53 menit: Bagian 5 - Cari jawaban berdasarkan tema

Setelah mengambil dan menyimpan pesan pengguna, tambahkan:

```python
answer = "Maaf, aku belum tahu. Coba tanyakan planet, matahari, bulan, atau astronaut."
clean_message = message.lower().strip()

for keyword, response in responses.items():
    if keyword in clean_message:
        answer = response
        break
```

Jelaskan:

- chatbot membaca setiap pasangan keyword dan jawaban.
- jika keyword ditemukan, variable `answer` diganti.
- `break` menghentikan pencarian setelah menemukan jawaban pertama.
- jawaban awal dipakai jika tidak ada keyword yang cocok.

Lanjutkan dengan menyimpan dan menampilkan jawaban seperti Week 6.

### 53-60 menit: Personalisasi, pengujian, dan demo

Setiap siswa wajib mengubah:

- nama chatbot
- judul dan deskripsi
- isi sidebar
- minimal empat keyword dan jawaban
- pesan fallback

Pengujian berpasangan:

1. Coba semua keyword yang tertulis di sidebar.
2. Coba satu pertanyaan yang tidak dikenali.
3. Kirim tiga pesan dan periksa history.
4. Tekan Clear Chat.
5. Minta teman mencoba tanpa menjelaskan kodenya.

Pengantar Week 8:

- chatbot akan dibuat lebih pintar dengan kombinasi keyword dan pilihan topik pengguna.

## Catatan Tutor

- Utamakan satu tema yang konsisten daripada jumlah jawaban yang terlalu banyak.
- Jawaban sebaiknya pendek agar mudah diperiksa siswa.
- Bantu siswa mencari fakta yang aman dan sederhana; jangan habiskan waktu untuk riset panjang.
- Jika waktu terbatas, gunakan kembali seluruh blok history Week 6 dan fokus pada `responses`, sidebar, serta personalisasi.
