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
st.subheader("rural vs urban")
rural_col="Main Workers - Rural -  Persons"
urban_col="Main Workers - Urban -  Persons"
if rural_col not in df.columns or urban_col not in df.columns:
         st.error("could not find ural and urbanworker columns.")
else:
         df[rural_col]=pd.to_numeric(df[rural_col],errors="coerce").fillna(0)
         df[urban_col]=pd.to_numeric(df[urban_col],errors="coerce").fillna(0)
         total_rural=df[rural_col].sum()
         total_urban=df[urban_col].sum()
         area_data=pd.DataFrame({"Area Type":["Rural","Urban"],"Total Workers":[total_rural,total_urban]})
         fig2=px.pie(area_data,values="Total Workers",names="Area Type",
                     title="rural vs urban workers split",color="Area Type",color_discrete_map={"Rural":"green","urban":"blue"})
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



  

  
 
