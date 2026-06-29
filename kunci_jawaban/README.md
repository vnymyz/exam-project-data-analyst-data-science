# Panduan Hasil & Data Storytelling

### Exam Project — Brazilian E-Commerce (Olist)

---

## Dataset Ini Tentang Apa?

Data ini berasal dari **Olist**, platform e-commerce terbesar di Brasil. Isinya adalah catatan transaksi nyata dari tahun **2016 sampai 2018** — mulai dari pesanan masuk, produk apa yang dibeli, berapa harganya, sampai kapan pesanan sampai ke pelanggan.

Kita pakai 3 tabel:

- **orders** — kapan pesanan dibuat dan statusnya
- **order_items** — produk apa, berapa harga dan ongkirnya
- **products** — kategori produk

---

## Temuan Utama Per Visualisasi

### 1. Top 10 Kategori Berdasarkan Revenue

**Apa yang dilihat:** Kategori produk mana yang menghasilkan uang paling banyak.

**Kesimpulan:**
Produk rumah tangga seperti kasur, seprai, dan peralatan mandi (**cama_mesa_banho**) selalu di posisi teratas. Bukan karena harganya paling mahal, tapi karena **paling banyak orang yang beli**. Orang Brasil beli kebutuhan rumah tangga secara online sama seperti kita beli di marketplace lokal.

---

### 2. Distribusi Status Pesanan

**Apa yang dilihat:** Dari semua pesanan, berapa yang berhasil sampai, berapa yang dibatalkan, dll.

**Kesimpulan:**
Lebih dari **96% pesanan berhasil delivered** — angka yang sangat bagus untuk ukuran platform e-commerce. Artinya sistem logistik Olist bekerja dengan baik. Tingkat pembatalan hanya sekitar 0.6%, sangat kecil.

---

### 3. Tren Pesanan per Bulan

**Apa yang dilihat:** Naik turunnya jumlah pesanan dari bulan ke bulan.

**Kesimpulan:**
Ada **lonjakan besar di November 2017** — ini bukan kebetulan. Brasil punya **Black Friday** yang jatuh di bulan November, dan data membuktikan dampaknya sangat besar terhadap penjualan. Secara keseluruhan tren terus naik dari 2016 ke 2018, artinya bisnis tumbuh sehat.

---

### 4. Performa Pengiriman — On-Time vs Terlambat

**Apa yang dilihat:** Berapa pesanan yang sampai tepat waktu vs terlambat dari estimasi.

**Kesimpulan:**
Sekitar **90%+ pesanan tiba tepat waktu atau lebih cepat dari estimasi**. Tapi untuk yang terlambat, rata-rata keterlambatannya beberapa hari. Ini penting karena keterlambatan pengiriman adalah penyebab utama komplain pelanggan dan bintang rendah di ulasan.

---

### 5. Freight Efficiency Ratio

**Apa yang dilihat:** Seberapa besar ongkos kirim dibanding harga produk — dalam persen.

**Kenapa penting ditampilkan:**
Bayangkan kamu beli produk seharga Rp 100.000 tapi ongkirnya Rp 40.000. Itu 40% dari harga produk habis buat ongkir — kemungkinan besar kamu tidak jadi beli. Inilah yang disebut Freight Efficiency Ratio: **ongkir dibagi harga produk, dikalikan 100%**.

Visualisasi ini penting karena:

- Membantu platform tahu **kategori mana yang bikin pelanggan kabur** karena ongkir terlalu mahal relatif terhadap harganya
- Membantu seller evaluasi apakah produk mereka **layak dijual online** atau lebih cocok dijual offline
- Warna **merah (>30%)** = perlu perhatian, **hijau (<15%)** = sehat, **oranye (15-30%)** = masih oke tapi perlu diawasi

