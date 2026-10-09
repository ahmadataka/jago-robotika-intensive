# Tutor Flow Week 8 - Smarter Rule-Based Chatbot

Durasi: `60 menit`

File utama:

- `app.py`

Tujuan:

- siswa membuat chatbot dengan beberapa pilihan topik
- siswa memakai kombinasi keyword untuk jawaban yang lebih tepat
- siswa memahami pentingnya urutan aturan
- siswa mempertahankan chat history dan clear chat
- siswa menguji chatbot dengan berbagai bentuk pertanyaan

## Persiapan Tutor

IDE yang dipakai:

- `Visual Studio Code (VS Code)`

Siswa membuat folder kerja sendiri, misalnya `chatbot-week-8`, lalu membuat satu file bernama `app.py`.

Jalankan dari terminal pada folder tersebut:

```bash
streamlit run app.py
```

Saat mengajar, file yang dibahas tetap `satu file yang sama`, tetapi ditulis bertahap.

## Alur 1 Jam

### 0-8 menit: Cek instalasi dan review Week 7

Langkah tutor:

1. Pastikan VS Code, Python, dan Streamlit sudah terpasang.
2. Minta siswa membuat folder `chatbot-week-8` dan file `app.py`.
3. Review Week 7: satu keyword menghasilkan satu jawaban bertema.
4. Tunjukkan masalah aturan terlalu umum: pertanyaan "planet terbesar" hanya dijawab sebagai "planet".
5. Jelaskan solusi Week 8: topik dan kombinasi beberapa keyword.

Perintah cek:

```bash
python3 --version
python3 -m pip show streamlit
```

Jika belum terpasang:

```bash
python3 -m pip install streamlit
```

### 8-15 menit: Bagian 1 - Kerangka app dan pilihan topik

Tulis bagian awal:

```python
import streamlit as st

BOT_NAME = "Nova"

st.title("Smart Space Bot")
st.caption("Chatbot bertopik dengan kombinasi beberapa keyword.")

topic = st.sidebar.selectbox("Pilih topik", ["Tata Surya", "Penjelajahan"])
st.sidebar.write("Coba pertanyaan berikut:")
```

Jelaskan:

- pengguna menentukan konteks percakapan melalui sidebar.
- topik membantu chatbot memilih kelompok aturan yang sesuai.
- nama topik dapat diganti mengikuti mini project Week 7.

### 15-27 menit: Bagian 2 - Aturan untuk setiap topik

Tambahkan aturan topik pertama:

```python
if topic == "Tata Surya":
    st.sidebar.write("- Apa planet terbesar?")
    st.sidebar.write("- Apa planet merah?")
    rules = [
        (["planet", "terbesar"], "Jupiter adalah planet terbesar di tata surya."),
        (["planet", "merah"], "Mars disebut planet merah karena permukaannya kaya zat besi."),
        (["planet"], "Tata surya kita memiliki delapan planet."),
        (["matahari"], "Matahari adalah bintang di pusat tata surya."),
    ]
```

Lanjutkan dengan `else` untuk topik Penjelajahan mengikuti kode lengkap.

Jelaskan:

- setiap aturan mempunyai list keyword dan satu respons.
- aturan spesifik diletakkan sebelum aturan umum.
- pertanyaan "planet terbesar" cocok dengan dua keyword.
- pertanyaan yang hanya berisi "planet" memakai jawaban umum.

### 27-35 menit: Bagian 3 - Reset chat saat topik berubah

Tambahkan:

```python
if "topic" not in st.session_state or st.session_state.topic != topic:
    st.session_state.topic = topic
    st.session_state.messages = [
        {"role": "assistant", "content": f"Halo! Aku {BOT_NAME}. Mari bahas {topic.lower()}!"}
    ]
```

Jelaskan:

- app mengingat topik yang sedang aktif.
- saat pengguna mengganti topik, percakapan lama dibersihkan.
- hal ini mencegah percakapan dua topik tercampur.

### 35-42 menit: Bagian 4 - Clear chat dan history

Gunakan kembali pola Week 6 dan Week 7:

```python
if st.sidebar.button("Clear Chat"):
    st.session_state.messages = [
        {"role": "assistant", "content": f"Chat dibersihkan. Tanyakan tentang {topic.lower()}, ya!"}
    ]
    st.rerun()

for item in st.session_state.messages:
    with st.chat_message(item["role"]):
        st.write(item["content"])
```

Tekankan bahwa fitur lama tetap dipakai dan ditingkatkan, bukan dibuang.

### 42-52 menit: Bagian 5 - Cocokkan semua keyword

Setelah mengambil dan menyimpan pesan pengguna, tambahkan:

```python
clean_message = message.lower().strip()
answer = f"Aku belum memahami pertanyaan itu. Coba lihat contoh topik {topic.lower()} di sidebar."

for keywords, response in rules:
    if all(keyword in clean_message for keyword in keywords):
        answer = response
        break
```

Jelaskan:

- loop memeriksa aturan dari atas ke bawah.
- `all(...)` berarti semua keyword pada aturan harus ditemukan.
- `break` menghentikan pencarian setelah aturan pertama cocok.
- karena itu, urutan aturan spesifik dan umum sangat penting.

Simpan dan tampilkan jawaban seperti Week 7.

### 52-60 menit: Pengujian dan perbaikan aturan

Pengujian wajib:

1. Tanyakan "Apa planet terbesar?" dan periksa jawaban Jupiter.
2. Tanyakan "Ceritakan planet" dan periksa jawaban umum.
3. Ganti susunan aturan umum ke paling atas dan amati jawaban yang salah, lalu kembalikan.
4. Ganti topik ke Penjelajahan dan pastikan history direset.
5. Coba pertanyaan yang tidak dikenal dan periksa fallback.
6. Tekan Clear Chat.

Latihan tambahan:

- tambahkan satu aturan dengan dua keyword.
- tambahkan satu pertanyaan contoh di sidebar.
- ganti topik dan isi aturan mengikuti project siswa sendiri.

Pengantar Week 9:

- siswa akan meminta teman menguji chatbot, memperbaiki jawaban, dan menyiapkan demo project.

## Catatan Tutor

- Fokuskan penjelasan `all(...)` pada arti "semua kata harus ada", bukan syntax generator secara mendalam.
- Urutan aturan adalah konsep utama Week 8; demonstrasikan satu contoh aturan yang sengaja salah urut.
- Jangan menambah terlalu banyak topik. Dua topik dengan beberapa aturan sudah cukup untuk satu jam.
- Jika waktu terbatas, gunakan blok history dari Week 7 dan fokus pada `rules`, pemilihan topik, dan kombinasi keyword.
