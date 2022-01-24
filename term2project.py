#IMPORTING MODULES

import datetime as dt
from datetime import datetime
import time as t
import os
import csv
import hashlib
import getpass

#------------------------------------------------

#DECLARING LISTS

studentrec=[]
bookrec=[]
currentissuedrecords=[]

#------------------------------------------------

#LOGIN SYSTEM

def password():
    ps='728db48989c9878bdb727058ae0d0968c5902f488dd9e3d4a4aa3f90410da5566fd0ca5f59c6a58154cce2e5c8e7a2586a79d88397d12c46b830ee50890971eb'
    gib=getpass.getpass('Enter your password: ')
    hash = hashlib.sha512(gib.encode('utf8')).hexdigest()

    if hash == ps:
        print('correct password')
        os.system('cls')
    else:
        print('wrong password')
        password()

password()

#------------------------------------------------

#READING CSV FILES

with open('Studentname.csv',newline='') as a:
    read= csv.reader(a)
    for row in read:
        studentrec.append(row)

with open('bookrecord.csv',newline='') as b:
    read= csv.reader(b)
    for row in read:
        bookrec.append(row)

with open('currentissuedbooks.csv',newline='') as c:
    read= csv.reader(c)
    for row in read:
        currentissuedrecords.append(row)

#------------------------------------------------

#EXCEPTION HANDLING

def exceptionraise_admnum():
    try:
        a=int(input('enter admission number'))
        return(a)
    except ValueError or TypeError:
        print("Enter in correct format")
        exceptionraise_admnum()

def exceptionraise_cls():
    try:
        a=int(input('enter your class'))
        if a<10:
            newa='0'+str(a)
            if newa == '000' or newa == '00':
                print('enter in proper format')
                exceptionraise_cls()

            return(newa)
        else:
            return(a)
    except ValueError or TypeError:
        print("Enter in correct format")
        exceptionraise_cls()

def exceptionraise_bookid():
    try:
        a=int(input('enter book id'))
        return(a)
    except ValueError or TypeError:
        print("Enter in correct format")
        exceptionraise_bookid()

def exceptionraise_choice():
    try:
        a=int(input('enter your choice'))
        return(a)
    except ValueError or TypeError:
        print("Enter in correct format")
        exceptionraise_choice()

def exceptionraise_ib():
    try:
        a=int(input('enter for how many days you want to issue the book: '))
        return(a)
    except ValueError or TypeError:
        print("Enter in correct format")
        exceptionraise_ib()

#------------------------------------------------

#FUNCTIONS

def choice1func():
    admnno=exceptionraise_admnum()
    while len(str(admnno))!=4:
        print('Invalid format please re-enter the admission number ')
        admnno=exceptionraise_admnum()
    name=input('enter the name of child ')
    cls=exceptionraise_cls()
    while len(str(cls)) != 2 :
        print('Enter the class in two digits (If you class is 8 enter 08)')
        cls=exceptionraise_cls()
    cls=int(cls)
        
    sec=input('enter your section ')
    while len(sec) != 1:
        print('enter in a proper format')
        sec=input('enter your section ')
    student=[]
    student.append(admnno)
    student.append(name.upper())
    student.append(cls)
    student.append(sec.upper())
    studentrec.append(student)
    print("student added succesfully")

def choice2func():
    bookname=input("enter book name")
    bookid=exceptionraise_bookid()
    book=[]
    book.append(bookid)
    book.append(bookname.upper())
    bookrec.append(book)
    print("Book added successfully")

