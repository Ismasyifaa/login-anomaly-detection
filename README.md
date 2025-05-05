# 🔐 Login Anomaly Detection with Isolation Forest

Deteksi aktivitas login mencurigakan menggunakan algoritma Machine Learning **Isolation Forest**.  
Proyek ini merupakan demo sederhana yang dimodifikasi dari proyek open-source GitHub, digunakan untuk mendeteksi anomali pada data login user, yang bisa mengindikasikan penyalahgunaan akun atau percobaan peretasan.

---

## 📚 Tentang Proyek

Proyek ini dikembangkan untuk memenuhi tugas **Metodologi Penelitian Informatika** oleh:

- 👩‍🎓 **Isma Sifa Aulia**  
- 🆔 **NIM**: 234110601072  
- 🎓 **Mahasiswa Informatika - Semester 4**  
- 🏫 **Universitas Islam Negeri Prof. K.H. Saifuddin Zuhri Purwokerto**

---

## 📁 Struktur Proyek

```
Anomaly-Detection-Exercise/
│
├── login_anomaly_demo.py       # Script utama deteksi anomali
├── login_data.csv              # Dataset login user (realistis)
├── README.md                   # Dokumentasi proyek
└── assets/
    └── anomaly_plot.png        # Visualisasi hasil deteksi
```

---

## 🚀 Fitur Utama

- ✅ Deteksi login abnormal menggunakan **Isolation Forest**
- ⚙️ Preprocessing otomatis untuk fitur kategorikal (`ip_address`, `user_agent`)
- 📊 Visualisasi anomali dalam bentuk scatter plot
- 💾 Output jelas dengan kolom `anomaly` (1
