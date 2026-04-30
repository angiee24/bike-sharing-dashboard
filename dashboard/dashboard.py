import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")
sns.set(style='whitegrid')

def create_monthly_rentals_df(df):
    monthly_rentals_df = df.resample(rule='M', on='dteday').agg({
        "cnt": "sum"
    })
    monthly_rentals_df.index = monthly_rentals_df.index.strftime('%b %Y')
    monthly_rentals_df = monthly_rentals_df.reset_index()
    return monthly_rentals_df

def create_weather_impact_df(df):
    weather_impact_df = df.groupby("weathersit").cnt.mean().reset_index()
    weather_dict = {1: 'Clear', 2: 'Misty', 3: 'Light Rain/Snow', 4: 'Heavy Rain/Snow'}
    weather_impact_df['weathersit'] = weather_impact_df['weathersit'].map(weather_dict)
    return weather_impact_df

path = os.path.dirname(__file__)
path_file = os.path.join(path, 'main_data.csv')
all_df = pd.read_csv(path_file)
all_df["dteday"] = pd.to_datetime(all_df["dteday"])

with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png") 
    
    min_date = all_df["dteday"].min()
    max_date = all_df["dteday"].max()
    
    try:
        date_range = st.date_input(
            label='Rentang Waktu',
            min_value=min_date,
            max_value=max_date,
            value=[min_date, max_date]
        )
        start_date, end_date = date_range
    except ValueError:
        st.error("Silakan pilih rentang tanggal yang lengkap.")
        st.stop()

main_df = all_df[(all_df["dteday"] >= pd.to_datetime(start_date)) & 
                (all_df["dteday"] <= pd.to_datetime(end_date))]

monthly_rentals_df = create_monthly_rentals_df(main_df)
weather_df = create_weather_impact_df(main_df)

st.header('Bike Sharing Analytics Dashboard 🚲')

total_rentals = main_df.cnt.sum()
avg_rentals = main_df.cnt.mean()

col1, col2 = st.columns(2)
with col1:
    st.metric("Total Penyewaan", value=f"{total_rentals:,}")
with col2:
    st.metric("Rata-rata Harian", value=f"{round(avg_rentals):,}")

st.subheader('Tren Penyewaan Sepeda Bulanan')
fig, ax = plt.subplots(figsize=(16, 6))
ax.plot(
    monthly_rentals_df["dteday"],
    monthly_rentals_df["cnt"],
    marker='o', 
    linewidth=2,
    color="#008080" 
)
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

st.subheader('Dampak Kondisi Cuaca Terhadap Penyewaan')
fig, ax = plt.subplots(figsize=(10, 6))
colors = ["#008080", "#73A8A8", "#E67E22", "#D32F2F"] 

sns.barplot(
    x="weathersit", 
    y="cnt",
    data=weather_df.sort_values(by="cnt", ascending=False),
    palette=colors,
    hue="weathersit",
    legend=False,
    ax=ax
)
ax.set_ylabel("Rata-rata Penyewaan")
ax.set_xlabel("Kondisi Cuaca")
st.pyplot(fig)

st.caption('Copyright (c) Angela Caroline Budiman 2026')