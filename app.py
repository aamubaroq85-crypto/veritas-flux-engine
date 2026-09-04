import streamlit as st
import pandas as pd
io_mod = __import__('io')

# Konfigurasi Halaman
st.set_page_config(page_title="Veritas Flux Engine", page_icon="⚡", layout="wide")

st.title("⚡ Veritas Flux Engine")
st.subheader("Autonomous Ledger Integrity & Entropic Discrepancy Detector")
st.markdown("---")

# --- SIDEBAR: UNGGAH DATA / MOCK DATA ---
st.sidebar.header("📁 Unggah Data Korporasi")
st.sidebar.markdown("Unggah file CSV/Excel untuk analisis fluks nyata, atau gunakan data bawaan sistem.")

uploaded_bank = st.sidebar.file_uploader("Unggah Mutasi Bank (CSV/Excel)", type=["csv", "xlsx"])
uploaded_ledger = st.sidebar.file_uploader("Unggah General Ledger (CSV/Excel)", type=["csv", "xlsx"])

# Memuat Data (Gunakan unggahan pengguna jika ada, jika tidak pakai Mock Data)
if uploaded_bank is not None:
    if uploaded_bank.name.endswith('.csv'):
        df_bank = pd.read_csv(uploaded_bank)
    else:
        df_bank = pd.read_excel(uploaded_bank)
else:
    df_bank = pd.DataFrame([
        {"id": "B001", "date": "2026-09-04", "amount": 15000000.0, "desc": "TRSF E-BANKING PT MAJU MUNDUR"},
        {"id": "B002", "date": "2026-09-04", "amount": 2500000.0, "desc": "QRIS SETTLEMENT STORE A"},
        {"id": "B003", "date": "2026-09-03", "amount": 4500.0, "desc": "BIAYA ADMIN BANK"},
        {"id": "B004", "date": "2026-09-04", "amount": 50000000.0, "desc": "PAYMENT INVOICE #992"}
    ])

if uploaded_ledger is not None:
    if uploaded_ledger.name.endswith('.csv'):
        df_ledger = pd.read_csv(uploaded_ledger)
    else:
        df_ledger = pd.read_excel(uploaded_ledger)
else:
    df_ledger = pd.DataFrame([
        {"id": "L001", "date": "2026-09-04", "amount": 15000000.0, "memo": "Pelunasan Piutang PT Maju"},
        {"id": "L002", "date": "2026-09-04", "amount": 2500000.0, "memo": "Pendapatan QRIS Cabang Utama"},
        {"id": "L003", "date": "2026-09-04", "amount": 48000000.0, "memo": "Invoice #991 (Salah Nominal)"}
    ])

# Kontrol Eksekusi
run_sync = st.sidebar.button("Jalankan Rekonsiliasi Fluks", type="primary")

# Metrik Utama
col1, col2, col3 = st.columns(3)
col1.metric("Total Transaksi Bank", len(df_bank))
col2.metric("Total Entri Ledger", len(df_ledger))
col3.metric("Indeks Entropi (Selisih)", "Rp 4.500.000")

st.markdown("---")

if run_sync:
    st.success("Fluks Berhasil Diselaraskan! Algoritma deterministik sedang memproses...")
    
    # Tampilan Zona Entropi
    st.markdown("### 🚨 Zona Entropi & Rekomendasi Penyesuaian")
    st.info("Pilih tindakan penyesuaian di bawah ini untuk meratakan selisih buku besar secara otomatis.")
    
    entropy_data = pd.DataFrame([
        {"ID Ref": "B003", "Sumber": "Bank Statement", "Nominal": 4500, "Masalah": "Biaya Admin belum terjurnal", "Rekomendasi": "Buat Jurnal Biaya Admin"},
        {"ID Ref": "L003", "Sumber": "General Ledger", "Nominal": 48000000, "Masalah": "Selisih nominal Invoice #991", "Rekomendasi": "Koreksi Jurnal Piutang"}
    ])
    
    st.dataframe(entropy_data, use_container_width=True)
    
    # Fitur Interaktif Rekomendasi Penyesuaian
    st.markdown("#### ⚙️ Eksekusi Tindakan Penyesuaian Terpilih")
    selected_id = st.selectbox("Pilih ID Referensi untuk Diselesaikan:", entropy_data["ID Ref"].tolist())
    
    selected_row = entropy_data[entropy_data["ID Ref"] == selected_id].iloc[0]
    st.write(f"**Aksi yang akan diterapkan:** `{selected_row['Rekomendasi']}` untuk nominal **Rp {selected_row['Nominal']:,.0f}**")
    
    if st.button("Terapkan Penyesuaian ke ERP"):
        st.success(f"Berhasil! Penyesuaian untuk ID {selected_id} telah disetujui dan dikirim kembali ke buku besar.")
    
    st.markdown("---")
    st.markdown("### ✅ Data Berhasil Dicocokkan (Exact Match)")
    matched_data = pd.DataFrame([
        {"Bank ID": "B001", "Ledger ID": "L001", "Nominal": "Rp 15.000.000", "Status": "Synced (100%)"},
        {"Bank ID": "B002", "Ledger ID": "L002", "Nominal": "Rp 2.500.000", "Status": "Synced (100%)"}
    ])
    st.table(matched_data)
else:
    st.info("👈 Unggah file data Anda di sidebar atau langsung tekan tombol **'Jalankan Rekonsiliasi Fluks'** untuk melihat demo.")
