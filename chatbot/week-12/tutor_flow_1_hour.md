# Tutor Flow Week 12 - Final Project: Gemini Chatbot

Durasi: 60 menit. Mulai dari [kode Week 11](../week-11/app.py); [app.py](app.py) adalah hasil akhir. Ikuti [panduan instalasi](dependency_installation.md) sebelum kelas.

Target: siswa mendemokan chatbot bertema yang bisa menjawab pertanyaan lanjutan menggunakan riwayat chat.

## 0-8 menit: Cek Week 11 dan pilih tema

1. Jalankan app Week 11 dan kirim satu pertanyaan.
2. Tanya apa yang terjadi jika pesan berikutnya hanya berbunyi "beri contoh lain".
3. Pilih satu tema: Tutor Python, Asisten Robotika, Pembuat Cerita, atau tema sendiri.

## 8-20 menit: Ganti form dengan chat UI

Ganti judul dan pindahkan konfirmasi data pribadi ke sidebar. Tambahkan `st.session_state.messages = []` dengan pengecekan seperti Week 6. Ganti `text_area` dan tombol `Tanya Gemini` dengan:

```python
question = st.chat_input(
    "Ketik pertanyaan...", disabled=not safe_to_send, max_chars=1000
)
```

Tampilkan riwayat sebelum input:

```python
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["text"])
```

Cek: input baru tampil di bagian bawah dan hanya aktif setelah konfirmasi. Sambungkan kembali blok request pada langkah berikutnya.

## 20-35 menit: Kirim riwayat ke Gemini

Tambahkan `types` pada import Gemini. Di dalam `if question and question.strip():`, tampilkan pesan siswa dan bangun `contents`:

```python
contents = []
for message in st.session_state.messages[-10:]:
    role = "model" if message["role"] == "assistant" else "user"
    contents.append(
        types.Content(role=role, parts=[types.Part.from_text(text=message["text"])])
    )
contents.append(
    types.Content(role="user", parts=[types.Part.from_text(text=question)])
)
```

Ganti `contents=prompt` Week 11 menjadi `contents=contents`. Pertahankan spinner dan penanganan error. Tampilkan jawaban di bubble `assistant`, lalu simpan pasangan pesan hanya jika Gemini memberikan teks:

```python
st.session_state.messages.append({"role": "user", "text": question})
st.session_state.messages.append({"role": "assistant", "text": answer})
```

Jelaskan: history di layar disimpan selama sesi; Gemini mendapat maksimal 10 pesan sebelumnya ditambah pesan terbaru. Format `assistant` dipakai UI dan `model` dipakai API. [Referensi Gemini](https://ai.google.dev/api/generate-content).

Cek: kirim "Contoh kita adalah sensor ultrasonik", lalu "Apa fungsi sensor tadi?" Gemini seharusnya merujuk sensor sebelumnya.

## 35-45 menit: Personalisasi tema dan reset

Buat dictionary `THEMES` berisi judul tema dan instruksi. Pindahkan instruksi dari f-string Week 11 ke `config` pada request:

```python
config=types.GenerateContentConfig(
    system_instruction=THEMES[theme] + " Jawab singkat dalam bahasa Indonesia.",
),
```

Gunakan `clear_chat()` untuk mengosongkan riwayat saat tema berubah atau tombol Hapus chat ditekan. Lihat kode akhir untuk penempatan callback dan pilihan model.

Cek: coba pertanyaan yang sama pada dua tema. Pastikan percakapan lama hilang saat tema berganti.

## 45-53 menit: Final testing

1. Coba satu pertanyaan awal dan satu pertanyaan lanjutan.
2. Matikan konfirmasi dan pastikan input tidak aktif.
3. Uji Hapus chat, lalu mulai ulang percakapan.
4. Periksa satu fakta dari jawaban dengan sumber lain.

## 53-60 menit: Showcase

Setiap siswa mendemokan selama 1-2 menit: nama dan tema chatbot, dua pesan yang saling berkaitan, serta satu keterbatasan. Jika peserta banyak, gunakan beberapa demo layar dan minta siswa lain menuliskan hasilnya di chat kelas.

Prioritas bila waktu mepet: satu tema, dua pesan yang nyambung, dan demo. Pilihan tema tambahan dapat diselesaikan setelah kelas.
