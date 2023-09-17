from check_latest import newimages
from pars_receipt import pars
from load_data import  load,add_to_db
from start import main



if __name__ == "__main__":

    pars('folder/20230114_172246.jpg')
    load('json/response.json')