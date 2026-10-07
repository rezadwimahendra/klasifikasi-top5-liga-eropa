# Tugas 2: Rumusan Masalah dan Pertanyaan Penelitian

## 1. Latar Belakang & Rumusan Masalah
Prediksi hasil akhir pertandingan sepak bola (*Home Win*, *Draw*, *Away Win*) merupakan tantangan klasifikasi non-linear yang kompleks karena dipengaruhi oleh berbagai variabel statistik pertandingan seperti efektivitas tembakan, penguasaan bola, hingga tingkat pelanggaran. Algoritma *Random Forest* terbukti mampu menangani hubungan non-linear antar variabel tersebut. Namun, performa model *Random Forest* standar sangat sensitif terhadap kombinasi *hyperparameter* (seperti `n_estimators`, `max_depth`, `min_samples_split`). 

Pendekatan optimasi konvensional seperti *Grid Search* memerlukan waktu komputasi yang tinggi dan kurang efisien. Oleh karena itu, penerapan **Optimasi Hyperparameter Bayesian** (*Bayesian Optimization*) berbasis *Probabilistic Surrogate Model* diperlukan untuk menemukan kombinasi parameter optimal secara lebih cepat dan akurat.

---

## 2. Pertanyaan Penelitian (*Research Questions*)

- **RQ1:** Bagaimana performa metrik evaluasi (Akurasi, Presisi, Recall, F1-Score, dan ROC-AUC) dari algoritma **Random Forest Baseline** (tanpa optimasi) dalam mengklasifikasikan hasil pertandingan sepak bola Top 5 Liga Eropa?
- **RQ2:** Seberapa besar tingkat peningkatan kinerja klasifikasi yang diperoleh setelah menerapkan teknik **Optimasi Hyperparameter Bayesian** (*Bayesian Optimization*) pada algoritma Random Forest?
- **RQ3:** Indikator statistik pertandingan manakah (*Feature Importance*) yang memberikan kontribusi paling dominan terhadap prediksi hasil akhir pertandingan?

---

## 3. Tujuan dan Manfaat Penelitian
- **Tujuan:**
  1. Membangun model klasifikasi *Random Forest* teroptimasi Bayesian untuk memprediksi hasil pertandingan Top 5 Liga Eropa.
  2. Mengevaluasi perbandingan kuantitatif performa model sebelum dan sesudah optimasi Bayesian.
  3. Mengidentifikasi fitur statistik yang paling krusial dalam menentukan kemenangan tim.
- **Manfaat:** Menjadi referensi akademis dalam penerapan algoritma *ensemble learning* teroptimasi Bayesian pada domain analisis olahraga (*sports analytics*).
