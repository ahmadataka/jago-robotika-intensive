# Dari Face Detector Week 9 ke Live Face Tracker

Kode awal: [Face Detector Week 9](../week-9/app.py).
Kode akhir: [video_face_tracker.py](video_face_tracker.py).

Tujuan: memakai blok deteksi wajah Week 9 pada setiap frame webcam. Kotak dan titik pusat mengikuti posisi wajah yang sedang terdeteksi.

Gunakan satu file `app.py` pada laptop siswa. OpenCV membuka kamera komputer yang menjalankan Python; versi ini digunakan secara lokal.

## 1. Jalankan kode awal

Pastikan Face Detector Week 9 dapat dijalankan:

```bash
streamlit run app.py
```

Dependency tetap sama:

```bash
python -m pip install streamlit pillow numpy "opencv-python-headless<5"
```

Di Mac, gunakan `python3` bila diperlukan.

Cek: foto kamera/upload dapat diproses menjadi kotak wajah.

## 2. Ganti import dan judul

Ganti blok import dengan:

```python
import time

import cv2
import streamlit as st
```

OpenCV sudah memberikan frame dalam bentuk array, sehingga kita tidak lagi memakai Pillow atau konversi NumPy.

Ganti judul:

```python
st.title("Live Face Tracker")
st.write("Kotak dan titik pusat mengikuti wajah saat kamera berjalan.")
```

## 3. Ganti input foto dengan checkbox

Hapus radio `input_mode` dan seluruh blok kamera/upload berikut:

```python
if input_mode == "Kamera":
    input_file = st.camera_input("Ambil satu frame")
else:
    input_file = st.file_uploader("Upload gambar", type=["png", "jpg", "jpeg"])
```

Pertahankan slider ukuran wajah. Susun kontrol baru tepat di bawah judul:

```python
minimum_size = st.sidebar.slider("Ukuran wajah minimum", 30, 150, 50, 10)
st.sidebar.info("Jalankan di laptop sendiri. OpenCV membuka kamera pada komputer yang menjalankan Python.")
run_camera = st.checkbox("Jalankan kamera")
```

`st.camera_input()` mengambil satu foto; checkbox baru mengontrol pembacaan frame webcam berulang.

Cek: checkbox terlihat. Pada tahap ini jangan mengaktifkannya sebelum pipeline foto lama diganti pada langkah berikut.

## 4. Pindahkan model keluar dari blok input

Dari kode Week 9, pindahkan dua baris model ke bawah checkbox, tanpa indentasi:

```python
model_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_detector = cv2.CascadeClassifier(model_path)
preview = st.empty()
status = st.empty()
```

Model cukup dimuat sekali sebelum loop. `st.empty()` menyediakan tempat yang dapat diperbarui tanpa menambahkan gambar baru terus-menerus ke halaman.

Hapus seluruh blok lama mulai dari `if input_file:` hingga akhir file. Blok deteksi dan kotaknya akan dimasukkan kembali dalam loop pada langkah 6-8. Gunakan kode Week 9 sebagai referensi saat menyalinnya.

## 5. Buka webcam dan baca frame

Di bawah `status = st.empty()`, tambahkan kerangka:

```python
if run_camera:
    camera = cv2.VideoCapture(0)
    try:
        if not camera.isOpened():
            st.error("Kamera tidak dapat dibuka. Periksa izin kamera dan tutup aplikasi kamera lain.")
        else:
            while run_camera:
                success, frame = camera.read()
                if not success:
                    st.warning("Frame kamera tidak terbaca. Matikan checkbox lalu coba lagi.")
                    break

                # Tambahkan pemrosesan frame di sini pada langkah 6-8.
                time.sleep(0.05)
    finally:
        camera.release()
else:
    st.info("Centang Jalankan kamera untuk mulai. Hilangkan centang untuk berhenti.")
```

Penjelasan:

- `0` memilih kamera default laptop.
- `read()` memberikan status keberhasilan dan satu frame.
- `break` menghentikan loop jika kamera gagal memberikan frame.
- `finally` memastikan webcam dilepas saat proses berakhir atau app rerun.
- `sleep` memberi jeda pendek antar-frame.

Cek: belum ada preview pada langkah ini. Hilangkan centang untuk berhenti, atau gunakan `Ctrl+C` pada terminal bila diperlukan.

## 6. Masukkan kembali grayscale dan deteksi Week 9

Ganti komentar di dalam loop dengan blok berikut. Letakkan setelah pengecekan `success`, sebelum `time.sleep(0.05)`:

```python
image_array = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
grayscale = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
faces = face_detector.detectMultiScale(
    grayscale,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(minimum_size, minimum_size),
)
```

Bandingkan dengan Week 9: hanya sumber gambar yang berubah. OpenCV memberikan BGR; kita mengubahnya menjadi RGB sebelum memakai pipeline yang sama.

## 7. Masukkan kembali kotak wajah dan tambahkan titik pusat

Masih di dalam loop, setelah `detectMultiScale(...)`, tambahkan:

```python
result = image_array.copy()
for x, y, width, height in faces:
    cv2.rectangle(result, (x, y), (x + width, y + height), (255, 80, 40), 5)
    center_x = x + width // 2
    center_y = y + height // 2
    cv2.circle(result, (center_x, center_y), 5, (0, 200, 80), -1)
```

Kotak persis seperti Week 9. Tiga baris baru menghitung dan menggambar pusat wajah. Untuk setiap frame, posisi dihitung kembali.

## 8. Perbarui preview

Setelah loop `for` berakhir tetapi masih di dalam `while`, tambahkan:

```python
preview.image(result, caption="Live face detection", width="stretch")
status.write(f"Jumlah wajah: {len(faces)}")
```

Kedua baris tersebut sejajar dengan `result = image_array.copy()`, bukan berada di dalam loop `for`. Dengan begitu, preview tetap diperbarui ketika tidak ada wajah.

Pertahankan `time.sleep(0.05)` sebagai baris terakhir di dalam `while`.

Cek: tampil satu preview bergerak yang terus diperbarui, bukan banyak gambar tersusun ke bawah.

## 9. Uji mulai, bergerak, dan berhenti

1. Centang **Jalankan kamera**.
2. Hadapkan wajah ke kamera dan periksa kotak serta titik pusat.
3. Bergerak perlahan ke kiri dan kanan.
4. Keluar frame: kotak harus hilang dan jumlah wajah menjadi 0.
5. Kembali ke frame: wajah dideteksi ulang.
6. Hilangkan centang: preview berhenti dan kamera dilepas.
7. Centang lagi: kamera dapat dibuka kembali.

Ini adalah deteksi wajah berulang pada video. App belum mempertahankan identitas orang antar-frame atau menggambar jejak; gerakan kotak berasal dari posisi deteksi terbaru.

## Jika Kamera Error

- Tutup Zoom/Meet atau aplikasi lain yang memakai webcam jika perangkat tidak mendukung berbagi kamera. Gunakan perangkat lain untuk mengikuti meeting bila perlu.
- Beri izin kamera kepada Python, terminal, atau VS Code di pengaturan privasi sistem.
- Coba `cv2.VideoCapture(1)` jika kamera yang diinginkan bukan kamera default.
- Jalankan di laptop sendiri. Deployment cloud memerlukan streaming webcam browser tambahan agar dapat menerima kamera siswa.
- Hentikan server dengan `Ctrl+C` jika perlu melepaskan kamera sepenuhnya.

Cocokkan kode dengan file akhir setelah langkah 8. Saat demo online, siswa dapat screen sharing hasil app tanpa perlu membagikan akses aplikasinya.
