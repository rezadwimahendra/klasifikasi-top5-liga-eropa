# Klasifikasi Hasil Pertandingan Top Lima Liga Eropa Musim 2025/2026 Berdasarkan Statistik Pertandingan Menggunakan Random Forest dengan Optimasi Hyperparameter Bayesian

Proyek ini bertujuan untuk memprediksi hasil akhir pertandingan sepak bola (*Home Win*, *Draw*, *Away Win*) pada Top 5 Liga Eropa (Premier League, La Liga, Bundesliga, Serie A, dan Ligue 1) musim 2025/2026 berdasarkan statistik pertandingan.

Metode utama yang digunakan adalah **Random Forest Classifier** yang dioptimasi menggunakan **Bayesian Optimization (Optuna)** untuk mencari kombinasi hyperparameter terbaik.

---

## 📁 Struktur Folder Proyek

```text
klasifikasi-top5-liga-eropa/
├── README.md
├── requirements.txt
├── data/
│   ├── data_top_5_liga.csv
│   └── README.md
├── docs/
│   ├── 01_Topik_dan_Judul_Penelitian.md
│   ├── 02_Rumusan_Masalah_dan_Pertanyaan.md
│   ├── 03_Tabel_State_of_the_Art_10_Artikel.md
│   ├── 04_Persiapan_Lingkungan_Pengembangan.md
│   └── Tabel_State_of_the_Art_10_Artikel_Lengkap.docx
├── notebooks/
│   └── klasifikasi_top5_liga.ipynb
└── src/
    ├── preprocess.py
    └── train_eval.py
```

---

## 🚀 Cara Menjalankan Kode

### 1. Aktivasi Environment & Install Dependensi
```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Menjalankan Kode Ekserimen Klasifikasi
```powershell
python src/train_eval.py
```

### 3. Menjalankan Jupyter Notebook
```powershell
jupyter notebook notebooks/klasifikasi_top5_liga.ipynb
```
