# Tutor Flow Week 9 - Improve and Present the Rule-Based Chatbot

Durasi: `60 menit`

File utama:

- `app.py`

Tujuan:

- siswa menguji chatbot secara mandiri dan dengan pertanyaan dari tutor
- siswa mencatat dan memperbaiki pertanyaan yang belum dikenali
- siswa menjelaskan kemampuan dan batasan chatbot secara jujur
- siswa merapikan pesan pembuka, sidebar, dan fallback response
- siswa mendemokan project rule-based sebelum masuk ke AI

## Persiapan Tutor

IDE yang dipakai:

- `Visual Studio Code (VS Code)`

Siswa membuat folder kerja sendiri, misalnya `chatbot-week-9`, lalu membuat satu file bernama `app.py`.

Jalankan dari terminal pada folder tersebut:

```bash
streamlit run app.py
```

Saat mengajar, file yang dibahas tetap `satu file yang sama`, tetapi ditulis dan diuji bertahap.

## Alur 1 Jam

### 0-8 menit: Cek instalasi dan tentukan target perbaikan

Langkah tutor:

1. Pastikan VS Code, Python, dan Streamlit sudah terpasang.
2. Minta siswa membuat folder `chatbot-week-9` dan file `app.py`.
3. Review Week 8: topik, kombinasi keyword, urutan rules, dan history.
4. Jelaskan bahwa Week 9 fokus pada kualitas app, bukan menambah banyak syntax.
5. Tentukan standar siap-demo: petunjuk jelas, jawaban benar, fallback jujur, dan tidak error.

Perintah cek:

```bash
python3 --version
python3 -m pip show streamlit
```

Jika belum terpasang:

```bash
python3 -m pip install streamlit
```

### 8-16 menit: Bagian 1 - Identitas, kemampuan, dan batasan

Tulis bagian awal:

```python
import streamlit as st

BOT_NAME = "Nova"

st.title("Nova Space Bot")
st.caption("Chatbot bertema luar angkasa yang siap diuji dan didemokan.")

topic = st.sidebar.selectbox("Pilih topik", ["Tata Surya", "Penjelajahan"])
st.sidebar.subheader("Kemampuan")
st.sidebar.write("Menjawab pertanyaan sederhana sesuai contoh keyword.")
st.sidebar.warning("Batasan: Nova belum memakai AI dan tidak memahami semua pertanyaan.")
```

Jelaskan:

- judul dan deskripsi harus menjelaskan tema project.
- kemampuan menyebutkan hal yang memang dapat dilakukan chatbot.
- batasan mencegah pengguna menganggap chatbot mengetahui semuanya.
- siswa mengganti nama dan isi sidebar sesuai project masing-masing.

### 16-25 menit: Bagian 2 - Rules yang siap diuji

Gunakan kembali aturan Week 8, lalu periksa:

- aturan spesifik berada sebelum aturan umum
- keyword ditulis dengan huruf kecil
- fakta dan ejaan jawaban sudah benar
- setiap topik memiliki contoh pertanyaan di sidebar
- fallback response singkat dan jujur

Contoh aturan:

```python
rules = [
    (["planet", "terbesar"], "Jupiter adalah planet terbesar di tata surya."),
    (["planet", "merah"], "Mars disebut planet merah karena permukaannya kaya zat besi."),
    (["planet"], "Tata surya kita memiliki delapan planet."),
]
```

### 25-33 menit: Bagian 3 - Siapkan catatan pengujian

Tambahkan sebelum chat diproses:

```python
if "unknown_questions" not in st.session_state:
    st.session_state.unknown_questions = []
```

Pada bagian pencarian jawaban, gunakan variable `found`:

```python
answer = "Maaf, pertanyaan itu belum ada dalam pengetahuanku."
found = False

for keywords, response in rules:
    if all(keyword in clean_message for keyword in keywords):
        answer = response
        found = True
        break

if not found:
    st.session_state.unknown_questions.append(f"[{topic}] {message}")
```

Jelaskan:

- `found` mencatat apakah ada rule yang cocok.
- pertanyaan gagal tidak dibuang, tetapi disimpan sebagai bahan perbaikan.
- catatan ini bukan jawaban AI; hanya daftar hasil pengujian.

### 33-40 menit: Bagian 4 - Tampilkan catatan di sidebar

Letakkan setelah bagian chat:

```python
with st.sidebar.expander(f"Catatan pengujian ({len(st.session_state.unknown_questions)})"):
    if st.session_state.unknown_questions:
        for question in st.session_state.unknown_questions:
            st.write("-", question)
    else:
        st.write("Belum ada pertanyaan yang gagal dijawab.")

    if st.button("Hapus Catatan"):
        st.session_state.unknown_questions = []
        st.rerun()
```

Jelaskan bahwa daftar ini membantu siswa menentukan rule yang perlu ditambah setelah online testing.

### 40-50 menit: Online testing bersama tutor

Siswa menjalankan app di komputer masing-masing. Tidak perlu bertukar link atau mengakses app siswa lain.

Tahap 1 - Self-testing:

1. Dua pertanyaan dari contoh sidebar.
2. Dua pertanyaan dengan susunan kata berbeda.
3. Satu pertanyaan di luar kemampuan chatbot.
4. Pergantian topik.
5. Clear Chat.

Tahap 2 - Tutor testing:

1. Minta siswa menyebutkan tema dan kemampuan chatbot.
2. Tutor menulis dua pertanyaan kejutan melalui meeting chat atau membacakannya saat siswa screen sharing.
3. Siswa memasukkan pertanyaan tersebut ke app miliknya.
4. Jika kelas memiliki beberapa siswa, tutor cukup mengambil satu demo layar secara bergantian; siswa lain tetap menguji app sendiri.

Siswa mencatat:

- jawaban yang salah
- pertanyaan yang masuk ke catatan pengujian
- petunjuk yang membingungkan
- fakta atau ejaan yang perlu diperbaiki

### 50-56 menit: Perbaikan final

Siswa memilih perbaikan paling penting:

- menambah atau mengganti keyword
- memperbaiki urutan rules
- memperjelas contoh pertanyaan
- memperbaiki fallback response
- memperbaiki judul, pesan pembuka, atau batasan

Setelah perubahan, ulangi minimal tiga pertanyaan untuk memastikan tidak ada regresi.

### 56-60 menit: Demo singkat

Format demo satu menit:

1. Sebutkan nama dan tema chatbot.
2. Jelaskan satu kemampuan dan satu batasan.
3. Tunjukkan pertanyaan dengan kombinasi keyword.
4. Tunjukkan pergantian topik atau Clear Chat.
5. Sebutkan satu perbaikan dari hasil online testing.

Pengantar Week 10:

- siswa akan membandingkan chatbot rule-based dengan AI chatbot serta mempelajari prompt, API, dan safety dasar.

## Catatan Tutor

- Hindari menambah terlalu banyak fitur baru; kualitas pengujian dan komunikasi adalah fokus utama.
- Pastikan siswa tidak mengklaim chatbot rule-based sebagai AI.
- Jika siswa memakai tema faktual, bantu memeriksa fakta singkat yang ditampilkan.
- Catatan pertanyaan gagal hanya tersimpan selama session Streamlit masih aktif.
- Jika waktu terbatas, prioritaskan self-testing, satu pertanyaan kejutan dari tutor, satu perbaikan nyata, dan demo singkat.