def choice3func():
    admnno_ib=exceptionraise_admnum()
    book_ib=input("Enter the name of the book")
    book_ib=book_ib.upper()

    while len(str(admnno_ib))!=4:
        print('Invalid format please re-enter the admission number ')
        admnno_ib=exceptionraise_admnum()


    for i in studentrec:
        if int(i[0]) == int(admnno_ib):
            class_stib=i[2]
            section_stib=i[3]
            name_stib=i[1]
            break
    else:
        print('Record not found')
        t.sleep(1)
        os.system('cls')
        mainmenue()

    book_ib=book_ib.upper()
    for i in bookrec:
        if i[1]==book_ib:
            bookname_ib=i[1]
            bookcode_ib=i[0]
            break
    else:
        print('book not found')
        t.sleep(1)
        os.system('cls')
        mainmenue()
    
    todaydate=dt.date.today()
    durationofib=exceptionraise_ib()
    datereturn=todaydate+dt.timedelta(durationofib)
    print('\nName: ',name_stib,'\n','Admission number: ',admnno_ib,'\n','Class and Section: ',class_stib,'-',section_stib,'\n','Book issued: ',bookname_ib)
    print('\nYour due date is: ',datereturn)

    studentbookprofile=[]
    studentbookprofile.append(admnno_ib)
    studentbookprofile.append(name_stib)
    studentbookprofile.append(class_stib)
    studentbookprofile.append(section_stib)
    studentbookprofile.append(todaydate)
    studentbookprofile.append(datereturn)
    studentbookprofile.append(bookname_ib)
    studentbookprofile.append(bookcode_ib)
    currentissuedrecords.append(studentbookprofile)
    print("Book issued successfully")

def choice4func():
    admnno_returnbook=exceptionraise_admnum()
    name_returnbook=input('Input enter you name')
    name_returnbook=name_returnbook.upper()
    for i in currentissuedrecords:
        if i[0]==str(admnno_returnbook) and i[1]==name_returnbook:
            currentissuedrecords.remove(i)
            print('Book returned successfully')
            t.sleep(2)
            os.system('cls')
            mainmenue()
        else:
            print('Record not found')
            t.sleep(2)
            os.system('cls')
            mainmenue()

def choice5func():

    admnno1=exceptionraise_admnum()
    while len(str(admnno1))!=4:
        print('Invalid format please re-enter the admission number ')
        admnno1=exceptionraise_admnum()
    for i in currentissuedrecords:
        if i[0] == admnno1:
            break
        break
    else:
        print('Record not found')
        t.sleep(1)
        os.system('cls')
        mainmenue()
    
        
    newl=i[5].split('-')
    year=int(newl[0])
    month=int(newl[1])
    day=int(newl[2])

    checkfine_returndate=dt.date(year,month,day)
    todaydate=dt.date.today()
    checkfine_days=todaydate-checkfine_returndate
    
    checkfine_days=str(checkfine_days)
    checkfine_days=checkfine_days.split(' days,')

    print('You are',checkfine_days[0],'days late')

    if 0<int(checkfine_days[0])<=5:
        print('Your fine is: ₹',int(checkfine_days[0])*2)
    elif 6<=int(checkfine_days[0])<=15:
        print('Your fine is: ₹', int(checkfine_days[0])*4)
    elif int(checkfine_days[0])>=16:
        print('Your fine is: ₹', int(checkfine_days[0])*5)   

def choice6func():
    checkperson=input('enter the name of the person')
    for i in currentissuedrecords:
        if i[1]==checkperson.upper():
            print(i[5])
            break
    else:
        print('record not found')
        t.sleep(1)
        os.system('cls')
        mainmenue()

def choice7func():
    print('''
         Find by:
         1)Student name
         2)Student's Admission number
        ''')
    st=exceptionraise_choice()
    if st == 1:
        name1=input('enter the name of the student ')
        name1=name1.upper()
        for i in studentrec:
            if i[1] == name1:
                print(i)
                break
        else:
            print('Record not found')
            t.sleep(1)
            os.system('cls')
            mainmenue()

    elif st == 2:
        admnno1=exceptionraise_admnum()
        while len(str(admnno1))!=4:
            print('Invalid format please re-enter the admission number ')
            admnno1=exceptionraise_admnum()
        for i in studentrec:
            if i[0] == admnno1:
                print(i)
                break
        else:
            print('Record not found')
            t.sleep(1)
            os.system('cls')
            mainmenue()

def choice8func():
    print('''
        Find by:
        1)Book name
        2)Book id
        ''')
    bk=exceptionraise_choice()
    if bk == 1:
        bookname1=input('enter the name of the book ')
        bookname1=bookname1.upper()
        for i in bookrec:
            if i[1]==bookname1:
                print(i)
                break
        else:
            print('record not found')
            t.sleep(1)
            os.system('cls')
            mainmenue()
    elif bk ==2:
        bookid1=exceptionraise_bookid()
        for i in bookrec:
            if i[0]==bookid1:
                print(i)
                break
        else:
            print('record not found')
            t.sleep(1)
            os.system('cls')
            mainmenue()

