from unicodedata import name
import numpy as np
import pandas as pd
import sklearn as skl

import loadTrainigData


DONOR_TRAIN_FILE = "../dane/spliceDTrainKIS.dat"
ACCEPTOR_TRAIN_FILE = "../dane/spliceATrainKIS.dat"


   
def main():
    global yd, nd
    global ya, na
    
    loadTrainigData.load(DONOR_TRAIN_FILE, ACCEPTOR_TRAIN_FILE)
    
    return 0

if __name__ == '__main__':
    main()
 