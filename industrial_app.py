import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import sklearn
import glob

#title
st.set_page_config(page_title="Industrial HR geo Visualization",layout="wide")
#image
st.image("https://static.vecteezy.com/system/resources/thumbnails/020/685/858/small/analyst-working-on-business-analytics-dashboard-with-kpi-charts-and-metrics-to-analyze-data-and-create-insight-reports-for-executives-and-strategical-decisions-operations-and-performance-management-photo.jpg",
         use_container_width=True)
st.title("Industrial Human Resource Geo Visualization")
st.markdown("### workforce distribution analysis across india")
st.divider()
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
st.subheader("top  states by mainworkers")
if("India/States" in df.columns and "Main Workers - Total -  Persons"in df.columns):
         df["Main Workers - Total -  Persons"]=pd.to_numeric(df["Main Workers - Total -  Persons"],errors="coerce")
         state_workers=(df.groupby("India/States")["Main Workers - Total -  Persons"].sum().reset_index())
         fig1=px.bar(state_workers,x="India/States",y="Main Workers - Total -  Persons",title="Workers by state")
         st.plotly_chart(fig1,use_container_width=True)

#male vs female pie chart
st.subheader("gender distribution")
df.columns=df.columns.str.strip()
male_col="Main Workers -Total - Males"
female_col="Main Workers - Total - Females"
if male_col not in df.columns or female_col not in  df.columns:
         st.error("could not find the exact column names")
         st.write("available columns in your file are:",list(df.columns))
else:
         df[male_col]=pd.to_nuumeric(df[male_col],errors="coerce").fillna(0)
         df[female_col]=pd.to_numeric(df[female_col],errors="coerce").fillna(0)
         total_males=df[male_col].sum()
         total_females=df[female_col].sum()
         gender_data=pd.DataFrame({"Group":["Males","Females"],
                                   "Total Workers":[total_males,total_females]})
         fig2=px.bar(gender_data,x="Gender",y="Total Workers",title="Male vs Female Workers",color="Group")
         st.plotly_chart(fig2,use_container_width=True)
#industry category chart
st.subheader("industrial categories")
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



  

  
 
