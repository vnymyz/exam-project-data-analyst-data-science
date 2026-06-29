import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import numpy as np

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Olist E-Commerce Dashboard",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---- CUSTOM CSS ----
st.markdown("""
<style>
    .main { background-color: #f8f9fb; }

    [data-testid="metric-container"] {
        background-color: #ffffff;
        border: 1px solid #e0e4ea;
        border-radius: 12px;
        padding: 16px 20px;
        box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    }
    [data-testid="metric-container"] label {
        font-size: 13px !important;
        color: #6b7280 !important;
        font-weight: 500;
    }
    [data-testid="metric-container"] [data-testid="stMetricValue"] {
        font-size: 24px !important;
        font-weight: 700;
        color: #111827;
    }

    .insight-box {
        background-color: #eff6ff;
        border-left: 4px solid #2563eb;
        border-radius: 6px;
        padding: 10px 14px;
        margin-top: 8px;
        font-size: 13px;
        color: #1e40af;
    }

    hr { border-color: #e5e7eb; margin: 8px 0; }
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ---- LOAD DATA ----
@st.cache_data
def load_data():
    orders = pd.read_csv('../dataset/orders.csv')
    order_items = pd.read_csv('../dataset/order_items.csv')
    products = pd.read_csv('../dataset/products.csv')

    orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
    orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])
    orders['order_estimated_delivery_date'] = pd.to_datetime(orders['order_estimated_delivery_date'])
    products['product_category_name'] = products['product_category_name'].fillna('Unknown')

    df = pd.merge(orders, order_items, on='order_id', how='left')
    df = pd.merge(df, products[['product_id', 'product_category_name']], on='product_id', how='left')
    df = df.dropna(subset=['price', 'freight_value', 'product_id'])

    df['order_month'] = df['order_purchase_timestamp'].dt.to_period('M').astype(str)
    df['order_year'] = df['order_purchase_timestamp'].dt.year
    df['month_only'] = df['order_purchase_timestamp'].dt.month
    df['day_of_week'] = df['order_purchase_timestamp'].dt.day_name()

    # Delivery performance
    delivered_mask = df['order_delivered_customer_date'].notna() & df['order_estimated_delivery_date'].notna()
    df.loc[delivered_mask, 'delivery_delay_days'] = (
        df.loc[delivered_mask, 'order_delivered_customer_date'] -
        df.loc[delivered_mask, 'order_estimated_delivery_date']
    ).dt.days
    df.loc[delivered_mask, 'on_time'] = df.loc[delivered_mask, 'delivery_delay_days'] <= 0

    # Freight efficiency ratio
    df['freight_ratio'] = df['freight_value'] / df['price']

    return df

df = load_data()

# ---- COLORS ----
PRIMARY   = '#2563eb'
SECONDARY = '#7c3aed'
SUCCESS   = '#16a34a'
DANGER    = '#dc2626'
GRAY      = '#6b7280'
PALETTE   = ['#2563eb', '#7c3aed', '#db2777', '#ea580c', '#16a34a',
             '#0891b2', '#ca8a04', '#9333ea', '#e11d48', '#0284c7']

def insight(text):
    st.markdown(f'<div class="insight-box">💡 {text}</div>', unsafe_allow_html=True)

# ---- SIDEBAR ----
with st.sidebar:
    st.markdown("## 📦 Olist Dashboard")
    st.markdown("*Brazilian E-Commerce Analytics*")
    st.markdown("---")
    st.markdown("### Filters")

    all_periods = sorted(df['order_month'].dropna().unique().tolist())
    period_start, period_end = st.select_slider(
        "Rentang Periode",
        options=all_periods,
        value=(all_periods[0], all_periods[-1])
    )

    all_status = sorted(df['order_status'].unique().tolist())
    selected_status = st.multiselect("Status Pesanan", options=all_status, default=all_status)

    all_categories = sorted(df['product_category_name'].dropna().unique().tolist())
    selected_categories = st.multiselect(
        "Kategori Produk",
        options=all_categories,
        default=all_categories[:15]
    )

    st.markdown("---")
    st.caption("Data: Olist Brazilian E-Commerce")
    st.caption("Kaggle · 2016–2018")

# ---- FILTER ----
filtered_df = df[
    (df['order_month'] >= period_start) &
    (df['order_month'] <= period_end) &
    (df['order_status'].isin(selected_status)) &
    (df['product_category_name'].isin(selected_categories))
]

# ---- HEADER ----
st.markdown("## 📊 E-Commerce Sales Dashboard")
st.markdown("Analisis performa penjualan platform **Olist** berdasarkan data transaksi Brasil 2016–2018.")
st.markdown("---")

# ---- KPI METRICS ----
total_orders  = filtered_df['order_id'].nunique()
total_revenue = filtered_df['price'].sum()
avg_price     = filtered_df['price'].mean()
avg_freight   = filtered_df['freight_value'].mean()
delivered_df  = df[df['order_status'] == 'delivered']
delivery_rate = (delivered_df['order_id'].nunique() / df['order_id'].nunique() * 100)
on_time_rate  = (delivered_df['on_time'].sum() / delivered_df['on_time'].notna().sum() * 100)

col1, col2, col3, col4, col5, col6 = st.columns(6)
col1.metric("Total Pesanan",    f"{total_orders:,}")
col2.metric("Total Revenue",    f"BRL {total_revenue:,.0f}")
col3.metric("Rata-rata Harga",  f"BRL {avg_price:,.2f}")
col4.metric("Rata-rata Ongkir", f"BRL {avg_freight:,.2f}")
col5.metric("Delivery Rate",    f"{delivery_rate:.1f}%")
col6.metric("On-Time Rate",     f"{on_time_rate:.1f}%")

st.markdown("<br>", unsafe_allow_html=True)

# ============================================================
# ROW 1: TOP KATEGORI + STATUS PESANAN
# ============================================================
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("Top 10 Kategori Berdasarkan Revenue")

    revenue_cat = (
        filtered_df.groupby('product_category_name')['price']
        .sum().sort_values(ascending=True).tail(10)
    )

    fig, ax = plt.subplots(figsize=(9, 5))
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')

    bars = ax.barh(revenue_cat.index, revenue_cat.values, color=PRIMARY, edgecolor='none', height=0.6)
    for bar in bars:
        width = bar.get_width()
        ax.text(width + revenue_cat.max() * 0.01, bar.get_y() + bar.get_height() / 2,
                f'BRL {width:,.0f}', va='center', ha='left', fontsize=8, color=GRAY)

    ax.set_xlabel('Total Revenue (BRL)', fontsize=10, color=GRAY)
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x/1e6:.1f}M'))
    ax.tick_params(colors=GRAY, labelsize=9)
    ax.spines[['top', 'right', 'left']].set_visible(False)
    ax.spines['bottom'].set_color('#e5e7eb')
    ax.grid(axis='x', linestyle='--', alpha=0.7, color='#d1d5db')
    ax.set_axisbelow(True)
    ax.set_title('Top 10 Kategori Produk', fontsize=13, fontweight='bold', color='#111827', pad=12)

    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    top1 = revenue_cat.index[-1]
    top1_rev = revenue_cat.values[-1]
    insight(f"Kategori <b>{top1}</b> memimpin dengan total revenue BRL {top1_rev:,.0f}. "
            f"Produk kebutuhan rumah tangga dan gaya hidup mendominasi penjualan platform ini.")

with col_right:
    st.subheader("Distribusi Status Pesanan")

    # Hanya tampilkan status yang ada di filtered_df, buang yang 0
    status_counts = filtered_df['order_status'].value_counts()
    status_counts = status_counts[status_counts > 0]

    fig2, ax2 = plt.subplots(figsize=(4, 5))
    fig2.patch.set_facecolor('#ffffff')
    ax2.set_facecolor('#ffffff')

    wedges, texts, autotexts = ax2.pie(
        status_counts.values,
        labels=None,
        autopct=lambda p: f'{p:.1f}%' if p > 1 else '',
        startangle=90,
        colors=PALETTE[:len(status_counts)],
        pctdistance=0.6,
        wedgeprops=dict(edgecolor='white', linewidth=2)
    )
    for at in autotexts:
        at.set_fontsize(9)
        at.set_color('white')
        at.set_fontweight('bold')

    # Legend dengan label + jumlah
    legend_labels = [f"{s}  ({v:,})" for s, v in zip(status_counts.index, status_counts.values)]
    ax2.legend(wedges, legend_labels, loc='lower center',
               bbox_to_anchor=(0.5, -0.22), ncol=1, fontsize=8, frameon=False)
    ax2.set_title('Status Pesanan', fontsize=13, fontweight='bold', color='#111827', pad=12)

    plt.tight_layout()
    st.pyplot(fig2)
    plt.close()

    delivered_pct = status_counts.get('delivered', 0) / status_counts.sum() * 100
    canceled_pct  = status_counts.get('canceled', 0) / status_counts.sum() * 100
    insight(f"<b>{delivered_pct:.1f}%</b> pesanan berhasil delivered. "
            f"Cancellation rate hanya <b>{canceled_pct:.1f}%</b> — performa fulfillment sangat baik.")

st.markdown("---")

# ============================================================
# ROW 2: TREN BULANAN
# ============================================================
st.subheader("Tren Jumlah Pesanan & Revenue per Bulan")

monthly = (
    filtered_df.groupby('order_month')
    .agg(total_orders=('order_id', 'nunique'), total_revenue=('price', 'sum'))
    .reset_index().sort_values('order_month')
)

fig3, ax3 = plt.subplots(figsize=(14, 4))
fig3.patch.set_facecolor('#ffffff')
ax3.set_facecolor('#ffffff')
ax3b = ax3.twinx()

ax3.fill_between(monthly['order_month'], monthly['total_orders'], alpha=0.15, color=PRIMARY)
ax3.plot(monthly['order_month'], monthly['total_orders'],
         color=PRIMARY, linewidth=2.5, marker='o', markersize=4, label='Jumlah Pesanan')
ax3b.plot(monthly['order_month'], monthly['total_revenue'],
          color=SECONDARY, linewidth=2, linestyle='--', marker='s', markersize=3, label='Revenue (BRL)')

ax3.set_ylabel('Jumlah Pesanan', color=PRIMARY, fontsize=10)
ax3b.set_ylabel('Revenue (BRL)', color=SECONDARY, fontsize=10)
ax3b.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x/1e6:.1f}M'))
ax3.tick_params(axis='x', rotation=45, labelsize=8, colors=GRAY)
ax3.tick_params(axis='y', colors=PRIMARY)
ax3b.tick_params(axis='y', colors=SECONDARY)
ax3.spines[['top', 'right']].set_visible(False)
ax3b.spines[['top']].set_visible(False)
ax3.spines['bottom'].set_color('#e5e7eb')
ax3.spines['left'].set_color('#e5e7eb')
ax3.grid(axis='both', linestyle='--', alpha=0.6, color='#d1d5db')
ax3.set_axisbelow(True)

lines1, labels1 = ax3.get_legend_handles_labels()
lines2, labels2 = ax3b.get_legend_handles_labels()
ax3.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=9, frameon=False)
ax3.set_title('Tren Bulanan — Pesanan & Revenue', fontsize=13, fontweight='bold', color='#111827', pad=12)

plt.tight_layout()
st.pyplot(fig3)
plt.close()

peak_month = monthly.loc[monthly['total_orders'].idxmax(), 'order_month']
peak_orders = monthly['total_orders'].max()
insight(f"Puncak penjualan terjadi di <b>{peak_month}</b> dengan <b>{peak_orders:,} pesanan</b>. "
        f"Lonjakan ini kemungkinan besar dipicu oleh event belanja besar seperti Black Friday. "
        f"Tren keseluruhan menunjukkan pertumbuhan positif sepanjang periode.")

st.markdown("---")

# ============================================================
# ROW 3: DELIVERY PERFORMANCE + FREIGHT EFFICIENCY
# ============================================================
col_d, col_f = st.columns(2)

with col_d:
    st.subheader("Performa Pengiriman — On-Time vs Terlambat")

    del_df = df[df['order_status'] == 'delivered'].dropna(subset=['delivery_delay_days'])
    on_time_count = (del_df['delivery_delay_days'] <= 0).sum()
    late_count = (del_df['delivery_delay_days'] > 0).sum()
    avg_delay = del_df[del_df['delivery_delay_days'] > 0]['delivery_delay_days'].mean()

    # Bar chart on-time vs late
    fig_d, ax_d = plt.subplots(figsize=(6, 4))
    fig_d.patch.set_facecolor('#ffffff')
    ax_d.set_facecolor('#ffffff')

    labels_d = ['On-Time / Lebih Cepat', 'Terlambat']
    values_d = [on_time_count, late_count]
    colors_d = [SUCCESS, DANGER]

    bars_d = ax_d.bar(labels_d, values_d, color=colors_d, edgecolor='none', width=0.5)
    for bar in bars_d:
        h = bar.get_height()
        ax_d.text(bar.get_x() + bar.get_width() / 2, h + 200,
                  f'{h:,}\n({h/sum(values_d)*100:.1f}%)',
                  ha='center', va='bottom', fontsize=10, fontweight='bold')

    ax_d.set_ylabel('Jumlah Pesanan', fontsize=9, color=GRAY)
    ax_d.tick_params(colors=GRAY, labelsize=10)
    ax_d.spines[['top', 'right', 'left']].set_visible(False)
    ax_d.spines['bottom'].set_color('#e5e7eb')
    ax_d.grid(axis='y', linestyle='--', alpha=0.6, color='#d1d5db')
    ax_d.set_axisbelow(True)
    ax_d.set_title('On-Time vs Terlambat', fontsize=12, fontweight='bold', color='#111827', pad=10)
    ax_d.set_ylim(0, max(values_d) * 1.15)

    plt.tight_layout()
    st.pyplot(fig_d)
    plt.close()

    insight(f"<b>{on_time_count:,} pesanan ({on_time_count/sum(values_d)*100:.1f}%)</b> tiba tepat waktu atau lebih cepat. "
            f"Untuk yang terlambat, rata-rata keterlambatan adalah <b>{avg_delay:.1f} hari</b>. "
            f"Perlu investigasi seller atau wilayah mana yang paling sering terlambat.")

with col_f:
    st.subheader("Freight Efficiency Ratio per Kategori")

    top10 = (
        df.groupby('product_category_name')['price']
        .sum().sort_values(ascending=False).head(10).index.tolist()
    )

    freight_eff = (
        filtered_df[filtered_df['product_category_name'].isin(top10)]
        .groupby('product_category_name')['freight_ratio']
        .mean()
        .sort_values(ascending=True)
    )

    fig_f, ax_f = plt.subplots(figsize=(6, 4))
    fig_f.patch.set_facecolor('#ffffff')
    ax_f.set_facecolor('#ffffff')

    bar_colors = [DANGER if v > 0.3 else SUCCESS if v < 0.15 else '#f97316'
                  for v in freight_eff.values]

    ax_f.barh(freight_eff.index, freight_eff.values * 100,
              color=bar_colors, edgecolor='none', height=0.6)
    ax_f.axvline(x=30, color=DANGER, linestyle='--', linewidth=1.5, alpha=0.7, label='Threshold 30%')
    ax_f.axvline(x=15, color=SUCCESS, linestyle='--', linewidth=1.5, alpha=0.7, label='Efisien <15%')

    ax_f.set_xlabel('Freight Ratio (%)', fontsize=9, color=GRAY)
    ax_f.tick_params(colors=GRAY, labelsize=8)
    ax_f.spines[['top', 'right', 'left']].set_visible(False)
    ax_f.spines['bottom'].set_color('#e5e7eb')
    ax_f.grid(axis='x', linestyle='--', alpha=0.7, color='#d1d5db')
    ax_f.set_axisbelow(True)
    ax_f.legend(fontsize=8, frameon=False)
    ax_f.set_title('Rasio Ongkir / Harga per Kategori', fontsize=12,
                   fontweight='bold', color='#111827', pad=10)

    plt.tight_layout()
    st.pyplot(fig_f)
    plt.close()

    worst_cat = freight_eff.index[-1]
    worst_ratio = freight_eff.values[-1] * 100
    best_cat = freight_eff.index[0]
    best_ratio = freight_eff.values[0] * 100
    insight(f"Kategori <b>{worst_cat}</b> paling tidak efisien — ongkir mencapai <b>{worst_ratio:.1f}%</b> dari harga produk. "
            f"Sebaliknya, <b>{best_cat}</b> paling efisien dengan rasio hanya <b>{best_ratio:.1f}%</b>. "
            f"Kategori merah (>30%) perlu evaluasi strategi pengiriman.")

st.markdown("---")

# ============================================================
# ROW 4: HARGA VS FREIGHT + HEATMAP
# ============================================================
col3a, col3b = st.columns(2)

with col3a:
    st.subheader("Rata-rata Harga vs Ongkir per Kategori")

    price_freight = (
        filtered_df[filtered_df['product_category_name'].isin(top10)]
        .groupby('product_category_name')[['price', 'freight_value']]
        .mean().sort_values('price', ascending=True)
    )

    fig4, ax4 = plt.subplots(figsize=(7, 5))
    fig4.patch.set_facecolor('#ffffff')
    ax4.set_facecolor('#ffffff')

    x = range(len(price_freight))
    w = 0.35
    ax4.barh([i + w/2 for i in x], price_freight['price'],
             height=w, color=PRIMARY, label='Harga Produk', edgecolor='none')
    ax4.barh([i - w/2 for i in x], price_freight['freight_value'],
             height=w, color='#f97316', label='Ongkos Kirim', edgecolor='none')

    ax4.set_yticks(list(x))
    ax4.set_yticklabels(price_freight.index, fontsize=8)
    ax4.set_xlabel('Nilai Rata-rata (BRL)', fontsize=9, color=GRAY)
    ax4.legend(fontsize=9, frameon=False)
    ax4.spines[['top', 'right', 'left']].set_visible(False)
    ax4.spines['bottom'].set_color('#e5e7eb')
    ax4.grid(axis='x', linestyle='--', alpha=0.7, color='#d1d5db')
    ax4.set_axisbelow(True)
    ax4.tick_params(colors=GRAY, labelsize=8)
    ax4.set_title('Harga vs Freight — Top 10 Kategori', fontsize=12,
                  fontweight='bold', color='#111827', pad=10)

    plt.tight_layout()
    st.pyplot(fig4)
    plt.close()

    high_price_cat = price_freight['price'].idxmax()
    insight(f"Kategori <b>{high_price_cat}</b> memiliki rata-rata harga tertinggi. "
            f"Perhatikan bahwa ongkos kirim relatif kecil dibanding harga — margin seller lebih sehat di kategori ini.")

with col3b:
    st.subheader("Revenue per Kategori per Bulan (Heatmap)")

    pivot_df = filtered_df[filtered_df['product_category_name'].isin(top10[:8])]
    pivot = pd.pivot_table(
        pivot_df, values='price',
        index='product_category_name', columns='month_only',
        aggfunc='sum', fill_value=0
    )

    fig5, ax5 = plt.subplots(figsize=(7, 5))
    fig5.patch.set_facecolor('#ffffff')
    ax5.set_facecolor('#ffffff')

    sns.heatmap(pivot / 1000, annot=True, fmt='.0f', cmap='Blues',
                linewidths=0.5, linecolor='#f1f5f9',
                cbar_kws={'label': 'Revenue (ribu BRL)', 'shrink': 0.8}, ax=ax5)

    ax5.set_xlabel('Bulan', fontsize=9, color=GRAY)
    ax5.set_ylabel('')
    ax5.tick_params(colors=GRAY, labelsize=8)
    ax5.set_title('Heatmap Revenue (ribu BRL)', fontsize=12,
                  fontweight='bold', color='#111827', pad=10)

    plt.tight_layout()
    st.pyplot(fig5)
    plt.close()

    insight("Warna lebih gelap = revenue lebih tinggi. "
            "Perhatikan pola musiman — bulan tertentu konsisten tinggi di hampir semua kategori, "
            "menandakan ada event atau musim belanja yang berulang setiap tahun.")

# ---- FOOTER ----
st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:#9ca3af; font-size:12px;'>"
    "Data: Brazilian E-Commerce Public Dataset by Olist · Kaggle · 2016–2018"
    "</div>",
    unsafe_allow_html=True
)
