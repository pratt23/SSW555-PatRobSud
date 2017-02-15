#!/usr/bin/python

import os
import sys
import codecs
import datetime

def refresh():
    global iden, name, sex, dob, dod, famc, fams, flag, hid, wid, dom, doe, cid
    iden = "NA"
    name = "NA"
    sex = "NA"
    dob = "NA"
    dod = "NA"
    famc = "NA"
    fams = "NA"
    hid = "NA"
    wid = "NA"
    dom = "NA"
    doe = "NA"
    cid = "NA"
    flag = 0 # 1 for indi, 2 for family in level 0 lines.

class individual:
    def __init__(self, pid, name, sex, dob, dod, famc, fams):
        self.pid=pid
        self.name=name
        self.sex=sex
        self.dob=dob
        self.dod=dod
        self.famc=famc
        self.fams=fams

    def showinfo(self):
        print('{} : {}'.format("ID",self.pid))
        print('{} : {}'.format("NAME",self.name))
        print('{} : {}'.format("SEX",self.sex))
        print('{} : {}'.format("D.O.B",self.dob))
        print('{} : {}'.format("D.O.D",self.dod))
        print('{} : {}'.format("FAMC",self.famc))
        print('{} : {}'.format("FAMS",self.fams))

class family:
    def __init__(self, fid, hid, wid, dom, doe, cid):
        self.fid=fid
        self.hid=hid
        self.wid=wid
        self.dom=dom
        self.doe=doe
        self.cid=cid

    def cout(self):
        print('{} : {}'.format("ID",self.fid))
        print('{} : {}'.format("HUSB",self.hid))
        print('{} : {}'.format("WIFE",self.wid))
        print('{} : {}'.format("D.O.M",self.dom))
        print('{} : {}'.format("D.O.E",self.doe))
        print('{} : {}'.format("CID",self.cid))

### VALID TAGS IN gedcom FILES ###
tags = [ "INDI" , "FAM" , "NAME" , "SEX" , "BIRT" , "DEAT" , "FAMC" , "FAMS" , 
"DATE" , "MARR" , "HUSB" , "WIFE" , "CHIL" , "DIV" ]

#filename = input ( "Enter the location of the file: " )
filename="/Users/sudhansh/Desktop/CS-555/test1.ged" #For testing purposes

### CHECKING IF GEDCOM IS ENTERED, HELP TAKEN FORM AKSHAY SUNDERWANI ###
path = os.getcwd ( )  # method to fetch working directory path.
basefilename = os.path.basename ( filename )
basefilename2 = os.path.splitext ( basefilename )
if basefilename2[ -1 ] != '.ged':
    print ( "Gedcom file not entered" )
    exit ( )

try:
    # OPEN FILE IN READ MODE
    refresh()
    with open ( filename ) as file:
        with open("output.txt", 'w') as write_to:
            # THE DIRECTORY FROM WHICH THE SCRIPT IS RUN IS WHERE output.txt IS GENERATED
            
            # READ FILE LINE BY LINE
            for line in file:
                # SPLIT LINE INTO LIST OF WORDS
                words = line.split ( )
                level = words[ 0 ]

                if level=='0':
                    iden = individual(iden,name, sex, dob, dod, famc, fams)
                    print(iden)
                    iden.showinfo()
                    refresh()
                    tag=words[-1]
                    if tag=="INDI":
                        flag=1
                    elif tag=="FAM":
                        flag=2
                    iden = words[1]
                if level != '0':
                    tag=words[1]
                    if tag in tags:
                        if tag == "NAME":
                            name=words[2:]
                        elif tag == "SEX":
                            sex=words[-1]
                        elif tag == "BIRT":
                            line=next(file)
                            words=line.split()
                            if words[1]=="DATE":
                                dd=words[2]
                                mm=words[3]
                                yy=words[4]
                                dob=dd+' '+mm+' '+yy
                        elif tag == "DEAT":
                            line=next(file)
                            words=line.split()
                            if words[1]=="DATE":
                                dd=words[2]
                                mm=words[3]
                                yy=words[4]
                        elif tag == "FAMC":
                            famc=words[-1]
                        elif tag == "FAMS":
                            fams=words[-1]






                '''
                if words[1] in tags:
                    # CHECKING FOR VALID TAGS
                    tag=words[1]
                elif words[-1] in tags:
                    # CHECKING FOR TAGS IN SPECIAL CONDITIONS
                    tag=words[-1]
                else:
                    tag="*** INVALID TAG ***"
                '''


                '''
                print ( "LEVEL: " + level + "\tTAG: " + tag + "\n" )
                print(line + "LEVEL: " + level + "\tTAG: " + tag + "\n", file=write_to)
                '''

except FileNotFoundError:
    # File not found
    print ( "\nSorry the file : " + filename + " does not exist.\n" )
