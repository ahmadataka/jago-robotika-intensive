# Tutor Flow Week 9 - Face Detection

Durasi: `60 menit`

File utama:

- `app.py`

Tujuan:

- siswa memahami perbedaan face detection dan face recognition
- siswa memakai model Haar Cascade yang sudah dilatih
- siswa mengubah gambar ke grayscale untuk deteksi
- siswa menggambar bounding box pada wajah
- siswa menguji keterbatasan model pada jarak, sudut, dan pencahayaan

## Persiapan Tutor

IDE yang dipakai:

- `Visual Studio Code (VS Code)`

Siswa membuat folder kerja sendiri, misalnya `computer-vision-week-9`, lalu membuat satu file bernama `app.py`.

Jalankan dari terminal pada folder tersebut:

```bash
streamlit run app.py
```

Siapkan webcam atau gambar yang memperlihatkan satu atau beberapa wajah dari arah depan. Minta izin sebelum menggunakan foto orang lain.

## Alur 1 Jam

### 0-10 menit: Cek instalasi dan kenalkan face detection

Langkah tutor:

1. Pastikan VS Code, Python, Streamlit, Pillow, NumPy, dan OpenCV sudah terpasang.
2. Minta siswa membuat folder `computer-vision-week-9` dan file `app.py`.
3. Review Week 8: kondisi pixel dapat dipakai untuk membuat mask.
4. Jelaskan bahwa Week 9 memakai model siap pakai untuk mencari pola wajah.
5. Bedakan face detection dan face recognition.

Perbedaan penting:

- face detection menjawab "di mana ada wajah?"
- face recognition mencoba menjawab "wajah siapa?"
- app Week 9 hanya melakukan face detection dan tidak menyimpan identitas

Perintah cek:

```bash
python3 --version
python3 -m pip show streamlit pillow numpy opencv-python-headless
```

Jika belum terpasang:

```bash
python3 -m pip install streamlit pillow numpy "opencv-python-headless<5"
```

### 10-18 menit: Bagian 1 - Tampilan dan input

Tulis bagian awal:

```python
import cv2
import numpy as np
from PIL import Image
import streamlit as st

st.title("Face Detector")
st.write("Gunakan model siap pakai untuk menemukan wajah pada gambar.")

input_mode = st.sidebar.radio("Sumber gambar", ["Kamera", "Upload"])
minimum_size = st.sidebar.slider("Ukuran wajah minimum", 30, 150, 50, 10)
st.sidebar.info("Face detection menemukan posisi wajah, bukan mengenali identitas orang.")
```

Tambahkan `st.camera_input` dan `st.file_uploader` mengikuti kode lengkap.

Jelaskan:

- kamera mengambil satu frame, bukan video real-time.
- upload menjadi fallback jika webcam tidak tersedia.
- ukuran minimum membantu mengabaikan pola yang terlalu kecil.

### 18-27 menit: Bagian 2 - Baca gambar dan buat grayscale

Di dalam `if input_file:`, tambahkan:

```python
image = Image.open(input_file).convert("RGB")
image_array = np.array(image)
grayscale = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
```

Jelaskan:

- Pillow membaca file dari Streamlit.
- NumPy mengubah gambar menjadi array pixel.
- OpenCV menerima array untuk diproses.
- grayscale membuat proses pencarian pola lebih sederhana dan cepat.

### 27-38 menit: Bagian 3 - Muat dan jalankan model siap pakai

Tambahkan:

```python
model_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_detector = cv2.CascadeClassifier(model_path)
faces = face_detector.detectMultiScale(
    grayscale,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(minimum_size, minimum_size),
)
```

Jelaskan:

- file XML berisi pola yang sudah dipelajari sebelumnya.
- siswa memakai model tersebut, bukan melatihnya dari awal.
- `detectMultiScale` mencari wajah dalam beberapa ukuran.
- `minNeighbors` membantu mengurangi deteksi yang salah.
- hasil `faces` berisi posisi dan ukuran setiap kotak wajah.

Tidak perlu membahas matematika Haar Cascade secara mendalam.

### 38-47 menit: Bagian 4 - Gambar bounding box

Tambahkan:

```python
result = image_array.copy()

for x, y, width, height in faces:
    cv2.rectangle(result, (x, y), (x + width, y + height), (255, 80, 40), 5)
```

Jelaskan:

- `x` dan `y` adalah titik kiri atas wajah.
- `width` dan `height` menentukan ukuran kotak.
- loop menggambar satu kotak untuk setiap wajah yang ditemukan.
- gambar asli disalin agar tidak ikut berubah.

Tampilkan gambar asli dan hasil deteksi dalam dua kolom mengikuti kode lengkap.

### 47-53 menit: Bagian 5 - Hitung dan beri status

Tambahkan:

```python
st.metric("Jumlah wajah", len(faces))

if len(faces) > 0:
    st.success("Wajah terdeteksi. Coba ubah jarak atau sudut kamera.")
else:
    st.warning("Wajah belum terdeteksi. Coba posisi lebih dekat dan cahaya lebih terang.")
```

Jelaskan bahwa jumlah kotak pada `faces` sama dengan jumlah wajah yang ditemukan model.

### 53-60 menit: Eksperimen dan penutup

Pengujian wajib:

1. Coba satu wajah dari arah depan.
2. Ubah jarak wajah terhadap kamera.
3. Ubah slider ukuran minimum.
4. Coba cahaya terang dan redup.
5. Coba wajah dari samping dan bandingkan hasilnya.
6. Jika memungkinkan, coba dua wajah dengan izin semua peserta.

Pertanyaan refleksi:

- kapan model gagal menemukan wajah?
- apakah kotak selalu tepat?
- mengapa deteksi dari samping lebih sulit?
- apakah aplikasi mengetahui nama orang? Jawabannya: tidak.

Pengantar Week 10:

- siswa akan memilih project vision interaktif seperti filter, color object finder, atau object counter sederhana.

## Catatan Tutor

- Pastikan siswa memahami bahwa detection berbeda dari recognition.
- Jangan menyimpan, membagikan, atau mengupload foto siswa tanpa izin.
- Haar Cascade bekerja paling baik pada wajah frontal dengan cahaya cukup.
- False positive dan wajah yang tidak terdeteksi adalah bahan diskusi tentang keterbatasan model.
- Jika kamera error, gunakan Upload tanpa mengubah bagian pemrosesan.
- Jika waktu terbatas, prioritaskan model, bounding box, jumlah wajah, dan satu eksperimen keterbatasan.
