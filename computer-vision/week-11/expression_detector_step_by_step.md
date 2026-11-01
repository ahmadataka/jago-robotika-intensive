# Dari Face Detector Week 9 ke Smile / Expression Detector

Kode awal: [Face Detector Week 9](../week-9/app.py).
Kode akhir: [expression_detector.py](expression_detector.py).

Kerjakan perubahan berikut pada satu file `app.py` milik siswa. Nomor langkah adalah urutan modifikasi; gunakan nama baris sebagai patokan karena nomor baris bergeser setelah penambahan kode.

## 1. Jalankan kode awal

Buka file Face Detector Week 9 di VS Code, simpan salinan sebagai `app.py` pada folder project Week 11, lalu jalankan dari terminal folder tersebut:

```bash
streamlit run app.py
```

Jika Streamlit belum terpasang:

```bash
python -m pip install streamlit pillow numpy "opencv-python-headless<5"
```

Di Mac, gunakan `python3` jika `python` tidak tersedia.

Cek: kamera atau upload menghasilkan kotak wajah dan jumlah wajah.

## 2. Ganti judul dan petunjuk

Ganti dua baris judul Week 9 dengan:

```python
st.title("Smile / Expression Detector")
st.write("Temukan wajah, lalu cari pola senyum pada area mulut.")
```

Setelah baris slider `minimum_size`, tambahkan slider baru. Ganti informasi sidebar lama sehingga blok sidebar menjadi:

```python
input_mode = st.sidebar.radio("Sumber gambar", ["Kamera", "Upload"])
minimum_size = st.sidebar.slider("Ukuran wajah minimum", 30, 150, 50, 10)
smile_neighbors = st.sidebar.slider("Ketatnya deteksi senyum", 5, 40, 20)
st.sidebar.info("Pola senyum pada gambar tidak menentukan perasaan seseorang.")
```

Cek: sidebar sekarang mempunyai dua slider. Bagian import dan input kamera/upload masih sama dengan Week 9.

## 3. Tambahkan model senyum

Cari:

```python
face_detector = cv2.CascadeClassifier(model_path)
```

Tepat di bawahnya, tambahkan:

```python
smile_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")
```

Baris tersebut tetap berada di dalam `if input_file:`, sejajar dengan `face_detector`. Pertahankan blok `faces = face_detector.detectMultiScale(...)`.

Penjelasan: model pertama mencari wajah, model kedua mencari pola senyum. Keduanya sudah tersedia pada instalasi OpenCV 4.

Cek: app tetap dapat menemukan wajah tanpa error model.

## 4. Potong area mulut dari setiap wajah

Cari blok lama:

```python
result = image_array.copy()
for x, y, width, height in faces:
    cv2.rectangle(result, (x, y), (x + width, y + height), (255, 80, 40), 5)
```

Tambahkan penghitung sebelum loop dan crop di dalam loop sehingga menjadi:

```python
result = image_array.copy()
smile_count = 0
for x, y, width, height in faces:
    mouth_y = y + height // 2
    mouth = grayscale[mouth_y:y + height, x:x + width]

    cv2.rectangle(result, (x, y), (x + width, y + height), (255, 80, 40), 5)
```

Penjelasan:

- `height // 2` menemukan setengah tinggi wajah.
- `mouth_y` adalah baris awal bagian bawah wajah.
- Crop array memakai urutan `[baris/y, kolom/x]`.
- Model senyum hanya menerima bagian bawah wajah agar pencarian lebih terarah.

Cek: app masih menampilkan kotak seperti sebelumnya. Crop belum ditampilkan dan belum mengubah hasil.

## 5. Deteksi senyum dan pilih label

Di dalam loop, setelah `mouth = ...` dan sebelum `cv2.rectangle(...)`, tambahkan:

```python
smiles = smile_detector.detectMultiScale(
    mouth, scaleFactor=1.7, minNeighbors=smile_neighbors, minSize=(20, 10)
)
if len(smiles) > 0:
    label = "Senyum terdeteksi"
    smile_count += 1
else:
    label = "Senyum belum terdeteksi"
```

Indentasi: `smiles` sejajar dengan `mouth`; isi `if` dan `else` masuk satu tingkat lagi.

Setiap wajah hanya menambah penghitung satu kali, walaupun model menemukan beberapa kandidat senyum pada crop yang sama.

Cek: ubah slider ketatnya deteksi. Angka lebih tinggi membuat deteksi lebih ketat.

## 6. Tampilkan label di atas wajah

Setelah `cv2.rectangle(...)` di dalam loop, tambahkan:

```python
cv2.putText(result, label, (x, max(20, y - 10)),
            cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 80, 40), 2)
```

Penjelasan: teks ditempatkan di atas kotak. `max(20, y - 10)` menjaga posisi teks agar tidak keluar dari bagian atas gambar.

Cek: setiap kotak wajah mempunyai label.

## 7. Rapikan output

Pertahankan dua kolom Week 9. Ganti caption hasil dan tambahkan metric senyum:

```python
left, right = st.columns(2)
left.image(image, caption="Gambar asli", width="stretch")
right.image(result, caption="Hasil deteksi ekspresi", width="stretch")
st.metric("Jumlah wajah", len(faces))
st.metric("Senyum terdeteksi", smile_count)
```

Hapus blok status lama `if len(faces) > 0: ... else: ...` di bawah metric karena versi akhir memakai dua metric.

Pertahankan `else` paling luar milik `if input_file:`, tetapi ganti isinya:

```python
else:
    st.info("Gunakan kamera atau upload gambar wajah dari arah depan.")
```

Cek: gambar tanpa wajah menunjukkan kedua metric bernilai 0.

## 8. Uji dan jelaskan

1. Ambil foto wajah frontal saat tersenyum.
2. Ambil ulang tanpa senyum.
3. Coba mulut terbuka dan amati kemungkinan deteksi salah.
4. Bandingkan cahaya terang dan redup.
5. Coba gambar tanpa wajah.
6. Pastikan angka senyum tidak melebihi jumlah wajah.

Project ini mendeteksi pola visual senyum, bukan mengukur kebahagiaan, kesedihan, atau emosi sebenarnya. Cocokkan hasil modifikasi dengan kode akhir jika ada perbedaan indentasi atau variabel.
