# Documentation Dataset Top 5 Liga Eropa Musim 2025/2026

## Deskripsi Dataset
Dataset ini berisi data statistik pertandingan dari Top 5 Liga Utama Eropa (Premier League, La Liga, Bundesliga, Serie A, Ligue 1) musim 2025/2026.

- **Lokasi File:** `data/data_top_5_liga.csv`
- **Jumlah Sampel:** 1.752 pertandingan
- **Format Delimiter:** Titik Koma (`;`)

## Atribut & Fitur Dataset (22 Kolom)

| No | Nama Atribut | Tipe Data | Deskripsi / Keterangan |
|---|---|---|---|
| 1 | `Date` | String | Tanggal Pertandingan (DD/MM/YYYY) |
| 2 | `HomeTeam` | String | Nama Tim Tuan Rumah (Home) |
| 3 | `AwayTeam` | String | Nama Tim Tamu (Away) |
| 4 | `FTHG` | Integer | Full Time Home Goals (Gol Akhir Tuan Rumah) |
| 5 | `FTAG` | Integer | Full Time Away Goals (Gol Akhir Tim Tamu) |
| 6 | `FTR` | Categorical | **Target Label (Full Time Result):**<br>`H` = Home Win (Tuan Rumah Menang)<br>`D` = Draw (Seri)<br>`A` = Away Win (Tim Tamu Menang) |
| 7 | `HTHG` | Integer | Half Time Home Goals (Gol Babak Pertama Tuan Rumah) |
| 8 | `HTAG` | Integer | Half Time Away Goals (Gol Babak Pertama Tim Tamu) |
| 9 | `HTR` | Categorical | Half Time Result (Hasil Babak Pertama) |
| 10 | `Referee` | String | Nama Wasit Pertandingan |
| 11 | `HS` | Integer | Home Shots (Total Tembakan Tuan Rumah) |
| 12 | `AS` | Integer | Away Shots (Total Tembakan Tim Tamu) |
| 13 | `HST` | Integer | Home Shots on Target (Tembakan Akurat Tuan Rumah) |
| 14 | `AST` | Integer | Away Shots on Target (Tembakan Akurat Tim Tamu) |
| 15 | `HF` | Integer | Home Fouls (Pelanggaran Tuan Rumah) |
| 16 | `AF` | Integer | Away Fouls (Pelanggaran Tim Tamu) |
| 17 | `HC` | Integer | Home Corners (Tendangan Sudut Tuan Rumah) |
| 18 | `AC` | Integer | Away Corners (Tendangan Sudut Tim Tamu) |
| 19 | `HY` | Integer | Home Yellow Cards (Kartu Kuning Tuan Rumah) |
| 20 | `AY` | Integer | Away Yellow Cards (Kartu Kuning Tim Tamu) |
| 21 | `HR` | Integer | Home Red Cards (Kartu Merah Tuan Rumah) |
| 22 | `AR` | Integer | Away Red Cards (Kartu Merah Tim Tamu) |
