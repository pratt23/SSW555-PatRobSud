#!/usr/bin/python

'''
Parser for Robert Basil Majdi, Prateek Tyagi and Sudhansh Aggarwal
CS-555/SSW-555 
'''

import os
import sys
import codecs
import datetime
from sudhansh import no_reps
from prateek import sibling_nos
# from prettytable import PrettyTable

def getdate(d,m,y):
    date=d+'-'+m+'-'+y
    return date

def refresh():
    global iden, name, sex, dob, dod, famc, fams, flag, hid, wid, dom, doe, cid
    iden = name = sex = "NA"
    dob = dod = famc = "NA"
    fams = hid = wid = "NA"
    dom = doe = "NA"
    cid = []
    flag = 0 # 1 for indi, 2 for family in level 0 lines.


'''
def display_all(persons, families):
    
    ### NEED TO FIGURE OUT HOW TO MAKE PRETTY TABLES IN A SEPARATE FUNCTION INSTEAD OF IN MAIN ###
    x = PrettyTable() # For people
    x.field_names = ["I.D.","NAME","SEX","BIRTH","DEATH","FAM_C","FAM_S"]
    for person in persons:

    x.addrow([])
    y = PrettyTable() # For Families
    y.field_names = ["I.D.","HUSBAND","WIFE","MARRIAGE","MARR END","CHILDREN"] '''

class individual:

    def __init__(self):
        self.pid="NA"
        self.name="NA"
        self.sex="NA"
        self.dob="NA"
        self.dod="NA"
        self.famc="NA"
        self.fams="NA"

    def info(self, pid, name, sex, dob, dod, famc, fams):
        self.pid=pid
        self.name=name
        self.sex=sex
        self.dob=dob
        self.dod=dod
        self.famc=famc
        self.fams=fams

    def showinfo(self):
        '''
        return self.pid,self.name,self.sex,self.dob,self.dod,self.famc,self.fams
        '''
        print('{} : {}'.format("ID",self.pid))
        print('{} : {}'.format("NAME",self.name))
        print('{} : {}'.format("SEX",self.sex))
        print('{} : {}'.format("D.O.B",self.dob))
        print('{} : {}'.format("D.O.D",self.dod))
        print('{} : {}'.format("FAMC",self.famc))
        print('{} : {}'.format("FAMS",self.fams))
        

class family:
    def __init__(self, fid, hid, wid, dom, doe, cid):
        self.fid="NA"
        self.hid="NA"
        self.wid="NA"
        self.dom="NA"
        self.doe="NA"
        self.cid=[]
        self.sib_no=0
    
    def info(self, fid, hid, wid, dom, doe, cid):
        self.fid=fid
        self.hid=hid
        self.wid=wid
        self.dom=dom
        self.doe=doe
        self.cid=cid
        self.sib_no=sibling_nos(cid)

    def cout(self):
        '''
        return self.fid,self.hid,self.wid,self.dom,self.doe,self.cid
        '''
        print('{} : {}'.format("ID",self.fid))
        print('{} : {}'.format("HUSB",self.hid))
        print('{} : {}'.format("WIFE",self.wid))
        print('{} : {}'.format("D.O.M",self.dom))
        print('{} : {}'.format("D.O.E",self.doe))
        print('{} : {}'.format("CID",self.cid))
        print('{} : {}'.format("No. of Siblings",self.sib_no))

### VALID TAGS IN gedcom FILES ###
tags = [ "INDI" , "FAM" , "NAME" , "SEX" , "BIRT" , "DEAT" , "FAMC" , "FAMS" , 
"DATE" , "MARR" , "HUSB" , "WIFE" , "CHIL" , "DIV" ]

filename = input ( "Enter the location of the file: " )
#filename="/Users/sudhansh/Desktop/CS-555/test1.ged" #For testing purposes

### CHECKING IF GEDCOM IS ENTERED, HELP TAKEN FORM AKSHAY SUNDERWANI ###
path = os.getcwd ( )  # method to fetch working directory path.
basefilename = os.path.basename ( filename )
basefilename2 = os.path.splitext ( basefilename )
if basefilename2[ -1 ] != '.ged':
    print ( "Gedcom file not entered" )
    exit ( )

indi=[]
famillia=[]
reps_i=[] #strores conflicting/repeating individual IDs
reps_f=[] #stores conflicting/repeating family IDs

'''
x = PrettyTable() # For people
x.field_names = ["I.D.","NAME","SEX","BIRTH","DEATH","FAM_C","FAM_S"]
y = PrettyTable() # For Families
y.field_names = ["I.D.","HUSBAND","WIFE","MARRIAGE","MARR_END","CHILDREN"]
'''

c_ind = 0
c_fam = 0

try:
    # OPEN FILE IN READ MODE

    #Counting the number of people/families
    with open (filename) as file:
        for line in file:
            words=line.split()
            if words[0]=='0':
                if words[-1] == "INDI":
                    c_ind++
                elif words[-1] == "FAM":
                    c_fam++
    refresh()
    with open ( filename ) as file:
        # READ FILE LINE BY LINE
        for line in file:
            # SPLIT LINE INTO LIST OF WORDS
            words = line.split()
            level = words[ 0 ]

            if level=='0':
                if flag == 1:
                    iden=no_reps(indi,iden,flag,reps_i)
                    indi.append(iden)
                    iden = individual(iden, name, sex, dob, dod, famc, fams)
                    #x.add_row([iden, name, sex, dob, dod, famc, fams])
                    iden.showinfo()
                elif flag == 2:
                    iden=no_reps(famillia,iden,flag,reps_f)
                    famillia.append(iden)
                    iden = family(iden, hid, wid, dom, doe, cid)
                    #y.add_row([iden, hid, wid, dom, doe, cid])
                    iden.cout()                    
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
                            dob=getdate(words[2],words[3],words[4])
                    elif tag == "DEAT":
                        line=next(file)
                        words=line.split()
                        if words[1]=="DATE":
                            dod=getdate(words[2],words[3],words[4])
                    elif tag == "FAMC":
                        famc=words[-1]
                    elif tag == "FAMS":
                        fams=words[-1]
                    elif tag == "HUSB":
                        hid = words[-1]
                    elif tag == "WIFE":
                        wid = words[-1]
                    elif tag == "CHIL":
                        cid.append(words[-1])
                    elif tag == "MARR":
                        line=next(file)
                        words=line.split()
                        if words[1]=="DATE":
                            dom=getdate(words[2],words[3],words[4])
                    elif tag == "DIV":
                        line=next(file)
                        words=line.split()
                        if words[1]=="DATE":
                            doe=getdate(words[2],words[3],words[4])

except FileNotFoundError:
    # File not found
    print ( "\nSorry the file : " + filename + " does not exist.\n" )
