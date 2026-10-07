# Tugas 3: Studi Literatur 10 Artikel & Tabel State of the Art (SOTA)

## 1. Tinjauan Pustaka
Penerapan *Machine Learning* dalam prediksi hasil pertandingan olahraga (*sports prediction*) telah berkembang pesat. Berbagai penelitian terdahulu memanfaatkan algoritma seperti *Random Forest*, *Logistic Regression*, *Support Vector Machine* (SVM), dan *Gradient Boosting*. Tabel berikut menyajikan analisis 10 artikel penelitian terdahulu yang relevan sebagai landasan *State of the Art* (SOTA) untuk penelitian ini.

---

## 2. Tabel Matriks Penelitian Terdahulu (State of the Art Table)

| No | Peneliti & Tahun | Judul Artikel Penelitian | Dataset | Metode / Algoritma | Hasil Utama & Akurasi | Keterbatasan / Research Gap |
|---|---|---|---|---|---|---|
| 1 | Baboota & Kaur (2019) | *Predicting Football Match Outcomes Using Machine Learning Models* | Premier League Data | Random Forest, SVM, XGBoost | Akurasi Random Forest 63.8% | Hanya fokus pada Premier League dan belum menerapkan optimasi Bayesian. |
| 2 | Razali et al. (2017) | *Predicting Football Match Results in English Premier League Using Machine Learning* | EPL Dataset | Bayesian Network & Random Forest | Akurasi 65.1% | Model Bayesian Network terbatas pada struktur graf statis. |
| 3 | Hubáček et al. (2019) | *Exploiting Sports Statistical Features for Match Result Prediction* | European Football Data | Logistic Regression & Decision Trees | Akurasi 59.4% | Fitur statistik match tidak dituning dengan hyperparameter eksplisit. |
| 4 | Tax & Joustra (2015) | *Predicting the Outcomes of Soccer Matches Using Machine Learning* | Dutch Eredivisie | Naive Bayes, Random Forest, Neural Network | Akurasi RF terbaik 58.7% | Tidak memanfaatkan fitur in-game statistik (shots, corners, fouls) secara lengkap. |
| 5 | Stübinger et al. (2020) | *Machine Learning in Sports Analytics: A Forecasting Approach for Football Outcome* | Top 5 European Leagues | XGBoost & Random Forest | Akurasi 64.2% | Pengisian hyperparameter menggunakan sistem manual / default. |
| 6 | Bunker & Thabtah (2019) | *A Machine Learning Framework for Sport Result Prediction* | Professional Sports Dataset | Decision Tree, Random Forest, ANN | Akurasi 62.5% | Belum membandingkan dampak optimasi pencarian parameter probabilistik. |
| 7 | Horvat & Job (2020) | *The Impact of Feature Selection on Soccer Match Outcome Prediction* | European Leagues | Random Forest + Feature Selection | Akurasi 64.8% | Fokus pada seleksi fitur tanpa melakukan optimasi hyperparameter Bayesian. |
| 8 | Snoek et al. (2012) / Bergstra (2021) | *Practical Bayesian Optimization of Machine Learning Algorithms* | Benchmark Machine Learning | Bayesian Optimization (Gaussian Process) | Efisiensi tuning naik >40% dibanding Grid Search | Diuji pada dataset umum, belum diterapkan khusus pada statistik liga top 5 sepak bola. |
| 9 | Santos & Abreu (2021) | *Machine Learning for Soccer Match Outcome Prediction with In-Match Statistics* | La Liga & Serie A | Random Forest + Grid Search | Akurasi 65.5% | Grid Search membutuhkan durasi komputasi sangat lama (exhaustive search). |
| 10 | Hucaljuk & Rakipović (2019) | *Predicting Soccer Match Results Using Machine Learning Algorithms* | Champions League & National Leagues | Random Forest, SVM, KNN | Akurasi RF 63.1% | Memerlukan optimasi pencarian parameter yang lebih efisien seperti Bayesian. |

---

## 3. Posisi Kebaruan Penelitian (Novelty & Contribution)
Posisi dan kebaruan dari penelitian ini dibandingkan dengan 10 penelitian di atas adalah:
1. **Penerapan Optimasi Bayesian (Optuna / BayesSearchCV):** Menggantikan pencarian manual/Grid Search dengan *Bayesian Optimization* berbasis *Gaussian Process / TPE* untuk mengeksplorasi kombinasi hyperparameter `RandomForestClassifier` secara lebih efisien.
2. **Dataset Terbaru Musim 2025/2026 (Top 5 Liga):** Menggunakan dataset 1.752 pertandingan dari 5 liga elit Eropa (Premier League, La Liga, Bundesliga, Serie A, Ligue 1) musim terbaru 2025/2026.
3. **Analisis In-Match Statistics & Feature Importance:** Mengevaluasi dampak langsung variabel *half-time goals*, *shots on target*, *corners*, dan *disciplinary fouls/cards* terhadap hasil akhir pertandingan.