**Kesimpulan:**
Produk besar dan berat (furnitur, konstruksi) punya rasio tinggi — wajar tapi tetap jadi hambatan penjualan. Produk kecantikan, fashion, dan aksesoris punya rasio rendah — paling ideal dijual online karena ongkirnya ringan relatif terhadap harganya.

---

### 6. Harga vs Ongkir per Kategori

**Apa yang dilihat:** Perbandingan rata-rata harga produk dengan rata-rata ongkos kirimnya.

**Kesimpulan:**
Kategori dengan harga tinggi tapi ongkir rendah = **paling menguntungkan untuk seller**. Sebaliknya, produk murah dengan ongkir mahal = seller rugi atau margin sangat tipis.

---

### 7. Heatmap Revenue per Kategori per Bulan

**Apa yang dilihat:** Di bulan mana setiap kategori paling ramai.

**Kesimpulan:**
Warna gelap = penjualan tinggi. Hampir semua kategori ramai di **bulan 8 (Agustus) dan 11 (November)**. Ini pola musiman yang berulang setiap tahun — bisa dimanfaatkan untuk perencanaan stok dan promosi.

---

## Cerita Besarnya (Data Storytelling)

Kalau semua temuan di atas digabungkan, ceritanya seperti ini:

> Olist adalah platform e-commerce yang **sedang tumbuh dengan sehat**. Penjualan naik konsisten dari 2016 ke 2018, dipimpin oleh kategori produk rumah tangga yang punya permintaan stabil sepanjang tahun. Sistem pengiriman mereka bekerja sangat baik — 96% pesanan sampai ke pelanggan.
>
> Peluang terbesar ada di **event musiman** seperti Black Friday — lonjakan penjualan sangat signifikan dan bisa diprediksi. Platform perlu siap dari sisi stok dan logistik jauh sebelum November.
>
> Tantangan utama adalah **efisiensi ongkos kirim** di kategori produk besar. Seller di kategori furnitur atau elektronik berat perlu strategi pengiriman yang lebih baik agar harga tetap kompetitif untuk pelanggan.

---

## 3 Rekomendasi Bisnis

1. **Fokus promosi di kategori teratas** (rumah tangga, olahraga, kecantikan) — volume tinggi, margin stabil
2. **Siapkan kampanye Black Friday dari jauh-jauh hari** — data membuktikan November selalu meledak
3. **Bantu seller kategori furnitur** negosiasi tarif pengiriman lebih murah — freight ratio mereka terlalu tinggi dan bisa menurunkan konversi

---

---

## Terjemahan Nama Kategori Produk (Portugis → Indonesia)

Semua nama kategori di dataset aslinya dalam Bahasa Portugis. Ini terjemahannya:

