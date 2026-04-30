# Bike-Sharing Data Analytics Project 🚲

## Project Overview
Proyek ini merupakan implementasi dari siklus analisis data lengkap menggunakan **Bike-Sharing Dataset**. Tujuan utama dari proyek ini adalah untuk mengidentifikasi pola perilaku pengguna sepeda berdasarkan variabel waktu (*temporal*) dan kondisi lingkungan (*weather*). Hasil analisis disajikan dalam bentuk dashboard interaktif guna mendukung pengambilan keputusan strategis dalam operasional bisnis.

## Project Structure
- **`/dashboard`**: Berisi file utama aplikasi dashboard (`dashboard.py`) dan dataset yang telah dibersihkan (`main_data.csv`).
- **`/data`**: Berisi dataset mentah asli (`day.csv` dan `hour.csv`).
- **`notebook.ipynb`**: Dokumentasi teknis proses analisis data (Wrangling, EDA, Visualization).
- **`requirements.txt`**: Daftar pustaka (libraries) Python yang diperlukan.
- **`README.md`**: Dokumentasi utama proyek.

## Setup Environment

### 1. Menggunakan venv (Virtual Environment)
```bash
# Membuat environment
python -m venv env

# Aktivasi environment
source env/bin/activate  # Untuk Linux/Mac
.\env\Scripts\activate   # Untuk Windows

# Instalasi Dependencies
pip install -r requirements.txt

# Membuat dan mengaktifkan environment
conda create --name bike-sharing-project python=3.9
conda activate bike-sharing-project

# Instalasi Dependencies
pip install -r requirements.txt

# Running Dashboard
streamlit run dashboard/dashboard.py

# Live Dashboard URL
Anda dapat mengakses dashboard yang telah dideploy secara publik melalui tautan berikut: https://bike-sharing-dashboard-nfclkypm5sa6h5dmbvikuw.streamlit.app/

## 📊 Business Insights

Berdasarkan hasil analisis data yang telah dilakukan, diperoleh beberapa poin penting sebagai berikut:

### 🌤️ Korelasi Cuaca
Terdapat **korelasi positif yang signifikan** antara kondisi cuaca cerah dengan volume penyewaan sepeda harian.

### 📅 Tren Musiman
Pola penggunaan sepeda menunjukkan **tren musiman yang konsisten** pada periode waktu tertentu setiap tahunnya.

### 🕒 Analisis Waktu
Volume penyewaan cenderung meningkat pada:
- **Hari kerja (weekdays)**
- **Jam sibuk (peak hours)**

---

## Action Items & Recommendations

### Optimalisasi Inventaris
Meningkatkan ketersediaan unit sepeda selama:
- Hari kerja
- Jam sibuk  
untuk mengakomodasi lonjakan permintaan.

### Distribusi Strategis
Mengoptimalkan distribusi sepeda di **lokasi dengan aktivitas pengguna tertinggi**.

### Manajemen Pemeliharaan
Melakukan **pemeliharaan rutin (maintenance)** pada saat **low season** untuk meminimalkan gangguan operasional.

### Predictive Analytics
Memanfaatkan data **prakiraan cuaca** sebagai variabel input untuk:
- Memprediksi permintaan
- Mengantisipasi fluktuasi penyewaan di masa depan
