import streamlit as st
import pandas as pd
df=pd.read_csv('Sentiment Data - audit_data.csv')
header=st.container()
input=st.container()
model=st.container()
with header:
 st.title('MY FIRST MODEL')
 st.text('hello in the model')
 st.write(df.head())
 disc=pd.DataFrame(df.sentiment.value_counts())
 st.bar_chart(disc)
with input:
 st.header('Enter the input')
 fcol,scol=st.columns(2)
 max_depth=fcol.slider('what should be the max?',min_value=10,max_value=100,value=30,step=10)
 estimate=scol.selectbox('what should be the estimate?',options=[100,200,300,'None'],index=0)
 ip=scol.text_input("Enter the text","Default")
 
with model:
 st.header('PREDICTIONS')
 st.subheader('the predictions are')