def choice9func():
    with open('Studentname.csv', 'w',newline='') as x: 
        write = csv.writer(x)
        write.writerows(studentrec) 
    with open('bookrecord.csv', 'w',newline='') as y: 
        write = csv.writer(y) 
        write.writerows(bookrec)
    with open('currentissuedbooks.csv', 'w',newline='') as z: 
        write = csv.writer(z) 
        write.writerows(currentissuedrecords)
    os.system('exit')

#------------------------------------------------

#INTEGRATING PROGRAM

def mainmenue():
    print('''
                              _      _  _                              
                             | |    (_)| |                             
                             | |     _ | |__   _ __  __ _  _ __  _   _ 
                             | |    | || '_ \ | '__|/ _` || '__|| | | |
                             | |____| || |_) || |  | (_| || |   | |_| |
                             \_____/|_||_.__/ |_|   \__,_||_|    \__, |
                                                                  __/ |
                                                                 |___/ 
              ___  ___                                                           _   
              |  \/  |                                                          | |  
              | .  . |  __ _  _ __    __ _   __ _   ___  _ __ ___    ___  _ __  | |_ 
              | |\/| | / _` || '_ \  / _` | / _` | / _ \| '_ ` _ \  / _ \| '_ \ | __|
              | |  | || (_| || | | || (_| || (_| ||  __/| | | | | ||  __/| | | || |_ 
              \_|  |_/ \__,_||_| |_| \__,_| \__, | \___||_| |_| |_| \___||_| |_| \__|
                                             __/ |                                   
                                            |___/                                    
                               _____              _                   
                              /  ___|            | |                  
                              \ `--.  _   _  ___ | |_  ___  _ __ ___  
                               `--. \| | | |/ __|| __|/ _ \| '_ ` _ \ 
                              /\__/ /| |_| |\__ \| |_|  __/| | | | | |
                              \____/  \__, ||___/ \__|\___||_| |_| |_|
                                       __/ |                          
                                      |___/                           
   

    ┌──────┬──────────────────────────┐
    │ S.NO │        ACTIONS           │
    ├──────┼──────────────────────────┤             ,..........   ..........,
    │      │                          │           ,..,'          '.'          ',..,
    │  1   │   Add new student        │          ,' ,'            :            ', ',
    │  2   │   Add new book           │         ,' ,'             :             ', ',
    │  3   │   Issue new book         │        ,' ,'              :              ', ',
    │  4.  │   Return a book          │       ,' ,'............., : ,.............', ',
    │  5.  │   Calculate fine         │      ,'  '............   '.'   ............' ',
    │  6   │   Check Due Date         │        ''''''''''''''''''''''''''''''''''''''
    │  7   │   Find student           │                         
    │  8   │   Find Book              │
    │  9   │   Exit                   │
    └──────┴──────────────────────────┘

    ''')
    choice=exceptionraise_choice()
    if choice==1:
        choice1func()
        t.sleep(1)
        os.system('cls')
        mainmenue()
    elif choice==2:
        choice2func()
        t.sleep(1)
        os.system('cls')
        mainmenue()
    elif choice==3:
        choice3func() 
        t.sleep(4)
        os.system('cls')
        mainmenue()
    elif choice==4:
        choice4func() 
        t.sleep(4)
        os.system('cls')
        mainmenue()
    elif choice==5:
        choice5func() 
        t.sleep(4)
        os.system('cls')
        mainmenue()
    elif choice==6:
        choice6func()
        t.sleep(1)
        os.system('cls')
        mainmenue()
    elif choice==7:
        choice7func()
        t.sleep(4)
        os.system('cls')
        mainmenue()
    elif choice==8:
        choice8func()
        t.sleep(4)
        os.system('cls')
        mainmenue()
    elif choice==9:
        choice9func()
    else:
        print("No option found as option",choice)
        mainmenue()

mainmenue()

#------------------------------------------------