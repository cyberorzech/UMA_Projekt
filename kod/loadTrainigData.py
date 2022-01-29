import numpy as np


FULL_SAMPLE = False


def load(df, af):
    ###################
    # Donors:
    ###################
    global yd, nd

    # read from disk:
    donorFile = open(df)
    donorText = donorFile.read()
    donorFile.close()
    
    # get strings representing the donors
    donorLines = np.array(donorText.splitlines())
    donorPositiveIdx = np.where(donorLines == '1')[0]
    donorNegativeIdx = np.where(donorLines == '0')[0]
    yesDonors = donorLines[donorPositiveIdx + 1]
    notDonors = donorLines[donorNegativeIdx + 1]
    
    # for testing of code, work with shorter arrays - faster
    if not FULL_SAMPLE:
        yesDonors = yesDonors[0:100]
        notDonors = notDonors[0:100]
    
    # check examples are of same length:
    l = len(yesDonors[0])
    if not all(map(lambda v: len(v) == l, yesDonors)):
        print ("[ error ] Przykłady pozytywne donorów nie są tej samej długości")
        return

    l = len(notDonors[0])
    if not all(map(lambda v: len(v) == l, notDonors)):
        print ("[ error ] Przykłady negatywne donorów nie są tej samej długości")
        return

    # create 2-d array to access all atributes:
    yd = [list(d) for d in yesDonors]
    nd = [list(d) for d in notDonors]

    ###################
    # Acceptors:
    ###################
    global ya, na

    # read from disk:
    acceptorFile = open(af)
    acceptorText = acceptorFile.read()
    acceptorFile.close()
    
    # get strings representing the acceptors:
    acceptorLines = np.array(acceptorText.splitlines())
    acceptorPositiveIdx = np.where(acceptorLines == '1')[0]
    acceptorNegativeIdx = np.where(acceptorLines == '0')[0]
    yesAcceptors = acceptorLines[acceptorPositiveIdx + 1]
    notAcceptors = acceptorLines[acceptorNegativeIdx + 1]
    
    # for testing of code, work with shorter arrays - faster:
    if not FULL_SAMPLE:
        yesAcceptors = yesAcceptors[0:100]
        notAcceptors = notAcceptors[0:100]
    
    # check examples are of same length:
    l = len(yesAcceptors[0])
    if not all(map(lambda v: len(v) == l, yesAcceptors)):
        print ("[ error ] Przykłady pozytywne akceptorów nie są tej samej długości")
        return

    l = len(notAcceptors[0])
    if not all(map(lambda v: len(v) == l, notAcceptors)):
        print ("[ error ] Przykłady negatywne akceptorów nie są tej samej długości")
        return

    # create 2-d array to access all atributes:
    ya = [list(a) for a in yesAcceptors]
    na = [list(a) for a in notAcceptors]
    
    return
 