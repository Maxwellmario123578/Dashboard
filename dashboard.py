import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import time


import os

# Get the directory where the script is located
base_dir = os.path.dirname(__file__)
csv_file_path = os.path.join(base_dir, 'bank.csv')

df = pd.read_csv(csv_file_path)
st.set_page_config(page_title='Real Time Scene Dashboard',layout='wide')

#Dashboard Title
st.title('Real time Data analytics')

#Filter sur Job
job_filter=st.selectbox('Select a job',pd.unique(df['job']))
df=df[df['job']==job_filter]

#Création d'indicateur
avg_age=np.mean(df['age'])
count_married = int(df[(df['marital']=='married')]['marital'].count())
balance=np.mean(df['balance'])

kpi1,kpi2,kpi3=st.columns(3)
kpi1.metric(label='Age',value=round(avg_age),delta=round(avg_age))
kpi2.metric(label='Married_count',value=count_married,delta=round(count_married))
kpi3.metric(label='Balance',value=f"{round(balance,2)}",delta=-round(balance/count_married))


#GRAPHIQUES
col1,col2=st.columns(2)

with col1:
    st.markdown('### First Chart')
    fig1=plt.figure()
    sns.barplot(data=df,y='age',x='marital',palette='muted')
    st.pyplot(fig1)
    
with col2:
    st.markdown('### Second Chard')
    fig2=plt.figure()
    sns.histplot(data=df,y='age',x='marital',palette='muted')
    st.pyplot(fig2)

st.markdown('#### Detailed Data View')
st.dataframe(df)
time.sleep(1)

##Utiliser pipreqs pour générer automatiquement le requirement.tx. Pour streamlit, enlever les versions