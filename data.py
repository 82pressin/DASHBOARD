import streamlit as st
import pandas as pd
import plotly.express as px

def load_data():
          df = pd.read_csv("dataset\covid_19_indonesia_time_series_all.csv")
          return df

def filter_data(df, year = None):
          if year:
                    df = df[df['Date'].astype(str).str.contains(str(year))]
          return df

def pilih_tahun():
          options = [None, 2020, 2021, 2022]
          
          def format_tahun(tahun):
                    if tahun is None:
                              return "Semua Tahun"
                    return str(tahun)
          
          select_year = st.sidebar.selectbox(
                    "Pilih Tahun",
                    options,
                    format_func=format_tahun)
          return select_year

def show_data(df):
          selected_columns = ['Location'] + list(df.loc[:, 'Total Cases':'Total Recovered'].columns)
          df_selected = df[selected_columns]
          st.subheader("Data COVID-19 di Indonesia")
          st.dataframe(df_selected.head(10))
          
          st.subheader("Statistik Deskriptif Dataset")
          st.write(df_selected.describe())

def total_cases(df):
          total_cases = df['Total Cases'].sum()
          return total_cases

def total_deaths(df):
          total_deaths = df['Total Deaths'].sum()
          return total_deaths

def total_recoveries(df):
          total_recoveries = df['Total Recovered'].sum()
          return total_recoveries

def kolom(df):
          kasus = total_cases(df)
          kematian = total_deaths(df)
          kesembuhan = total_recoveries(df)
          
          col1, col2, col3 = st.columns(3)
          
          col1.metric(label="Total Kasus 📊", value=f"{kasus/1000:.1f}k", border=True)
          col2.metric(label="Total Kematian ☠️", value=f"{kematian/1000:.1f}k", border=True)
          col3.metric(label="Total Kesembuhan 🌿", value=f"{kesembuhan/1000:.1f}k", border=True)

def pie_chart(df):
          total_cases = df['Total Cases'].sum()
          total_deaths = df['Total Deaths'].sum()
          total_recoveries = df['Total Recovered'].sum()
          
          data = {
                    'Status' : ['Total Kasus', 'Total Kematian', 'Total Kesembuhan'],
                    'Jumlah' : [total_cases, total_deaths, total_recoveries]}
          
          fig = px.pie(data, 
                       names='Status', 
                       values='Jumlah', 
                       title='Distribusi Kasus COVID-19 di Indonesia', 
                       hole = 0.5, 
                       color_discrete_sequence = ['#FF6B6B', '#4ECDC4', '#1A535C'])
          
          st.plotly_chart(fig, use_container_width=True)