from datetime import datetime
from datetime import date

def sibling_nos(sibs):
	if len(sibs)>16:
		sibs.append('MoreThan16')
	return len(sibs)

def convert_2date(dob): 
    return datetime.strptime(dob, '%d %b %Y') 

def calculate_age(dob):
    today = date.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
