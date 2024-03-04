"""
Pertanyaan:
1. Bagaimana hubungan antara musim (season) dengan jumlah sewa sepeda (cnt)?
2. Bagaimana hubungan antara suhu (temp) dengan jumlah sewa sepeda (cnt)?
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Fungsi untuk memuat data dari file CSV
@st.cache_data
def muat_data():
    return pd.read_csv('https://raw.githubusercontent.com/Ach111es/Submission-Projek-Data-Analisis/main/data/day.csv')

data = muat_data()

# Fungsi untuk menunjukkan hubungan antara suhu dan jumlah pendaftaran
def tampilkan_hubungan_suhu_pendaftaran(data):
    fig, ax = plt.subplots(figsize=(12, 4), dpi=200)
    sns.scatterplot(data=data, x='temp', y='registered', ax=ax)
    plt.title('Hubungan antara Suhu dan Pengguna Terdaftar')
    plt.ylabel('Pengguna Terdaftar')
    plt.xlabel('Suhu (temp)')
    return fig

# Fungsi untuk menunjukkan hubungan antara musim dan jumlah pendaftaran
def tampilkan_hubungan_musim_pendaftaran(data):
    fig, ax = plt.subplots(figsize=(6, 4), dpi=200)
    sns.barplot(data=data, x="season", y="cnt", estimator="sum", errorbar=None, ax=ax)
    ax.set_ylim(0, 1200000)
    for p in ax.patches:
        ax.annotate(format(p.get_height(), '.0f'),
                    (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha = 'center', va = 'center',
                    xytext = (0, 9),
                    textcoords = 'offset points')
    plt.title('Total Penyewaan Sepeda Menurut Musim')
    plt.ylabel('Total Count')
    plt.xlabel('Musim')
    return fig

# Sidebar
st.sidebar.title("Dashboard Analisis Data 'Bike Sharing'")
page = st.sidebar.radio('Pilih halaman', ['Suhu-Pendaftaran','Musim-Pendaftaran'])

# Main content
st.title("Analisis Data Bike Sharing")

if page == 'Suhu-Pendaftaran':
    st.subheader("Hubungan antara suhu dan penyewaan sepeda")
    fig = tampilkan_hubungan_suhu_pendaftaran(data)
    st.pyplot(fig)

elif page == "Musim-Pendaftaran":
    st.subheader("Total penyewaan sepeda menurut musim")
    fig = tampilkan_hubungan_musim_pendaftaran(data)
    st.pyplot(fig)