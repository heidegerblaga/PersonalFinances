import pandas as pd
import streamlit as st
import psycopg2


conn = psycopg2.connect(user="postgres",
              password="qwest1",
              host="localhost",
              database="Finances")


query = "select * from outgoings;"

df = pd.read_sql(query,conn)

df = df.drop(columns=['filename'])

st.dataframe(df)






