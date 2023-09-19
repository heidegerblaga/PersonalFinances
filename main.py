from check_latest import newimages
from pars_receipt import pars
from load_data import  load,add_to_db
from start import main



if __name__ == "__main__":

    #pars('folder/20230114_172246.jpg')
    ld = load('json/response.json')
    add_to_db(ld[0],ld[1],ld[2],ld[3])