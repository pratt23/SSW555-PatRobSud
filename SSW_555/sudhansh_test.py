#!/usr/bin/python

import unittest
from sudhansh import no_reps

i=["I0922","I0065","I1994","133262"]
f=["F3600","753F","GD192","BLINK182"]
empty=[]

opg=[]
ii="I0922"
io="I0922REP"
ip="147699"
fi="BLINK182"
fo="BLINK182REP"
fp="TUPAC"

class TestMyFunctions(unittest.TestCase):
	### TESTS FOR NO REPETITION BEGIN ###
	def test_indi_contains(self):
		self.assertEqual(no_reps(i,ii,1,opg),io)
	def test_indi_no_contain(self):
		self.assertEqual(no_reps(i,ip,1,opg),ip)
	def test_indi_no_contain_E(self):
		# EMPTY LIST
		self.assertEqual(no_reps(empty,ip,1,opg),ip)
	def test_fam_contains(self):
		self.assertEqual(no_reps(f,fi,2,opg),fo)
	def test_fam_no_contain(self):
		self.assertEqual(no_reps(f,fp,2,opg),fp)
	def test_fam_no_contain_E(self):
		# EMPTY LIST
		self.assertEqual(no_reps(empty,fp,2,opg),fp)
	def test_diff_flag(self):
		self.assertEqual(no_reps(i,"90771",9,opg),0)
	### TESTS FOR NO REPETITION END ###

def main():
	unittest.main()

if __name__=='__main__':
	main()