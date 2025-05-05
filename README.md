# 🔐 Login Anomaly Detection with Isolation Forest

Deteksi aktivitas login mencurigakan menggunakan algoritma Machine Learning **Isolation Forest**.  
Proyek ini adalah demo sederhana berbasis kode sumber terbuka dari GitHub yang dimodifikasi untuk mendeteksi anomali login yang bisa mengindikasikan penyalahgunaan akun atau potensi peretasan.

---

## 📚 Tentang Proyek

Proyek ini dikembangkan untuk memenuhi tugas **Metodologi Penelitian Informatika** oleh:

- 🎓 **Isma Sifa Aulia**  
- 🆔 **NIM: 234110601072**  
- 📘 **Mahasiswa Informatika - Semester 4**  
- 🏫 **Universitas Islam Negeri Prof. K.H. Saifuddin Zuhri Purwokerto**

---

## 📁 Struktur Proyek

Anomaly-Detection-Exercise/
│
├── login_anomaly_demo.py # Script utama deteksi anomali login
├── login_data.csv # Dataset login user (data realistis)
├── README.md # Dokumentasi proyek
└── assets/
└── anomaly_plot.png # Visualisasi hasil deteksi

yaml
Copy code

---

## 🚀 Fitur Utama

- ✅ Deteksi login abnormal menggunakan algoritma **Isolation Forest**
- ⚙️ Preprocessing otomatis (ip_address, user_agent)
- 📊 Visualisasi anomali dengan scatter plot
- 💾 Output data login ditandai kolom `anomaly` (1 = normal, -1 = anomali)
- 🔧 Kode modular & mudah dimodifikasi

---

## 📈 Contoh Dataset (login_data.csv)

```csv
user_id,login_time,ip_address,user_agent
1,2025-05-05 08:00:00,192.168.1.1,Firefox
1,2025-05-05 09:00:00,192.168.1.1,Chrome
2,2025-05-05 10:00:00,192.168.1.2,Edge
1,2025-05-05 11:00:00,192.168.1.3,Firefox
3,2025-05-05 12:00:00,192.168.1.2,Chrome
💡 Cara Kerja
Membaca data login dari login_data.csv

Melakukan encoding fitur kategorikal (ip_address, user_agent)

Menerapkan model Isolation Forest

Menandai data yang terdeteksi anomali

Visualisasi hasil menggunakan scatter plot

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
Setelah dijalankan, kamu akan mendapatkan:

File CSV output dengan kolom anomaly

File visualisasi: assets/anomaly_plot.png

🖼️ Contoh Visualisasi


✨ Sumber Asal Proyek
Repositori ini dimodifikasi dari:
🔗 GitHub - omkarpawar1430/Anomaly-Detection-Exercise

📝 Lisensi
Proyek ini dibuat untuk pembelajaran dan eksperimen akademik.
Bebas digunakan dengan mencantumkan atribusi yang sesuai.