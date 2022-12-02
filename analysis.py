import pandas as pd
import matplotlib.pyplot as plt
from models import (Base, session,
                    Shopping, Products, engine)
from datetime import datetime
from collections import Counter



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
        pass
    elif choice==4:
        pass




navigator()