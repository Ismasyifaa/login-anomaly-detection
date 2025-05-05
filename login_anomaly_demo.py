# Import library yang diperlukan
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Membaca data login dari CSV
df = pd.read_csv('login_data.csv')

# Mengonversi kolom 'login_time' ke dalam format timestamp
df['login_time'] = pd.to_datetime(df['login_time'])
df['login_time'] = df['login_time'].astype(int) / 10**9  # Mengonversi ke detik

# Mengonversi kolom kategorikal 'ip_address' dan 'user_agent' ke angka
le = LabelEncoder()
df['ip_address'] = le.fit_transform(df['ip_address'])
df['user_agent'] = le.fit_transform(df['user_agent'])

# Menampilkan data setelah preprocessing
print(df.head())

# Menentukan fitur yang digunakan untuk deteksi anomali
features = df[['user_id', 'login_time', 'ip_address', 'user_agent']]

# Membuat model Isolation Forest
model = IsolationForest(contamination=0.1)  # 10% data dianggap anomali

# Melatih model dengan data
model.fit(features)

# Memprediksi anomali (1 = normal, -1 = anomali)
df['anomaly'] = model.predict(features)

# Menampilkan hasil deteksi anomali
print(df)

# Visualisasi hasil deteksi anomali
plt.scatter(df['login_time'], df['user_id'], c=df['anomaly'], cmap='coolwarm')
plt.xlabel('Login Time')
plt.ylabel('User ID')
plt.title('Deteksi Anomali Login')
plt.show()
