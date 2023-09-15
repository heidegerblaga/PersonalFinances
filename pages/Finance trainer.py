import pandas as pd
import streamlit as st
import psycopg2
import itertools


conn = psycopg2.connect(user="postgres",
                        password="qwest1",
                        host="localhost",
                        database="Finances")

query = "select * from outgoings;"

df = pd.read_sql(query, conn)

df = df.drop(columns=['filename'])

lt = list(df['total'])

y = list(itertools.accumulate(lt))

# for v in range(0,len(lt)) :
#     print(v)
#     if v == 0 :
#         y.append(lt[0])
#     else:
#      y.append(y[v-1]+lt[v])

print(y)

df['sum'] = y

print(df)
df['date'] = pd.to_datetime(df['date'])

df = df.sort_values(by='id', ascending= True)

st.bar_chart(df.set_index('date')['total'])

st.line_chart(df.set_index('id')['sum'])

