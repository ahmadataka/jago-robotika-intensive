# IoT Demo: ESP32 + Wokwi + Backend API + Streamlit

Contoh ini dibuat untuk model `teacher-prepared backend`:

- siswa fokus pada kode ESP32 di Wokwi
- tutor menyiapkan backend API lokal
- dashboard Streamlit menampilkan data yang dikirim dari simulasi

## Struktur

- `wokwi-esp32-sensor/`: project Wokwi ESP32 dengan sensor DHT22
- `backend/server.py`: API lokal untuk menerima data sensor
- `dashboard/app.py`: dashboard Streamlit untuk melihat data
- `data/`: database SQLite lokal

## Cara Menjalankan

Install dependency:

```bash
pip install -r iot/requirements.txt
```

Jalankan backend API:

```bash
python3 iot/backend/server.py
```

Jalankan dashboard Streamlit:

```bash
streamlit run iot/dashboard/app.py
```

## Menjalankan Wokwi

Project Wokwi ini memakai WiFi virtual `Wokwi-GUEST` dan mengirim data ke backend lokal.

Untuk mengakses backend lokal dari Wokwi, gunakan:

- `Private Wokwi IoT Gateway`

URL tujuan di dalam sketch:

- `http://host.wokwi.internal:8000/api/readings`

## Catatan Pembelajaran

Siswa tidak perlu membangun backend sendiri. Fokus siswa bisa pada:

- membaca sensor
- memformat data
- mengirim data ke endpoint
- memahami bahwa data sensor bisa muncul di dashboard web
