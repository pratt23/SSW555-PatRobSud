# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 21:46:16 2017

@author: basilmajdi
"""

from datetime import datetime
import unittest
        
def convert_2date(date1):
    return datetime.strptime(date1, '%d %b %Y')    

def birth_b4_dth(dob, dod):
    

    
    if dod == "NA" or dob == "NA": 
        return True
    
    elif convert_2date(dod) < convert_2date(dob):    
        return False
    else:    
        return True




class Test_my_functions(unittest.TestCase):
    def test_true(self):
        self.assertTrue(birth_b4_dth('3 MAR 2015', '3 MAR 2015'))
        self.assertTrue(birth_b4_dth('26 APR 2014', '3 MAR 2015'))
        
    
    def test_wrong(self):
        self.assertFalse(birth_b4_dth('3 MAR 2017', '3 MAR 2015'))
        self.assertFalse(birth_b4_dth('3 MAR 2017', '24 DEC 2011'))
        
    
        
if __name__=='__main__':
    unittest.main(exit=False)