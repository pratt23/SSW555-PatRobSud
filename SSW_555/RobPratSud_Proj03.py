#!/usr/bin/python

# NOT TO SELF: FOr output formatting https://docs.python.org/3.0/tutorial/inputoutput.html
# CHANGE STRING TO DATE: http://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python

import os
import sys
import codecs
import datetime

def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect date entry")

def reset_vars():
    # RESETTING THE VARIABLES FOR THE NEXT ITERATION
    tag=pid=name="NA"
    dob=dod=sex="NA"
    famc=fid=husb="NA"
    fams=wife=div="NA"
    cid=[]
    # RESETTING COMPLETE

class person():
	# Person ID, name, Date of Birth, Gender and Date of Death(NA if alive)
	def __init__(self, pid, name, dob, sex, dod, famc, fams):
		self.pid=pid
		self.name=name
		self.dob=dob
		self.sex=sex
		self.famc=famc
		self.fams=fams
class fam():
	# Person ID for the people, Date of marriage and Date of death/divorce; whatever ends the marriage
	def __init__(self, fid, husb, wife, dom, dod):
		self.fid=fid
		self.husb=husb
		self.wife=wife
		self.dom=dom
		self.dod=dod
        #self.child=[]

    # def addChild(self, cid)
    #     self.child.append(cid)

### VALID TAGS IN gedcom FILES ###
tags2 = [ "INDI" , "NAME" , "SEX" , "BIRT" , "DEAT" , "FAMC" , "FAMS" , "CITY" , "STAE" , "CTRY" , "SURN" , "DATE" ,"ADDR" , "FAM" , "DIV" , "MARR" , "HUSB" , "WIFE" , "CHIL" , "GIVN" , "DATE" , "HEAD" , "TRLR" , "NOTE" , "RFN" , "CHAN" ,"TIME" , "_MAR" , "SUBM" ]

### TAGS WE'LL USE
tags = [ "INDI" , "FAM" , "NAME" , "SEX" , "BIRT" , "DEAT" , "FAMC" , "FAMS" , "DATE" , "MARR" , "HUSB" , "WIFE" , "CHIL" , "DIV" ]

#filename = input ( "Enter the location of the file: " )
filename="/Users/sudhansh/Desktop/CS-555/Proj01_SudhanshAggarwal_CS555.ged" #For testing purposes

### CHECKING IF GEDCOM IS ENTERED, HELP TAKEN FORM AKSHAY SUNDERWANI ###
path = os.getcwd ( )  # method to fetch working directory path.
basefilename = os.path.basename ( filename )
basefilename2 = os.path.splitext ( basefilename )
if basefilename2[ -1 ] != '.ged':
    print ( "Gedcom file not entered" )
    exit ( )

### VARIABLES BEING USED for INDI - tag pid name dob dod sex famc, fams 
### VARIABLES BEING USED for FAMI - tag fid husb wife dom dod cid

indno=0
famno=0

try:
    # OPEN FILE IN READ MODE
    with open ( filename ) as file:
        with open("output.txt", 'w') as write_to:
            # THE DIRECTORY FROM WHICH THE SCRIPT IS RUN IS WHERE output.txt IS GENERATED

            # READ FILE LINE BY LINE
            for line in file:
                # SPLIT LINE INTO LIST OF WORDS
                words = line.split ( )
                #print (line)
                level = words[ 0 ]
                if level=='0':
                    reset_vars()
                    if words[-1] in tags:
                        # CHECKING FOR TAGS IN SPECIAL CONDITIONS
                        tag=words[-1]
                        if tag == "INDI":
                            pid=words[1]
                        else:
                            fid=words[1]
                    else:
                        tag="*** INVALID/UNUSED TAG ***"
                        continue
                else:
                    if words[1] in tags:
                    # CHECKING FOR VALID TAGS
                        tag=words[1]
                        if tag == "NAME":
                            name=words
                        elif tag=="SEX":
                            sex=words[2]
                        elif tag=="BIRT":
                            dd=words[2]
                            mm=words[3]
                            yy=words[4]
                            dob=yy+'-'+mm+'-'+dd
                        elif tag=="DEAT":
                            dd=words[2]
                            mm=words[3]
                            yy=words[4]
                            #REFER LINK TO CHANGE IT TO DATE
                            dod=yy+'-'+mm+'-'+dd
                        elif tag=="MARR":
                            dd=words[2]
                            mm=words[3]
                            yy=words[4]
                            #REFER LINK TO CHANGE IT TO DATE
                            dom=yy+'-'+mm+'-'+dd
                        elif tag=="DIV":
                            dd=words[2]
                            mm=words[3]
                            yy=words[4]
                            #REFER LINK TO CHANGE IT TO DATE
                            div=yy+'-'+mm+'-'+dd
                        elif tag=="FAMC":
                            famc=words[2]
                        elif tag=="FAMS":
                            fams=words[2]
                        elif tag=="HUSB":
                            husb=words[2]
                        elif tag=="WIFE":
                            wife=words[2]
                        elif tag=="CHIL":
                            cid.append(words[2])

                # print ( "LEVEL: " + level + "\tTAG: " + tag + "\n" )
                # print(line + "LEVEL: " + level + "\tTAG: " + tag + "\n", file=write_to)

except FileNotFoundError:
    # File not found
    print ( "\nSorry the file : " + filename + " does not exist.\n" )
