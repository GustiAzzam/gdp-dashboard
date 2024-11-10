import streamlit as st
import pandas as pd

st.title(":blue[Daniel Ndara Palako]")
st.write("22220044")

# Memuat dataset IoT Botnet
df_botnet = pd.read_csv("Network_dataset_23.csv")

# Konversi kolom 'stime' (Unix timestamp) ke format datetime
df_botnet["stime"] = pd.to_datetime(df_botnet["stime"], unit='s', errors='coerce')

# Menghapus baris yang memiliki tanggal tidak valid atau nilai yang hilang
df_botnet = df_botnet.dropna(subset=["stime"])

# Tampilkan kolom dataset dan beberapa baris pertama untuk verifikasi
st.write("Kolom Dataset:", df_botnet.columns)
st.write(df_botnet.head())

# Pilih kolom numerik yang relevan untuk analisis (misalnya, 'pkts', 'bytes', 'srate', 'drate')
numerical_columns = ['pkts', 'bytes', 'srate', 'drate']

# Buat tabel pivot dengan 'stime' sebagai index dan agregasi kolom numerik
df_botnet_analysis = df_botnet.pivot_table(index='stime', values=numerical_columns, aggfunc='sum')

# Tampilkan grafik area
st.title("Grafik Area")
st.area_chart(df_botnet_analysis)

st.markdown("---")

# Tampilkan grafik batang
st.title("Grafik Batang")
st.bar_chart(df_botnet_analysis)

st.markdown("---")

# Tampilkan grafik garis
st.title("Grafik Garis")
st.line_chart(df_botnet_analysis)
