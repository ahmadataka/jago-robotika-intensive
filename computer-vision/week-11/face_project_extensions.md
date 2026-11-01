# Week 11 - Pengembangan Face Detector Week 9

Kedua file sengaja mengikuti struktur `../week-9/app.py`. Mulai dengan kode Week 9 milik siswa, lalu ubah bagian yang dijelaskan di bawah.

Panduan modifikasi lengkap per project:

- [Smile / Expression Detector: langkah demi langkah](expression_detector_step_by_step.md)
- [Live Face Tracker: langkah demi langkah](video_face_tracker_step_by_step.md)

## Install dan Run

Dependency sama dengan Week 9:

```bash
python3 -m pip install streamlit pillow numpy "opencv-python-headless<5"
```

Jalankan project pilihan pada terminal di folder file Python:

```bash
streamlit run expression_detector.py
```

atau:

```bash
streamlit run video_face_tracker.py
```

Siswa dapat memakai nama `app.py` untuk file miliknya dan menjalankan `streamlit run app.py`. Di Windows, jika perintah Streamlit tidak dikenali gunakan `python -m streamlit run app.py`; di Mac gunakan `python3 -m streamlit run app.py`.

## Siswa 1 - Smile / Expression Detector

File: `expression_detector.py`.

Pertahankan import, camera/upload, slider ukuran wajah, grayscale, model wajah, dan dua kolom hasil Week 9. Tidak perlu membuat fungsi baru.

Perubahan bertahap:

1. Tambahkan slider `smile_neighbors` di sidebar.
2. Setelah memuat face detector, muat `haarcascade_smile.xml` dengan `cv2.CascadeClassifier`.
3. Sebelum loop wajah, buat `smile_count = 0`.
4. Di dalam loop `for x, y, width, height in faces:`, potong bagian bawah wajah:

```python
mouth_y = y + height // 2
mouth = grayscale[mouth_y:y + height, x:x + width]
```

5. Jalankan smile detector pada crop tersebut, lalu buat label berdasarkan `len(smiles)`.
6. Pertahankan kotak wajah Week 9, tambahkan `cv2.putText` untuk label.
7. Tampilkan jumlah senyum dengan `st.metric`.

Saran: mulai dengan smile detection sebelum mencoba model ekspresi lain. Label menunjukkan pola senyum, bukan perasaan seseorang. Tidak terdeteksi senyum tidak berarti orang tersebut sedih atau marah.

### Tutor flow 60 menit

1. 0-10: cek instalasi dan jalankan kode Week 9.
2. 10-20: tambahkan model senyum dan kenalkan crop area mulut.
3. 20-35: tambahkan deteksi senyum di dalam loop wajah yang sudah ada.
4. 35-45: tambahkan label dan jumlah senyum.
5. 45-55: uji senyum, tanpa senyum, mulut terbuka, sudut wajah, dan cahaya.
6. 55-60: screen sharing demo dan jelaskan satu hasil yang salah.

Slider lebih tinggi membuat deteksi senyum lebih ketat. Gunakan wajah frontal, ukuran cukup besar, dan foto dengan izin pemiliknya.

## Siswa 2 - Live Face Tracker

File: `video_face_tracker.py`. Nama file dipertahankan, sumbernya kini live webcam laptop.

`st.camera_input()` mengambil satu foto. Untuk membaca video langsung pada app lokal, ganti sumber tersebut dengan `cv2.VideoCapture(0)`, lalu baca frame berulang menggunakan `camera.read()`.

OpenCV mengakses kamera komputer yang menjalankan Python. Versi ini untuk laptop siswa yang menjalankan Streamlit secara lokal. Jika di-deploy ke cloud, OpenCV tidak dapat mengakses webcam browser siswa; streaming browser memerlukan pendekatan tambahan seperti WebRTC.

Perubahan bertahap dari Week 9:

1. Pertahankan import OpenCV, sidebar ukuran wajah, model wajah, dan `detectMultiScale`.
2. Hapus input upload/foto, `Image.open`, dan konversi NumPy karena OpenCV sudah memberikan array frame.
3. Tambahkan checkbox `run_camera`, serta `preview = st.empty()` dan `status = st.empty()`.
4. Jika checkbox aktif, buka `camera = cv2.VideoCapture(0)`.
5. Di dalam loop `while run_camera:`, baca `success, frame = camera.read()`. Jika pembacaan gagal, tampilkan pesan lalu `break`.
6. Ubah BGR dari OpenCV ke RGB untuk tampilan, lalu gunakan blok grayscale dan deteksi wajah Week 9.
7. Pertahankan loop kotak wajah; tambahkan titik pusat:

```python
center_x = x + width // 2
center_y = y + height // 2
cv2.circle(result, (center_x, center_y), 5, (0, 200, 80), -1)
```

8. Tampilkan hasil dengan `preview.image` agar frame baru menggantikan frame sebelumnya.
9. Letakkan `camera.release()` di `finally` agar kamera dilepas saat loop berakhir atau app rerun.

Tracking pada versi dasar berarti kotak dan pusat mengikuti hasil deteksi pada setiap frame. App belum menyimpan identitas, jejak, atau asosiasi orang antar-frame. Wajah yang hilang tidak diberi kotak; wajah yang kembali akan dideteksi ulang.

### Tutor flow 60 menit

1. 0-10: jalankan Week 9 dan jelaskan foto versus video.
2. 10-20: tambahkan checkbox, `VideoCapture(0)`, dan placeholder hasil.
3. 20-35: pindahkan pipeline deteksi Week 9 ke dalam loop pembacaan frame.
4. 35-45: tambahkan titik pusat dan jumlah wajah.
5. 45-55: uji mulai/berhenti, gerakan perlahan, keluar frame, dan kembali.
6. 55-60: demo serta jelaskan bahwa video terdiri dari banyak frame.

## Penggunaan Kamera

- Centang **Jalankan kamera** untuk mulai, hilangkan centang untuk berhenti. Perubahan checkbox membuat Streamlit menjalankan ulang app.
- Jika perlu, hentikan server melalui terminal dengan `Ctrl+C`.
- Beri izin akses kamera kepada Python atau terminal/VS Code di pengaturan privasi sistem.
- Tutup aplikasi lain yang memakai webcam; coba index `1` sebagai pengganti `0` bila perangkat memakai kamera lain.
- Jika kamera tidak tersedia, gunakan project ekspresi dengan Upload; project live memerlukan webcam.
- Gerakan cepat, wajah menyamping, dan cahaya redup dapat membuat kotak hilang.

Tutor memberi skenario uji melalui meeting chat atau screen sharing. Siswa menguji app masing-masing.

Referensi: [OpenCV Cascade Classifier](https://docs.opencv.org/4.11.0/db/d28/tutorial_cascade_classifier.html).
