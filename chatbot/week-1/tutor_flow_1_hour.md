# Tutor Flow Week 1 - Chatbot

Durasi: `60 menit`

File utama:

- `chatbot/week-1/app.py`

Tujuan:

- siswa review dasar `Streamlit`
- siswa paham alur `input -> proses -> output`
- siswa selesai membuat mini app bertema chatbot

## Persiapan Tutor

IDE yang dipakai:

- `Visual Studio Code (VS Code)`

Jalankan:

```bash
streamlit run chatbot/week-1/app.py
```

Saat mengajar, file yang dibahas tetap `satu file yang sama`, tetapi dibuat bertahap.

## Alur 1 Jam

### 0-10 menit: Cek instalasi dan buka project

Langkah tutor:

1. Buka folder project di `VS Code`
2. Cek apakah `Python` dan `Streamlit` sudah terpasang
3. Jika belum, install dulu
4. Jalankan app pertama kali

Perintah cek:

```bash
python3 --version
python3 -m pip show streamlit
```

Jika belum terpasang:

```bash
python3 -m pip install streamlit
```

### 10-20 menit: Bagian 1 - Kerangka app

Fokus baris awal:

- `import streamlit as st`
- `st.title(...)`
- `st.write(...)`

Tujuan penjelasan:

- apa itu Streamlit
- kenapa butuh import
- bagaimana memberi judul dan deskripsi di app

Target hasil sementara:

- siswa melihat app dengan judul dan deskripsi sederhana

### 20-30 menit: Bagian 2 - Sidebar dan pilihan topik

Lanjutkan ke bagian:

- `st.sidebar.title(...)`
- `st.sidebar.selectbox(...)`
- `st.sidebar.write(...)`

Tujuan penjelasan:

- fungsi sidebar
- bagaimana membuat pilihan untuk user

Target hasil sementara:

- app punya sidebar dengan pilihan topik

### 30-40 menit: Bagian 3 - Input nama dan mood

Lanjutkan ke bagian:

- `st.text_input(...)`
- `st.radio(...)`
- `st.button(...)`

Tujuan penjelasan:

- input teks untuk nama
- memilih salah satu opsi dengan `radio`
- button sebagai pemicu aksi

Target hasil sementara:

- siswa bisa mengisi nama, memilih mood, dan menekan tombol

### 40-55 menit: Bagian 4 - Output dan logika

Lanjutkan ke bagian:

- `if st.button(...)`
- `if name:`
- `st.success(...)`
- `st.write(...)`
- `else:`

Tujuan penjelasan:

- konsep kondisi `if`
- perbedaan saat tombol ditekan atau belum
- perbedaan saat nama diisi atau kosong

Target hasil sementara:

- app bisa memberi respon berbeda sesuai input user

### 55-60 menit: Variasi kecil dan penutup

Latihan:

- ganti pilihan topik
- ganti teks sapaan
- ubah judul app

Tujuan:

- siswa berani memodifikasi code sederhana
- siswa memahami bahwa app sederhana bisa dikembangkan jadi chatbot

## Catatan Tutor

- Tidak perlu menulis semua file dari nol di awal.
- Tulis bertahap di file yang sama sesuai urutan bagian di atas.
- Jika siswa masih awal sekali, tutor bisa mengetik bersama per 2-3 baris.
- Jika waktu mepet, fokus utama cukup sampai app bisa menerima nama dan memberi sapaan.
