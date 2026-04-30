import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set style seaborn
sns.set(style='whitegrid')

# Helper function untuk menyiapkan data tren bulanan
def create_monthly_rentals_df(df):
    monthly_rentals_df = df.resample(rule='M', on='dteday').agg({
        "cnt": "sum"
    })
    monthly_rentals_df.index = monthly_rentals_df.index.strftime('%B %Y')
    monthly_rentals_df = monthly_rentals_df.reset_index()
    return monthly_rentals_df

# Helper function untuk impact cuaca
def create_weather_impact_df(df):
    weather_impact_df = df.groupby("weathersit").cnt.mean().reset_index()
    return weather_impact_df

# Load data yang sudah bersih
# Pastikan file main_data.csv ada di folder yang sama dengan dashboard.py
all_df = pd.read_csv("main_data.csv")
all_df["dteday"] = pd.to_datetime(all_df["dteday"])

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png") # Opsional: Logo
    
    # Filter Rentang Waktu
    min_date = all_df["dteday"].min()
    max_date = all_df["dteday"].max()
    
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Filter Data Berdasarkan Tanggal
main_df = all_df[(all_df["dteday"] >= str(start_date)) & 
                (all_df["dteday"] <= str(end_date))]

# Menyiapkan DataFrame untuk visualisasi
monthly_rentals_df = create_monthly_rentals_df(main_df)
weather_df = create_weather_impact_df(main_df)

# --- MAIN PAGE ---
st.header('Bike Sharing Analytics Dashboard 🚲')

# Metric: Total Penyewaan
total_rentals = main_df.cnt.sum()
st.metric("Total Penyewaan Sepeda", value=total_rentals)

# Visualisasi 1: Tren Bulanan
st.subheader('Tren Penyewaan Sepeda Bulanan')
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    monthly_rentals_df["dteday"],
    monthly_rentals_df["cnt"],
    marker='o', 
    linewidth=2,
    color="#008080" # Teal
)
plt.xticks(rotation=45)
st.pyplot(fig)

# Visualisasi 2: Dampak Cuaca
st.subheader('Rata-rata Penyewaan Berdasarkan Cuaca')
fig, ax = plt.subplots(figsize=(10, 6))

# Mapping warna untuk cuaca
colors = ["#008080", "#73A8A8", "#E67E22"] # Teal, Light Teal, Orange

sns.barplot(
    x="weathersit", 
    y="cnt",
    data=weather_df.sort_values(by="cnt", ascending=False),
    palette=colors,
    ax=ax
)
ax.set_ylabel("Rata-rata Penyewaan")
ax.set_xlabel("Kondisi Cuaca")
st.pyplot(fig)

st.caption('Copyright (c) Angela Caroline Budiman 2026')