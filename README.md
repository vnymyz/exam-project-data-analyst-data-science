# Exam Project — Data Analyst Bootcamp

## Tentang Exam Ini

Ini adalah exam akhir untuk materi **Data Analyst** yang sudah kamu pelajari, meliputi:
- Data Understanding
- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Data Storytelling
- Streamlit Dashboard

---

## Dataset

Dataset yang digunakan adalah **Brazilian E-Commerce Public Dataset** dari perusahaan e-commerce Brasil bernama **Olist**.

**Sumber:** [Kaggle — Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

Dataset ini berisi data transaksi e-commerce nyata dari Brasil tahun 2016–2018, mencakup informasi pesanan, produk, dan pelanggan.

File yang digunakan dalam exam ini:

| File | Keterangan |
|------|------------|
| `dataset/orders.csv` | Data pesanan (status, tanggal, customer) |
| `dataset/order_items.csv` | Detail item per pesanan (harga, ongkir) |
| `dataset/products.csv` | Informasi produk (kategori, berat, dimensi) |

---

## Struktur Folder

```
Exam-DataAnalyst/
├── dataset/
│   ├── orders.csv
│   ├── order_items.csv
│   └── products.csv
├── exam_notebook.ipynb   ← kerjakan di sini
├── app.py                ← buat Streamlit dashboard di sini
└── README.md
```

---

## Cara Mengerjakan

1. Buka `exam_notebook.ipynb` di Jupyter Notebook atau VS Code
2. Kerjakan setiap section secara berurutan
3. **Wajib mengisi semua bagian `Jawab di sini`** — bagian ini yang paling dinilai
4. Setelah notebook selesai, kerjakan `app.py` untuk membuat Streamlit dashboard
5. Jalankan dashboard dengan perintah di Terminal:
   ```
   streamlit run app.py
   ```

---

## Yang Dinilai

| Section | Bobot |
|---------|-------|
| Data Understanding | 10% |
| Data Cleaning & Merge | 20% |
| EDA (visualisasi + operasi Pandas) | 25% |
| Data Storytelling & Insight | 35% |
| Streamlit Dashboard | 10% |

> Kode boleh dibantu AI. Yang dinilai adalah **pemahaman dan insight kamu sendiri** — tulis dengan kata-katamu sendiri di setiap bagian jawaban.
