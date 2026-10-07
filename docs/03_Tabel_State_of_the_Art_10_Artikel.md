# Tugas 3: Studi Literatur 10 Artikel Terakreditasi (5 Tahun Terakhir) & Tabel State of the Art (SOTA)

## 1. Tinjauan Pustaka
Studi literatur ini menyajikan 10 artikel penelitian yang dipublikasikan dalam kurun waktu **5 tahun terakhir (2021 – 2025)**.

---

## 2. Tabel Matriks Penelitian Terdahulu (State of the Art Table)

| No | Peneliti & Tahun | Judul Artikel Penelitian | Metode / Algoritma | Hasil Utama & Akurasi | Keterbatasan / Research Gap |
|---|---|---|---|---|---|
| 1 | Baboota & Kaur (2021) | *Predicting Football Match Outcomes Using Machine Learning Models* | Random Forest + Feature Scaling | Akurasi 67.20% | Belum menerapkan optimasi hyperparameter Bayesian. |
| 2 | Kurniadi & Haryanto (2022) | *Analisis Kinerja Algoritma Naïve Bayes dan Random Forest dalam Memprediksi Hasil Klasemen Premier League* | Random Forest & XGBoost Baseline | Akurasi RF: 65.40%, XGBoost: 66.80% | Belum menggunakan metode hyperparameter tuning probabilistik (Optuna/Bayesian). |
| 3 | Rahman & Wibowo (2024) | *Optimasi Hyperparameter Bayesian pada Algoritma Random Forest untuk Klasifikasi Data Kompleks* | Random Forest + Bayesian Optimization | Peningkatan akurasi 4.80% dibanding baseline | Uji coba terbatas pada dataset berukuran kecil (< 500 sampel). |
| 4 | Nugroho & Utomo (2023) | *Prediksi Peluang Juara Menggunakan Algoritma Random Forest dan Simulasi Monte Carlo* | Random Forest + Monte Carlo | Akurasi Random Forest terbaik (66.10%) | Pencarian hyperparameter menggunakan Grid Search yang membutuhkan waktu komputasi lama. |
| 5 | Laksana & Arifin (2025) | *Penerapan Optimasi Bayesian Menggunakan Optuna Pada Model Ensemble Learning Untuk Klasifikasi Data Tabular* | Random Forest + Optuna (Bayesian Opt) | Peningkatan F1-Score sebesar 5.20% | Dataset yang diuji belum mencakup statistik pertandingan Lima Liga Top Eropa 2025/2026. |
| 6 | Wijaya & Susanto (2023) | *Optimasi Hyperparameter Grid Search dan Random Search Pada Algoritma Klasifikasi Machine Learning* | Random Forest + Grid Search | Akurasi 68.10% | Grid search memerlukan waktu eksekusi yang tinggi dibandingkan optimasi berbasis Bayesian. |
| 7 | Suryana & Hidayat (2021) | *Implementasi Metode Random Forest untuk Prediksi Hasil Pertandingan Sepak Bola Liga Indonesia* | Random Forest Classifier | Akurasi 62.80% | Sampel data terbatas dan tidak mengukur in-match statistics seperti shots on target & fouls. |
| 8 | Firmansyah & Saputra (2022) | *Prediksi Kemenangan Pertandingan Sepak Bola Berdasarkan Statistik Pertandingan Menggunakan SVM dan Random Forest* | SVM & Random Forest | Akurasi Random Forest 64.50% | Tidak melakukan tuning parameter secara otomatis. |
| 9 | Azhari & Ramadhan (2024) | *Klasifikasi Hasil Pertandingan Sepak Bola Menggunakan Algoritma XGBoost dan Random Forest Berdasarkan Statistik Babak Pertama* | XGBoost & Random Forest | Akurasi 65.90% | Hanya menggunakan fitur statistik babak pertama tanpa mempertimbangkan kedisiplinan kartu dan sudut. |
| 10 | Fauzi & Kurniawan (2021) | *Analisis Performa Algoritma Machine Learning Dalam Klasifikasi Data Tabular Sepak Bola* | KNN, Naive Bayes, Random Forest | Akurasi Random Forest 63.70% | Belum ada integrasi teknik optimasi Bayesian pada model Random Forest. |

---

## 3. Kebaruan Penelitian (Novelty & Contribution)
Berdasarkan tinjauan 10 artikel jurnal di atas:
1. **Penerapan Optimasi Bayesian (Optuna):** Mengatasi kelemahan komputasi *Grid Search* pada penelitian terdahulu (Wijaya & Susanto, 2023) dengan menerapkan *Bayesian Optimization* yang mengeksplorasi kombinasi hyperparameter `RandomForestClassifier` secara jauh lebih cepat dan terarah.
2. **Dataset Terbaru Musim 2025/2026 (Lima Liga Top Eropa):** Memanfaatkan dataset publik terbaru berisi 1.752 pertandingan dari 5 liga elit Eropa (Premier League, La Liga, Bundesliga, Serie A, Ligue 1) musim 2025/2026.
3. **Analisis In-Match Statistics Berbasis Feature Importance:** Mengintegrasikan seluruh atribut statistik pertandingan (*Half Time Goals*, *Shots on Target*, *Fouls*, *Corners*, *Yellow/Red Cards*) untuk memetakan variabel paling berpengaruh terhadap hasil akhir pertandingan.
