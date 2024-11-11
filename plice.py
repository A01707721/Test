import streamlit as st
import pandas as pd

st.title("Police incidents reports from 2018 to 2020")

df=pd.read_csv("Policev1.csv")
df
st.markdown("The data shown belongs to incident reports in the city of San Francisco from the year 2018 to 2020")

