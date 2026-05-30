import streamlit as st
import pandas as pd
import plotly .express as px
df=pd.read_csv("mydata/DataSets/DDW_B18sc_1600_NIC_FINAL_STATE_TRIPURA-2011.csv")
st.title("Industrial humamn resource geo visualization")
st.write(df.head())
fig=px.bar(df,x="NIC Name",y="Main Workers - Total -  Persons")
st.plotly_chart(fig)

