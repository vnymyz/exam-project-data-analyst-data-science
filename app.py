import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# INSTRUKSI DASHBOARD
# ============================================================
# Buat dashboard sederhana yang menampilkan:
#
# 1. JUDUL & DESKRIPSI
#    - Judul dashboard
#    - Penjelasan singkat dataset ini tentang apa
#
# 2. SIDEBAR FILTER
#    - Filter berdasarkan kategori produk (multiselect)
#    - Filter berdasarkan status pesanan (multiselect)
#    - Gunakan: st.sidebar.multiselect()
#
# 3. METRIC (minimal 1, boleh lebih)
#    - Contoh: total pesanan, total revenue, rata-rata harga
#    - Gunakan: st.metric()
#    - Tip: tampilkan dalam beberapa kolom pakai st.columns()
#
# 4. CHART (minimal 2, harus berubah sesuai filter)
#    - Chart 1: bebas pilihanmu (contoh: bar chart top kategori)
#    - Chart 2: bebas pilihanmu (contoh: line chart tren per bulan)
#    - Gunakan matplotlib/seaborn lalu tampilkan dengan st.pyplot()
#
# ============================================================
# CARA MENJALANKAN (di Terminal Mac / zsh):
#   streamlit run app.py
# ============================================================


# ---- PAGE CONFIG ----
# Tip: st.set_page_config() harus dipanggil paling pertama sebelum kode lain
st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")


# ---- LOAD DATA ----
# Tip: gunakan @st.cache_data supaya data tidak di-reload setiap ada interaksi
@st.cache_data
def load_data():
    orders = pd.read_csv('dataset/orders.csv')
    order_items = pd.read_csv('dataset/order_items.csv')
    products = pd.read_csv('dataset/products.csv')

    # Lanjutkan: konversi tanggal, handle missing values, merge ketiga tabel
    # (sama seperti yang kamu lakukan di notebook)

    return df  # ganti dengan nama dataframe hasil merge kamu

df = load_data()


# ---- JUDUL ----
# Tulis judul dan deskripsi dashboard kamu di sini


# ---- SIDEBAR FILTER ----
st.sidebar.header("Filter Data")

# Tulis filter kategori dan status pesanan di sini
# Tip: filtered_df = df[df['kolom'].isin(pilihan)]


# ---- METRIC ----
# Tulis metric kamu di sini
# Tip: col1, col2, col3 = st.columns(3)
#      with col1: st.metric("Label", value)


# ---- CHART 1 ----
st.subheader("Tulis judul chart 1 kamu")

# Tulis kode chart pertama kamu di sini
# Tip: fig, ax = plt.subplots()
#      ... buat chart ...
#      st.pyplot(fig)


# ---- CHART 2 ----
st.subheader("Tulis judul chart 2 kamu")

# Tulis kode chart kedua kamu di sini
