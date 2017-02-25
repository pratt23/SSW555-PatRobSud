# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 12:58:24 2017

@author: basilmajdi
"""

from datetime import datetime
import unittest
        
def convert_2date(date1): #this function converts the givin date format to the required format
    return datetime.strptime(date1, '%d %b %Y')    

def birth_b4_marg(dob, dom):# this function takes the dates of birth and marriage(if any) and 
                            # returns false if the date of marriage is before date of birth 
    
    

    
    if dom == "None": 
        return True
    
    elif convert_2date(dom) <= convert_2date(dob):    
        return False
    else:    
        return True




class Test_my_functions(unittest.TestCase):
    def test_true(self):
        self.assertTrue(birth_b4_marg('3 MAR 2015', '3 MAR 2015'))
        self.assertTrue(birth_b4_marg('26 APR 2014', '3 MAR 2015'))
        
    
    def test_wrong(self):
        self.assertFalse(birth_b4_marg('3 MAR 2017', '3 MAR 2015'))
        self.assertFalse(birth_b4_marg('3 MAR 2017', '24 DEC 2011'))
        
    
        
if __name__=='__main__':
    unittest.main(exit=False)