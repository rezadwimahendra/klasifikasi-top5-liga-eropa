# Klasifikasi Hasil Pertandingan Top Lima Liga Eropa Musim 2025/2026 Berdasarkan Statistik Pertandingan Menggunakan Random Forest dengan Optimasi Hyperparameter Bayesian

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3-orange.svg)](https://scikit-learn.org/)
[![Optuna](https://img.shields.io/badge/Optuna-Bayesian%20Opt-blueviolet.svg)](https://optuna.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Repository ini dibuat untuk memenuhi tugas mata kuliah **Pemrograman Mobile Lanjut / Klasifikasi**, yang mencakup 7 tahapan pengerjaan utama dari pencarian dataset hingga komit dan push ke GitHub.

---

## 📌 Ringkasan 7 Poin Tugas

1. **Mencari Dataset Public:** 
   - Dataset pertandingan sepak bola Top 5 Liga Eropa musim 2025/2026 (`data top 5 liga.csv` - 1.752 baris, 22 atribut).
2. **Persiapan Lingkungan Pengembangan Lokal:** 
   - Konfigurasi Python 3.10, Virtual Environment (`.venv`), OpenCode / VS Code, Hermes CLI, Git, serta pustaka `pandas`, `scikit-learn`, `optuna`, `xgboost`, `jupyter`.
3. **Menentukan Topik Penelitian:** 
   - Klasifikasi Prediksi Hasil Pertandingan Sepak Bola Top 5 Liga Eropa Berdasarkan Statistik Pertandingan.
4. **Menentukan Judul Penelitian:** 
   - *"Klasifikasi Hasil Pertandingan Top Lima Liga Eropa Musim 2025/2026 Berdasarkan Statistik Pertandingan Menggunakan Random Forest dengan Optimasi Hyperparameter Bayesian"*
5. **Menentukan Pertanyaan Penelitian (Rumusan Masalah):** 
   - RQ1 (Kinerja Random Forest Baseline), RQ2 (Peningkatan Akurasi pasca Optimasi Bayesian), dan RQ3 (Fitur Statistik Match paling dominan / Feature Importance).
6. **Studi Literatur 10 Artikel & Tabel Penelitian Terdahulu (State of the Art):** 
   - Dokumentasi lengkap matriks perbandingan 10 artikel jurnal bereputasi pada berkas [`docs/03_Tabel_State_of_the_Art_10_Artikel.md`](docs/03_Tabel_State_of_the_Art_10_Artikel.md).
7. **Commit dan Push GitHub:** 
   - Pengelolaan repositori versi kontrol menggunakan Git.

---

## 📁 Struktur Direktori Repositori
```text
.
├── .gitignore                      # Berkas pengecualian Git
├── README.md                       # Dokumentasi utama proyek & tugas
├── requirements.txt                # Berkas dependensi Python
├── data top 5 liga.csv             # Dataset publik pertandingan Top 5 Liga Eropa
├── docs/
│   ├── 01_Topik_dan_Judul_Penelitian.md
│   ├── 02_Rumusan_Masalah_dan_Pertanyaan.md
│   ├── 03_Tabel_State_of_the_Art_10_Artikel.md
│   └── 04_Persiapan_Lingkungan_Pengembangan.md
├── notebooks/
│   └── klasifikasi_top5_liga.ipynb # Notebook interaktif
└── src/
    ├── preprocess.py               # Module pra-pemrosesan data
    └── train_eval.py               # Module eksperimen Random Forest + Bayesian Opt
```

---

## 🚀 Panduan Jalankan Proyek Lokal

### 1. Aktivasi Environment
```powershell
.\.venv\Scripts\Activate.ps1
```

### 2. Menjalankan Kode Eksperimen
```powershell
.\.venv\Scripts\python.exe src/train_eval.py
```

### 3. Menjalankan Notebook Interaktif
```powershell
.\.venv\Scripts\jupyter notebook notebooks/klasifikasi_top5_liga.ipynb
```
