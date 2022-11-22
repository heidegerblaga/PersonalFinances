import os
from models import (Base, session,
                    Shopping, engine)




def newimages():

    os.chdir('H:\Mój dysk/recipes')

    path = []
    for dirpath, dirnames, filenames in os.walk('H:\Mój dysk/recipes'): #os.walk przeglada wszystkie pliki w sciezce
        for file in filenames:

            try:
                if session.query(Shopping).filter(Shopping.filename == file).first().filename == file:
                    pass
            except:
                path.append(dirpath + "/" + file)
                #musi zwracać pełną ścieżkę a nie tylko nazwę
    return path





