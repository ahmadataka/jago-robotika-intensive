# Tutor Flow Week 4 - Color and Filters

Durasi: `60 menit`

File utama:

- `app.py`

Tujuan:

- siswa mengatur brightness dan contrast gambar
- siswa mencoba blur dan sharpen
- siswa memahami bahwa gambar RGB memiliki channel merah, hijau, dan biru
- siswa membandingkan gambar asli dengan hasil filter

## Persiapan Tutor

IDE yang dipakai:

- `Visual Studio Code (VS Code)`

Siswa membuat folder kerja sendiri, misalnya `computer-vision-week-4`, lalu membuat satu file bernama `app.py`.

Jalankan dari terminal pada folder tersebut:

```bash
streamlit run app.py
```

Saat mengajar, file yang dibahas tetap `satu file yang sama`, tetapi ditulis bertahap.

## Alur 1 Jam

### 0-10 menit: Cek instalasi dan review Week 3

Langkah tutor:

1. Pastikan VS Code, Python, Streamlit, dan Pillow sudah terpasang.
2. Minta siswa membuat folder `computer-vision-week-4` dan file `app.py`.
3. Review Week 3: crop, resize, rotate, dan flip mengubah bentuk atau posisi gambar.
4. Jelaskan bahwa Week 4 mengubah tampilan warna dan ketajaman pixel.

Perintah cek:

```bash
python3 --version
python3 -m pip show streamlit pillow
```

Jika belum terpasang:

```bash
python3 -m pip install streamlit pillow
```

### 10-20 menit: Bagian 1 - Kerangka app dan upload gambar

Tulis bagian awal:

```python
from io import BytesIO

from PIL import Image, ImageEnhance, ImageFilter
import streamlit as st

st.title("Image Filter Lab")
st.write("Atur warna dan ketajaman gambar dengan filter sederhana.")

uploaded_file = st.file_uploader("Upload gambar", type=["png", "jpg", "jpeg"])
```

Jelaskan:

- `ImageEnhance` mengatur brightness, contrast, dan sharpness.
- `ImageFilter` menyediakan efek seperti blur.
- `BytesIO` menyiapkan hasil gambar agar dapat didownload.

### 20-28 menit: Bagian 2 - Pilihan dan kekuatan filter

Tambahkan setelah gambar dibuka:

```python
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    effect = st.selectbox(
        "Pilih filter",
        ["Brightness", "Contrast", "Blur", "Sharpen", "Red Channel", "Green Channel", "Blue Channel"],
    )
    strength = st.slider("Kekuatan filter", 1, 3, 2)
```

Jelaskan:

- `selectbox` menentukan jenis filter.
- `slider` memberi nilai kekuatan dari 1 sampai 3.
- satu variable input dapat memengaruhi hasil visual secara langsung.

### 28-40 menit: Bagian 3 - Brightness, contrast, blur, dan sharpen

Tambahkan:

```python
if effect == "Brightness":
    result = ImageEnhance.Brightness(image).enhance(1 + strength * 0.3)
elif effect == "Contrast":
    result = ImageEnhance.Contrast(image).enhance(1 + strength * 0.4)
elif effect == "Blur":
    result = image.filter(ImageFilter.GaussianBlur(radius=strength))
elif effect == "Sharpen":
    result = ImageEnhance.Sharpness(image).enhance(1 + strength)
```

Jelaskan secara visual:

- brightness membuat gambar lebih terang.
- contrast memperjelas perbedaan bagian gelap dan terang.
- blur menghaluskan detail gambar.
- sharpen menegaskan detail dan tepi objek.

Minta siswa mencoba nilai slider 1 dan 3 pada gambar yang sama.

### 40-50 menit: Bagian 4 - Memisahkan channel RGB

Tambahkan:

```python
else:
    red, green, blue = image.split()
    empty = Image.new("L", image.size, 0)

    if effect == "Red Channel":
        result = Image.merge("RGB", (red, empty, empty))
    elif effect == "Green Channel":
        result = Image.merge("RGB", (empty, green, empty))
    else:
        result = Image.merge("RGB", (empty, empty, blue))
```

Jelaskan:

- gambar RGB tersusun dari tiga lapisan warna.
- `split()` memisahkan ketiga channel.
- `empty` adalah channel kosong dengan nilai nol.
- `merge()` menyatukan kembali channel menjadi gambar RGB.

### 50-57 menit: Bagian 5 - Bandingkan dan download

Tambahkan:

```python
left, right = st.columns(2)
left.image(image, caption="Gambar asli", width="stretch")
right.image(result, caption=effect, width="stretch")

buffer = BytesIO()
result.save(buffer, format="PNG")
st.download_button("Download hasil", buffer.getvalue(), "hasil_filter.png", "image/png")
```

Target hasil:

- gambar asli dan hasil tampil berdampingan.
- pilihan filter dan slider mengubah hasil.
- hasil filter dapat didownload sebagai PNG.

### 57-60 menit: Variasi dan penutup

Latihan:

- ubah batas slider dari 3 menjadi 5.
- bandingkan channel warna pada foto alam dan foto manusia.
- tentukan filter terbaik untuk foto yang terlalu gelap atau kurang tajam.

Pengantar Week 5:

- setelah mengubah pixel dengan filter, siswa akan menggambar garis, kotak, lingkaran, dan teks di atas gambar.

## Catatan Tutor

- Gunakan gambar yang memiliki banyak warna agar perbedaan channel RGB mudah terlihat.
- Jelaskan filter melalui perubahan visual, tidak perlu masuk ke rumus matematika.
- Jika waktu terbatas, prioritaskan brightness, blur, dan satu color channel.
