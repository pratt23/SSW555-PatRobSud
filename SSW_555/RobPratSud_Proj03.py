#!/usr/bin/python

import os
import sys
import codecs

class person():
	# Persin ID, name, Date of Birth, Gender and Date of Death(0 if alive)
	def __init__(self, pid, name, dob, sex, dod, chi, spo):
		self.pid=pid
		self.name=name
		self.dob=dob
		self.sex=sex
		self.dod=dod
		self.chi=chi
		self.spo=spo

class fam():
	# Person ID for the people, Date of marriage and Date of death/divorce; whatever ends the marriage
	def __init__(self, fid, husb, wife, dom, chil1, chil2, dod):
		self.fid=fid
		self.husb=husb
		self.wife=wife
		self.dom=dom
		self.chil1=chil1
		self.chil2=chil2
		self.dod=dod

### VALID TAGS IN gedcom FILES ###
tags = [ "INDI" , "NAME" , "SEX" , "BIRT" , "DEAT" , "FAMC" , "FAMS" , "CITY" , "STAE" , "CTRY" , "SURN" , "DATE" ,"ADDR" , "FAM" , "MARR" , "HUSB" , "WIFE" , "CHIL" , "GIVN" , "DATE" , "HEAD" , "TRLR" , "NOTE" , "RFN" , "CHAN" ,"TIME" , "_MAR" , "SUBM" ]

filename = input ( "Enter the location of the file: " )
#filename="/Users/sudhansh/Desktop/CS-555/Proj01_SudhanshAggarwal_CS555.ged" #For testing purposes

### CHECKING IF GEDCOM IS ENTERED, HELP TAKEN FORM AKSHAY SUNDERWANI ###
path = os.getcwd ( )  # method to fetch working directory path.
basefilename = os.path.basename ( filename )
basefilename2 = os.path.splitext ( basefilename )
if basefilename2[ -1 ] != '.ged':
    print ( "Gedcom file not entered" )
    exit ( )

try:
    # OPEN FILE IN READ MODE
    with open ( filename ) as file:
        with open("output.txt", 'w') as write_to:
            # THE DIRECTORY FROM WHICH THE SCRIPT IS RUN IS WHERE output.txt IS GENERATED
            
            # READ FILE LINE BY LINE
            for line in file:
                # SPLIT LINE INTO LIST OF WORDS
                words = line.split ( )
                print (line)
                level = words[ 0 ]
                if words[1] in tags:
                    # CHECKING FOR VALID TAGS
                    tag=words[1]
                elif words[-1] in tags:
                    # CHECKING FOR TAGS IN SPECIAL CONDITIONS
                    tag=words[-1]
                else:
                    tag="*** INVALID TAG ***"
                print ( "LEVEL: " + level + "\tTAG: " + tag + "\n" )
                print(line + "LEVEL: " + level + "\tTAG: " + tag + "\n", file=write_to)

except FileNotFoundError:
    # File not found
    print ( "\nSorry the file : " + filename + " does not exist.\n" )
