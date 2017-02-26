#!/usr/bin/python

### MADE BY SUDHANSH AGGARWAL

from datetime import datetime

#noreps makes sure there are no repeated IDs
def no_reps(group,id_, flag,op_group):
    if flag !=1 and flag !=2:
        return 0
    else:
        if id_ in group:
            op_group.append(id_)
            id_=id_+"REP"
        return id_

#Returns false if the date is invalid or in the future
def valid_date(date_):
    try:
        datetime.strptime(date_, '%d-%m-%Y')
        if datetime.strptime(date_, '%d-%m-%Y') <= datetime.now():
            return True
        else:
            return False
        raise ValueError

    except ValueError:
        return False

#def sibs_no_marry(fid, used, all_fams):