| Nama di Dataset                                | Terjemahan                         |
| ---------------------------------------------- | ---------------------------------- |
| agro_industria_e_comercio                      | Pertanian, Industri & Perdagangan  |
| alimentos                                      | Makanan                            |
| alimentos_bebidas                              | Makanan & Minuman                  |
| artes                                          | Seni                               |
| artes_e_artesanato                             | Seni & Kerajinan Tangan            |
| artigos_de_festas                              | Perlengkapan Pesta                 |
| artigos_de_natal                               | Dekorasi Natal                     |
| audio                                          | Audio & Speaker                    |
| automotivo                                     | Otomotif & Aksesoris Kendaraan     |
| bebes                                          | Perlengkapan Bayi                  |
| bebidas                                        | Minuman                            |
| beleza_saude                                   | Kecantikan & Kesehatan             |
| brinquedos                                     | Mainan Anak                        |
| cama_mesa_banho                                | Kasur, Meja & Perlengkapan Mandi   |
| casa_conforto                                  | Kenyamanan Rumah                   |
| casa_conforto_2                                | Kenyamanan Rumah (Lainnya)         |
| casa_construcao                                | Material Bangunan Rumah            |
| cds_dvds_musicais                              | CD & DVD Musik                     |
| cine_foto                                      | Kamera & Fotografi                 |
| climatizacao                                   | AC & Pendingin Ruangan             |
| consoles_games                                 | Konsol & Game                      |
| construcao_ferramentas_construcao              | Alat Bangunan & Konstruksi         |
| construcao_ferramentas_ferramentas             | Perkakas & Alat Kerja              |
| construcao_ferramentas_iluminacao              | Lampu & Pencahayaan                |
| construcao_ferramentas_jardim                  | Alat Berkebun                      |
| construcao_ferramentas_seguranca               | Keamanan & Alat Keselamatan        |
| cool_stuff                                     | Produk Unik & Keren                |
| dvds_blu_ray                                   | DVD & Blu-Ray                      |
| eletrodomesticos                               | Peralatan Rumah Tangga Besar       |
| eletrodomesticos_2                             | Peralatan Rumah Tangga (Lainnya)   |
| eletronicos                                    | Elektronik                         |
| eletroportateis                                | Elektronik Portabel                |
| esporte_lazer                                  | Olahraga & Rekreasi                |
| fashion_bolsas_e_acessorios                    | Tas & Aksesoris Fashion            |
| fashion_calcados                               | Sepatu & Alas Kaki                 |
| fashion_esporte                                | Pakaian Olahraga                   |
| fashion_roupa_feminina                         | Pakaian Wanita                     |
| fashion_roupa_infanto_juvenil                  | Pakaian Anak & Remaja              |
| fashion_roupa_masculina                        | Pakaian Pria                       |
| fashion_underwear_e_moda_praia                 | Pakaian Dalam & Busana Pantai      |
| ferramentas_jardim                             | Alat Taman                         |
| flores                                         | Bunga                              |
| fraldas_higiene                                | Popok & Kebersihan Bayi            |
| industria_comercio_e_negocios                  | Industri, Komersial & Bisnis       |
| informatica_acessorios                         | Komputer & Aksesoris               |
| instrumentos_musicais                          | Alat Musik                         |
| la_cuisine                                     | Peralatan Masak & Dapur            |
| livros_importados                              | Buku Impor                         |
| livros_interesse_geral                         | Buku Umum                          |
| livros_tecnicos                                | Buku Teknis & Akademik             |
| malas_acessorios                               | Koper & Aksesoris Perjalanan       |
| market_place                                   | Marketplace (Campuran)             |
| moveis_colchao_e_estofado                      | Kasur & Sofa                       |
| moveis_cozinha_area_de_servico_jantar_e_jardim | Furnitur Dapur, Makan & Taman      |
| moveis_decoracao                               | Furnitur & Dekorasi Rumah          |
| moveis_escritorio                              | Furnitur Kantor                    |
| moveis_quarto                                  | Furnitur Kamar Tidur               |
| moveis_sala                                    | Furnitur Ruang Tamu                |
| musica                                         | Musik                              |
| papelaria                                      | Alat Tulis & Kantor                |
| pc_gamer                                       | PC Gaming                          |
| pcs                                            | Komputer & Laptop                  |
| perfumaria                                     | Parfum & Wewangian                 |
| pet_shop                                       | Perlengkapan Hewan Peliharaan      |
| portateis_casa_forno_e_cafe                    | Oven & Pembuat Kopi Portabel       |
| portateis_cozinha_e_preparadores_de_alimentos  | Alat Masak Portabel                |
| relogios_presentes                             | Jam Tangan & Hadiah                |
| seguros_e_servicos                             | Asuransi & Layanan                 |
| sinalizacao_e_seguranca                        | Rambu & Keamanan                   |
| tablets_impressao_imagem                       | Tablet, Printer & Kamera           |
| telefonia                                      | Telepon & Aksesoris                |
| telefonia_fixa                                 | Telepon Rumah                      |
| utilidades_domesticas                          | Peralatan Rumah Tangga Sehari-hari |

---

_Dokumen ini untuk keperluan review dan pembahasan hasil exam — tidak untuk dibagikan ke murid._
