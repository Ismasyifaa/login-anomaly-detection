🔐 Login Anomaly Detection with Isolation Forest
Deteksi aktivitas login mencurigakan menggunakan algoritma Machine Learning Isolation Forest. Proyek ini adalah demo sederhana berbasis kode sumber terbuka dari GitHub yang dimodifikasi untuk mendeteksi anomali login user yang bisa mengindikasikan penyalahgunaan akun atau potensi peretasan.

📚 Tentang Proyek
Proyek ini dikembangkan untuk memenuhi tugas Metodologi Penelitian Informatika oleh:

🎓 Isma Sifa Aulia
🆔 NIM: 234110601072
📘 Mahasiswa Informatika - Semester 4
🏫 Universitas [Isi Nama Kampus Anda]

📁 Struktur Proyek
bash
Copy code
Anomaly-Detection-Exercise/
│
├── login_anomaly_demo.py       # Script utama untuk deteksi anomali login
├── login_data.csv              # Dataset login user (data realistis)
├── README.md                   # Dokumentasi proyek
└── assets/
    └── anomaly_plot.png        # Visualisasi hasil deteksi
🚀 Fitur Utama
✅ Deteksi Login Abnormal menggunakan algoritma Isolation Forest.

⚙️ Preprocessing Otomatis untuk fitur kategorikal (ip_address, user_agent).

📊 Visualisasi Anomali berbentuk scatter plot berdasarkan hasil deteksi.

💾 Output jelas dengan penambahan kolom anomaly (1 = normal, -1 = anomali).

🔧 Kode modular dan mudah dimodifikasi sesuai kebutuhan studi kasus login.

📈 Contoh Dataset (login_data.csv)
csv
Copy code
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

