import streamlit as st 
import numpy as np 
import pandas as pd 


with st.sidebar:
    st.title('Makintouch')
    
music_data = pd.read_csv("music.csv")
    
with st.expander("📂 View Dataset"):
    ps = st.dataframe(music_data)
    st.write(ps)

df = pd.DataFrame(np.random.rand(4,5),[1,2,3,4],['Cost','Revenue','Expens','Profit','Expenditure'])
st.dataframe(df)
st.bar_chart(df)

st.markdown('---')

df1 = pd.DataFrame({
    'x': np.random.rand(100),
    'y': np.random.rand(100),
})
st.dataframe(df1)

st.markdown("---")

df2 = pd.DataFrame({
    'Country': ['London','Lagos','Paris','Lome'],
    'Location': ['Europe','Africa','Europe','Africa'],
    'Age': [1000,20000,3000,5000],
})
st.dataframe(df2)