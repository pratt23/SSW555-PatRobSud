#!/usr/bin/python

def sibling_nos(sibs):
	if len(sibs)>16:
		sibs.append('MoreThan16')
	return len(sibs)