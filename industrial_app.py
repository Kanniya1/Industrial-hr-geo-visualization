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
  except Exception as e:
    st.warning(f"could not read{file}:{e}")
if len(frames)==0:
  st.error("no csv files found in repository")
  st.stop()
  #merge datasets
df=pd.concat(frames,ignore_index=True)
#data cleaning
df.drop_duplicates(inplace=True)
df.columns=df.columns.str.strip()
text_cols=df.select_dtypes(include=["object"]).columns
df[text_cols]=df[text_cols].fillna("Unknown")
num_cols=df.select_dtypes(include=["number"]).columns
df[num_cols]=df[num_cols].fillna(0)
#save merged dataset
df.to_csv("merged_dataset.csv",index=False)
#save merged dataset
st.subheader("Column Names")
st.write(df.columns.tolist())
# nlp industry classification
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
  elif "chemical" in text:
    return "Chemical"
  elif "plastic" in text:
    return "Plastic"
  elif "rubber" in text:
    return "Rubber"
  else:
    return "others"
#find industry description column
if "NIC Name" in df.columns:
  df["Industry_Category"]=(df["NIC Name"].astype(str).apply(classify_industry))
else:
  df["Industry_Category"]="others"
  #data preview
st.subheader("dataset preview")
st.dataframe(df.head())
#data shape
st.subheader("Dataset Shape")
st.write(df.shape)
#sate fiter
if "India/States" in df.columns:
  selected_state=st.sidebar.selectbox(
    "Select State",sorted(df["India/States"].astype (str).unique())
    )
  filtered_df=df[
  df["India/States"] ==
selected_state
  ]
else:
  st.warning("'India/States' column not found")
  filtered_df=df
#workers by state bar chart
if(
  "India/States" in df.columns
   and
   "Main Workers - Total - Persons"
   in df.columns):
     df["Main Workers - Total - Persons"]=pd.to_numeric(df["Main Workers - Total - Persons"],errors="coerce")
     state_workers=(df.groupby("India/States")["Main Workers - Total - Persons"].sum().reset_index())
     fig1=px.bar(state_workers,x="India/States",y="Main Workers - Total - Persons",title="Workers by State")
     st.plotly_chart(fig1,use_container_width=True)
#male vs female pie chart
if(
  "Main Workers -Total - Males" in df.columns
  and
  "Main Workers - Total - Females"
  in df.columns
):
  male=pd.to_numeric(df["Main Workers - Total - Males"],errors="coerce").sum()
  female=pd.to_numeric(df["Main Workers - Total - Females"],errors="coerce").sum()
  Gender_data=pd.DataFrame({"Gender":["Male","Female"],"Workers":[male,female]})
  fig2=px.pie(Gender_data ,names ="Gender",values="Workers",title="male vs female workers")
  st.plotly_chart(fig2,use_container_width=True)
#industry category chart

industry_count=(df["Industry_Category"].value_counts().reset_index())
industry_count.columns=["Industry","Count"]
fig3=px.bar(industry_count,x="Industry",y="Count",title="Industry Categories")
st.plotly_chart(fig3,use_container_width=True)

#download button
csv=df.to_csv(index=False)
st.download_button("Download Merged Dtaset",csv,"merged_dataset.csv","text/csv")
#summary
st.subheader("Summary")
st.write("Rows:",df.shape[0])
st.write("column:",df.shape[1])
st.write("Industry Categories:",df['Industry_Category'].nunique())



  

  
 
