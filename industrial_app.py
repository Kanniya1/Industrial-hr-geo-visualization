import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import sklearn
import glob
#title
st.set_page_config(page_title="Industrial HR geo Visualization",layout="wide")
st.title("Industrial Human Resourcr Geo Visualization")
#merge and load csv files
files=glob.glob("*.csv")
frames=[]
for file in files:
  try:
    frames.append(
        pd.read_csv(
            file,
            encoding="latin1",
            engine="python",
            on_bad_lines="skip"
        )
    )
    print("loaded:",file)
  except Exception as e:
    print("Error:",file)
    print(e)
df=pd.concat(frames,ignore_index=True)
#data cleaning
df.drop_duplicates(inplace=True)
df.columns=df.columns.str.strip()
df.fillna("Unknown",inplace=True)
#save merged file
df.to_csv("merged_dataset.csv",index=false)
#industry classification
def classify_industry(text):
  text=str(text).lower()
  if "retail" in text:
    return "Retail"
  elif "agriculture" in text:
    return "Agriculture"
  elif "poultry" in text:
    return "Poultry"
  elif "manufacturing" in text:
    return "Manufacturing"
  elif "construction" in text:
    return "Contruction"
  else:
    return "others"
#find industry description column
India/States=None
for col in df.columns:
  if "India/States" in col .lower():
   India/States=col
if India/States:
  df["Industry_Category"]=(df[India/States].astype(str).apply(classify_industry))
else:
  df["industry_Category"]="others"
  #data preview
st.subheader("dataset preview")
#datainfo
st.subheader("dataset shape")
st.write(df.shape)
#sate fiter
if "India/Stae" in df.columns:
  selected_state=
  st.sidebar.selectbox(
    "Select State",sorted(df["India/
    States"].unique())
    )
  filtered_df=df[
  df["India/State"]==
  selected_state
  ]
else:
   filtered_df=df
#workers by state
if("India/Stattes" in df.columns
   and
   "Main Workers - total - Persons"
   in df.columns):
     state_workers=(df.groupby("India/States")["Main Workers - total - Persons"].sum().reset_index())
     fig1=px.bar(state_workers,x="India/States",y="Main Workers - total - Persons",title="Workers by State")
     st.plotly_chart(fig1,use_container_width=True)
#male vs female
if("Main Workers -Total -Males"indf.columns and "Main Workers - Total - Females" in df.columns):
  male=df["Main Workers - Total - Males"].sum()
  female=df["Main Workers - Total - Females"].sum()
  Gender_data=pd.DataFrame({"Gender":["Male","Female"],"Workers":[male,female]})
  fig2=px.pie(Gender_data ,names ="Gender",values="Workers",title="male vs female workers")
  st.plotly_chart(fig2,use_container_width=True)
#industry category
industry_count=(df["Industry_Category"].value_counts().reset_index())
industry_count.columns=["Industry ","Count"]
fig3=px.bar(industry_count,x="Industry",y="count",title="Industry Cattegories")
st.plotly_chart(fig3,use_container_width=True)
#download merged dataset
csv=df.to_csv(index=False)
st.download_button(label="Download Merged Dtaset",data=csv,file_name="merged_dataset.csv",mime="text/csv")
#summary
st.subheader("Summary")
st.write(
  f"""
  Total Records:{df.shape[0]}
  Total Columns:{df.shape[1]}
  Industry Categories:{df['Industry_Category'].nunique()}
  """)



  

  
 
