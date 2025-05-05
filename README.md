# 🔐 Login Anomaly Detection with Isolation Forest

Deteksi aktivitas login mencurigakan menggunakan algoritma Machine Learning Isolation Forest.  
Proyek ini adalah demo sederhana yang dimodifikasi untuk mendeteksi anomali login yang bisa menunjukkan penyalahgunaan akun atau potensi peretasan.

---

## 📚 Tentang Proyek

Proyek ini dikembangkan untuk memenuhi tugas **Metodologi Penelitian Informatika** oleh:

- 👩‍🎓 **Isma Sifa Aulia**
- 🆔 **NIM**: 234110601072  
- 🎓 **Mahasiswa Informatika - Semester 4**  
- 🏫 **Universitas Islam Negeri Prof. K.H. Saifuddin Zuhri Purwokerto**

---

## 📁 Struktur Proyek

Anomaly-Detection-Exercise/
├── login_anomaly_demo.py # Script utama
├── login_data.csv # Dataset login user
├── README.md # Dokumentasi proyek
└── assets/
└── anomaly_plot.png # Visualisasi hasil

yaml
Copy code

---

## 🚀 Fitur Utama

- ✅ Deteksi login abnormal dengan algoritma Isolation Forest  
- ⚙️ Preprocessing otomatis untuk fitur `ip_address` dan `user_agent`  
- 📊 Visualisasi hasil dalam bentuk scatter plot  
- 💾 Output dengan kolom `anomaly` (1 = normal, -1 = anomali)  
- 🔧 Kode modular dan mudah dimodifikasi

---

## 📈 Contoh Dataset

```csv
user_id,login_time,ip_address,user_agent
1,2025-05-05 08:00:00,192.168.1.1,Firefox
1,2025-05-05 09:00:00,192.168.1.1,Chrome
2,2025-05-05 10:00:00,192.168.1.2,Edge
1,2025-05-05 11:00:00,192.168.1.3,Firefox
3,2025-05-05 12:00:00,192.168.1.2,Chrome
💡 Cara Kerja Singkat
Baca data login dari CSV

Encode ip_address dan user_agent

Terapkan Isolation Forest

Tandai data login anomali

Visualisasi hasil sebagai scatter plot

🧠 Teknologi & Library
Python 3.x

pandas

scikit-learn

matplotlib

seaborn

📦 Instalasi Library
bash
Copy code
pip install pandas scikit-learn matplotlib seaborn
▶️ Cara Menjalankan
bash
Copy code
python login_anomaly_demo.py
Output:

File assets/anomaly_plot.png

Tabel login dengan kolom anomaly

📌 Catatan
Dataset bisa diperluas untuk eksperimen lanjutan

Dataset ini sintetik namun cukup realistis untuk tugas akademik

✨ Kredit dan Referensi
Repositori ini dimodifikasi dari:
🔗 omkarpawar1430/Anomaly-Detection-Exercise

📝 Lisensi
Proyek ini dibuat untuk tujuan akademik dan pembelajaran.
Bebas digunakan dengan mencantumkan atribusi.

yaml
Copy code
