import streamlit as st 
from data import *

def judul():
          st.title("DASHBOARD COVID-19 🦠")
          st.write("Selamat datang di dashboard interaktif untuk menganalisis data COVID-19 di Indonesia! ")
      
st.sidebar.title("MENU")
menu = st.sidebar.radio("Pilih Menu:", ("Home", "Data"))

if menu == "Home":
          judul()
          df = load_data()
          
          year = pilih_tahun()
          location = pilih_provinsi(df)
          df_filtered = filter_data(df, year, location)
          
          kolom(df_filtered)
          pie_chart(df_filtered)
          bar_chart1(df_filtered)
          bar_chart2(df_filtered)
          map_chart(df_filtered)
          
          st.sidebar.markdown("---")
          st.sidebar.caption("© INTAN BEYOND THE STAR - 184240014")
          
          st.markdown("---")
          st.markdown("© INTAN BEYOND THE STAR - 184240014")
          
elif menu == "Data":
          judul()
          df = load_data()
          
          year = pilih_tahun()
          location = pilih_provinsi(df)

          df_filtered = filter_data(df, year, location)
          show_data(df_filtered)
          
          st.sidebar.markdown("---")
          st.sidebar.caption("© INTAN BEYOND THE STAR - 184240014")
          
          st.markdown("---")
          st.markdown("© INTAN BEYOND THE STAR - 184240014")


