# 🔐 Login Anomaly Detection with Isolation Forest

Deteksi aktivitas login mencurigakan menggunakan algoritma Machine Learning **Isolation Forest**.  
Proyek ini merupakan demo sederhana yang dimodifikasi dari proyek open-source GitHub, digunakan untuk mendeteksi anomali pada data login user, yang bisa mengindikasikan penyalahgunaan akun atau percobaan peretasan.

---

## 📚 Tentang Proyek

Proyek ini dikembangkan untuk memenuhi tugas **Metodologi Penelitian Informatika** oleh:

- 👩‍🎓 **Isma Sifa Aulia**  
- 🆔 **NIM**: 234110601072  
- 🎓 **Mahasiswa Informatika - Semester 4**  
- 🏫 **Universitas Islam Negri Prof.K.H Saifuddin Zuhri Purwokerto**

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
- 💾 Output jelas dengan kolom `anomaly` (1 = normal, -1 = anomali)
- 🔧 Kode modular dan mudah dimodifikasi sesuai kebutuhan

---

## 📈 Contoh Dataset (`login_data.csv`)

```csv
user_id,login_time,ip_address,user_agent
1,2025-05-05 08:00:00,192.168.1.1,Firefox
1,2025-05-05 09:00:00,192.168.1.1,Chrome
2,2025-05-05 10:00:00,192.168.1.2,Edge
1,2025-05-05 11:00:00,192.168.1.3,Firefox
3,2025-05-05 12:00:00,192.168.1.2,Chrome
```

---

## 💡 Cara Kerja Singkat

1. Membaca data login dari file `.csv`
2. Melakukan encoding pada kolom kategorikal
3. Menerapkan algoritma **Isolation Forest**
4. Menandai anomali pada data login
5. Menampilkan hasil deteksi dengan grafik

---

## 🧠 Teknologi & Library

- Python 3.x
- pandas
- scikit-learn
- matplotlib
- seaborn

### 📦 Instalasi Library

```bash
pip install pandas scikit-learn matplotlib seaborn
```

---

## ▶️ Cara Menjalankan

Untuk menjalankan proyek:

```bash
python login_anomaly_demo.py
```

Output:
- Tabel dengan kolom `anomaly` (1 = normal, -1 = anomali)
- Gambar visualisasi disimpan di: `assets/anomaly_plot.png`

---

## 🖼️ Contoh Visualisasi

![Visualisasi Anomali](assets/anomaly_plot.png)

---

## 📌 Catatan

- Kamu dapat menambahkan lebih banyak data login untuk menguji algoritma
- Dataset ini sintetis tapi menyerupai data asli
- Cocok untuk tugas akademik dan eksperimen sederhana

---

## ✨ Kontribusi Awal

Proyek ini dimodifikasi dari:  
🔗 [omkarpawar1430/Anomaly-Detection-Exercise](https://github.com/omkarpawar1430/Anomaly-Detection-Exercise)

---

## 📝 Lisensi

Proyek ini untuk pembelajaran dan eksperimen akademik.  
Bebas digunakan dengan menyebutkan atribusi.

---

