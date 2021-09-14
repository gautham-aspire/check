#Employee management system
#Author G Gautham
#modified on 17-Aug-2021 6:30pm
#modified by G Gautham

import re
import math
import datetime
from datetime import date


def validateempname():
    ename=input("enter employee first name");
    if(bool(re.match('^[a-zA-Z]*$', ename)) == True and len(ename)>3 and ename.isspace()==False):
        print(ename);
    else:
        print("incorrect name,your name should not contain space,numbers or special characters");
        validateempname()
        


def validatedob():
    year=int(input("enter birth year"));
    month=int(input("enter month number"));
    day=int(input("enter day of month"));
    born = datetime.datetime(year,month,day);
    age=(datetime.datetime.now()-born);
    convertdays=int(age.days);
    ageyears=convertdays/365
    if(ageyears>=18 and ageyears<=60):
        print(f"Age is {ageyears} years");
    else:
        print("your age should be less than 60 years and greater than 18 years  so enter a valid dob");
        validatedob()


def validatedoj():
    year=int(input("enter joining year"));
    month=int(input("enter joining month"));
    day=int(input("enter day of joining"));
    joining = datetime.datetime(year,month,day);
    exp=(datetime.datetime.now()-joining);
    convertdays=int(exp.days);
    expyears=(convertdays/365);
    if(expyears>0):
        print(f"experience is {expyears} years");
    else:
        print("invalid doj,doj cannot be in future");
        validatedoj();
   


def validateempid():
    eid=input("enter  4 digit employee id without 'ACE' ex:5698");
    if(bool(re.match('^[0-9]', eid)) == True and len(eid)==4 and int(eid)>0):
        print("ACE"+eid);
    else:
        print("incorrect id,enter  4 digit employee id without 'ACE' ex:5698");
        validateempid()

def validateeph():
    ephn= input("enter 10 digit phone number starting with 6,7,8 or 9");
    if(bool(re.match('^[0-9]', ephn)) == True and len(ephn)==10 and int(ephn)>=6000000000):
        print(ephn);
    else:
        print("incorrect phone number, your number should contain 10 digits and start with 6,7,8 or 9");
        validateeph()
    
def validateempsal():
    sal=input("enter salary in the range of 1000-1000000 rs");
    if(int(sal)>=1000 and int(sal)<=1000000):
        print(sal);
    else:
        print("invalid salary your salary should be in 1000-1000000 rs range");
        validateempsal()

def validateemail():
    empemail=input("enter email ID ex:jack51@gmail.com");
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z.]+.[A-Z|a-z]\b';
    if(re.fullmatch(regex, empemail)):
        print(empemail);
    else:
        print("Invalid Email, email should not contain numeric,space,special characters except '.' after '@'")
        validateemail();
        
    

    
def validatequalification():
    choice=int(input(" Select qualification 1. B.Tech 2. MCA 3.BCA 4.B.sc 5.others"));
    if(choice==1):
        print("B.Tech")
    else:
        if(choice==2):
            print("MCA")
        else:
            if(choice==3):
                print("BCA")
            else:
                if(choice==4):
                    print("B.sc")
                else:
                    if(choice==5):
                        print("please specify")
                        course=input("enter course name");
                        print(course);
                    else:
                        print("please give a valid input,valid entries are 1,2,3,4 and 5");
                        validatequalification()
        
def nextemployee():
    cont1=input("if you want to continue then press 'Y' else press 'N'");
    if (cont1=='Y'):
        return 'Y';
    else:
        if(cont1=='N'):
            return 'N';
        else:
            print("invalid input please enter 'Y' or 'N'");
            nextemployee();
    
cont='Y';
while(cont=='Y'):
    validateempname()
    validateempid()
    validateeph()
    validateempsal()
    validateemail()
    validatedob()
    validatedoj()
    validatequalification()
    cont=nextemployee();
    
         

