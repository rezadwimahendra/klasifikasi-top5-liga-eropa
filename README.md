# Klasifikasi Hasil Pertandingan Top 5 Liga Eropa 2025/2026 Menggunakan Random Forest Dengan Optimasi Hyperparameter Bayesian

Proyek ini melakukan **klasifikasi hasil pertandingan sepak bola** (*Home Win*, *Draw*, *Away Win*) pada Top 5 Liga Eropa (Premier League, La Liga, Bundesliga, Serie A, dan Ligue 1) musim 2025/2026 berdasarkan statistik pertandingan menggunakan algoritma **Random Forest** yang dioptimasi dengan **Optimasi Hyperparameter Bayesian (Optuna)**.

---

##  Struktur Folder Proyek

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

##  Cara Menjalankan Kode

### 1. Aktivasi Environment & Install Dependensi
```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Menjalankan Kode Eksperimen Klasifikasi
```powershell
python src/train_eval.py
```

### 3. Menjalankan Jupyter Notebook
```powershell
jupyter notebook notebooks/klasifikasi_top5_liga.ipynb
```
