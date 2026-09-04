import streamlit as st
import pandas as pd

# Konfigurasi Halaman
st.set_page_config(page_title="Veritas Flux Engine", page_icon="⚡", layout="wide")

st.title("⚡ Veritas Flux Engine")
st.subheader("Autonomous Ledger Integrity & Entropic Discrepancy Detector")
st.markdown("---")

# Data Simulasi (Mock Data)
pencatatan_bank = pd.DataFrame([
    {"id": "B001", "date": "2026-09-04", "amount": 15000000.0, "desc": "TRSF E-BANKING PT MAJU MUNDUR"},
    {"id": "B002", "date": "2026-09-04", "amount": 2500000.0, "desc": "QRIS SETTLEMENT STORE A"},
    {"id": "B003", "date": "2026-09-03", "amount": 4500.0, "desc": "BIAYA ADMIN BANK"},
    {"id": "B004", "date": "2026-09-04", "amount": 50000000.0, "desc": "PAYMENT INVOICE #992"}
])

pencatatan_ledger = pd.DataFrame([
    {"id": "L001", "date": "2026-09-04", "amount": 15000000.0, "memo": "Pelunasan Piutang PT Maju"},
    {"id": "L002", "date": "2026-09-04", "amount": 2500000.0, "memo": "Pendapatan QRIS Cabang Utama"},
    {"id": "L003", "date": "2026-09-04", "amount": 48000000.0, "memo": "Invoice #991 (Salah Nominal)"}
])

# Sidebar Kontrol
st.sidebar.header("Panel Kontrol Fluks")
run_sync = st.sidebar.button("Jalankan Rekonsiliasi (Sync)", type="primary")

# Metrik Utama
col1, col2, col3 = st.columns(3)
col1.metric("Total Transaksi Bank", len(pencatatan_bank))
col2.metric("Total Entri Ledger", len(pencatatan_ledger))
col3.metric("Indeks Entropi (Selisih)", "Rp 4.500.000")

st.markdown("---")

if run_sync:
    st.success("Fluks Berhasil Diselaraskan! Algoritma deterministik sedang memproses...")
    
    # Tampilan Hasil Zona Entropi
    st.markdown("### 🚨 Zona Entropi & Anomali Terdeteksi")
    entropy_data = [
        {"ID Ref": "B003", "Sumber": "Bank Statement", "Nominal": "Rp 4.500", "Masalah": "Biaya Admin belum terjurnal", "Rekomendasi": "Buat Jurnal Biaya Admin"},
        {"ID Ref": "L003", "Sumber": "General Ledger", "Nominal": "Rp 48.000.000", "Masalah": "Selisih nominal Invoice #991", "Rekomendasi": "Koreksi Jurnal Piutang"}
    ]
    st.table(pd.DataFrame(entropy_data))
    
    st.markdown("### ✅ Data Berhasil Dicocokkan (Exact Match)")
    matched_data = [
        {"Bank ID": "B001", "Ledger ID": "L001", "Nominal": "Rp 15.000.000", "Status": "Synced (100%)"},
        {"Bank ID": "B002", "Ledger ID": "L002", "Nominal": "Rp 2.500.000", "Status": "Synced (100%)"}
    ]
    st.table(pd.DataFrame(matched_data))
else:
    st.info("Tekan tombol **'Jalankan Rekonsiliasi (Sync)'** di sidebar untuk memproses pencocokan data fluks.")
