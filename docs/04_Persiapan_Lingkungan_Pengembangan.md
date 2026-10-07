# Tugas 4: Persiapan Lingkungan Pengembangan Lokal

## 1. Komponen Lingkungan Pengembangan (Development Stack)

| Komponen Tool | Versi / Spesifikasi | Fungsi & Peran dalam Proyek |
|---|---|---|
| **Python** | Python 3.10.1 | Runtime eksekusi bahasa pemrosesan & ML |
| **Virtual Environment** | Python `.venv` | Isolasi paket dependensi proyek |
| **IDE / Editor** | OpenCode / VS Code | Penulisan kode script dan notebook |
| **CLI / Agent** | Hermes CLI / Terminal Subagent | Eksekusi otomatis perintah shell |
| **Version Control** | Git 2.49.0 & GitHub | Manajemen repositori & riwayat commit |

---

## 2. Pustaka Python (`requirements.txt`)
- `pandas` (>= 2.0.0): Membaca & mengolah file dataset `data top 5 liga.csv` (semicolon delimited).
- `numpy` (>= 1.24.0): Perhitungan matriks & transformasi numerik.
- `scikit-learn` (>= 1.3.0): Pra-pemrosesan (`StandardScaler`, `LabelEncoder`), pembagian data (`train_test_split`), model `RandomForestClassifier`, dan metrik evaluasi.
- `optuna` (>= 3.0.0): Framework *Bayesian Optimization* untuk pencarian hyperparameter optimal.
- `scikit-optimize` (>= 0.9.0): Pustaka pendukung algoritma Bayesian Search.
- `xgboost` (>= 2.0.0): Algoritma *Gradient Boosting* sebagai model pembanding pendukung.
- `matplotlib` & `seaborn`: Visualisasi grafik bar *Feature Importance* dan *Confusion Matrix*.
- `jupyter` & `ipykernel`: Notebook interaktif `.ipynb`.

---

## 3. Langkah Aktivasi & Eksekusi

### 1. Aktivasi Virtual Environment
```powershell
.\.venv\Scripts\Activate.ps1
```

### 2. Menjalankan Pemodelan Python Script
```powershell
.\.venv\Scripts\python.exe src/train_eval.py
```

### 3. Menjalankan Jupyter Notebook
```powershell
.\.venv\Scripts\jupyter notebook notebooks/klasifikasi_top5_liga.ipynb
```
