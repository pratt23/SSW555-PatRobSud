#!/usr/bin/python

### MADE BY SUDHANSH AGGARWAL

from datetime import datetime
from time import strftime
#from RobPratSud_Proj03 import individual

#noreps makes sure there are no repeated IDs
def no_reps(group,id_, flag):
    if flag !=1 and flag !=2:
        return False
    else:
        if id_ in group:
            return True
        return False

#Returns false if the date is invalid or in the future
def valid_date(date_):
    try:
        if date_ == "NA":
            return True
        datetime.strptime(date_, '%d-%b-%Y')
        if datetime.strptime(date_, '%d-%b-%Y') <= datetime.now():
            return True
        else:
            return False
        raise ValueError

    except ValueError:
        return False

#Returns false if siblings are married
def sibs_no_marry(hid, wid, cids):
    #Checks each family's hid and wid in all other families' cids. 
    if hid in cids and wid in cids:
        return False
    return True
