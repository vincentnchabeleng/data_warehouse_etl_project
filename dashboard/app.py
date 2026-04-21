import streamlit as st
import sqlite3
import pandas as pd

st.title("📊 Data Warehouse Dashboard")

conn = sqlite3.connect(r'C:\Users\HP\Documents\warehouse.db')

df = pd.read_sql_query("SELECT * FROM sales_table", conn)

st.subheader("Sales Data")
st.dataframe(df)

st.subheader("Summary Statistics")
st.write(df.describe())

st.subheader("Filter by Product")
product = st.selectbox("Choose product", df['product'].unique())

filtered = df[df['product'] == product]
st.write(filtered)

conn.close()