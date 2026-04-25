import streamlit as st 
from data import *

def judul():
          st.title("Dashboard COVID-19 🦠")
          st.write("Selamat datang di dashboard interaktif untuk menganalisis data COVID-19 di Indonesia! ")
          
st.sidebar.title("Menu")
menu = st.sidebar.radio("Pilih Menu", ("Home", "Data"))

if menu == "Home":
          judul()
          year = pilih_tahun()
          df = load_data()
          df_filtered = filter_data(df, year)
          kolom(df_filtered)
          pie_chart(df_filtered)
          
elif menu == "Data":
          judul()
          year = pilih_tahun()
          df = load_data()
          df_filtered = filter_data(df, year)
          show_data(df_filtered)

footer()
          