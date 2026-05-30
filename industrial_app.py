import streamlit as st
import pandas as pd
import plotly.express as px
st.title("Industrial Human Resource Geo Visualization")
df=pd.read_csv("merged_dataset.csv")
st.dataframe(df.head())
state_workers=df.groupby("India/States")["Main Workers - Total -  Persons"].sum().reset_index()
fig=px.bar(state_workers,x="India/States",y="Main Workers - Total -  Persons")
st.plotly_chart(fig)
