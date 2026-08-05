# Jago Robotika Intensive

Koleksi materi Python untuk kelas intensive Jago Robotika yang dikumpulkan ke satu repository.

## Struktur

- `pygame/`: materi dan proyek berbasis `pygame`, termasuk aset audio, gambar, dan beberapa subfolder pendukung.
- `streamlit/`: materi dan proyek berbasis `streamlit`.
- `iot/`: contoh proyek `ESP32 + Wokwi + backend API + dashboard Streamlit`.
- `docs/`: dokumentasi inventaris dan catatan struktur.

## Catatan Restruktur

- Struktur internal folder `pygame/` dipertahankan agar referensi aset lokal seperti `player.png`, `enemy.png`, `background.jpeg`, `win.mp3`, dan file sejenis tetap kompatibel dengan script yang ada.
- File `coba_streamlit.py` dipindahkan ke area `streamlit/` karena dependensinya memakai `streamlit`.
- Sumber asli di `~/Documents` tidak diubah; repository ini adalah salinan yang sudah dirapikan untuk pengelolaan dengan Git.

## Menjalankan

Contoh `pygame`:

```bash
python3 "pygame/Week 1 - Intro, Screen, Movement.py"
```

Contoh `streamlit`:

```bash
streamlit run "streamlit/Week 1 - Coba Streamlit.py"
```

Contoh `iot` dashboard:

```bash
streamlit run "iot/dashboard/app.py"
```
