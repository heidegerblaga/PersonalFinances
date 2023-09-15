from check_latest import newimages
from load_data import load, add_to_db
from pars_receipt import pars
from models import (Base, session,
                    Shopping, Products, engine)


#if __name__=="__main__":

def main():
  for path in newimages():
    print(path)
    if "jpg" in path:

      if session.query(Shopping).filter(Shopping.filename==path).first() == None:

        pars(path)
        #try:
        add = load(path)
        #except :
         # print("\n\n\nProbably you daily quota has exceed, try later.")
          #break


        print('''Do you want add this to data base ?\n
        1) yes \n
        0) no \n
        ''')
        choice = input()

        if int(choice)==1:
            add_to_db(add[0],add[1],add[2],add[3])

        else:
            continue

