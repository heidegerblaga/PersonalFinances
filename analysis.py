import pandas as pd
import matplotlib.pyplot as plt
from models import (Base, session,
                    Shopping, Products, engine)
from datetime import datetime, timedelta
from collections import Counter
from functools import reduce
from statistics import mean

products = pd.read_sql_table('products', 'sqlite:///budget.db')
shopping = pd.read_sql_table('shopping', 'sqlite:///budget.db')
merchant = pd.read_sql_table('merchant', 'sqlite:///budget.db')

table = pd.merge(products, shopping, left_on="shopping_id", right_index=True, how="left", sort=False)



def periodic_balance(a,b):
    mask = (table['date'] > a) & (table['date'] <= b)
    #print(round(table.loc[mask]["totalprice"].sum(),2))
    return table.loc[mask]


def typical_shopping_cart():
    print(table['item'].value_counts())
    print(table.item.mode())
    return table.item.mode()


def macro():

        x= shopping.sort_values(by="date")
        x.reset_index(inplace=True)
        del x['index']
        x["date"] = pd.to_datetime(x["date"])

        dates = [date.date() for date in pd.to_datetime(x["date"])]
        x = []
        for i in range(0,len(dates)-1):
            x.append((dates[i+1] - dates[i]).days)

        frequency = round(30/mean(x))
        print("Your shopping frequency is %d shopping's per month" % (frequency))











def navigator():
    print('''                   ANALIZA WYDATKÓW
             1. Rozliczenie okresowe
             2. Typowy koszyk [najczęściej kupowane produkty]
             3. Analiza makro [częstotliwość zakupów, średnie wydatki na jedne zakupy, najdroższe produkty, współczynnik "świadomych zakupów"]
             4. Świadome zakupy [miesięczna lista zakupów + sugestie z typowego koszyka]\n''')

    choice = int(input())

    if choice==1:

        print("Wprowadź okres który chcesz sprawdzić w formacie rrrr-mm-dd \n Data początkowa:")

        a = datetime.strptime(input(), '%Y-%m-%d')

        print("\n Data końcowa:")

        b = datetime.strptime(input(), '%Y-%m-%d')

        periodic_balance(a,b)
    elif choice==2:
        typical_shopping_cart()
    elif choice==3:
        macro()
    elif choice==4:
        pass




navigator()