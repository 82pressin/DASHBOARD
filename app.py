import streamlit as st 
from data import show_data

def judul():
          st.title("Dashboard COVID-19")
          st.write("Selamat datang di dashboard interaktif untuk menganalisis data COVID-19 di Indonesia!")
          
st.sidebar.title("Menu")
menu = st.sidebar.radio("Pilih Menu", ("Home", "Data"))
if menu == "Home":
          judul()
elif menu == "Data":
          judul()
          show_data()
          