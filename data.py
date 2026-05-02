import streamlit as st
import pandas as pd
import plotly.express as px

def load_data():
          df = pd.read_csv("covid_19_indonesia_time_series_all.csv")
          df = df[df['Location'] != 'Indonesia']
          return df

def filter_data(df, year = None, location = None):
          if year:
              df = df[df['Date'].astype(str).str.contains(str(year))]
          if location:
              df = df[df['Location'].isin(location)]
          return df

def pilih_tahun():
    return st.sidebar.selectbox("Pilih Tahun", options = [None, 2020, 2021, 2022],
                                format_func=lambda x: "Semua Tahun" if x is None else str(x))

def pilih_provinsi(df):
    locations = sorted(df['Location'].unique())
    
    return st.sidebar.multiselect("Pilih Provinsi", 
                                    options = locations,
                                    default = locations)

def show_data(df):
          selected_columns = ['Location'] + list(df.loc[:, 'Total Cases':'Total Recovered'].columns)
          df_selected = df[selected_columns]
          st.subheader("Data COVID-19 di Indonesia")
          st.dataframe(df_selected.head(10))
          
          st.subheader("Statistik Deskriptif Dataset")
          st.write(df_selected.describe())

def total_cases(df):
          total_cases = df.sort_values('Date').groupby('Location', as_index = False).last()
          return total_cases['Total Cases'].sum()

def total_deaths(df):
          total_deaths = df.sort_values('Date').groupby('Location', as_index = False).last()
          return total_deaths['Total Deaths'].sum()

def total_recoveries(df):
          total_recoveries = df.sort_values('Date').groupby('Location', as_index = False).last()
          return total_recoveries['Total Recovered'].sum()

def kolom(df):
          kasus = total_cases(df)
          kematian = total_deaths(df)
          kesembuhan = total_recoveries(df)
          
          col1, col2, col3 = st.columns(3)
          
          col1.metric(label="Total Kasus 📊", value=f"{kasus/1000:.1f}k", border=True)
          col2.metric(label="Total Kematian ☠️", value=f"{kematian/1000:.1f}k", border=True)
          col3.metric(label="Total Kesembuhan 🌿", value=f"{kesembuhan/1000:.1f}k", border=True)


def pie_chart(df):
    st.markdown("#### Distribusi Kasus COVID-19 di Indonesia")
    total_deaths = df['Total Deaths'].sum()
    total_recoveries = df['Total Recovered'].sum()
    
    data = {'Status' : ['Total Kematian', 'Total Kesembuhan'],
            'Jumlah' : [total_deaths, total_recoveries]}
    
    fig = px.pie(data, names='Status', values='Jumlah', 
                 hole = 0.5, color_discrete_sequence = ['#4ECDC4', '#FF6B6B'])
    
    st.plotly_chart(fig, use_container_width=True)

def bar_chart1(df):
    st.markdown("#### 5 Provinsi dengan Total Kematian Tertinggi")
        
    df_last = df.sort_values('Date').groupby('Location', as_index=False).last()
    top5 = df_last.nlargest(5, 'Total Deaths')
    
    fig = px.bar(top5, x='Location', y='Total Deaths',
                 color='Total Deaths', color_continuous_scale='Reds',
                 labels={'Total Deaths': 'Total Kematian', 'Location': 'Provinsi'})
    
    fig.update_layout(xaxis_title='Provinsi', yaxis_title='Total Kematian')
    st.plotly_chart(fig, use_container_width=True)
    
def bar_chart2(df):
    st.markdown("#### 5 Provinsi dengan Total Kesembuhan Tertinggi")
    
    df_last = df.sort_values('Date').groupby('Location', as_index=False).last()
    top5 = df_last.nlargest(5, 'Total Recovered')
    
    fig = px.bar(top5, x='Location', y='Total Recovered',
                 color='Total Recovered', color_continuous_scale='Greens',
                 labels={'Total Recovered': 'Total Kesembuhan', 'Location': 'Provinsi'})
    
    fig.update_layout(xaxis_title='Provinsi', yaxis_title='Total Kesembuhan')
    st.plotly_chart(fig, use_container_width=True)

def map_chart(df, year = None):
    st.markdown(f'#### Peta Sebaran Kasus COVID-19 di Indonesia ({year if year else "Semua Tahun"})')
    
    df['Date'] = pd.to_datetime(df['Date'])
    
    if year:
        df = df[df['Date'].dt.year == year]
        
    df_agg = df.groupby(['Location', 'Latitude', 'Longitude'], as_index=False)['Total Cases'].sum()
    df_map = df_agg.dropna(subset=['Latitude', 'Longitude', 'Total Cases'])
    
    if df_map.empty:
        st.info("Peta tidak dapat ditampilkan karena data lokasi tidak lengkap.")
        return
    
    fig = px.scatter_mapbox(df_map, lat='Latitude', lon='Longitude', size='Total Cases',
                            color='Total Cases', hover_name='Location', zoom=4, 
                            center={'lat': -2.5, 'lon': 115}, size_max=20, opacity=0.7, 
                            color_continuous_scale='OrRd')
    
    fig.update_layout(mapbox_style='open-street-map', height=400, margin={'r':0,'t':30,'l':0,'b':0})
    
    st.plotly_chart(fig, use_container_width=True)

