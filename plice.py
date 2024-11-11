import streamlit as st
import pandas as pd
import numpy as np
st.title("Police incidents reports from 2018 to 2020")

df=pd.read_csv("Policev1.csv")
df
st.markdown("The data shown belongs to incident reports in the city of San Francisco from the year 2018 to 2020")

mapa=pd.DataFrame()
mapa['Date']=df['Incident Date']
mapa['Day']=df['Incident Day of Week']
mapa['Neigborhood']=df['Analysis Neighborhood']
mapa['Police District']=df['Police District']
mapa['Incident Category']=df['Incident Category']
mapa['Incident Subcategory']=df['Incident Subcategory']
mapa['Resolution']=df['Resolution']
mapa['lat']=df['Latitude']
mapa['lon']=df['Longitude']
mapa=mapa.dropna()

