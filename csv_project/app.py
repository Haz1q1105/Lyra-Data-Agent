import pandas as pd
import streamlit as st

st.title("Data Ingestion Agent Test")

file_uploaded = st.file_uploader("Drop Your CSV here")

if file_uploaded is not None:
    df = pd.read_csv(file_uploaded)
    st.dataframe(df)
    col1,col2 = st.columns(2)
    with col1:
        st.metric(label="Total rows :",value =df.shape[0])
    with col2:
        st.metric(label="Total columns:",value =df.shape[1])
    missing = df.isnull().sum()
    summary = pd.DataFrame({
        "Data Type":df.dtypes.astype(str),
        "Missing values": missing.values
    })
    st.subheader("Dataframe Schema ")
    st.dataframe(summary,use_container_width=True)
    st.subheader("Ask Our Agent Lyra! It will help you understand your data and gain insights about it")
    user = st.text_input("Ask Lyra about your data")
