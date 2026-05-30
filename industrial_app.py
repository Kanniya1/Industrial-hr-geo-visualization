import glob
import pandas as pd
import numpy as np
import plotly 
import sklearn
import streamlit as st
import os
for f in os.listdir("."):
  print(f)
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
print(df.shape)
df.head()
df.drop_duplicates(inplace=True)
df.fillna("Unknown",inplace=True)
print(df.isnull().sum())
print(df.info())
print(df.describe())
print(df.columns)
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
df["Industry_Category"]=df["India/States"].apply(classify_industry)
df.head()
state_workers=df.groupby("India/States")["Main Workers - Total -  Persons"].sum().reset_index()
print(state_workers.head())
import plotly.express as px
fig=px.bar(state_workers,x="India/States",y="Main Workers - Total -  Persons",title="state wise performance")
fig.show()
print(df.columns.tolist())
import plotly.express as px
male=df["Main Workers - Total - Males"].sum()
female=df["Main Workers - Total - Females"].sum()
Gender_data=pd.DataFrame({"Gender":["Male","Female"],"Workers":[male,female]})
fig=px.pie(Gender_data ,names ="Gender",values="Workers",title="male vs female workers")
fig.show()
for col in df.columns:
  print(col)
  import os
print("merged_dataset.csv"in
os.listdir('.'))
files=glob.glob('*.csv')
print("number of files:",len(files))
df_list=[]
for filr in files:
  try:
    temp=pd.read_csv(file,encoding='latin1')
    df_list.append(temp)
  except Exception as e:
    print("error in",file,":",e)
df.to_csv('./merged_dataset.csv',index=False)
print("merged file created successfully")
print("shape:",df.shape)
import streamlit as st
male=df['Main Workers - Total - Males'].sum()
female=df['Main Workers - Total - Females'].sum()
Gender_data=pd.DataFrame({'Gender':['male','female'],'workers':[male,female]})
fig2=px.pie(Gender_data,names='Gender',values='workers',title='male vs female workers')
st.plotly_chart(fig2)
fig2.show()
import os
print(os.listdir())
import os
print(os.path.exists("industrial_app.py"))

import streamlit as st
import pandas as pd
import plotly.express as px
st.title("Industrial Human Resource Geo Visualization")
df=pd.read_csv("merged_dataset.csv")
st.dataframe(df.head())
state_workers=df.groupby("India/States")["Main Workers - Total -  Persons"].sum().reset_index()
fig=px.bar(state_workers,x="India/States",y="Main Workers - Total -  Persons")
st.plotly_chart(fig)
import os
print(os.path.exists("industrial_app(3).py"))
uploaded_file=st.file_uploader("upload csv",type=(["csv"])
                               if uploaded_file is not None:
                                   df=pd.read_csv(uploaded_file)
                               
files.download('industrial_app.py')
import streamlit as st
st.download_button("download csv",df.to_csv(index=False),
                   "merged_dataset.csv",
                   "text/csv")
