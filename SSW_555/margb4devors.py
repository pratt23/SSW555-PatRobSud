# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 13:35:40 2017

@author: basilmajdi
"""

from datetime import datetime
import unittest
        
def convert_2date(date1): #this function converts the givin date format to the required format
    return datetime.strptime(date1, '%d %b %Y')    

def marg_b4_dvors(doe, dom):# this function takes the dates of marriage and devorce (if any) and 
                            # returns false if the date of devorce is before date of marriage
    

    if doe == "None": 
        return True
    
    elif convert_2date(doe) < convert_2date(dom):    
        return False
    else:    
        return True




class Test_my_functions(unittest.TestCase):
    def test_true(self):
        self.assertTrue(marg_b4_dvors('3 MAR 2015', '3 MAR 2015'))
        self.assertTrue(marg_b4_dvors('26 APR 2014', '3 MAR 2015'))
        
    
    def test_wrong(self):
        self.assertFalse(marg_b4_dvors('3 MAR 2017', '3 MAR 2015'))
        self.assertFalse(marg_b4_dvors('3 MAR 2017', '24 DEC 2011'))
        
    
        
if __name__=='__main__':
    unittest.main(exit=False)