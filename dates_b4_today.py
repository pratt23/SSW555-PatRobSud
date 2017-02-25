# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 13:51:32 2017

@author: basilmajdi
"""


from datetime import date
from datetime import datetime
import unittest
        
def convert_2date(date1): #this function converts the givin date format to the required format
    return datetime.strptime(date1, '%d %b %Y')    

def dates_b4_today(dates): #this function compares any givin date to today's date. it returns false if the given date 
                            # is after today's date  
    
    today = date.today()
    
    
    if convert_2date(dates) >= convert_2date(today):
        return False
    else:    
        return True




class Test_my_functions(unittest.TestCase):
    def test_true(self):
        self.assertTrue(dates_b4_today('3 MAR 2015'))
        self.assertTrue(dates_b4_today('26 APR 2014'))
        
    
    def test_wrong(self):
        self.assertFalse(dates_b4_today('3 MAR 2018'))
        self.assertFalse(dates_b4_today('3 MAR 2019'))
        
    
        
if __name__=='__main__':
    unittest.main(exit=False)