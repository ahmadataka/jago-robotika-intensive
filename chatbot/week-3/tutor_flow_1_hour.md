# Tutor Flow Week 3 - Rule-Based Chatbot with If-Else

Durasi: `60 menit`

File utama:

- `app.py`

Tujuan:

- siswa memahami bahwa chatbot dapat memilih jawaban berdasarkan keyword
- siswa memakai `.lower()`, `.strip()`, dan `if-elif-else`
- siswa membuat chatbot yang menjawab beberapa topik dan memiliki respons cadangan

## Persiapan Tutor

IDE yang dipakai:

- `Visual Studio Code (VS Code)`

Siswa membuat folder kerja sendiri, misalnya `chatbot-week-3`, lalu membuat satu file bernama `app.py`.

Jalankan dari terminal pada folder tersebut:

```bash
streamlit run app.py
```

Saat mengajar, file yang dibahas tetap `satu file yang sama`, tetapi ditulis bertahap.

## Alur 1 Jam

### 0-10 menit: Cek instalasi dan review Week 2

Langkah tutor:

1. Pastikan VS Code, Python, dan Streamlit sudah terpasang.
2. Minta siswa membuat folder `chatbot-week-3` dan file `app.py`.
3. Review Week 2: chatbot menerima pesan lalu selalu memberi respons yang sama.
4. Tanyakan: bagaimana agar bot menjawab berbeda saat membaca kata `robot` atau `python`?

Perintah cek:

```bash
python3 --version
python3 -m pip show streamlit
```

Jika belum terpasang:

```bash
python3 -m pip install streamlit
```

### 10-20 menit: Bagian 1 - Kerangka chatbot

Tulis sampai input pesan:

```python
import streamlit as st

st.title("Rule-Based Chatbot")
st.write("Chatbot ini mulai menjawab berdasarkan kata yang kamu tulis.")

bot_name = st.sidebar.selectbox("Pilih nama chatbot", ["Robo", "Milo", "Luna"])
message = st.text_input("Kamu:")
```

Jelaskan:

- struktur app masih mirip Week 2.
- yang berubah adalah cara bot memilih jawaban.
- `message` menyimpan semua teks yang ditulis pengguna.

### 20-30 menit: Bagian 2 - Merapikan pesan

Tambahkan di dalam blok tombol:

```python
if st.button("Kirim Pesan"):
    if message:
        clean_message = message.lower().strip()
```

Jelaskan:

- `.lower()` membuat semua huruf menjadi kecil, jadi `HALO`, `Halo`, dan `halo` diperlakukan sama.
- `.strip()` menghapus spasi berlebih di awal dan akhir pesan.
- `clean_message` adalah versi pesan yang siap diperiksa chatbot.

Latihan cepat:

- minta siswa mencoba menulis `HALO`, ` halo `, dan `Halo`.

### 30-45 menit: Bagian 3 - Keyword dan if-elif-else

Tambahkan logika berikut:

```python
if "halo" in clean_message:
    answer = "Halo juga! Senang bisa ngobrol denganmu."
elif "nama" in clean_message:
    answer = f"Namaku {bot_name}. Aku chatbot buatanmu!"
elif "robot" in clean_message:
    answer = "Robot adalah mesin yang dapat diprogram untuk melakukan tugas."
elif "python" in clean_message:
    answer = "Python adalah bahasa pemrograman yang kita pakai."
else:
    answer = "Maaf, aku belum memahami pesan itu."
```

Jelaskan:

- `in` mengecek apakah sebuah kata ada di dalam pesan.
- `if` memeriksa kondisi pertama; `elif` memeriksa kondisi berikutnya.
- `else` adalah respons cadangan ketika keyword tidak ditemukan.
- bot ini belum AI; ia hanya mengikuti aturan yang kita tulis.

### 45-55 menit: Bagian 4 - Menampilkan percakapan

Tambahkan:

```python
st.write(f"**Kamu:** {message}")
st.success(f"**{bot_name}:** {answer}")
```

Target hasil:

- pesan pengguna tampil di app.
- chatbot memberi jawaban yang berbeda untuk setiap keyword.
- pesan yang belum dikenali memunculkan fallback response.

Pengujian wajib:

- `Halo`
- `Siapa namamu?`
- `Aku suka robot`
- `Apa itu Python?`
- satu pertanyaan lain yang belum ada di daftar keyword

### 55-60 menit: Variasi dan penutup

Latihan:

- tambahkan keyword `game`, `sekolah`, atau `kucing`.
- ubah jawaban untuk keyword `robot` agar sesuai gaya masing-masing siswa.
- ubah fallback response agar lebih ramah.

Pengantar Week 4:

- chatbot bisa punya lebih dari satu respons untuk keyword yang sama agar percakapannya tidak monoton.

## Catatan Tutor

- Siswa tidak perlu menghafal `if-elif-else`; fokus pada hubungan "jika ada kata ini, beri jawaban itu".
- Minta siswa menguji semua keyword setelah menulis kode.
- Jika siswa selesai lebih cepat, minta mereka menambah dua keyword sendiri.
