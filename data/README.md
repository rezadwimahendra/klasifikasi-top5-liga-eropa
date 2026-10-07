# UCI Heart Disease Dataset Documentation

## Deskripsi Dataset
Dataset ini berisi data klinis pasien untuk memprediksi risiko penyakit jantung (*Heart Disease Risk Prediction*). Dataset ini diadaptasi dari UCI Machine Learning Repository (Cleveland Heart Disease Database).

## Fitur & Atribut (14 Kolom)

| No | Nama Atribut | Tipe Data | Deskripsi / Keterangan |
|---|---|---|---|
| 1 | `age` | Integer | Usia pasien (tahun) |
| 2 | `sex` | Categorical | Jenis kelamin (1 = Laki-laki, 0 = Perempuan) |
| 3 | `cp` | Categorical | Tipe nyeri dada (*Chest Pain Type*):<br>0: Typical angina<br>1: Atypical angina<br>2: Non-anginal pain<br>3: Asymptomatic |
| 4 | `trestbps` | Integer | Tekanan darah istirahat dalam mmHg (*Resting Blood Pressure*) |
| 5 | `chol` | Integer | Kadar kolesterol serum dalam mg/dl |
| 6 | `fbs` | Categorical | Gula darah puasa > 120 mg/dl (1 = ya, 0 = tidak) |
| 7 | `restecg` | Categorical | Hasil elektrokardiografi istirahat (0, 1, 2) |
| 8 | `thalach` | Integer | Detak jantung maksimum yang dicapai (*Maximum Heart Rate*) |
| 9 | `exang` | Categorical | Angina akibat olahraga / *exercise induced angina* (1 = ya, 0 = tidak) |
| 10 | `oldpeak` | Float | Depresi ST yang diinduksi oleh latihan relatif terhadap istirahat |
| 11 | `slope` | Categorical | Kemiringan puncak segmen ST latihan (0, 1, 2) |
| 12 | `ca` | Integer | Jumlah pembuluh darah utama (0-4) yang diwarnai dengan fluoroskopi |
| 13 | `thal` | Categorical | Jenis talasemia (1 = normal, 2 = fixed defect, 3 = reversible defect) |
| 14 | `target` | Binary | Variabel Target / Label:<br>0 = Tidak Terdeteksi Penyakit Jantung (Sehat)<br>1 = Terdeteksi Penyakit Jantung |

## Ringkasan Distribusi Data
- Total Sampel: 303 responden
- Kelas 0 (Sehat): 152 pasien (50.17%)
- Kelas 1 (Penyakit Jantung): 151 pasien (49.83%)
