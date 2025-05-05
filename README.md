# 🔐 Login Anomaly Detection with Isolation Forest#

Deteksi aktivitas login mencurigakan menggunakan algoritma **Machine Learning Isolation Forest**. Proyek ini adalah **demo sederhana** berbasis kode sumber terbuka dari GitHub yang dimodifikasi untuk mendeteksi **anomali login user** yang bisa mengindikasikan **penyalahgunaan akun** atau potensi **peretasan**.

---

## 📚 Tentang Proyek

Proyek ini dikembangkan untuk memenuhi tugas **Metodologi Penelitian Informatika** oleh:

🎓 **Isma Sifa Aulia**  
🆔 **NIM:** 234110601072  
📘 **Mahasiswa Informatika - Semester 4**  
🏫 **Universitas Islam Negri Prof.K.H.Saifuddin Zuhri Purwokerto**

---

## 📁 Struktur Proyek

Anomaly-Detection-Exercise/
│
├── login_anomaly_demo.py # Script utama untuk deteksi anomali login
├── login_data.csv # Dataset login user (data realistis)
├── README.md # Dokumentasi proyek
└── assets/
└── anomaly_plot.png # Visualisasi hasil deteksi

yaml
Copy code

---

## 🚀 Fitur Utama

- ✅ **Deteksi Login Abnormal** menggunakan algoritma **Isolation Forest**.
- ⚙️ **Preprocessing Otomatis** untuk fitur kategorikal (`ip_address`, `user_agent`).
- 📊 **Visualisasi Anomali** berbentuk scatter plot berdasarkan hasil deteksi.
- 💾 **Output jelas** dengan penambahan kolom `anomaly` (1 = normal, -1 = anomali).
- 🔧 **Kode modular** dan mudah dimodifikasi sesuai kebutuhan studi kasus login.

---

## 📈 Contoh Dataset (`login_data.csv`)

```csv
user_id,login_time,ip_address,user_agent
1,2025-05-05 08:00:00,192.168.1.1,Firefox
1,2025-05-05 09:00:00,192.168.1.1,Chrome
2,2025-05-05 10:00:00,192.168.1.2,Edge
1,2025-05-05 11:00:00,192.168.1.3,Firefox
3,2025-05-05 12:00:00,192.168.1.2,Chrome
💡 Cara Kerja Singkat
Baca data login dari file CSV.

Lakukan encoding terhadap kolom kategorikal seperti ip_address dan user_agent.

Terapkan Isolation Forest untuk deteksi anomali login.

Deteksi dan tandai anomali pada data login.

Visualisasikan hasil deteksi dalam bentuk grafik scatter plot.

🧠 Teknologi & Library
Python 3.x

pandas

scikit-learn

matplotlib

seaborn

📦 Instalasi library (jika belum terpasang):

bash
Copy code
pip install pandas scikit-learn matplotlib seaborn
▶️ Cara Menjalankan
Untuk menjalankan demo, gunakan perintah berikut di terminal:

bash
Copy code
python login_anomaly_demo.py
Jika berhasil, kamu akan mendapatkan:

Tabel deteksi dengan kolom anomaly (1 = normal, -1 = anomali).

File gambar hasil visualisasi: assets/anomaly_plot.png.

🖼️ Contoh Visualisasi
Berikut adalah contoh visualisasi hasil deteksi anomali:


📌 Catatan
Kamu dapat menambahkan lebih banyak data login untuk menguji algoritma.

Semakin kompleks data yang diberikan, hasil deteksi akan semakin kuat.

Dataset ini sintetis namun realistis dan cocok untuk eksperimen dan tugas akademik.

✨ Kontribusi Awal Proyek
Proyek ini dimodifikasi dari:

🔗 GitHub - omkarpawar1430/Anomaly-Detection-Exercise

📝 Lisensi
Proyek ini dibuat untuk keperluan pembelajaran dan eksperimen akademik. Bebas digunakan dengan mencantumkan atribusi yang sesuai.

### 2. **Langkah-Langkah Memperbaiki dan Menyusun README di GitHub**

#### Langkah 1: **Periksa dan Perbaiki Format Markdown di Editor**
1. **Buka editor teks** seperti **Visual Studio Code (VSC)** atau gunakan **Dillinger.io** untuk mengedit file Markdown.
2. **Salin kode** di atas dan paste ke dalam file `README.md` di dalam repositori kamu.
3. Pastikan **spasi, indentasi**, dan penggunaan tanda seperti **`#`**, **`-`**, dan **```** sesuai dengan standar Markdown yang benar.

#### Langkah 2: **Menambahkan atau Mengupdate File ke Repositori GitHub**

Jika kamu sudah selesai memperbaiki file `README.md` dan ingin mendorong perubahan ke GitHub:

1. **Buka terminal** atau **command prompt** di folder projek.
2. **Tambah perubahan ke staging area**:
   ```bash
   git add README.md
<h1 align="center">🔐 Login Anomaly Detection</h1>

<p align="center">
  <i>Deteksi aktivitas login mencurigakan menggunakan algoritma Isolation Forest</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10+-blue?logo=python">
  <img src="https://img.shields.io/badge/scikit--learn-1.2+-orange?logo=scikitlearn">
  <img src="https://img.shields.io/badge/status-demo--project-green">
</p>

---

## 📌 Deskripsi Singkat

Proyek ini mendeteksi **login abnormal/anomali** yang berpotensi menjadi aktivitas mencurigakan seperti peretasan akun. Menggunakan pendekatan unsupervised dengan **algoritma Isolation Forest**.

---

## 🧑‍💻 Identitas Pengembang

- **Nama**: Isma Sifa Aulia  
- **NIM**: 234110601072  
- **Prodi**: Informatika – Semester 4  
- **Universitas**: Islam Negri Prof.K.H.Saifuddin Zuhri Purwokerto

---

## 📂 Struktur Proyek

login-anomaly-detection/
├── login_anomaly_demo.py ← Skrip utama
├── login_data.csv ← Dataset login sintetis
├── assets/
│ └── anomaly_plot.png ← Visualisasi hasil
└── README.md ← Dokumentasi ini

yaml
Copy code

---

## 💡 Cara Kerja

1. Baca data login dari file `login_data.csv`.
2. Encoding `ip_address` & `user_agent` menjadi angka.
3. Jalankan Isolation Forest untuk mendeteksi anomali.
4. Hasil ditandai kolom `anomaly`:  
   `-1` = anomali, `1` = normal.
5. Visualisasi hasil berupa scatter plot disimpan di folder `assets`.

---

## 🧪 Contoh Data Login

```csv
user_id,login_time,ip_address,user_agent
1,2025-05-05 08:00:00,192.168.1.1,Firefox
1,2025-05-05 09:00:00,192.168.1.1,Chrome
2,2025-05-05 10:00:00,192.168.1.2,Edge
1,2025-05-05 11:00:00,192.168.1.3,Firefox
3,2025-05-05 12:00:00,192.168.1.2,Chrome
📸 Contoh Visualisasi Hasil

⚙️ Teknologi & Library
Python 3.x

pandas

scikit-learn

matplotlib

seaborn

🚀 Cara Menjalankan
Jalankan dari terminal atau VS Code:

bash
Copy code
pip install pandas scikit-learn matplotlib seaborn
python login_anomaly_demo.py
🔗 Repositori Asal
Modifikasi dari:
omkarpawar1430/Anomaly-Detection-Exercise

📄 Lisensi
Proyek ini hanya untuk tujuan pembelajaran.
Silakan fork & modifikasi dengan mencantumkan atribusi.