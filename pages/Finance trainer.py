import pandas as pd
import streamlit as st
import psycopg2
import itertools
from collections import defaultdict
import matplotlib.pyplot as plt


conn = psycopg2.connect(user="postgres",
                        password="qwest1",
                        host="localhost",
                        database="Finances")

query = "select * from outgoings;"

df = pd.read_sql(query, conn)

df = df.drop(columns=['filename'])

lt = list(df['total'])

y = list(itertools.accumulate(lt))


suma_dict = defaultdict(int)

for index, row in df.iterrows():
    data = row['date']
    wartosc = row['total']
    suma_dict[data] += wartosc

suma_dict = dict(suma_dict)

print(suma_dict)


print(y)

df['sum'] = y

print(df)

df['date'] = pd.to_datetime(df['date'])

df = df.sort_values(by='id', ascending= True)

daty = list(suma_dict.keys())
sumy = list(suma_dict.values())

df1 = pd.DataFrame({'date': daty, 'sum': sumy})

daty = list(map(lambda data: data.strftime("%Y-%m-%d"), daty))


st.bar_chart(df1.set_index('date'))

st.line_chart(df.set_index('id')['sum'])

