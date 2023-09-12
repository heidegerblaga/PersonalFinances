from check_latest import newimages
from pars_receipt import pars
from load_data import  load,add_to_db



if __name__ == "__main__":

    for path in newimages():

        print(path)
        pars(path)
        data = load(path)
        add_to_db(data[0],data[1],data[2],data[3])