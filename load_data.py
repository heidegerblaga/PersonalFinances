import json
from datetime import datetime
from models import (Base, session,
                    Shopping, Products, engine)
import re


def clean_shoping(text):
    text = text.split("\n")
    total = 0
    merchant_name = text[0].strip()
    #tu dodaj funkcje znajdującą sklep w bazie danych

    for i in range(0, len(text) - 1):
        if "SUMA PLN" in text[i]:
            total = re.sub(",", ".", re.sub("SUMA PLN", "", text[i]).strip())

    return total, merchant_name;


def clean_products(text):

    staff = []
    listofproducts = {}
    text = text.split("\n")

    for i in range(0, len(text)-1):
        text[i] = text[i].strip()

        if text[i] == "PARAGON FISKALNY":
            j = i + 1
            while "SPRZEDAZ OPODATKOWANA" not in text[j]:
                staff.append(text[j])
                j += 1



    for i in range(0, len(staff)):
        match = re.sub(r'[ ]+[A-H]?[ ]+', ' X ', staff[i].strip())
        match = re.split(r' X ', match)

        print(match)
        if (len(match) == 2) and bool(re.search("[\d ]+[x*X][\d, ]+[\w]", match[1])):
            match[1] = re.sub(r'(szt.)?', '', match[1])
            listofproducts[match[0]] = re.findall(r'[\d+,(.)?]+[A-C]?', match[1].strip())
            listofproducts[match[0]][2] = re.sub(r'[A-C]?', '', listofproducts[match[0]][2])
            listofproducts[match[0]][0] = re.sub(r',', '.', listofproducts[match[0]][0])
            listofproducts[match[0]][1] = re.sub(r',', '.', listofproducts[match[0]][1])
            listofproducts[match[0]][2] = re.sub(r',', '.', listofproducts[match[0]][2])
    print(listofproducts)
    return listofproducts


def load(file):
    path = "H:\Mój dysk/recipes/response.json"
    with open(path, "r") as f:
        data = json.load(f)

    text = data["receipts"][0]["ocr_text"]
    print(text)
    date = re.findall(r'(20\d\d-\d\d-\d\d)', text)
    products = clean_products(text)
    shopping_info = clean_shoping(text)

    return shopping_info,date,products,file


def add_to_db(shopping_info,date,products,file):

    add_shopping = Shopping(merchant_name=shopping_info[1],
                            total=float(shopping_info[0]),
                            date=datetime.strptime(date[0] ,"%Y-%m-%d"),
                            filename=file)

    session.add(add_shopping)
    session.commit()

    for product in products:

        print(products[product])
        add_product = Products(item=product,
                                price=float(products[product][1]),
                                quantity=float(products[product][0]),
                                total =float(products[product][2]),
                                shopping_id=session.query(Shopping).order_by(Shopping.id.desc()).first().id)

        session.add(add_product)
        session.commit()

