#! /usr/bin/python3
import pymysql # mysql-connector-python
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
import tkinter.messagebox
import re
import datetime
import random

# user  user123456 u1@beltline.com not approved
# visitor visitor123 v1@beltline.com
# adm dsmith456 dsmith@outlook.com
# man manager1 m1@beltline.com
# man,vis manager2 m2@beltline.com
# sta staff1234 s1@beltline.com
# sta,vis staff7890 s3@beltline.com

class DB:
    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        passwd = "Evdot0404MySQL"
        database = "CS4400_T77"
        self.conn = pymysql.connect(host=host,user=user,passwd=passwd,database=database)
        # if self.conn.is_connected():
        #     print("Connect to MySQL database")
        self.cursor = self.conn.cursor()

    def __del__(self): #destructor
        self.cursor.close()

    def close(self):
        self.cursor.close()
        self.conn.close()

    # Seach database
    def search(self,arg):
        self.cursor.execute(arg)
        rows = self.cursor.fetchall()
        return rows

    # Insert database
    def insert(self,arg):
        self.cursor.execute(arg)
        self.conn.commit()

    # Update database
    def update(self,arg):
        self.cursor.execute(arg)
        self.conn.commit()

    # Delete from database
    def delete(self,arg):
        self.cursor.execute(arg)
        self.conn.commit()
# Mutural functions 
username_login = ['staff3']

take_transit = ['']
transit_his = ['']
man_profile = ['']
man_user = ['']
man_transit = ['']
man_site = ['']
exp_site = ['']
exp_event = ['']
vis_his = ['']
man_event = ['']
view_site_report = ['']
view_sta = ['']
view_schedule = ['']
newemail = []
newemail_vis = []
newemail_emp = []
newemail_emp_and_vis = []
newemail_profile = ['m2@beltline.com']
oriemail_profile = ['m2@beltline.com']
site_to_be_edited = ['']
transit_to_be_edited = ['']
site_daily_detail = ['']
event_to_be_edited = ['']
whos_site = ['']
event_to_view = ['']

#1 finished
def WIN_user_login():
    db = DB()
    # Initialization
    window = Tk()
    window.title("User Login")
    window.geometry('400x200')
    window.resizable(0, 0)
    window.configure(background="#fff")

    # Labels
    l0 = Label(window, text="Atlanta Beltline Login", width=36,font=('Arial', 18, 'bold'))
    l0.place(x=10,y=20)

    l1 = Label(window, text="Email",font=('Times 14 normal'))
    l1.place(x=25,y=60)

    l2 = Label(window, text="Password",font=('Times 14 normal'))
    l2.place(x=25,y=100)

    #entry
    e1_content = StringVar()
    e1 = Entry(window,width=20, bg='powder blue',textvariable=e1_content)
    """ focus is that as soon as the GUI appears, we can type into this text box without having to click it first """
    e1.focus() 
    e1.place(x=150,y=60)
    # e1.focus_set()

    e2_content = StringVar()
    e2 = Entry(window,width=20, bg='powder blue',textvariable=e2_content,show='*')
    e2.place(x=150,y=100)

    # Buttons
    def login(password):
        command = "SELECT U.etype FROM user as U " + "WHERE U.password='" + password + "'"
        etype = db.search(command)
        command = "SELECT U.username FROM user as U " + "WHERE U.password='" + password + "'"
        username = db.search(command)
        username_login[0] = username[0][0]
        # print(username_login[0])

        # For WIN17 profiles
        command = "SELECT * FROM manage_profile WHERE username='" + username_login[0] + "'"
        profile = db.search(command)
        for info in profile:
            newemail_profile.append(info[7])
            oriemail_profile.append(info[7])

        if 'Employee' in etype[0]:
            username_tmp = str(username[0][0])
            command = "SELECT Em.etype FROM employee as Em " + "WHERE Em.eusername='" + username_tmp + "'"
            etype_emp = db.search(command)
            if 'Admin' in etype_emp[0]:
                WIN_FUN_adm();db.close() 
            elif 'Manager' in etype_emp[0]:
                WIN_FUN_man();db.close()
            elif 'Staff' in  etype_emp[0]:
                WIN_FUN_sta();db.close()
        elif 'employee,visitor' in etype[0]:
            username_tmp = str(username[0][0])
            command = "SELECT Em.etype FROM employee as Em " + "WHERE Em.eusername='" + username_tmp + "'"
            etype_emp = db.search(command)
            if 'Admin' in etype_emp[0]:
                WIN_FUN_adm_and_vis();db.close()
            elif 'Manager' in etype_emp[0]:
                WIN_FUN_man_and_vis();db.close()
            elif 'Staff' in etype_emp[0]:
                WIN_FUN_sta_and_vis();db.close()
        elif 'User' in etype[0]:
            WIN_FUN_user();db.close()
        elif 'Visitor' in etype[0]:
            WIN_FUN_vis();db.close()

    def checkaccount():
        email = e1_content.get()
        password = e2_content.get() 
        command = "SELECT E.email,U.password FROM user as U JOIN email as E on E.username = U.username WHERE U.status='Approved'"
        email_and_password = db.search(command)
        if (email,password) in email_and_password:
            window.destroy()
            login(password)
        else: 
            tkinter.messagebox.showwarning('Invalid Account','Incorrect email and password combination!')

    def register():
        window.destroy()
        WIN_regi_nav();db.close()
 
    b1 = Button(window, text="Login", width=6, height=2,bg='white',fg='grey',font=('Arial 9 bold'), command=(lambda: checkaccount()))
    b1.place(x=75,y=150)

    b2 = Button(window, text="Register", width=8, height=2,bg='white',fg='grey',font=('Arial 9 bold'), command=(lambda: register()))
    b2.place(x=250,y=150)

    window.mainloop()
#2 finished
def WIN_regi_nav():

    window = Tk()
    window.title("Register Navigation")
    window.geometry('250x250')
    window.resizable(0, 0)
    window.configure(background="#fff")

    def navigation(number):
        window.destroy()
        if   number == 0:
            WIN_regi_user()
        elif number == 1:
            WIN_regi_vis()
        elif number == 2:
            WIN_regi_emp()
        elif number == 3:
            WIN_regi_emp_and_vis()

    def back():
        window.destroy()
        WIN_user_login()

    l0 = Label(window,text="Register Navigation", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    b1 = Button(window,text="User Only", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(0)))
    b1.place(x=75,y=60)

    b2 = Button(window,text="Visitor Only", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(1)))
    b2.place(x=75,y=90)

    b3 = Button(window,text="Employee Only", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(2)))
    b3.place(x=75,y=120)

    b4 = Button(window,text="Employee-Visitor", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda:navigation(3)))
    b4.place(x=75,y=150)

    b5 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: back()))
    b5.place(x=75,y=180)

    window.mainloop()
#3 finished
def WIN_regi_user():
    db = DB()
    geometry = '600x' + str(len(newemail)*40+300)

    window = Tk()
    window.title("Register User")
    window.geometry(geometry)
    window.resizable(0, 0)
    window.configure(background="#fff")

    def confirmpwd():
        if len(e3_content.get()) < 8 :
            tkinter.messagebox.showwarning('Password Error','Password should at least 8 characters')  
        elif e3_content.get() != e5_content.get():
            tkinter.messagebox.showwarning('Not same password','Incorrect confirmed password, try again!')
        else:return e3_content.get()

    def checkusername():
        command = 'SELECT username FROM user'
        usernames_tmp = db.search(command)
        usernames = []
        for user in usernames_tmp:
            usernames.append(user[0])
        if e2_content.get() in usernames:
            tkinter.messagebox.showwarning('Existed Username','The username exists, try another username!')
        else:return e2_content.get()

    def checkemail():
        command = 'SELECT email FROM email'
        emails_tmp = db.search(command)
        emails = []
        for email in emails_tmp:
            emails.append(email[0])
        if not re.match(r'^[0-9a-zA-Z]+@{1}[0-9a-zA-Z]+\.{1}[0-9a-zA-Z]+',e6_content.get()):
            tkinter.messagebox.showwarning('Email Error','Not valid email!')
        elif e6_content.get() in emails:
            tkinter.messagebox.showwarning('Existed Email','The email exists, try another email!')
        elif e6_content.get() in newemail:
            tkinter.messagebox.showwarning('Existed Email','The email exists, try another email!')
        else:
            newemail.append(e6_content.get())
    
    def register_checks():
        if e1_content.get() == '':
            tkinter.messagebox.showwarning('First Name Error','First Name should not be none')
        if e4_content.get() == '':
            tkinter.messagebox.showwarning('Last Name Error','Last Name should not be none')
        if e2_content.get() == '':
            tkinter.messagebox.showwarning('Username Error','Username should not be none')  
        if len(newemail) == 0:
            tkinter.messagebox.showwarning('Email Error','Email should not be none')  
        fname = "fname='" + e1_content.get() + "'"
        lname = "lname='" + e4_content.get() + "'"
        password_tmp = confirmpwd()
        username_tmp = checkusername()
        if None not in (fname,lname,password_tmp,username_tmp) and newemail != []:
            password = "password='" + password_tmp + "'"
            username = "username='" + username_tmp + "'"
            etype = "etype='User'"
            command = "INSERT INTO user SET status='Pending'," + username + "," + password + "," + fname + "," + lname + "," + etype
            db.insert(command)
            for email_tmp in newemail:     
                email = "email='" + email_tmp + "'"
                command = "INSERT INTO email SET " + username + "," + email
                db.insert(command)
            window.destroy()
            newemail.clear()
            db.close()
            WIN_user_login()

    def addemail():
        checkemail()
        window.destroy()
        WIN_regi_user()

    def removeemail(email):
        newemail.remove(email)
        window.destroy()
        WIN_regi_user()

    def back():
        window.destroy()
        newemail.clear()
        db.close()
        WIN_regi_nav()

    l0 = Label(window,text="Register User", width=36,font=('Arial', 18, 'bold'))
    l0.place(x=100,y=0)

    l1 = Label(window,text="Fisrt Name", font=('Times 14 normal'))
    l1.place(x=25,y=60)
    
    l2 = Label(window,text="Username", font=('Times 14 normal'))
    l2.place(x=25,y=100)

    l3 = Label(window,text="Password", font=('Times 14 normal'))
    l3.place(x=25,y=140)

    l4 = Label(window,text="Last Name", font=('Times 14 normal'))
    l4.place(x=275,y=60)
    
    l5 = Label(window,text="Confirm Password",font=('Times 14 normal'))
    l5.place(x=275,y=140)

    l6 = Label(window,text="Email", font=('Times 14 normal'))
    l6.place(x=25,y=180)

    labelname = {}
    buttonname = {}
    for email in newemail:
        i = newemail.index(email)
        labelname[email] = Label(window,text=newemail[i], font=('Times 12 normal'))
        labelname[email].place(x=120,y=180 + i*40) 
        buttonname[email] = Button(window,text="Remove", width=6, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: removeemail(email)))  
        buttonname[email].place(x=400,y=180 + i*40)   

    e1_content = StringVar()
    e1 = Entry(window,width=14, bg='powder blue',textvariable=e1_content)
    e1.focus()
    e1.place(x=120,y=60)

    e2_content = StringVar()
    e2 = Entry(window,width=14, bg='powder blue',textvariable=e2_content)
    e2.place(x=120,y=100)

    e3_content = StringVar()
    e3 = Entry(window,width=14, bg='powder blue',textvariable=e3_content,show='*')
    e3.place(x=120,y=140)

    e4_content = StringVar()
    e4 = Entry(window,width=14, bg='powder blue',textvariable=e4_content)
    e4.place(x=400,y=60)

    e5_content = StringVar()
    e5 = Entry(window,width=14, bg='powder blue',textvariable=e5_content,show='*')
    e5.place(x=400,y=140)

    e6y = len(newemail)*40 + 180

    e6_content = StringVar()
    e6 = Entry(window,width=20, bg='powder blue',textvariable=e6_content)
    e6.place(x=120,y=e6y)

    b3 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: back()))
    b3.place(x=175,y=250+len(newemail)*40)

    b4 = Button(window,text="Register", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda:register_checks()))
    b4.place(x=325,y=250+len(newemail)*40)

    b6add = Button(window,text="Add", width=6, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: addemail()))
    b6add.place(x=400,y=e6y)

    window.mainloop()
#4 finished
def WIN_regi_vis():
    db = DB()
    geometry = '600x' + str(len(newemail_vis)*40+300)
    
    window = Tk()
    window.title("Register Visitor")
    window.geometry(geometry)
    window.resizable(0, 0)
    window.configure(background="#fff")

    def confirmpwd():
        if len(e3_content.get()) < 8 :
            tkinter.messagebox.showwarning('Password Error','Password should at least 8 characters')    
        elif e3_content.get() != e5_content.get():
            tkinter.messagebox.showwarning('Not same password','Incorrect confirmed password, try again!')
        else:return e3_content.get()

    def checkusername():
        command = 'SELECT username FROM user'
        usernames_tmp = db.search(command)
        usernames = []
        for user in usernames_tmp:
            usernames.append(user[0])
        if e2_content.get() in usernames:
            tkinter.messagebox.showwarning('Existed Username','The username exists, try another username!')
        else:return e2_content.get()

    def checkemail():
        command = 'SELECT email FROM email'
        emails_tmp = db.search(command)
        emails = []
        for email in emails_tmp:
            emails.append(email[0])
        if not re.match(r'^[0-9a-zA-Z]+@{1}[0-9a-zA-Z]+\.{1}[0-9a-zA-Z]+',e6_content.get()):
            tkinter.messagebox.showwarning('Email Error','Not valid email!')
        elif e6_content.get() in emails:
            tkinter.messagebox.showwarning('Existed Email','The email exists, try another email!')
        elif e6_content.get() in newemail_vis:
            tkinter.messagebox.showwarning('Existed Email','The email exists, try another email!')
        else:
            newemail_vis.append(e6_content.get())
    
    def register_checks():
        if e1_content.get() == '':
            tkinter.messagebox.showwarning('First Name Error','First Name should not be none')
        if e4_content.get() == '':
            tkinter.messagebox.showwarning('Last Name Error','Last Name should not be none')
        if e2_content.get() == '':
            tkinter.messagebox.showwarning('Username Error','Username should not be none')  
        if len(newemail_vis) == 0:
            tkinter.messagebox.showwarning('Email Error','Email should not be none')  
        fname = "fname='" + e1_content.get() + "'"
        lname = "lname='" + e4_content.get() + "'"
        password_tmp = confirmpwd()
        username_tmp = checkusername()
        if None not in (fname,lname,password_tmp,username_tmp) and newemail_vis != []:
            password = "password='" + password_tmp + "'"
            username = "username='" + username_tmp + "'"
            etype = "etype='Visitor'"
            command = "INSERT INTO user SET status='Pending'," + username + "," + password + "," + fname + "," + lname + "," + etype
            db.insert(command)
            for email_tmp in newemail_vis:     
                email = "email='" + email_tmp + "'"
                command = "INSERT INTO email SET " + username + "," + email
                db.insert(command)
            window.destroy()
            newemail_vis.clear()
            db.close()
            WIN_user_login()

    def addemail():
        checkemail()
        window.destroy()
        WIN_regi_vis()

    def removeemail(email):
        newemail_vis.remove(email)
        window.destroy()
        WIN_regi_vis()

    def back():
        window.destroy()
        newemail_vis.clear()
        db.close()
        WIN_regi_nav()

    l0 = Label(window,text="Register Visitor", width=36,font=('Arial', 18, 'bold'))
    l0.place(x=100,y=0)

    l1 = Label(window,text="Fisrt Name", font=('Times 14 normal'))
    l1.place(x=25,y=60)
    
    l2 = Label(window,text="Username", font=('Times 14 normal'))
    l2.place(x=25,y=100)

    l3 = Label(window,text="Password", font=('Times 14 normal'))
    l3.place(x=25,y=140)

    l4 = Label(window,text="Last Name", font=('Times 14 normal'))
    l4.place(x=275,y=60)
    
    l5 = Label(window,text="Confirm Password",font=('Times 14 normal'))
    l5.place(x=275,y=140)

    l6 = Label(window,text="Email", font=('Times 14 normal'))
    l6.place(x=25,y=180)

    labelname = {}
    buttonname = {}
    for email in newemail_vis:
        i = newemail_vis.index(email)
        labelname[email] = Label(window,text=newemail_vis[i], font=('Times 12 normal'))
        labelname[email].place(x=120,y=180 + i*40) 
        buttonname[email] = Button(window,text="Remove", width=6, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: removeemail(email)))  
        buttonname[email].place(x=400,y=180 + i*40)   

    e1_content = StringVar()
    e1 = Entry(window,width=14, bg='powder blue',textvariable=e1_content)
    e1.focus()
    e1.place(x=120,y=60)

    e2_content = StringVar()
    e2 = Entry(window,width=14, bg='powder blue',textvariable=e2_content)
    e2.place(x=120,y=100)

    e3_content = StringVar()
    e3 = Entry(window,width=14, bg='powder blue',textvariable=e3_content,show='*')
    e3.place(x=120,y=140)

    e4_content = StringVar()
    e4 = Entry(window,width=14, bg='powder blue',textvariable=e4_content)
    e4.place(x=400,y=60)

    e5_content = StringVar()
    e5 = Entry(window,width=14, bg='powder blue',textvariable=e5_content,show='*')
    e5.place(x=400,y=140)

    e6y = len(newemail_vis)*40 + 180

    e6_content = StringVar()
    e6 = Entry(window,width=20, bg='powder blue',textvariable=e6_content)
    e6.place(x=120,y=e6y)

    b3 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: back()))
    b3.place(x=175,y=250+len(newemail_vis)*40)

    b4 = Button(window,text="Register", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda:register_checks()))
    b4.place(x=325,y=250+len(newemail_vis)*40)

    b6add = Button(window,text="Add", width=6, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: addemail()))
    b6add.place(x=400,y=e6y)

    window.mainloop()
#5 #!NEED TEST
def WIN_regi_emp():
    db = DB()
    geometry = '600x' + str(len(newemail_emp)*40+400)

    window = Tk()
    window.title("Register Employee")
    window.geometry(geometry)
    window.resizable(0, 0)
    window.configure(background="#fff")

    def confirmpwd():
        if len(e3_content.get()) < 8 :
            tkinter.messagebox.showwarning('Password Error','Password should at least 8 characters')  
        elif e3_content.get() != e5_content.get():
            tkinter.messagebox.showwarning('Not same password','Incorrect confirmed password, try again!')
        else:return e3_content.get()

    def checkusername():
        command = 'SELECT username FROM user'
        usernames_tmp = db.search(command)
        usernames = []
        for user in usernames_tmp:
            usernames.append(user[0])
        if e2_content.get() in usernames:
            tkinter.messagebox.showwarning('Existed Username','The username exists, try another username!')
        else:return e2_content.get()

    def checkemail():
        command = 'SELECT email FROM email'
        emails_tmp = db.search(command)
        emails = []
        for email in emails_tmp:
            emails.append(email[0])
        if not re.match(r'^[0-9a-zA-Z]+@{1}[0-9a-zA-Z]+\.{1}[0-9a-zA-Z]+',e6_content.get()):
            tkinter.messagebox.showwarning('Email Error','Not valid email!')
        elif e6_content.get() in emails:
            tkinter.messagebox.showwarning('Existed Email','The email exists, try another email!')
        else:
            newemail_emp.append(e6_content.get())

    def checkphone():
        command = 'SELECT phone FROM employee'
        phones = db.search(command)
        if e8_content.get() == '':
            tkinter.messagebox.showwarning('Phone Error','Phone should not be none')  
        elif not re.match('^[0-9]{9}',e8_content.get()):
            tkinter.messagebox.showwarning('Phone Error','Not valid phone!')
        elif e8_content.get() in phones:
            tkinter.messagebox.showwarning('Existed Phone','The phone exists, try another phone!')
        else:return e8_content.get()

    def checkzipcode():
        if e12_content.get() == '':
            tkinter.messagebox.showwarning('Zipcode Error','Zipcode should not be none')  
        elif not re.match('^[0-9]{5}',e12_content.get()):
            tkinter.messagebox.showwarning('Zipcode Error','Not valid zipcode!')
        else:return e12_content.get()

    def register_checks():
        if e1_content.get() == '':
            tkinter.messagebox.showwarning('First Name Error','First Name should not be none')
        if e4_content.get() == '':
            tkinter.messagebox.showwarning('Last Name Error','Last Name should not be none')
        if e2_content.get() == '':
            tkinter.messagebox.showwarning('Username Error','Username should not be none')  
        if len(newemail_emp) == 0:
            tkinter.messagebox.showwarning('Email Error','Email should not be none')  
        fname = e1_content.get()
        lname = e4_content.get()
        password = confirmpwd()
        phone = checkphone()
        username = checkusername()
        if e10_content.get() == '':
            tkinter.messagebox.showwarning('City Error','City should not be none') 
        city = e10_content.get() 
        state = option11.get()
        address = e9_content.get()
        usertype = option7.get()
        zipcode = checkzipcode()
        status = "Pending"
        comusertype = "Employee"
        
        command = "SELECT employeeID FROM employee ORDER BY employeeID"
        eids = db.search(command)
        leid = eids[-1][0]
        employeeid = int(leid) + 1
        employeeid = '0' * (9 - len(list(str(int(leid) + 1)))) + str(employeeid)
           
        if None not in (fname,lname,password,username,phone,zipcode,city,state,usertype,address) and newemail_emp != []:
            try:
                command = "INSERT INTO `employee` SET `employeeID`='" \
                                + employeeid + "'," + \
                            "`phone`=" + phone  + "," + \
                            "`address`='" + address + "'," + \
                            "`city` ='" + city + "'," + \
                            "`state`='" + state + "',"  +\
                            "`zipcode` = " + zipcode + "," + \
                            "`eusername`='" + username + "'" + \
                            "`etype`='" + usertype + "'"
                db.insert(command)
                command = "INSERT INTO `user` SET `username` ='" + username + "'," +   \
                            "`password` = '" + password + "'," + \
                            "`status` = '" + status + "'," + \
                            "`fname` = '" + fname + "'," + \
                            "`lname` = '" + lname + "'" + \
                            "`etype` = '" + comusertype + "'"
                db.insert(command)
                for email in newemail_emp:
                    command ="INSERT INTO `email` SET `username` ='" + username + "',email='" + email + "'"
                    db.insert(command)
            except:
                tkinter.messagebox.showwarning('Error','Incomplete information!') 

        window.destroy()
        WIN_user_login()

    def addemail():
        checkemail()
        window.destroy()
        WIN_regi_emp()

    def removeemail(email):
        # print(email)
        newemail_emp.remove(email)
        window.destroy()
        WIN_regi_emp()

    def back():
        window.destroy()
        WIN_regi_nav()

    l0 = Label(window,text="Register Employee", width=36,font=('Arial', 18, 'bold'))
    l0.place(x=100,y=0)

    l1 = Label(window,text="Fisrt Name", font=('Times 14 normal'))
    l1.place(x=25,y=60)
    
    l2 = Label(window,text="Username", font=('Times 14 normal'))
    l2.place(x=25,y=100)

    l3 = Label(window,text="Password", font=('Times 14 normal'))
    l3.place(x=25,y=140)

    l4 = Label(window,text="Last Name", font=('Times 14 normal'))
    l4.place(x=275,y=60)
    
    l5 = Label(window,text="Comfirm Password",font=('Times 14 normal'))
    l5.place(x=275,y=140)

    l6 = Label(window,text="Email", font=('Times 14 normal'))
    l6.place(x=25,y=260)

    l7 = Label(window,text="User Type", font=('Times 14 normal'))
    l7.place(x=275,y=100)
    
    l8 = Label(window,text="Phone", font=('Times 14 normal'))
    l8.place(x=25,y=180)

    l9 = Label(window,text="Address", font=('Times 14 normal'))
    l9.place(x=275,y=180)

    l10 = Label(window,text="City", font=('Times 14 normal'))
    l10.place(x=25,y=220)
    
    l11 = Label(window,text="State",font=('Times 14 normal'))
    l11.place(x=200,y=220)

    l12 = Label(window,text="Zipcode", font=('Times 14 normal'))
    l12.place(x=325,y=220)

    labelname = {}
    buttonname = {}
    for email in newemail_emp:
        i = newemail_emp.index(email)
        labelname[email] = Label(window,text=newemail_emp[i], font=('Times 12 normal'))
        labelname[email].place(x=120,y=260 + i*40) 
        buttonname[email] = Button(window,text="Remove", width=6, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: removeemail(email)))  
        buttonname[email].place(x=400,y=260 + i*40) 
    
    e1_content = StringVar()
    e1 = Entry(window,width=14, bg='powder blue',textvariable=e1_content)
    e1.place(x=120,y=60)

    e2_content = StringVar()
    e2 = Entry(window,width=14, bg='powder blue',textvariable=e2_content)
    e2.place(x=120,y=100)

    e3_content = StringVar()
    e3 = Entry(window,width=14, bg='powder blue',textvariable=e3_content,show='*')
    e3.place(x=120,y=140)

    e4_content = StringVar()
    e4 = Entry(window,width=14, bg='powder blue',textvariable=e4_content)
    e4.place(x=400,y=60)

    e5_content = StringVar()
    e5 = Entry(window,width=14, bg='powder blue',textvariable=e5_content,show='*')
    e5.place(x=400,y=140)

    e6y = len(newemail_emp)*40 + 260

    e6_content = StringVar()
    e6 = Entry(window,width=14, bg='powder blue',textvariable=e6_content)
    e6.place(x=120,y=e6y)

    e8_content = StringVar()
    e8 = Entry(window,width=14, bg='powder blue',textvariable=e8_content)
    e8.place(x=120,y=180)

    e9_content = StringVar()
    e9 = Entry(window,width=14, bg='powder blue',textvariable=e9_content)
    e9.place(x=400,y=180)

    e10_content = StringVar()
    e10 = Entry(window,width=6, bg='powder blue',textvariable=e10_content)
    e10.place(x=120,y=220)

    e12_content = StringVar()
    e12 = Entry(window,width=14, bg='powder blue',textvariable=e12_content)
    e12.place(x=400,y=220)

    option7 = StringVar()
    o7 = ttk.Combobox(window,width=12, textvariable=option7)
    o7['values'] = ('Manager','Staff')
    o7.place(x=400,y=100)
    o7.current(0)

    option11 = StringVar()
    o11 = ttk.Combobox(window,width=4, textvariable=option11)
    o11['values'] = ('AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','Other') 
    o11.place(x=250,y=220)
    o11.current(0)

    b3 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: back()))
    b3.place(x=175,y=350+len(newemail_emp)*40)

    b4 = Button(window,text="Register", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda:register_checks()))
    b4.place(x=325,y=350+len(newemail_emp)*40)

    b6add = Button(window,text="Add", width=6, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: addemail()))
    b6add.place(x=400,y=e6y)

    window.mainloop()
#6 #!NEED TEST
def WIN_regi_emp_and_vis():
    db = DB()
    geometry = '600x' + str(len(newemail_emp_and_vis)*40+400)

    window = Tk()
    window.title("Register Employee-Visitor")
    window.geometry(geometry)
    window.resizable(0, 0)
    window.configure(background="#fff")

    def confirmpwd():
        if len(e3_content.get()) < 8 :
            tkinter.messagebox.showwarning('Password Error','Password should at least 8 characters')  
        elif e3_content.get() != e5_content.get():
            tkinter.messagebox.showwarning('Not same password','Incorrect confirmed password, try again!')
        else:return e3_content.get()

    def checkusername():
        command = 'SELECT username FROM user'
        usernames_tmp = db.search(command)
        usernames = []
        for user in usernames_tmp:
            usernames.append(user[0])
        if e2_content.get() in usernames:
            tkinter.messagebox.showwarning('Existed Username','The username exists, try another username!')
        else:return e2_content.get()

    def checkemail():
        command = 'SELECT email FROM email'
        emails_tmp = db.search(command)
        emails = []
        for email in emails_tmp:
            emails.append(email[0])
        if not re.match(r'^[0-9a-zA-Z]+@{1}[0-9a-zA-Z]+\.{1}[0-9a-zA-Z]+',e6_content.get()):
            tkinter.messagebox.showwarning('Email Error','Not valid email!')
        elif e6_content.get() in emails:
            tkinter.messagebox.showwarning('Existed Email','The email exists, try another email!')
        else:
            newemail_emp_and_vis.append(e6_content.get())

    def checkphone():
        command = 'SELECT phone FROM employee'
        phones = db.search(command)
        if e8_content.get() == '':
            tkinter.messagebox.showwarning('Phone Error','Phone should not be none')  
        elif not re.match('^[0-9]{9}',e8_content.get()):
            tkinter.messagebox.showwarning('Phone Error','Not valid phone!')
        elif e8_content.get() in phones:
            tkinter.messagebox.showwarning('Existed Phone','The phone exists, try another phone!')
        else:return e8_content.get()

    def checkzipcode():
        if e12_content.get() == '':
            tkinter.messagebox.showwarning('Zipcode Error','Zipcode should not be none')  
        elif not re.match('^[0-9]{5}',e12_content.get()):
            tkinter.messagebox.showwarning('Zipcode Error','Not valid zipcode!')
        else:return e12_content.get()

    def register_checks():
        if e1_content.get() == '':
            tkinter.messagebox.showwarning('First Name Error','First Name should not be none')
        if e4_content.get() == '':
            tkinter.messagebox.showwarning('Last Name Error','Last Name should not be none')
        if e2_content.get() == '':
            tkinter.messagebox.showwarning('Username Error','Username should not be none')  
        if len(newemail_emp) == 0:
            tkinter.messagebox.showwarning('Email Error','Email should not be none')  
        fname = e1_content.get()
        lname = e4_content.get()
        password = confirmpwd()
        phone = checkphone()
        username = checkusername()
        if e10_content.get() == '':
            tkinter.messagebox.showwarning('City Error','City should not be none') 
        city = e10_content.get() 
        state = option11.get()
        address = e9_content.get()
        usertype = option7.get()
        zipcode = checkzipcode()
        status = "Pending"
        comusertype = "employee,visitor"
        
        command = "SELECT employeeID FROM employee ORDER BY employeeID"
        eids = db.search(command)
        leid = eids[-1][0]
        employeeid = int(leid) + 1
        employeeid = '0' * (9 - len(list(str(int(leid) + 1)))) + str(employeeid)
           
        if None not in (fname,lname,password,username,phone,zipcode,city,state,usertype,address) and newemail_emp != []:
            try:
                command = "INSERT INTO `employee` SET `employeeID`='" \
                                + employeeid + "'," + \
                            "`phone`=" + phone  + "," + \
                            "`address`='" + address + "'," + \
                            "`city` ='" + city + "'," + \
                            "`state`='" + state + "',"  +\
                            "`zipcode` = " + zipcode + "," + \
                            "`eusername`='" + username + "'" + \
                            "`etype`='" + usertype + "'"
                db.insert(command)
                command = "INSERT INTO `user` SET `username` ='" + username + "'," +   \
                            "`password` = '" + password + "'," + \
                            "`status` = '" + status + "'," + \
                            "`fname` = '" + fname + "'," + \
                            "`lname` = '" + lname + "'," + \
                            "`etype` = '" + comusertype + "'"
                db.insert(command)
                for email in newemail_emp_and_vis:
                    command ="INSERT INTO `email` SET `username` ='" + username + "',email='" + email + "'"
                    db.insert(command)
            except:
                tkinter.messagebox.showwarning('Error','Incomplete information!') 

        window.destroy()
        WIN_user_login()

    def addemail():
        checkemail()
        window.destroy()
        WIN_regi_emp_and_vis()

    def removeemail(email):
        # print(email)
        newemail_emp_and_vis.remove(email)
        window.destroy()
        WIN_regi_emp_and_vis()

    def back():
        window.destroy()
        WIN_regi_nav()

    l0 = Label(window,text="Register Employee-Visitor", width=36,font=('Arial', 18, 'bold'))
    l0.place(x=100,y=0)

    l1 = Label(window,text="Fisrt Name", font=('Times 14 normal'))
    l1.place(x=25,y=60)
    
    l2 = Label(window,text="Username", font=('Times 14 normal'))
    l2.place(x=25,y=100)

    l3 = Label(window,text="Password", font=('Times 14 normal'))
    l3.place(x=25,y=140)

    l4 = Label(window,text="Last Name", font=('Times 14 normal'))
    l4.place(x=275,y=60)
    
    l5 = Label(window,text="Comfirm Password",font=('Times 14 normal'))
    l5.place(x=275,y=140)

    l6 = Label(window,text="Email", font=('Times 14 normal'))
    l6.place(x=25,y=260)

    l7 = Label(window,text="User Type", font=('Times 14 normal'))
    l7.place(x=275,y=100)
    
    l8 = Label(window,text="Phone", font=('Times 14 normal'))
    l8.place(x=25,y=180)

    l9 = Label(window,text="Address", font=('Times 14 normal'))
    l9.place(x=275,y=180)

    l10 = Label(window,text="City", font=('Times 14 normal'))
    l10.place(x=25,y=220)
    
    l11 = Label(window,text="State",font=('Times 14 normal'))
    l11.place(x=200,y=220)

    l12 = Label(window,text="Zipcode", font=('Times 14 normal'))
    l12.place(x=325,y=220)

    labelname = {}
    buttonname = {}
    for email in newemail_emp_and_vis:
        i = newemail_emp_and_vis.index(email)
        labelname[email] = Label(window,text=newemail_emp_and_vis[i], font=('Times 12 normal'))
        labelname[email].place(x=120,y=260 + i*40) 
        buttonname[email] = Button(window,text="Remove", width=6, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: removeemail(email)))  
        buttonname[email].place(x=400,y=260 + i*40) 
    
    e1_content = StringVar()
    e1 = Entry(window,width=14, bg='powder blue',textvariable=e1_content)
    e1.place(x=120,y=60)

    e2_content = StringVar()
    e2 = Entry(window,width=14, bg='powder blue',textvariable=e2_content)
    e2.place(x=120,y=100)

    e3_content = StringVar()
    e3 = Entry(window,width=14, bg='powder blue',textvariable=e3_content,show='*')
    e3.place(x=120,y=140)

    e4_content = StringVar()
    e4 = Entry(window,width=14, bg='powder blue',textvariable=e4_content)
    e4.place(x=400,y=60)

    e5_content = StringVar()
    e5 = Entry(window,width=14, bg='powder blue',textvariable=e5_content,show='*')
    e5.place(x=400,y=140)

    e6y = len(newemail_emp_and_vis)*40 + 260

    e6_content = StringVar()
    e6 = Entry(window,width=14, bg='powder blue',textvariable=e6_content)
    e6.place(x=120,y=e6y)

    e8_content = StringVar()
    e8 = Entry(window,width=14, bg='powder blue',textvariable=e8_content)
    e8.place(x=120,y=180)

    e9_content = StringVar()
    e9 = Entry(window,width=14, bg='powder blue',textvariable=e9_content)
    e9.place(x=400,y=180)

    e10_content = StringVar()
    e10 = Entry(window,width=6, bg='powder blue',textvariable=e10_content)
    e10.place(x=120,y=220)

    e12_content = StringVar()
    e12 = Entry(window,width=14, bg='powder blue',textvariable=e12_content)
    e12.place(x=400,y=220)

    option7 = StringVar()
    o7 = ttk.Combobox(window,width=12, textvariable=option7)
    o7['values'] = ('Manager','Staff')
    o7.place(x=400,y=100)
    o7.current(0)

    option11 = StringVar()
    o11 = ttk.Combobox(window,width=4, textvariable=option11)
    o11['values'] = ('AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','Other') 
    o11.place(x=250,y=220)
    o11.current(0)

    b3 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: back()))
    b3.place(x=175,y=350+len(newemail_emp_and_vis)*40)

    b4 = Button(window,text="Register", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda:register_checks()))
    b4.place(x=325,y=350+len(newemail_emp_and_vis)*40)

    b6add = Button(window,text="Add", width=6, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: addemail()))
    b6add.place(x=400,y=e6y)

    window.mainloop()
#7 finished
def WIN_FUN_user():
 
    window = Tk()
    window.title("User Functionality")
    window.geometry('250x175')
    window.configure(background="#fff")

    def navigation(value):
        if value == 1:
            window.destroy()
            take_transit[0] = 'user'
            WIN_take_transit()
        if value == 2:
            window.destroy()
            transit_his[0] = 'user'
            WIN_transit_his()
        if value == 3:
            window.destroy()
            WIN_user_login()        
    
    l0 = Label(window,text="User Functionality", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    b1 = Button(window,text="Take Transit", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(1)))
    b1.place(x=75,y=60)

    b2 = Button(window,text="View Transit History", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(2)))
    b2.place(x=75,y=90)

    b3 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(3)))
    b3.place(x=75,y=120)

    window.mainloop()
#8 finished
def WIN_FUN_adm():
 
    window = Tk()
    window.title("Administrator Functionality")
    window.geometry('250x300')
    window.configure(background="#fff")

    def navigation(value):
        if value == 1:
            window.destroy()
            man_profile[0] = 'adm'
            WIN_emp_manage_profile()
        if value == 2:
            window.destroy()
            man_user[0] = 'adm'
            WIN_adm_manage_user()
        if value == 3:
            window.destroy()
            man_transit[0] = 'adm'
            WIN_adm_manage_transit()
        if value == 4:
            window.destroy()
            man_site[0] = 'adm'
            WIN_adm_manage_site() 
        if value == 5:
            window.destroy()
            take_transit[0] = 'adm'
            WIN_take_transit()
        if value == 6:
            window.destroy()
            transit_his[0] = 'adm'
            WIN_transit_his() 
        if value == 7:
            window.destroy()
            WIN_user_login() 

    l0 = Label(window,text="Administrator Functionality", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    b1 = Button(window,text="Manage Profile", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(1)))
    b1.place(x=75,y=60)

    b2 = Button(window,text="Manage User", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(2)))
    b2.place(x=75,y=90)

    b3 = Button(window,text="Manage Transit", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(3)))
    b3.place(x=75,y=120)

    b4 = Button(window,text="Manage Site", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(4)))
    b4.place(x=75,y=150)

    b5 = Button(window,text="Take Transit", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(5)))
    b5.place(x=75,y=180)

    b6 = Button(window,text="View Transit History", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(6)))
    b6.place(x=75,y=210)

    b7 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(7)))
    b7.place(x=75,y=240)

    window.mainloop()
#9 finished
def WIN_FUN_adm_and_vis():

    window = Tk()
    window.title("Administrator-Visitor Functionality")
    window.geometry('250x400')
    window.configure(background="#fff")

    def navigation(value):
        if value == 1:
            window.destroy()
            man_profile[0] = 'admuser'
            WIN_emp_manage_profile()
        if value == 2:
            window.destroy()
            man_user[0] = 'admuser'
            WIN_adm_manage_user()
        if value == 3:
            window.destroy()
            man_transit[0] = 'admuser'
            WIN_adm_manage_transit()
        if value == 4:
            window.destroy()
            man_transit[0] = 'admuser'
            WIN_adm_manage_site() 
        if value == 5:
            window.destroy()
            take_transit[0] = 'admuser'
            WIN_take_transit()
        if value == 6:
            window.destroy()
            exp_site[0] = 'admuser'
            WIN_vis_explore_site() 
        if value == 7:
            window.destroy()
            exp_event[0] = 'admuser'
            WIN_vis_explore_event()
        if value == 8:
            window.destroy()
            transit_his[0] = 'admuser'
            WIN_transit_his()  
        if value == 9:
            window.destroy()
            vis_his[0] = 'admuser'
            WIN_vis_visit_his()
        if value == 10:
            window.destroy()
            WIN_user_login() 

    l0 = Label(window,text="Administrator Functionality", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    b1 = Button(window,text="Manage Profile", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(1)))
    b1.place(x=75,y=60)

    b2 = Button(window,text="Manage User", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(2)))
    b2.place(x=75,y=90)

    b3 = Button(window,text="Manage Transit", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(3)))
    b3.place(x=75,y=120)

    b4 = Button(window,text="Manage Site", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(4)))
    b4.place(x=75,y=150)

    b5 = Button(window,text="Take Transit", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(5)))
    b5.place(x=75,y=180)

    b6 = Button(window,text="Explore Site", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(6)))
    b6.place(x=75,y=210)

    b7 = Button(window,text="Explore Event", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(7)))
    b7.place(x=75,y=240)

    b8 = Button(window,text="View Transit History", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(8)))
    b8.place(x=75,y=270)

    b9 = Button(window,text="View Visit History", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(9)))
    b9.place(x=75,y=300)

    b10 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(10)))
    b10.place(x=75,y=330)

    window.mainloop()
#10 finished 
def WIN_FUN_man():
  
    window = Tk()
    window.title("Manager Functionality")
    window.geometry('250x300')
    window.configure(background="#fff")

    def navigation(value):
        if value == 1:
            window.destroy()
            man_profile[0] = 'man'
            WIN_emp_manage_profile()
        if value == 2:
            window.destroy()
            man_event[0] = 'man'
            WIN_man_manage_event()
        if value == 3:
            window.destroy()
            view_site_report[0] = 'man'
            WIN_man_site_report()
        if value == 4:
            window.destroy()
            view_sta[0] = 'man'
            WIN_man_manage_staff() 
        if value == 5:
            window.destroy()
            take_transit[0] = 'man'
            WIN_take_transit()
        if value == 6:
            window.destroy()
            transit_his[0] = 'man'
            WIN_transit_his() 
        if value == 7:
            window.destroy()
            WIN_user_login()

    l0 = Label(window,text="Manager Functionality", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    b1 = Button(window,text="Manage Profile", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(1)))
    b1.place(x=75,y=60)

    b2 = Button(window,text="Manage Event", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(2)))
    b2.place(x=75,y=90)

    b3 = Button(window,text="View Site Report", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(3)))
    b3.place(x=75,y=120)

    b4 = Button(window,text="View Staff", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda:navigation(4)))
    b4.place(x=75,y=150)

    b5 = Button(window,text="Take Transit", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(5)))
    b5.place(x=75,y=180)

    b6 = Button(window,text="View Transit History", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(6)))
    b6.place(x=75,y=210)

    b7 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(7)))
    b7.place(x=75,y=240)

    window.mainloop()
#11 finished
def WIN_FUN_man_and_vis():

    window = Tk()
    window.title("Manager-Visitor Functionality")
    window.geometry('250x400')
    window.configure(background="#fff")

    def navigation(value):
        if value == 1:
            window.destroy()
            man_profile[0] = 'manuser'
            WIN_emp_manage_profile()
        if value == 2:
            window.destroy()
            man_event[0] = 'manuser'
            WIN_man_manage_event()
        if value == 4:
            window.destroy()
            view_site_report[0] = 'manuser'
            WIN_man_site_report()
        if value == 3:
            window.destroy()
            view_sta[0] = 'manuser'
            WIN_man_manage_staff()
        if value == 5:
            window.destroy()
            exp_site[0] = 'manuser'
            WIN_vis_explore_site() 
        if value == 6:
            window.destroy()
            exp_event[0] = 'manuser'
            WIN_vis_explore_event() 
        if value == 7:
            window.destroy()
            take_transit[0] = 'manuser'
            WIN_take_transit()
        if value == 8:
            window.destroy()
            transit_his[0] = 'manuser'
            WIN_transit_his() 
        if value == 9:
            window.destroy()
            vis_his[0] = 'manuser'
            WIN_vis_visit_his()
        if value == 10:
            window.destroy()
            WIN_user_login()

    l0 = Label(window,text="Manager Functionality", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    b1 = Button(window,text="Manage Profile", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(1)))
    b1.place(x=75,y=60)

    b2 = Button(window,text="Manage Event", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(2)))
    b2.place(x=75,y=90)

    b3 = Button(window,text="View Staff", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(3)))
    b3.place(x=75,y=120)

    b4 = Button(window,text="View Site Report", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(4)))
    b4.place(x=75,y=150)

    b5 = Button(window,text="Explore Site", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(5)))
    b5.place(x=75,y=180)

    b6 = Button(window,text="Explore Event", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(6)))
    b6.place(x=75,y=210)

    b7 = Button(window,text="Take Transit", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(7)))
    b7.place(x=75,y=240)

    b8 = Button(window,text="View Transit History", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(8)))
    b8.place(x=75,y=270)

    b9 = Button(window,text="View Visit History", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(9)))
    b9.place(x=75,y=300)

    b10 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(10)))
    b10.place(x=75,y=330)

    window.mainloop()
#12 finished
def WIN_FUN_sta():
    # global take_transit
  
    window = Tk()
    window.title("Staff Functionality")
    window.geometry('250x250')
    window.configure(background="#fff")

    def navigation(value):
        if value == 1:
            window.destroy()
            man_profile[0] = 'sta'
            WIN_emp_manage_profile()
        if value == 2:
            window.destroy()
            view_schedule[0] = 'sta'
            WIN_sta_view_schedule()
        if value == 3:
            window.destroy()
            take_transit[0] = 'sta'
            print(take_transit)
            WIN_take_transit()
        if value == 4:
            window.destroy()
            transit_his[0] = 'sta'
            WIN_transit_his()
        if value == 5:
            window.destroy()
            WIN_user_login() 

    l0 = Label(window,text="Staff Functionality", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    b1 = Button(window,text="Manage Profile", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(1)))
    b1.place(x=75,y=60)

    b2 = Button(window,text="View Schedule", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(2)))
    b2.place(x=75,y=90)

    b3 = Button(window,text="Take Tansit", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(3)))
    b3.place(x=75,y=120)

    b4 = Button(window,text="View Transit History", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(4)))
    b4.place(x=75,y=150)

    b5 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(5)))
    b5.place(x=75,y=180)

    window.mainloop()
#13 finished
def WIN_FUN_sta_and_vis():

    window = Tk()
    window.title("Staff-Visitor Functionality")
    window.geometry('250x320')
    window.configure(background="#fff")

    def navigation(value):
        if value == 1:
            window.destroy()
            man_profile[0] = 'stauser'
            WIN_emp_manage_profile()
        if value == 2:
            window.destroy()
            view_schedule[0] = 'stauser'
            WIN_sta_view_schedule()
        if value == 3:
            window.destroy()
            exp_event[0] = 'stauser'
            WIN_vis_explore_event() 
        if value == 4:
            window.destroy()
            exp_site[0] = 'stauser'
            WIN_vis_explore_site() 
        if value == 5:
            window.destroy()
            take_transit[0] = 'stauser'
            WIN_take_transit()
        if value == 6:
            window.destroy()
            vis_his[0] = 'stauser'
            WIN_vis_visit_his()            
        if value == 7:
            window.destroy()
            transit_his[0] = 'stauser'
            WIN_transit_his()
        if value == 8:
            window.destroy()
            WIN_user_login() 

    l0 = Label(window,text="Staff Functionality", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    b1 = Button(window,text="Manage Profile", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(1)))
    b1.place(x=75,y=60)

    b2 = Button(window,text="View Schedule", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(2)))
    b2.place(x=75,y=90)

    b3 = Button(window,text="Explore Event", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(3)))
    b3.place(x=75,y=120)

    b4 = Button(window,text="Explore Site", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(4)))
    b4.place(x=75,y=150)

    b5 = Button(window,text="Take Transit", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(5)))
    b5.place(x=75,y=180)

    b6 = Button(window,text="View Visit History", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(6)))
    b6.place(x=75,y=210)

    b7 = Button(window,text="View Transit History", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(7)))
    b7.place(x=75,y=240)

    b8 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(8)))
    b8.place(x=75,y=270)

    window.mainloop()
#14 finished
def WIN_FUN_vis():
 
    window = Tk()
    window.title("Visitor Functionality")
    window.geometry('250x250')
    window.configure(background="#fff")

    l0 = Label(window,text="Visitor Functionality", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    def navigation(value):
        if value == 1:
            window.destroy()
            exp_event = 'vis'
            WIN_vis_explore_event() 
        if value == 2:
            window.destroy()
            exp_site = 'vis'
            WIN_vis_explore_site()
        if value == 3:
            window.destroy()
            vis_his = 'vis'
            WIN_vis_visit_his()     
        if value == 4:
            window.destroy()
            take_transit = 'vis'
            WIN_take_transit()           
        if value == 5:
            window.destroy()
            transit_his = 'vis'
            WIN_transit_his()
        if value == 6:
            window.destroy()
            WIN_user_login() 

    b1 = Button(window,text="Explore Event", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(1)))
    b1.place(x=75,y=60)

    b2 = Button(window,text="Explore Site", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(2)))
    b2.place(x=75,y=90)

    b3 = Button(window,text="View Visit History", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(3)))
    b3.place(x=75,y=120)

    b4 = Button(window,text="Take Transit", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(4)))
    b4.place(x=75,y=150)

    b5 = Button(window,text="View Transit History", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(5)))
    b5.place(x=75,y=180)

    b6 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(6)))
    b6.place(x=75,y=210)

    window.mainloop()
#15 testing
def WIN_take_transit():
    db = DB()
    command = "select route,type,price,sitename from transit join connect on route = transitroute"
    table_raw = db.search(command)
    table = {}
    for row in table_raw:
        if row[0] not in table:
            table[row[0]] = [row[0],row[1],str(row[2]).split("'")[0],[row[3]]]
        else:
            table[row[0]][3].append(row[3])
    table_list = [table[value] for value in table]
    isreversed = [0]
    filtered_list = table_list[:]
    selectitem = {}

    sites = []
    for item in table_list:
        for element in item[3]:
            if element not in sites:
                sites.append(element)

    window = Tk()
    window.title("User Take Transit")
    window.geometry('500x500')
    window.resizable(0, 0)
    window.configure(background="#fff")

    def sorting(arg):
        if arg == 'route':
            tree.delete(*tree.get_children())
            if isreversed[0] % 2 == 0:
                route_list = sorted(filtered_list, key = lambda x: x[0])
                isreversed[0] += 1
            else:
                route_list = sorted(filtered_list, key = lambda x: x[0],reverse=True)
                isreversed[0] += 1
            for item in route_list:
                tree.insert("",'end',values=(item[0],item[1],item[2],len(item[3])))
        elif arg == 'ttype':
            tree.delete(*tree.get_children())
            if isreversed[0] % 2 == 0:
                ttype_list = sorted(filtered_list, key = lambda x: x[1])
                isreversed[0] += 1
            else:
                ttype_list = sorted(filtered_list, key = lambda x: x[1],reverse=True)
                isreversed[0] += 1
            for item in ttype_list:
                tree.insert("",'end',values=(item[0],item[1],item[2],len(item[3])))
        elif arg == 'price':
            tree.delete(*tree.get_children())
            if isreversed[0] % 2 == 0:
                price_list = sorted(filtered_list, key = lambda x: x[2])
                isreversed[0] += 1
            else:
                price_list = sorted(filtered_list, key = lambda x: x[2],reverse=True)
                isreversed[0] += 1
            for item in price_list:
                tree.insert("",'end',values=(item[0],item[1],item[2],len(item[3])))
        elif arg == 'csites':
            tree.delete(*tree.get_children())
            if isreversed[0] % 2 == 0:
                csites_list = sorted(filtered_list, key = lambda x: len(x[3]))
                isreversed[0] += 1
            else:
                csites_list = sorted(filtered_list, key = lambda x: len(x[3]),reverse=True)
                isreversed[0] += 1
            for item in csites_list:
                tree.insert("",'end',values=(item[0],item[1],item[2],len(item[3])))

    def filter(table_list):
        start = e1_content.get()
        end = e2_content.get()
        if start != '' and end != '':
            if float(end) < float(start):
                tkinter.messagebox.showwarning('Error','Its not a good price range') 
            else:
                filtered_list.clear()
                for item in table_list:
                    if float(item[2]) >= float(start) and float(item[2]) <= float(end):
                        filtered_list.append(item)
                tree.delete(*tree.get_children())
                for item in filtered_list:
                    tree.insert("",'end',values=(item[0],item[1],item[2],len(item[3])))

    def filtersite(event):
        filtered_list = table_list[:]
        sitename = event.widget.get()
        if sitename == '--ALL--':
            filtered_list = table_list[:]
            tree.delete(*tree.get_children())
            for item in table_list:
                tree.insert("",'end',values=(item[0],item[1],item[2],len(item[3])))
        else:
            filtered_list.clear()
            for item in table_list:
                if sitename in item[3]:
                    filtered_list.append(item)
            tree.delete(*tree.get_children())
            for item in filtered_list:
                tree.insert("",'end',values=(item[0],item[1],item[2],len(item[3])))      
    
    def filtertype(event):
        filtered_list = table_list[:]
        ttype = event.widget.get()
        if ttype == '--ALL--':
            filtered_list.clear()
            filtered_list = table_list[:]
            tree.delete(*tree.get_children())
            for item in table_list:
                tree.insert("",'end',values=(item[0],item[1],item[2],len(item[3])))
        else:
            filtered_list.clear()
            for item in table_list:
                if ttype in item[1]:
                    filtered_list.append(item)
            tree.delete(*tree.get_children())
            for item in filtered_list:
                tree.insert("",'end',values=(item[0],item[1],item[2],len(item[3])))
      
    def logtransit():
        if not re.match(r'^^\d\d\d\d-(0?[1-9]|[12][0-9]|3[01])-(0?[1-9]|1[0-2])',e3_content.get()):
            tkinter.messagebox.showwarning('Date Error','Not valid date!')            
        else:
            if selectitem != {}:
                transitdate = e3_content.get()
                info = selectitem['values']['values']
                command = "SELECT date,transitroute FROM take where username='" + username_login[0] + "'"
                com = db.search(command)
                transitroute = info[0]
                newdate = "date='" + transitdate + "'"
                newroute = "transitroute='" + str(info[0]) + "'"
                newtype = "transittype='" + info[1] + "'"
                newusername = "username='" + username_login[0] + "'"
                
                if com != None:
                    if (transitdate,transitroute) not in com:
                        try:
                            command =  "INSERT INTO take SET " + newdate + "," + newroute + "," + newtype + "," + newusername
                            db.insert(command)      
                        except:
                            tkinter.messagebox.showwarning('Error','You have take the same transit that day!') 
                else:
                    try:
                        command =  "INSERT INTO take SET " + newdate + "," + newroute + "," + newtype + "," + newusername
                        db.insert(command)    
                    except:
                        tkinter.messagebox.showwarning('Error','Wrong Date or Selection!') 
            else:
                tkinter.messagebox.showwarning('Route Error','Choose a route please!') 
        
    def back():
        if take_transit[0] == 'user':
            window.destroy()
            WIN_FUN_user()
        elif take_transit[0] == 'adm':
            window.destroy() 
            WIN_FUN_adm()           
        elif take_transit[0] == 'admuser':
            window.destroy()
            WIN_FUN_adm_and_vis()
        elif take_transit[0] == 'man':
            window.destroy()
            WIN_FUN_man()
        elif take_transit[0] == 'manuser':
            window.destroy()
            WIN_FUN_man_and_vis()
        elif take_transit[0] == 'sta':
            window.destroy()
            WIN_FUN_sta()
        elif take_transit[0] == 'stauser':
            window.destroy()
            WIN_FUN_sta_and_vis()
        elif take_transit[0] == 'vis':
            window.destroy()
            WIN_FUN_vis()
        else: pass

    l0 = Label(window,text="Take Transit", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    l1 = Label(window,text="Contain Site", font=('Times', 14, 'normal'))
    l1.place(x=25,y=60)

    l2 = Label(window,text="Transport Type", font=('Times', 14, 'normal'))
    l2.place(x=250,y=60)

    l3 = Label(window,text="Price Range", font=('Times', 14, 'normal'))
    l3.place(x=25,y=100)

    l4 = Label(window,text="--", font=('Times', 14, 'normal'))
    l4.place(x=175,y=100)

    l5 = Label(window,text="Transit Date", font=('Times', 14, 'normal'))
    l5.place(x=160,y=450)

    e1_content = StringVar()
    e1 = Entry(window,width=3, bg='powder blue',textvariable=e1_content)
    e1.place(x=120,y=100)

    e2_content = StringVar()
    e2 = Entry(window,width=3, bg='powder blue',textvariable=e2_content)
    e2.place(x=200,y=100)
    
    e3_content = StringVar()
    e3 = Entry(window,width=8, bg='powder blue',textvariable=e3_content)
    e3.place(x=250,y=450)

    option1 = StringVar()
    o1 = ttk.Combobox(window,width=10, textvariable=option1)
    o1['values'] = tuple(sites)#tuple(x for x in (['--ALL--'] + list(x for x in sites)))
    o1.place(x=125,y=60)
    o1.bind("<<ComboboxSelected>>",filtersite)
    o1.current(0)
    
    option2 = StringVar()
    o2 = ttk.Combobox(window,width=8, textvariable=option2)
    o2['values'] = ('--ALL--','MARTA','Bus','Bike') # More states should be involved
    o2.place(x=350,y=60)
    o2.bind("<<ComboboxSelected>>",filtertype)
    o2.current(0)

    b1 = Button(window,text="Filter", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: filter(table_list)))
    b1.place(x=300,y=100)

    b2 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: back()))
    b2.place(x=50,y=450)

    b3 = Button(window,text="Log Transit", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: logtransit()))
    b3.place(x=350,y=450)
    
    def selectItem(event):
        item = tree.focus()
        selectitem['values'] = tree.item(item)
        
    tree = ttk.Treeview(window)
    tree.place(x=25,y=160)
    vsb = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    vsb.place(x=425, y=160, height=240)
    tree["show"] = 'headings'
    tree.configure(yscrollcommand=vsb.set,height=12)
    tree["columns"]=("one","two","three","four")
    tree.column("one", width=100)
    tree.column("two", width=100)
    tree.column("three",width=100)
    tree.column("four",width=100)
    tree.heading("one", text="Route",command=(lambda: sorting("route")))
    tree.heading("two", text="Transport Type",command=(lambda: sorting("ttype")))
    tree.heading("three", text="Price($)",command=(lambda: sorting("price")))
    tree.heading("four",text="# Connected Sites",command=(lambda: sorting("csites")))
    tree.bind('<ButtonRelease-1>', selectItem)
    for item in table_list:
        tree.insert("",'end',values=(item[0],item[1],item[2],len(item[3])))

    window.mainloop()

    #The table
#16 testing
def WIN_transit_his():
    db = DB()
    command = "SELECT date,transitroute,transittype,price FROM take JOIN transit on  take.transitroute =  transit.route WHERE username='" + username_login[0] +"'"
    table_raw = db.search(command)
    # print(table_raw)

    table_list = []
    for row in table_raw:
        table_list.append(row)
    # print(table_list)
    sitenames = {}
    routes = set(x[1] for x in table_list)
    for route in routes:
        command = "SELECT transitroute,sitename FROM connect WHERE transitroute='" + route + "'"
        info = db.search(command)
        for site in info:
            if route not in sitenames:
                sitenames[route] = [site[1]]
            else:
                sitenames[route].append(site[1])
    sites = []
    for i in range(len(table_list)):
        table_list[i] = [table_list[i][0],table_list[i][1],table_list[i][2],table_list[i][3],sitenames[table_list[i][1]]]

    for value,item in sitenames.items():
        for element in item:
            if element not in sites:
                sites.append(element)
    # for item from table_list:pass
    isreversed = [0]
    filtered_list = table_list[:]
    selectitem = {}
           
    window = Tk()
    window.title("User Transit History")
    window.geometry('500x500')
    window.resizable(0, 0)
    window.configure(background="#fff")

    def sorting(arg):
        if arg == 'route':
            tree.delete(*tree.get_children())
            if isreversed[0] % 2 == 0:
                route_list = sorted(filtered_list, key = lambda x: x[0])
                isreversed[0] += 1
            else:
                route_list = sorted(filtered_list, key = lambda x: x[0],reverse=True)
                isreversed[0] += 1
            for item in route_list:
                tree.insert("",'end',values=(item[0],item[1],item[2],item[3]))
        elif arg == 'ttype':
            tree.delete(*tree.get_children())
            if isreversed[0] % 2 == 0:
                ttype_list = sorted(filtered_list, key = lambda x: x[1])
                isreversed[0] += 1
            else:
                ttype_list = sorted(filtered_list, key = lambda x: x[1],reverse=True)
                isreversed[0] += 1
            for item in ttype_list:
                tree.insert("",'end',values=(item[0],item[1],item[2],item[3]))
        elif arg == 'price':
            tree.delete(*tree.get_children())
            if isreversed[0] % 2 == 0:
                price_list = sorted(filtered_list, key = lambda x: x[2])
                isreversed[0] += 1
            else:
                price_list = sorted(filtered_list, key = lambda x: x[2],reverse=True)
                isreversed[0] += 1
            for item in price_list:
                tree.insert("",'end',values=(item[0],item[1],item[2],item[3]))
        elif arg == 'csites':
            tree.delete(*tree.get_children())
            if isreversed[0] % 2 == 0:
                csites_list = sorted(filtered_list, key = lambda x: x[3])
                isreversed[0] += 1
            else:
                csites_list = sorted(filtered_list, key = lambda x: x[3],reverse=True)
                isreversed[0] += 1
            for item in csites_list:
                tree.insert("",'end',values=(item[0],item[1],item[2],item[3]))

    def checkstartdate():
        if not re.match(r'^\d\d\d\d-(0?[1-9]|[12][0-9]|3[01])-(0?[1-9]|1[0-2])',e4_content.get()):
            tkinter.messagebox.showwarning('Date Error','Not valid Start date!')            
        else:
            return e4_content.get()

    def checkenddate():
        if not re.match(r'^\d\d\d\d-(0?[1-9]|[12][0-9]|3[01])-(0?[1-9]|1[0-2])',e5_content.get()):
            tkinter.messagebox.showwarning('Date Error','Not valid End date!')            
        else:
            return  e5_content.get()

    def filter():
        route = e3_content.get()
        if e4_content.get() != '' and e5_content.get() != '' and e3_content.get() != '':
            startdate = checkstartdate()
            enddate = checkenddate()
            startdate_date = datetime.date(int(startdate.split("-")[0]),int(startdate.split("-")[1]),int(startdate.split("-")[2]))
            enddate_date = datetime.date(int(enddate.split("-")[0]),int(enddate.split("-")[1]),int(enddate.split("-")[2]))
            if startdate > enddate:
                tkinter.messagebox.showwarning('Date Error','Start Date should be before End date!') 
            else:
                filtered_list.clear()
                for item in table_list:      
                    if route == item[1] and startdate_date <= item[0] and enddate_date >= item[0]:
                        filtered_list.append(item)
                tree.delete(*tree.get_children())
                for item in filtered_list:
                    tree.insert("",'end',values=(item[0],item[1],item[2],item[3]))
        elif e4_content.get() != '' and e5_content.get() != '' and e3_content.get() == '':
            startdate = checkstartdate()
            enddate = checkenddate()
            startdate_date = datetime.date(int(startdate.split("-")[0]),int(startdate.split("-")[1]),int(startdate.split("-")[2]))
            enddate_date = datetime.date(int(enddate.split("-")[0]),int(enddate.split("-")[1]),int(enddate.split("-")[2]))
            if startdate > enddate:
                tkinter.messagebox.showwarning('Date Error','Start Date should be before End date!') 
            else:
                filtered_list.clear()
                for item in table_list:      
                    if startdate_date <= item[0] and enddate_date >= item[0]:
                        filtered_list.append(item)
                tree.delete(*tree.get_children())
                for item in filtered_list:
                    tree.insert("",'end',values=(item[0],item[1],item[2],item[3]))
        elif e4_content.get() == '' and e5_content.get() == '' and e3_content.get() != '':
            filtered_list.clear()
            for item in table_list:
                if route == item[1]:
                    filtered_list.append(item)
            tree.delete(*tree.get_children())
            for item in filtered_list:
                tree.insert("",'end',values=(item[0],item[1],item[2],item[3]))
        else:pass

    def filtersite(event):
        filtered_list = table_list[:]
        sitename = event.widget.get()
        if sitename == '--ALL--':
            filtered_list = table_list[:]
            tree.delete(*tree.get_children())
            for item in table_list:
                tree.insert("",'end',values=(item[0],item[1],item[2],item[3]))
        else:
            filtered_list.clear()
            for item in table_list:
                if sitename in item[4]:
                    filtered_list.append(item)
            tree.delete(*tree.get_children())
            for item in filtered_list:
                tree.insert("",'end',values=(item[0],item[1],item[2],item[3]))     
    
    def filtertype(event):
        filtered_list = table_list[:]
        ttype = event.widget.get()
        if ttype == '--ALL--':
            filtered_list.clear()
            filtered_list = table_list[:]
            tree.delete(*tree.get_children())
            for item in table_list:
                tree.insert("",'end',values=(item[0],item[1],item[2],item[3]))
        else:
            filtered_list.clear()
            for item in table_list:
                if ttype in item[2]:
                    filtered_list.append(item)
            tree.delete(*tree.get_children())
            for item in filtered_list:
                tree.insert("",'end',values=(item[0],item[1],item[2],item[3]))
      
    def back():
        if transit_his[0] == 'user':
            window.destroy()
            WIN_FUN_user()
        elif transit_his[0] == 'adm':
            window.destroy() 
            WIN_FUN_adm()           
        elif transit_his[0] == 'admuser':
            window.destroy()
            WIN_FUN_adm_and_vis()
        elif transit_his[0]== 'man':
            window.destroy()
            WIN_FUN_man()
        elif transit_his[0] == 'manuser':
            window.destroy()
            WIN_FUN_man_and_vis()
        elif transit_his[0] == 'sta':
            window.destroy()
            WIN_FUN_sta()
        elif transit_his[0] == 'stauser':
            window.destroy()
            WIN_FUN_sta_and_vis()
        elif transit_his[0] == 'vis':
            window.destroy()
            WIN_FUN_vis()
        else: pass
        
    l0 = Label(window,text="Transit History", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    l1 = Label(window,text="Contain Site", font=('Times', 14, 'normal'))
    l1.place(x=25,y=60)

    l2 = Label(window,text="Transport Type", font=('Times', 14, 'normal'))
    l2.place(x=250,y=60)

    l3 = Label(window,text="Route", font=('Times', 14, 'normal'))
    l3.place(x=25,y=100)

    l4 = Label(window,text="Start Date", font=('Times', 14, 'normal'))
    l4.place(x=150,y=100)

    l5 = Label(window,text="End Date", font=('Times', 14, 'normal'))
    l5.place(x=300,y=100)

    e3_content = StringVar()
    e3 = Entry(window,width=6, bg='powder blue',textvariable=e3_content)
    e3.place(x=75,y=100)

    e4_content = StringVar()
    e4 = Entry(window,width=6, bg='powder blue',textvariable=e4_content)
    e4.place(x=225,y=100)

    e5_content = StringVar()
    e5 = Entry(window,width=6, bg='powder blue',textvariable=e5_content)
    e5.place(x=375,y=100)

    option1 = StringVar()
    o1 = ttk.Combobox(window,width=10, textvariable=option1)
    o1['values'] = tuple(sites)
    o1.bind("<<ComboboxSelected>>",filtersite)
    o1.place(x=125,y=60)
    o1.current(0)

    option2 = StringVar()
    o2 = ttk.Combobox(window,width=8, textvariable=option2)
    o2['values'] = ('--ALL--','MARTA','Bus','Bike') # More states should be involved
    o2.bind("<<ComboboxSelected>>",filtertype)
    o2.place(x=350,y=60)
    o2.current(0)

    b1 = Button(window,text="Filter", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: filter()))
    b1.place(x=200,y=150)

    b2 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: back()))
    b2.place(x=200,y=450)
    
    def selectItem(event):
        item = tree.focus()
        selectitem['values'] = tree.item(item)
        
    tree = ttk.Treeview(window)
    tree.place(x=25,y=200)
    vsb = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    vsb.place(x=425, y=200, height=240)
    tree["show"] = 'headings'
    tree.configure(yscrollcommand=vsb.set,height=12)
    tree["columns"]=("one","two","three","four")
    tree.column("one", width=100)
    tree.column("two", width=100)
    tree.column("three",width=100)
    tree.column("four",width=100)
    tree.heading("one", text="Date",command=(lambda: sorting("route")))
    tree.heading("two", text="Route",command=(lambda: sorting("ttype")))
    tree.heading("three", text="Transport Type",command=(lambda: sorting("price")))
    tree.heading("four",text="Price($)",command=(lambda: sorting("csites")))
    tree.bind('<ButtonRelease-1>', selectItem)
    for item in table_list:
        tree.insert("",'end',values=(item[0],item[1],item[2],item[3]))

    window.mainloop()

    #The table
#17 testing
def WIN_emp_manage_profile():
    db = DB()
    command = "SELECT * FROM manage_profile WHERE username='" + username_login[0] + "'"
    profile = db.search(command)
    # print(profile)
    command = "SELECT * FROM user WHERE username='" + username_login[0] + "'"
    if db.search(command)[0][5] == 'employee,visitor':
        Etype = "manuser"
        isVis = 1
    else:
        Etype = "man"
        isVis = 0

    Fname = profile[0][0]
    Lname = profile[0][1]
    Username = profile[0][2]
    Sitename = profile[0][3]
    Employeeid = profile[0][4]
    Phone = profile[0][5]
    Address = profile[0][6]

    geometry = '600x' + str(len(newemail_profile)*40+400)
    window = Tk()
    window.title("Employee Manage Profile")
    window.geometry(geometry)
    window.resizable(0, 0)
    window.configure(background="#fff")

    def update():
        newfname = e1_content.get() 
        newlname = e2_content.get()
        newphone = e9_content.get() 
        IsVis = chVarDis.get()
        if newfname != Fname or newlname != Lname or int(newphone) != int(Phone) or newemail_profile != oriemail_profile:
            try:    
                if newfname != Fname or newlname != Lname:
                    command = "UPDATE user SET fname='" + newfname + "',lname='" + newlname  + "' WHERE username='" + username_login[0] + "'"
                    db.update(command)
                if int(newphone) != int(Phone):
                    command = "UPDATE employee SET phone=" + newphone  + " WHERE eusername='" + username_login[0] + "'"
                    db.update(command)
                if newemail_profile != oriemail_profile:
                    for email in oriemail_profile:
                        if email not in newemail_profile:
                            command = "DELETE FROM email WHERE username='" + username_login[0] + "' AND email='" + email + "'" 
                            db.update(command)
                    for email in newemail_profile:
                        if email not in oriemail_profile:
                            command = "INSERT INTO email SET username='" + username_login[0] + "',email='" + email + "'"
                            db.update(command)
                if IsVis != isVis:
                    if IsVis == 1:
                        command = "UPDATE user SET etype='employee,visitor' WHERE username='" + username_login[0] + "'"
                        db.update(command)
                    else:
                        command = "UPDATE user SET etype='Employee' WHERE username='" + username_login[0] + "'"
                        db.update(command)
                tkinter.messagebox.showinfo('Success!','Profile updated, please relogin.')
                window.destroy()
                WIN_user_login()
            except:
                tkinter.messagebox.showwarning('Update Error','At least one email! No changes or invalid information')

    def checkemail():
        command = 'SELECT email FROM email'
        emails_tmp = db.search(command)
        emails = []
        for email in newemail_profile:
            emails.append(email[0])
        if not re.match(r'^[0-9a-zA-Z]+@{1}[0-9a-zA-Z]+\.{1}[0-9a-zA-Z]+',e12_content.get()):
            tkinter.messagebox.showwarning('Email Error','Not valid email!')
        elif e12_content.get() in emails_tmp:
            tkinter.messagebox.showwarning('Existed Email','The email exists, try another email!')
        elif e12_content.get() in newemail_profile:
            tkinter.messagebox.showwarning('Existed Email','The email exists, try another email!')
        else:
            newemail_profile.append(e12_content.get())
            
    def addemail():
        checkemail()
        window.destroy()
        WIN_emp_manage_profile()

    def removeemail(email):
        newemail_profile.remove(email)
        window.destroy()
        WIN_emp_manage_profile()

    def back():
        if man_profile[0] == 'user':
            window.destroy()
            WIN_FUN_user()
        elif man_profile[0] == 'adm':
            window.destroy() 
            WIN_FUN_adm()           
        elif man_profile[0] == 'admuser':
            window.destroy()
            WIN_FUN_adm_and_vis()
        elif man_profile[0] == 'man':
            window.destroy()
            WIN_FUN_man()
        elif man_profile[0] == 'manuser':
            window.destroy()
            WIN_FUN_man_and_vis()
        elif man_profile[0] == 'sta':
            window.destroy()
            WIN_FUN_sta()
        elif man_profile[0] == 'stauser':
            window.destroy()
            WIN_FUN_sta_and_vis()
        elif man_profile[0] == 'vis':
            window.destroy()
            WIN_FUN_vis()
        else: pass

    l0 = Label(window,text="Manage Profile", width=36,font=('Arial', 18, 'bold'))
    l0.place(x=100,y=0)

    l1 = Label(window,text="Fisrt Name", font=('Times 14 normal'))
    l1.place(x=25,y=60)
    
    l2 = Label(window,text="Last Name", font=('Times 14 normal'))
    l2.place(x=275,y=60)

    l3 = Label(window,text="Username", font=('Times 14 normal'))
    l3.place(x=25,y=100)

    l4 = Label(window,text=Username, font=('Times 14 italic bold'))
    l4.place(x=120,y=100)
    
    l5 = Label(window,text="Site Name",font=('Times 14 normal'))
    l5.place(x=275,y=100)
    
    l6 = Label(window,text=Sitename,font=('Times 14 italic bold'))
    l6.place(x=400,y=100)

    l7 = Label(window,text="Employee ID", font=('Times 14 normal'))
    l7.place(x=25,y=140)

    l8 = Label(window,text=Employeeid, font=('Times 14 italic bold'))
    l8.place(x=120,y=140)
    
    l9 = Label(window,text="Phone", font=('Times 14 normal'))
    l9.place(x=275,y=140)

    l10 = Label(window,text="Address", font=('Times 14 normal'))
    l10.place(x=25,y=180)

    l11 = Label(window,text=Address, font=('Times 14 italic bold'))
    l11.place(x=120,y=180)

    l12 = Label(window,text="Email", font=('Times 14 normal'))
    l12.place(x=25,y=220)

    labelname = {}
    buttonname = {}
    for email in newemail_profile:
        i = newemail_profile.index(email)
        labelname[email] = Label(window,text=newemail_profile[i], font=('Times 12 normal'))
        labelname[email].place(x=120,y=220 + i*40) 
        buttonname[email] = Button(window,text="Remove", width=6, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: removeemail(email)))  
        buttonname[email].place(x=400,y=220 + i*40) 

    e1_content = StringVar()
    e1 = Entry(window,width=14, bg='powder blue',textvariable=e1_content)
    e1.insert(END,Fname)
    e1.place(x=120,y=60)

    e2_content = StringVar()
    e2 = Entry(window,width=14, bg='powder blue',textvariable=e2_content)
    e2.insert(END,Lname)
    e2.place(x=400,y=60)

    e9_content = StringVar()
    e9 = Entry(window,width=14, bg='powder blue',textvariable=e9_content)
    e9.insert(END,Phone)
    e9.place(x=400,y=140)

    e12y = len(newemail_profile)*40 + 220
    e12_content = StringVar()
    e12 = Entry(window,width=20, bg='powder blue',textvariable=e12_content)
    e12.place(x=120,y=e12y)

    chVarDis = IntVar()
    c1 = Checkbutton(window, text='Visitor Account',variable=chVarDis)
    if Etype == 'manuser':
        c1.select()
    else:
        c1.deselect()
    c1.place(x=250,y=325+len(newemail_profile)*40)

    b3 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: back()))
    b3.place(x=175,y=350+len(newemail_profile)*40)

    b4 = Button(window,text="Update", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: update()))
    b4.place(x=325,y=350+len(newemail_profile)*40)

    b12add = Button(window,text="Add", width=6, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: addemail()))
    b12add.place(x=400,y=e12y)

    window.mainloop()
#18 testing
def WIN_adm_manage_user():
    db = DB()
    command = "SELECT DISTINCT `manage_user`.`username` AS `username`,`status`,`etype`,( SELECT COUNT(  DISTINCT(`email`) ) FROM `email` WHERE `email`.`username` = `manage_user`.`username`) AS `Email Count` FROM manage_user"
    userinfo = db.search(command)
    # print(userinfo)
    table_list = []
    for row in userinfo:
        table_list.append(row)
    # print(table_list)
    isreversed = [0]
    filtered_list = table_list[:]
    selectitem = {}
        
    window = Tk()
    window.title("Administrator Manage User")
    window.geometry('600x400')
    window.resizable(0, 0)
    window.configure(background="#fff")

    def sorting(arg):
        if arg == 'Username':
            tree.delete(*tree.get_children())
            if isreversed[0] % 2 == 0:
                route_list = sorted(filtered_list, key = lambda x: x[0])
                isreversed[0] += 1
            else:
                route_list = sorted(filtered_list, key = lambda x: x[0],reverse=True)
                isreversed[0] += 1
            for item in route_list:
                tree.insert("",'end',values=(item[0],item[3],item[2],item[1]))
        elif arg == 'Email Count':
            tree.delete(*tree.get_children())
            if isreversed[0] % 2 == 0:
                ttype_list = sorted(filtered_list, key = lambda x: x[3])
                isreversed[0] += 1
            else:
                ttype_list = sorted(filtered_list, key = lambda x: x[3],reverse=True)
                isreversed[0] += 1
            for item in ttype_list:
                tree.insert("",'end',values=(item[0],item[3],item[2],item[1]))
        elif arg == 'User Type':
            tree.delete(*tree.get_children())
            if isreversed[0] % 2 == 0:
                price_list = sorted(filtered_list, key = lambda x: x[2])
                isreversed[0] += 1
            else:
                price_list = sorted(filtered_list, key = lambda x: x[2],reverse=True)
                isreversed[0] += 1
            for item in price_list:
                tree.insert("",'end',values=(item[0],item[3],item[2],item[1]))
        elif arg == 'Status':
            tree.delete(*tree.get_children())
            if isreversed[0] % 2 == 0:
                csites_list = sorted(filtered_list, key = lambda x: x[1])
                isreversed[0] += 1
            else:
                csites_list = sorted(filtered_list, key = lambda x: x[1],reverse=True)
                isreversed[0] += 1
            for item in csites_list:
                tree.insert("",'end',values=(item[0],item[3],item[2],item[1]))

    def usernamefilter():
        filteruser = e1_content.get()
        tree.delete(*tree.get_children())
        for user in table_list:   
            if filteruser == user[0]:    
                tree.insert("",'end',values=(user[0],user[3],user[2],user[1]))

    def filterstatus(event):
        filtered_list = table_list[:]
        status = event.widget.get()
        if status == '--ALL--':
            filtered_list = table_list[:]
            tree.delete(*tree.get_children())
            for item in table_list:
                tree.insert("",'end',values=(item[0],item[3],item[2],item[1]))
        else:
            filtered_list.clear()
            for item in table_list:
                if status in item[1]:
                    filtered_list.append(item)
            tree.delete(*tree.get_children())
            for item in filtered_list:
                tree.insert("",'end',values=(item[0],item[3],item[2],item[1]))      
    
    def filtertype(event):
        filtered_list = table_list[:]
        utype = event.widget.get()
        if utype == '--ALL--':
            filtered_list.clear()
            filtered_list = table_list[:]
            tree.delete(*tree.get_children())
            for item in table_list:
                tree.insert("",'end',values=(item[0],item[3],item[2],item[1]))
        else:
            filtered_list.clear()
            for item in table_list:
                if utype in item[2]:
                    filtered_list.append(item)
            tree.delete(*tree.get_children())
            for item in filtered_list:
                tree.insert("",'end',values=(item[0],item[3],item[2],item[1]))
    def approve():
        if selectitem != {}:
            status = selectitem['values']['values'][3]
            if status != 'Approved':
                try:
                    command = "UPDATE user SET status='Approved' WHERE username='" + selectitem['values']['values'][0] + "'"
                    db.update(command)
                    window.destroy()
                    WIN_adm_manage_user()
                except:
                    tkinter.messagebox.showwarning('Error','Cannot approve!') 
    
    def decline():
        if selectitem != {}:
            status = selectitem['values']['values'][3]
            if status == 'Pending':
                try:
                    command = "UPDATE user SET status='Declined' WHERE username='" + selectitem['values']['values'][0] + "'"
                    print(command)
                    db.update(command)
                    window.destroy()
                    WIN_adm_manage_user()
                except:
                    tkinter.messagebox.showwarning('Error','Cannot decline!') 

    def back():
        if man_user[0] == 'adm':
            window.destroy()
            WIN_FUN_adm()
        elif man_user[0] == 'admuser':
            window.destroy() 
            WIN_FUN_adm_and_vis()  
        else:pass    

    l0 = Label(window,text="Manage User", width=36,font=('Arial', 18, 'bold'))
    l0.place(x=100,y=0)

    l1 = Label(window,text="Username", font=('Times 14 normal'))
    l1.place(x=25,y=60)
    
    l2 = Label(window,text="Type", font=('Times 14 normal'))
    l2.place(x=250,y=60)

    l3 = Label(window,text="Status", font=('Times 14 normal'))
    l3.place(x=425,y=60)
    
    e1_content = StringVar()
    e1 = Entry(window,width=10, bg='powder blue',textvariable=e1_content)
    e1.place(x=120,y=60)

    option2 = StringVar()
    o2 = ttk.Combobox(window,width=8, textvariable=option2)
    o2['values'] = ('--ALL--','User','Visitor','Manager','Staff')
    o2.bind("<<ComboboxSelected>>",filtertype)
    o2.place(x=300,y=60)
    o2.current(0)

    option3 = StringVar()
    o3 = ttk.Combobox(window,width=6, textvariable=option3)
    o3['values'] = ('--ALL--','Approved','Pending','Declined') # More states should be involved
    o3.bind("<<ComboboxSelected>>",filterstatus)
    o3.place(x=475,y=60)
    o3.current(0)

    b1 = Button(window,text="Filter", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: usernamefilter()))
    b1.place(x=25,y=100)

    b2 = Button(window,text="Approve", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: approve()))
    b2.place(x=350,y=100)

    b3 = Button(window,text="Decline", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: decline()))
    b3.place(x=450,y=100)

    b4 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: back()))
    b4.place(x=250,y=350)

    def selectItem(event):
        item = tree.focus()
        selectitem['values'] = tree.item(item)
        
    tree = ttk.Treeview(window)
    tree.place(x=75,y=160)
    vsb = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    vsb.place(x=475, y=160, height=180)
    tree["show"] = 'headings'
    tree.configure(yscrollcommand=vsb.set,height=8)
    tree["columns"]=("one","two","three","four")
    tree.column("one", width=100)
    tree.column("two", width=100)
    tree.column("three",width=100)
    tree.column("four",width=100)
    tree.heading("one", text="Username",command=(lambda: sorting("Username")))
    tree.heading("two", text="Email Count",command=(lambda: sorting("Email Count")))
    tree.heading("three", text="User Type",command=(lambda: sorting("User Type")))
    tree.heading("four",text="Status",command=(lambda: sorting("Status")))
    tree.bind('<ButtonRelease-1>', selectItem)
    for item in table_list:
        tree.insert("",'end',values=(item[0],item[3],item[2],item[1]))

    window.mainloop()
#19 testing
def WIN_adm_manage_site():
    db = DB()
    command = "SELECT * FROM manage_site"
    table_raw = db.search(command)
    table_list = []
    for row in table_raw:
        if row[1] == 0:
            table_list.append([row[0],row[2],"No"])
        else:
            table_list.append([row[0],row[2],"Yes"])
    isreversed = [0]
    filtered_list = table_list[:]
    selectitem = {} 

    sites = ['--ALL--']
    for item in table_list:
        if item[0] not in sites:
                sites.append(item[0])

    managers = ['--ALL--']
    for item in table_list:
        if item[1] not in sites:
                managers.append(item[1])
         
    window = Tk()
    window.title("Administrator Manage Site")
    window.geometry('500x400')
    window.resizable(0, 0)
    window.configure(background="#fff")

    def sorting(arg):
        if arg == 'Sitename':
            tree.delete(*tree.get_children())
            if isreversed[0] % 2 == 0:
                sitename_list = sorted(filtered_list, key = lambda x: x[0])
                isreversed[0] += 1
            else:
                sitename_list = sorted(filtered_list, key = lambda x: x[0],reverse=True)
                isreversed[0] += 1
            for item in sitename_list:
                tree.insert("",'end',values=(item[0],item[1],item[2]))
        elif arg == 'Manager':
            tree.delete(*tree.get_children())
            if isreversed[0] % 2 == 0:
                man_list = sorted(filtered_list, key = lambda x: x[1])
                isreversed[0] += 1
            else:
                man_list = sorted(filtered_list, key = lambda x: x[1],reverse=True)
                isreversed[0] += 1
            for item in man_list:
                tree.insert("",'end',values=(item[0],item[1],item[2]))
        elif arg == 'Open':
            tree.delete(*tree.get_children())
            if isreversed[0] % 2 == 0:
                open_list = sorted(filtered_list, key = lambda x: x[2])
                isreversed[0] += 1
            else:
                open_list = sorted(filtered_list, key = lambda x: x[2],reverse=True)
                isreversed[0] += 1
            for item in open_list:
                tree.insert("",'end',values=(item[0],item[1],item[2]))

    def filtersite(event):
        filtered_list = table_list[:]
        sitename = event.widget.get()
        if sitename == '--ALL--':
            filtered_list = table_list[:]
            tree.delete(*tree.get_children())
            for item in table_list:
                tree.insert("",'end',values=(item[0],item[1],item[2]))
        else:
            filtered_list.clear()
            for item in table_list:
                if sitename in item[0]:
                    filtered_list.append(item)
            tree.delete(*tree.get_children())
            for item in filtered_list:
                tree.insert("",'end',values=(item[0],item[1],item[2]))      
    
    def filterman(event):
        filtered_list = table_list[:]
        manname = event.widget.get()
        if manname == '--ALL--':
            filtered_list = table_list[:]
            tree.delete(*tree.get_children())
            for item in table_list:
                tree.insert("",'end',values=(item[0],item[1],item[2]))
        else:
            filtered_list.clear()
            for item in table_list:
                if manname in item[1]:
                    filtered_list.append(item)
            tree.delete(*tree.get_children())
            for item in filtered_list:
                tree.insert("",'end',values=(item[0],item[1],item[2]))  

    def filteropen(event):
        filtered_list = table_list[:]
        ifopen = event.widget.get()
        if ifopen == 'No':
            filtered_list = table_list[:]
            tree.delete(*tree.get_children())
            for item in table_list:
                tree.insert("",'end',values=(item[0],item[1],item[2]))
        else:
            filtered_list.clear()
            for item in table_list:
                if ifopen in item[2]:
                    filtered_list.append(item)
            tree.delete(*tree.get_children())
            for item in filtered_list:
                tree.insert("",'end',values=(item[0],item[1],item[2]))    

    def navigation(value):
        if value == 1:
            window.destroy()
            WIN_adm_create_site()
        if value == 2:
            if selectitem != {}:
                site_to_be_edited[0] =  selectitem['values']['values'][0]
                window.destroy()
                WIN_adm_edit_site()

    def deletesite():
        if selectitem != {}:
            try:
                command = "DELETE FROM site WHERE sitename='" + selectitem['values']['values'][0] + "'"
                db.delete(command)
                window.destroy()
                WIN_adm_manage_site()
            except:
                tkinter.messagebox.showwarning('Error','Cannot delete!') 

    def back():
        if man_site[0] == 'admuser':
            window.destroy()
            WIN_FUN_adm_and_vis()
        elif man_site[0] == 'adm':
            window.destroy() 
            WIN_FUN_adm()           
        else: pass    

    l0 = Label(window,text="Manage Site", width=36,font=('Arial', 18, 'bold'))
    l0.grid(sticky='n')

    l1 = Label(window,text="Site", font=('Times 14 normal'))
    l1.place(x=25,y=60)
    
    l2 = Label(window,text="Manager", font=('Times 14 normal'))
    l2.place(x=275,y=60)

    l3 = Label(window,text="Open Everyday", font=('Times 14 normal'))
    l3.place(x=125,y=100)

    option1 = StringVar()
    o1 = ttk.Combobox(window,width=8, textvariable=option1)
    o1['values'] = tuple(sites)
    o1.bind("<<ComboboxSelected>>",filtersite)
    o1.place(x=100,y=60)
    o1.current(0)

    option2 = StringVar()
    o2 = ttk.Combobox(window,width=8, textvariable=option2)
    o2['values'] = tuple(managers)
    o2.bind("<<ComboboxSelected>>",filterman)
    o2.place(x=350,y=60)
    o2.current(0)

    option3 = StringVar()
    o3 = ttk.Combobox(window,width=6, textvariable=option3)
    o3['values'] = ('No','Yes') # More states should be involved
    o3.bind("<<ComboboxSelected>>",filteropen)
    o3.place(x=275,y=100)
    o3.current(0)

    # b1 = Button(window,text="Filter", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    # b1.place(x=25,y=140)

    b2 = Button(window,text="Create", width=12, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(1)))
    b2.place(x=200,y=140)

    b3 = Button(window,text="Edit", width=12, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(2)))
    b3.place(x=300,y=140)

    b4 = Button(window,text="Delete", width=12, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: deletesite()))
    b4.place(x=400,y=140)

    b5 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: back()))
    b5.place(x=200,y=350)

    def selectItem(event):
        item = tree.focus()
        selectitem['values'] = tree.item(item)

    tree = ttk.Treeview(window)
    tree.place(x=75,y=180)
    vsb = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    vsb.place(x=425, y=180, height=160)
    tree["show"] = 'headings'
    tree.configure(yscrollcommand=vsb.set,height=8)
    tree["columns"]=("one","two","three")
    tree.column("one", width=150)
    tree.column("two", width=100)
    tree.column("three",width=100)
    tree.heading("one", text="Name",command=(lambda: sorting("Sitename")))
    tree.heading("two", text="Manager",command=(lambda: sorting("Manager")))
    tree.heading("three", text="Open Everyday",command=(lambda: sorting("Open")))
    tree.bind('<ButtonRelease-1>', selectItem)
    for item in table_list:
        tree.insert("",'end',values=(item[0],item[1],item[2]))


    window.mainloop()
#20 managers
def WIN_adm_edit_site():
    db = DB()
    command = "SELECT * FROM edit_site WHERE sitename='" + site_to_be_edited[0] + "'"
    siteinfo = db.search(command)[0]

    command = "SELECT DISTINCT   `P`.`employeeID`,   `P`.`username`,   `P`.`Manager Name` FROM  \
         ( SELECT    `employee`.`employeeID`,   `user`.`username`,   CONCAT( `user`.`fname`, ' ',`user`.`lname` ) as `Manager Name`  FROM  \
              `employee` JOIN `user` ON `employee`.`eusername` = `user`.`username`  WHERE   `employee`.`etype` = 'Manager'  )  AS `P`   LEFT JOIN  \
                   ( SELECT    `employee`.`employeeID`,   `user`.`username`,   CONCAT( `user`.`fname`, ' ',`user`.`lname` ) as `Manager Name`  FROM \
                       `employee` JOIN `user` ON `employee`.`eusername` = `user`.`username`   JOIN `site` ON `site`.`employeeID` = `employee`.`employeeID`  WHERE  \
                            `employee`.`etype` = 'Manager'  )  AS `Q` ON  `P`.`employeeID` = `Q`.`employeeID` WHERE  `Q`.`employeeID` IS NULL"
    
    unassigned_man_tmp = db.search(command)
    unassigned_man = []
    for man in unassigned_man_tmp:
        unassigned_man.append(man[2])
    managers = [siteinfo[4]]

    window = Tk()
    window.title("Administrator Edit Site")
    window.geometry('400x250')
    window.resizable(0, 0)
    window.configure(background="#fff")

    def back():
        window.destroy()
        WIN_adm_manage_site()

    def update():
        newsitename = e1_content.get()
        newzip = e2_content.get()
        newaddress = e3_content.get()
        if option4.get() != managers[0]: 
            for man in unassigned_man_tmp:
                if man[2] in option4.get():
                    ID = man[0]
            try: 
                command = "UPDATE site SET employeeID='" + ID + "' WHERE sitename='"  + site_to_be_edited[0] + "'"
                print(command)
                db.update(command)
                tkinter.messagebox.showinfo('Success','New manager assigned') 
                back()  
            except:
                pass
        elif newsitename != siteinfo[2] or newzip != siteinfo[0] or newaddress != siteinfo[1]:
            try:
                command = "UPDATE site SET sitename='" + newsitename + "',zipcode=" + newzip + ",address='" + newaddress + "',openeveryday=" + str(chVarDis.get()) + " WHERE sitename='" + site_to_be_edited[0] + "'"
                db.update(command)
                tkinter.messagebox.showinfo('Success','Site info updated') 
                back()
            except:
                tkinter.messagebox.showwarning('Update Error','No changes or invalid information')  

    l0 = Label(window,text="Edit Site", width=36,font=('Arial', 18, 'bold'))
    l0.grid(sticky='n')

    l1 = Label(window,text="Name", font=('Times 14 normal'))
    l1.place(x=25,y=60)
    
    l2 = Label(window,text="Zipcode", font=('Times 14 normal'))
    l2.place(x=225,y=60)

    l3 = Label(window,text="Address", font=('Times 14 normal'))
    l3.place(x=25,y=100)

    l4 = Label(window,text="Manager", font=('Times 14 normal'))
    l4.place(x=25,y=140)

    e1_content = StringVar()
    e1 = Entry(window,width=10, bg='powder blue',textvariable=e1_content)
    e1.insert(END,siteinfo[2])
    e1.place(x=100,y=60)

    e2_content = StringVar()
    e2 = Entry(window,width=8, bg='powder blue',textvariable=e2_content)
    e2.insert(END,siteinfo[0])
    e2.place(x=300,y=60)

    e3_content = StringVar()
    e3 = Entry(window,width=26, bg='powder blue',textvariable=e3_content)
    e3.insert(END,siteinfo[1])
    e3.place(x=100,y=100)

    option4 = StringVar()
    o4 = ttk.Combobox(window,width=12, textvariable=option4)
    o4['values'] = tuple(managers + unassigned_man)
    o4.place(x=100,y=140)
    o4.current(0)

    chVarDis = IntVar()
    c1 = Checkbutton(window, text='Open Everyday',variable=chVarDis)
    if siteinfo[3] == 1:
        c1.select()
    else:
        c1.deselect()
    c1.place(x=250,y=140)

    b1 = Button(window,text="Back", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: back()))
    b1.place(x=25,y=200)

    b2 = Button(window,text="Update", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: update()))
    b2.place(x=275,y=200)

    window.mainloop()   
#21 managers
def WIN_adm_create_site():
    db = DB()
    command = "SELECT DISTINCT   `P`.`employeeID`,   `P`.`username`,   `P`.`Manager Name` FROM  \
         ( SELECT    `employee`.`employeeID`,   `user`.`username`,   CONCAT( `user`.`fname`, ' ',`user`.`lname` ) as `Manager Name`  FROM  \
              `employee` JOIN `user` ON `employee`.`eusername` = `user`.`username`  WHERE   `employee`.`etype` = 'Manager'  )  AS `P`   LEFT JOIN  \
                   ( SELECT    `employee`.`employeeID`,   `user`.`username`,   CONCAT( `user`.`fname`, ' ',`user`.`lname` ) as `Manager Name`  FROM \
                       `employee` JOIN `user` ON `employee`.`eusername` = `user`.`username`   JOIN `site` ON `site`.`employeeID` = `employee`.`employeeID`  WHERE  \
                            `employee`.`etype` = 'Manager'  )  AS `Q` ON  `P`.`employeeID` = `Q`.`employeeID` WHERE  `Q`.`employeeID` IS NULL"
    
    unassigned_man_tmp = db.search(command)
    unassigned_man = []
    for man in unassigned_man_tmp:
        unassigned_man.append(man[2])

    window = Tk()
    window.title("Administrator Create Site")
    window.geometry('400x250')
    window.resizable(0, 0)
    window.configure(background="#fff")

    def create():
        newsitename = e1_content.get()
        newzip = e2_content.get()
        newaddress = e3_content.get()
        for man in unassigned_man_tmp:
            if man[2] in option4.get():
                newemployID = man[0]
        try:
            command = "INSERT INTO site SET sitename='" + newsitename + "',zipcode=" + newzip + ",address='" + newaddress + "',openeveryday=" + str(chVarDis.get()) + ",employeeID='" + newemployID + "'" \
                        + ",city='Atlanta',state='GA'"
            db.insert(command)
            tkinter.messagebox.showinfo('Success','New site created.') 
            back()
        except:
            tkinter.messagebox.showwarning('Create Error','Sitename should be unique or zipcode should be 5 digits')  
        

    def back():
        window.destroy()
        WIN_adm_manage_site()

    l0 = Label(window,text="Create Site", width=36,font=('Arial', 18, 'bold'))
    l0.grid(sticky='n')

    l1 = Label(window,text="Name", font=('Times 14 normal'))
    l1.place(x=25,y=60)
    
    l2 = Label(window,text="Zipcode", font=('Times 14 normal'))
    l2.place(x=225,y=60)

    l3 = Label(window,text="Address", font=('Times 14 normal'))
    l3.place(x=25,y=100)

    l4 = Label(window,text="Manager", font=('Times 14 normal'))
    l4.place(x=25,y=140)

    e1_content = StringVar()
    e1 = Entry(window,width=10, bg='powder blue',textvariable=e1_content)
    e1.place(x=100,y=60)

    e2_content = StringVar()
    e2 = Entry(window,width=8, bg='powder blue',textvariable=e2_content)
    e2.place(x=300,y=60)

    e3_content = StringVar()
    e3 = Entry(window,width=26, bg='powder blue',textvariable=e3_content)
    e3.place(x=100,y=100)

    option4 = StringVar()
    o4 = ttk.Combobox(window,width=12, textvariable=option4)
    o4['values'] = tuple(unassigned_man)
    o4.place(x=100,y=140)
    o4.current(0)

    chVarDis = IntVar()
    c1 = Checkbutton(window, text='Open Everyday',variable=chVarDis)
    if True:
        c1.select()
    else:
        c1.deselect()
    c1.place(x=250,y=140)

    b1 = Button(window,text="Back", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: back()))
    b1.place(x=25,y=200)

    b2 = Button(window,text="Create", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: create()))
    b2.place(x=275,y=200)

    window.mainloop()   
#22 #! Transit Logged
def WIN_adm_manage_transit():
    db = DB()
    command = "select * from manage_transit"
    table_raw = db.search(command)
    table = {}
    sites = []
    ttype = []
    for row in table_raw:
        if row[0] not in table:
            table[row[0]] = [row[0],row[1],str(row[2]),row[3],[row[4]]]
        elif row[4] not in table[row[0]][4]:
            table[row[0]][4].append(row[4])
        if row[4] not in sites:
            sites.append(row[4])
        if row[1] not in ttype:
            ttype.append(row[1])
    table_list = [table[value] for value in table]
    isreversed = [0]
    filtered_list = table_list[:]
    selectitem = {}
     
    window = Tk()
    window.title("Administrator Manage Transit")
    window.geometry('500x400')
    window.resizable(0, 0)
    window.configure(background="#fff")

    def filtersite(event):
        filtered_list = table_list[:]
        sitename = event.widget.get()
        if sitename == '--ALL--':
            filtered_list = table_list[:]
            tree.delete(*tree.get_children())
            for item in table_list:
                tree.insert("",'end',values=(item[0],item[1],item[2],len(item[4])))
        else:
            filtered_list.clear()
            for item in table_list:
                if sitename in item[4]:
                    filtered_list.append(item)
            tree.delete(*tree.get_children())
            for item in filtered_list:
                tree.insert("",'end',values=(item[0],item[1],item[2],len(item[4])))  

    def filter(table_list):
        start = e5a_content.get()
        end = e5b_content.get()
        if start != '' and end != '':
            if float(end) < float(start):
                tkinter.messagebox.showwarning('Error','Its not a good price range') 
            else:
                filtered_list.clear()
                for item in table_list:
                    if float(item[2]) >= float(start) and float(item[2]) <= float(end):
                        filtered_list.append(item)
                tree.delete(*tree.get_children())
                for item in filtered_list:
                    tree.insert("",'end',values=(item[0],item[1],item[2],len(item[4])))  
        elif e2_content.get() != '' :
            filtered_list.clear()
            for item in table_list:
                if e2_content.get() == item[0]:
                    filtered_list.append(item)
            tree.delete(*tree.get_children())
            for item in filtered_list:
                tree.insert("",'end',values=(item[0],item[1],item[2],len(item[4])))  
        
    
    def filtertype(event):
        filtered_list = table_list[:]
        ttype = event.widget.get()
        if ttype == '--ALL--':
            filtered_list.clear()
            filtered_list = table_list[:]
            tree.delete(*tree.get_children())
            for item in table_list:
                tree.insert("",'end',values=(item[0],item[1],item[2],len(item[4])))
        else:
            filtered_list.clear()
            for item in table_list:
                if ttype in item[1]:
                    filtered_list.append(item)
            tree.delete(*tree.get_children())
            for item in filtered_list:
                tree.insert("",'end',values=(item[0],item[1],item[2],len(item[4])))
    
    def deletetransit():
        if selectitem != {}:
            try:
                command = "DELETE FROM transit WHERE route='" + str(selectitem['values']['values'][0]) + "' and type='" + selectitem['values']['values'][1] + "'"
                db.delete(command)
                window.destroy()
                WIN_adm_manage_transit()
            except:
                tkinter.messagebox.showwarning('Error','Cannot delete!') 

    def navigation(value):
        if value == 1:
            window.destroy()
            WIN_adm_create_transit()
        if value == 2:
            window.destroy()
            transit_to_be_edited[0] = str(selectitem['values']['values'][0])
            WIN_adm_edit_transit()

    def back():
        if man_transit[0] == 'adm':
            window.destroy() 
            WIN_FUN_adm()           
        elif man_transit[0] == 'admuser':
            window.destroy()
            WIN_FUN_adm_and_vis()
        else: pass

    l0 = Label(window,text="Take Transit", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    l1 = Label(window,text="Transport Type", font=('Times', 14, 'normal'))
    l1.place(x=25,y=60)

    l2 = Label(window,text="Route", font=('Times', 14, 'normal'))
    l2.place(x=250,y=60)

    l3 = Label(window,text="Contain Site", font=('Times', 14, 'normal'))
    l3.place(x=25,y=100)

    l4 = Label(window,text="Price Range", font=('Times', 14, 'normal'))
    l4.place(x=250,y=100)

    l5 = Label(window,text="--", font=('Times', 14, 'normal'))
    l5.place(x=400,y=100)

    e5a_content = StringVar()
    e5a = Entry(window,width=3, bg='powder blue',textvariable=e5a_content)
    e5a.place(x=350,y=100)

    e5b_content = StringVar()
    e5b = Entry(window,width=3, bg='powder blue',textvariable=e5b_content)
    e5b.place(x=425,y=100)

    e2_content = StringVar()
    e2 = Entry(window,width=14, bg='powder blue',textvariable=e2_content)
    e2.place(x=350,y=60)

    option1 = StringVar()
    o1 = ttk.Combobox(window,width=10, textvariable=option1)
    o1['values'] = tuple(ttype)
    o1.bind("<<ComboboxSelected>>",filtertype)
    o1.place(x=125,y=60)
    o1.current(0)

    option3 = StringVar()
    o3 = ttk.Combobox(window,width=8, textvariable=option3)
    o3['values'] = tuple(sites) # More states should be involved
    o3.bind("<<ComboboxSelected>>",filtersite)
    o3.place(x=125,y=100)
    o3.current(0)

    b1 = Button(window,text="Filter", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: filter(table_list)))
    b1.place(x=25,y=140)

    b2 = Button(window,text="Create", width=12, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(1)))
    b2.place(x=200,y=140)

    b3 = Button(window,text="Edit", width=12, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(2)))
    b3.place(x=300,y=140)

    b4 = Button(window,text="Delete", width=12, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: deletetransit()))
    b4.place(x=400,y=140)

    b5 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: back()))
    b5.place(x=200,y=350)

    def selectItem(event):
        item = tree.focus()
        selectitem['values'] = tree.item(item)
        
    tree = ttk.Treeview(window)
    tree.place(x=25,y=160)
    vsb = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    vsb.place(x=425, y=160, height=240)
    tree["show"] = 'headings'
    tree.configure(yscrollcommand=vsb.set,height=12)
    tree["columns"]=("one","two","three","four","five")
    tree.column("one", width=80)
    tree.column("two", width=80)
    tree.column("three",width=80)
    tree.column("four",width=60)
    tree.column("four",width=60)
    tree.heading("one", text="Route",command=(lambda: None))
    tree.heading("two", text="Transport Type",command=(lambda: None))
    tree.heading("three", text="Price($)",command=(lambda: None))
    tree.heading("four",text="# Connected Sites",command=(lambda: None))
    tree.heading("five",text="# Transit Logged",command=(lambda: None))
    tree.bind('<ButtonRelease-1>', selectItem)
    for item in table_list:
        tree.insert("",'end',values=(item[0],item[1],item[2],len(item[4])))

    window.mainloop()
#23 testing
def WIN_adm_edit_transit():
    db = DB()
    command = "SELECT * FROM edit_transit WHERE route='" + transit_to_be_edited[0] + "'"
    transitinfo = db.search(command)
    orisites = []
    for row in transitinfo:
        if row[0] not in orisites:
            orisites.append(row[0])
        price = row[1]
        ttype = row[3]

    command = "SELECT sitename FROM site"
    sites_tmp = list(db.search(command))
    sites = []
    for site in sites_tmp:
        sites.append(site)
    selectitem = {} 
    window = Tk()
    window.title("Administrator Edit Transit")
    window.geometry('400x300')
    window.resizable(0, 0)
    window.configure(background="#fff")

    def update():
        if e1_content.get() != '' and e2_content.get() != '' and selectitem != {}:
            try:
                command = "UPDATE transit SET route='" + e1_content.get() + "',price='" + e2_content.get()  + "' WHERE route='" +  transit_to_be_edited[0] + "'"
                db.update(command)
                if selectitem['values'] != []:
                    command = "DELETE FROM connect WHERE transitroute='" + transit_to_be_edited[0] + "' and transittype='" + ttype + "'" 
                    db.delete(command)
                    for site in selectitem['values']:
                        command = "INSERT INTO connect SET transitroute='" + e1_content.get()  + "',sitename='" + site + "',transittype='" + ttype + "'" 
                        db.update(command)
                    tkinter.messagebox.showinfo('Good','Edited a  transit!') 
            except:
                tkinter.messagebox.showwarning('Error','Cannot edit this transit!') 
        
    def back():
        window.destroy()
        WIN_adm_manage_transit()

    l0 = Label(window,text="Edit Transit", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    l1 = Label(window,text="Transport Type", font=('Times', 14, 'normal'))
    l1.place(x=25,y=60)

    l2 = Label(window,text=ttype, font=('Times', 14, 'italic','bold'))
    l2.place(x=125,y=60)

    l3 = Label(window,text="Route", font=('Times', 14, 'normal'))
    l3.place(x=175,y=60)

    l4 = Label(window,text="Price($)", font=('Times', 14, 'normal'))
    l4.place(x=275,y=60)

    l5 = Label(window,text="Connected Sites", font=('Times', 14, 'normal'))
    l5.place(x=25,y=140)

    e1_content = StringVar()
    e1 = Entry(window,width=3, bg='powder blue',textvariable=e1_content)
    e1.insert(END,transit_to_be_edited[0])
    e1.place(x=225,y=60)

    e2_content = StringVar()
    e2 = Entry(window,width=3, bg='powder blue',textvariable=e2_content)
    e2.insert(END,price)
    e2.place(x=325,y=60)

    def selectItem(event):
        selectitem.clear()
        item = tree.selection()
        selectitem['values'] = []
        for i in item:
            selectitem['values'].append( tree.item(i)['values'][0])

    tree = ttk.Treeview(window)
    tree.place(x=150,y=100)
    vsb = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    vsb.place(x=400, y=100, height=120)
    tree["show"] = 'headings'
    tree.configure(yscrollcommand=vsb.set,height=6)
    tree["columns"]=("one")
    tree.column("one", width=200)
    tree.heading("one", text="Name",command=(lambda: None))
    
    tree.bind('<ButtonRelease-1>', selectItem)
    i = 0
    for item in sites:
        # print(item)
        tree.insert("",i,item[0],values=(item))
        i = i + 1
    tree.selection_set(orisites)
    tree.focus_set()

    for site in orisites:
        tree.focus(site)
    
    b1 = Button(window,text="Back", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: back()))
    b1.place(x=25,y=250)

    b2 = Button(window,text="Update", width=12, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: update()))
    b2.place(x=300,y=250)

    window.mainloop() 
#24 #! update the view
def WIN_adm_create_transit():
    db = DB()
    command = "SELECT sitename FROM site"
    sites_tmp = list(db.search(command))
    sites = []
    for site in sites_tmp:
        sites.append(site)
    selectitem = {} 
                 
    window = Tk()
    window.title("Administrator Create Transit")
    window.geometry('400x300')
    window.resizable(0, 0)
    window.configure(background="#fff")
    
    def create():
        if len(selectitem['values']) < 2:
            tkinter.messagebox.showwarning('Error','At least two connected sites!') 
        elif e1_content.get() != '' and e2_content.get() != '':
            try:
                command = "INSERT INTO transit SET route='" + e1_content.get() + "',price=" + e2_content.get() + ",type='" + option1.get() + "'"
                db.update(command)
                for site in selectitem['values']:
                    command = "INSERT INTO connect SET transitroute='" + e1_content.get() + "',transittype='" + option1.get() + "',sitename='" + site + "'"
                    db.update(command)
                command = "DROP VIEW IF EXISTS `manage_transit`;"
                db.update(command)
                #! Bugs here
                command = "CREATE VIEW `manage_transit` AS\
                                SELECT\
                                    `transit`.`route`,\
                                    `transit`.`type`,\
                                    `transit`.`price`,\
                                    `take`.`username`,	\
                                    `connect`.`sitename`	\
                                FROM\
                                    `transit` JOIN `take` ON `transit`.`route` = `take`.`transitroute` AND `take`.`transittype` = `transit`.`type`\
                                    JOIN `connect` ON `take`.`transittype` = `connect`.`transittype` AND `take`.`transitroute` = `connect`.`transitroute`"
                db.update(command)
                tkinter.messagebox.showinfo('Good','Create a new transit!') 
            except:
                tkinter.messagebox.showwarning('Error','Cannot create this new transit!') 

    def back():
        window.destroy()
        WIN_adm_manage_transit()

    l0 = Label(window,text="Create Transit", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    l1 = Label(window,text="Transport Type", font=('Times', 14, 'normal'))
    l1.place(x=25,y=60)

    l3 = Label(window,text="Route", font=('Times', 14, 'normal'))
    l3.place(x=200,y=60)

    l4 = Label(window,text="Price($)", font=('Times', 14, 'normal'))
    l4.place(x=300,y=60)

    l5 = Label(window,text="Connected Sites", font=('Times', 14, 'normal'))
    l5.place(x=25,y=140)

    e1_content = StringVar()
    e1 = Entry(window,width=3, bg='powder blue',textvariable=e1_content)
    e1.place(x=250,y=60)

    e2_content = StringVar()
    e2 = Entry(window,width=3, bg='powder blue',textvariable=e2_content)
    e2.place(x=350,y=60)

    option1 = StringVar()
    o1 = ttk.Combobox(window,width=5, textvariable=option1)
    o1['values'] = ('MARTA','Bus','Bike')
    o1.place(x=125,y=60)
    o1.current(0)
    # For now, it's fixed

    b1 = Button(window,text="Back", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: back()))
    b1.place(x=25,y=250)

    b2 = Button(window,text="Create", width=12, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: create()))
    b2.place(x=300,y=250)

    def selectItem(event):
        selectitem.clear()
        item = tree.selection()
        selectitem['values'] = []
        for i in item:
            selectitem['values'].append( tree.item(i)['values'][0])

    tree = ttk.Treeview(window)
    tree.place(x=150,y=100)
    vsb = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    vsb.place(x=400, y=100, height=120)
    tree["show"] = 'headings'
    tree.configure(yscrollcommand=vsb.set,height=6)
    tree["columns"]=("one")
    tree.column("one", width=200)
    tree.heading("one", text="Name",command=(lambda: None))
    tree.bind('<ButtonRelease-1>', selectItem)
    for item in sites:
        tree.insert("",'end',values=(item))

    window.mainloop() 
#25 #! change the event information for all the corresponding visits
def WIN_man_manage_event():
    db = DB()
    command = "SELECT * FROM manage_event"
    eventinfo = db.search(command)
    table_list = []
    for row in eventinfo:
        table_list.append(row)
    isreversed = [0]
    filtered_list = table_list[:]
    selectitem = {} 
            
    window = Tk()
    window.title("Manager Manage Event")
    window.geometry('500x500')
    window.resizable(0, 0)
    window.configure(background="#fff")

    def navigation(value):
        command = "SELECT employeeID FROM employee WHERE eusername='" + username_login[0] + "'"
        ID = db.search(command)[0][0]
        command = "SELECT sitename FROM site WHERE employeeID='" + ID + "'"
        sitename = db.search(command)[0][0]
        whos_site[0] = [sitename,ID]
        if value == 1:
            window.destroy()
            WIN_man_create_event()
        if value == 2:
            event_to_be_edited[0] = selectitem['values']['values'][0]
            window.destroy()
            WIN_man_VE_event()

    def filter():
        name = e1_content.get()
        keyword = e2_content.get()
        startdate = e3_content.get()
        enddate = e4_content.get()
        duration_s = e6a_content.get()
        duration_e = e6b_content.get()
        visit_s = e8a_content.get()
        visit_e = e8b_content.get()
        revenue_s = e10a_content.get()
        revenue_e = e10b_content.get()
        if name != '':
            filtered_list.clear()
            for item in table_list:
                if name in item[0]:
                    if item not in filtered_list:
                        filtered_list.append(item)
            tree.delete(*tree.get_children())
            for item in filtered_list:
                tree.insert("",'end',values=(item[0],item[12],item[9],item[11],item[10])) 
        elif keyword != '':
            filtered_list.clear()
            for item in table_list:
                if keyword in item[3]:
                    if item not in filtered_list:
                        filtered_list.append(item)
            tree.delete(*tree.get_children())
            for item in filtered_list:
                tree.insert("",'end',values=(item[0],item[12],item[9],item[11],item[10])) 
        elif startdate != '' and enddate != '':
            startdate_date = datetime.date(int(startdate.split("-")[0]),int(startdate.split("-")[1]),int(startdate.split("-")[2]))
            enddate_date = datetime.date(int(enddate.split("-")[0]),int(enddate.split("-")[1]),int(enddate.split("-")[2]))
            if startdate > enddate_date:
                tkinter.messagebox.showwarning('Date Error','Start Date should be before End date!') 
            else:
                filtered_list.clear()
                for item in table_list:      
                    if startdate_date <= enddate_date:
                        if (startdate_date <= item[1] and enddate_date >= item[1]) or (startdate_date <= item[2] and enddate_date >= item[1]):
                            if item not in filtered_list:
                                filtered_list.append(item)
                tree.delete(*tree.get_children())
                for item in filtered_list:
                    tree.insert("",'end',values=(item[0],item[12],item[9],item[11],item[10]))
        elif duration_e != 0 and duration_s != 0:
            filtered_list.clear()
            for item in table_list: 
                if duration_s <= item[9] and duration_e >= item[9]:
                    if item not in filtered_list:
                        filtered_list.append(item)
            tree.delete(*tree.get_children())
            for item in filtered_list:
                tree.insert("",'end',values=(item[0],item[12],item[9],item[11],item[10]))
        elif visit_s != 0 and visit_e != 0:
            filtered_list.clear()
            for item in table_list: 
                if visit_s <= item[11] and visit_e >= item[11]:
                    if item not in filtered_list:
                        filtered_list.append(item)
            tree.delete(*tree.get_children())
            for item in filtered_list:
                tree.insert("",'end',values=(item[0],item[12],item[9],item[11],item[10]))
        elif revenue_s != 0 and revenue_e != 0: 
            filtered_list.clear()
            for item in table_list: 
                if visit_s <= item[10] and visit_e >= item[10]:
                    if item not in filtered_list:
                        filtered_list.append(item)
            tree.delete(*tree.get_children())
            for item in filtered_list:
                tree.insert("",'end',values=(item[0],item[12],item[9],item[11],item[10]))
        else:pass

    def deleteevent():
        if selectitem != {}:
            try:
                command = "DELETE FROM event WHERE eventname='" + str(selectitem['values']['values'][0]) + "'"
                db.delete(command)
                window.destroy()
                WIN_man_manage_event()
            except:
                tkinter.messagebox.showwarning('Error','Cannot delete!') 

    def back():
        if man_event[0] == 'man':
            window.destroy() 
            WIN_FUN_man()           
        elif man_event[0] == 'manuser':
            window.destroy()
            WIN_FUN_man_and_vis()
        else: pass

    l0 = Label(window,text="Manage Event", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    l1 = Label(window,text="Name", font=('Times', 14, 'normal'))
    l1.place(x=25,y=60)

    l2 = Label(window,text="Description Keyword", font=('Times', 14, 'normal'))
    l2.place(x=250,y=60)

    l3 = Label(window,text="Start Date", font=('Times', 14, 'normal'))
    l3.place(x=25,y=100)

    l4 = Label(window,text="End Date", font=('Times', 14, 'normal'))
    l4.place(x=250,y=100)

    l5 = Label(window,text="Duration Range", font=('Times', 14, 'normal'))
    l5.place(x=25,y=140)

    l6 = Label(window,text="--", font=('Times', 14, 'normal'))
    l6.place(x=175,y=140)

    l7 = Label(window,text="Total Visits Range", font=('Times', 14, 'normal'))
    l7.place(x=250,y=140)

    l8 = Label(window,text="--", font=('Times', 14, 'normal'))
    l8.place(x=425,y=140)

    l9 = Label(window,text="Total Revenue Range", font=('Times', 14, 'normal'))
    l9.place(x=100,y=180)

    l10 = Label(window,text="--", font=('Times', 14, 'normal'))
    l10.place(x=300,y=180)

    e1_content = StringVar()
    e1 = Entry(window,width=10, bg='powder blue',textvariable=e1_content)
    e1.place(x=100,y=60)

    e2_content = StringVar()
    e2 = Entry(window,width=8, bg='powder blue',textvariable=e2_content)
    e2.place(x=400,y=60)

    e3_content = StringVar()
    e3 = Entry(window,width=14, bg='powder blue',textvariable=e3_content)
    e3.place(x=100,y=100)

    e4_content = StringVar()
    e4 = Entry(window,width=14, bg='powder blue',textvariable=e4_content)
    e4.place(x=350,y=100)

    e6a_content = IntVar()
    e6a = Entry(window,width=3, bg='powder blue',textvariable=e6a_content)
    e6a.place(x=135,y=140)

    e6b_content = IntVar()
    e6b = Entry(window,width=3, bg='powder blue',textvariable=e6b_content)
    e6b.place(x=190,y=140)

    e8a_content = IntVar()
    e8a = Entry(window,width=3, bg='powder blue',textvariable=e8a_content)
    e8a.place(x=385,y=140)

    e8b_content = IntVar()
    e8b = Entry(window,width=3, bg='powder blue',textvariable=e8b_content)
    e8b.place(x=440,y=140)

    e10a_content = IntVar()
    e10a = Entry(window,width=3, bg='powder blue',textvariable=e10a_content)
    e10a.place(x=260,y=180)

    e10b_content = IntVar()
    e10b = Entry(window,width=3, bg='powder blue',textvariable=e10b_content)
    e10b.place(x=315,y=180)

    b1 = Button(window,text="Filter", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: filter()))
    b1.place(x=25,y=220)

    b2 = Button(window,text="Create", width=12, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(1)))
    b2.place(x=200,y=220)

    b3 = Button(window,text="ViewEdit", width=12, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(2)))
    b3.place(x=300,y=220)

    b4 = Button(window,text="Delete", width=12, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: deleteevent()))
    b4.place(x=400,y=220)

    b5 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: back()))
    b5.place(x=200,y=450)

    def selectItem(event):
        item = tree.focus()
        selectitem['values'] = tree.item(item)

    tree = ttk.Treeview(window)
    tree.place(x=25,y=260)
    vsb = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    vsb.place(x=425, y=260, height=160)
    tree["show"] = 'headings'
    tree.configure(yscrollcommand=vsb.set,height=8)
    tree["columns"]=("one","two","three","four","five")
    tree.column("one", width=80)
    tree.column("two", width=80)
    tree.column("three",width=80)
    tree.column("four",width=80)
    tree.column("five",width=80)
    tree.heading("one", text="Name",command=(lambda: None))
    tree.heading("two", text="Staff Count",command=(lambda: None))
    tree.heading("three", text="Duration(days)",command=(lambda: None))
    tree.heading("four", text="Total Visits",command=(lambda: None))
    tree.heading("five", text="Total Revenue",command=(lambda: None))
    tree.bind('<ButtonRelease-1>', selectItem)
    for item in table_list:
        tree.insert("",'end',values=(item[0],item[12],item[9],item[11],item[10]))

    window.mainloop()
#26 #! check staff assigned date
def WIN_man_VE_event():
    db = DB()
    command = "SELECT * FROM edit_event WHERE eventname='" + event_to_be_edited[0] + "'"
    eventinfo = db.search(command)
    table_list = []
    staffs = []
    for row in eventinfo:
        table_list.append(row)
        if row[7] not in staffs:
            staffs.append(row[7])
    filtered_list = table_list[:]
    window = Tk()
    window.title("Manager View/Edit Event")
    window.geometry('400x800')
    window.resizable(0, 0)
    window.configure(background="#fff")

    command = "SELECT CONCAT(fname,' ',lname) from user WHERE username in (SELECT eusername FROM employee WHERE etype='Staff')"
    allstaffs = db.search(command)
    selectitem = {}

    oristaffsid = []
    for staff in staffs:
        command = "SELECT username FROM user WHERE CONCAT(fname,' ',lname)='" + staff + "'"
        username = db.search(command)[0][0]
        command = "SELECT employeeID FROM employee WHERE eusername='" + username + "'"
        oristaffsid.append(db.search(command)[0][0])

    Eventname =  event_to_be_edited[0]
    Price = table_list[0][3]
    Startdate = table_list[0][1]
    Enddate = table_list[0][2]
    Minsta = table_list[0][6]
    Capacity = table_list[0][4]

    def filter():
        visit_s = e16a_content.get()
        visit_e = e16b_content.get()
        revenue_s = e18a_content.get()
        revenue_e = e18b_content.get()
        if visit_s != 0 and visit_e != 0:
            filtered_list.clear()
            tmp_list = []
            for item in table_list: 
                if visit_s <= item[10] and visit_e >= item[10]:
                    if (item[9],item[10],item[11]) not in tmp_list:
                        filtered_list.append(item)
                        tmp_list.append((item[9],item[10],item[11]))
            tree.delete(*tree.get_children())
            for item in filtered_list:
                tree.insert("",'end',values=(item[9],item[10],item[11]))
        elif revenue_s != 0 and revenue_e != 0: 
            filtered_list.clear()
            for item in table_list: 
                if revenue_s <= item[11] and revenue_e >= item[11]:
                    if (item[9],item[10],item[11]) not in tmp_list:
                        filtered_list.append(item)
                        tmp_list.append((item[9],item[10],item[11]))
            tree.delete(*tree.get_children())
            for item in filtered_list:         
                tree.insert("",'end',values=(item[9],item[10],item[11]))
        else:pass

    def update():
        if len(selectitem['values']) >= Minsta:
            newstaffs = []
            for staff in selectitem['values']:
                #! check staff assigned date
                command = "SELECT username FROM user WHERE CONCAT(fname,' ',lname)='" + staff + "'"
                # print(command)
                username = db.search(command)[0][0]
                command = "SELECT employeeID FROM employee WHERE eusername='" + username + "'"
                # print(command)
                ID = db.search(command)[0][0]
                newstaffs.append(ID)
            for staff in selectitem['values']:
                command = "SELECT username FROM user WHERE CONCAT(fname,' ',lname)='" + staff + "'"
                # print(command)
                username = db.search(command)[0][0]
                command = "SELECT employeeID FROM employee WHERE eusername='" + username + "'"
                # print(command)
                ID = db.search(command)[0][0]
                command = "SELECT sitename FROM event WHERE eventname='" + event_to_be_edited[0] + "'"
                # print(command)
                sitesinfo = db.search(command)
                sites = []
                for site in sitesinfo:
                    if site[0] not in sites:
                        sites.append(site[0])
                try:
                    for site in sites:
                        eventstartdate = str(table_list[0][1]).split(",")[0]
                        for oriID in oristaffsid:
                            if oriID not in newstaffs:                       
                                command = "DELETE FROM assign_to WHERE employeeID='" + oriID + "'"
                                db.delete(command)
                        try:
                            command = "INSERT INTO assign_to SET eventname='" + event_to_be_edited[0] + "',eventstartdate='" + eventstartdate  + "',employeeID='" +  str(ID) + "',sitename='" + site + "'"
                            db.update(command)
                        except:
                            pass 
                        tkinter.messagebox.showinfo('Good','Edited an event!') 
                except:
                    tkinter.messagebox.showwarning('Error','Cannot edit this transit!') 
        
    def back():
        window.destroy()
        WIN_man_manage_event()

    l0 = Label(window,text="View/Edit Event", width=36,font=('Arial', 18, 'bold'))
    l0.place(x=25,y=0)

    l1 = Label(window,text="Name", font=('Times 14 normal'))
    l1.place(x=25,y=60)
    
    l2 = Label(window,text=Eventname, font=('Times 14 italic bold'))
    l2.place(x=100,y=60)

    l3 = Label(window,text="Price($)", font=('Times 14 normal'))
    l3.place(x=225,y=60)

    l4 = Label(window,text=Price, font=('Times 14 italic bold'))
    l4.place(x=300,y=60)
    
    l5 = Label(window,text="Start Date",font=('Times 14 normal'))
    l5.place(x=25,y=100)
    
    l6 = Label(window,text=Startdate,font=('Times 14 italic bold'))
    l6.place(x=100,y=100)

    l7 = Label(window,text="End Date", font=('Times 14 normal'))
    l7.place(x=225,y=100)

    l8 = Label(window,text=Enddate, font=('Times 14 italic bold'))
    l8.place(x=300,y=100)
    
    l9 = Label(window,text="Minimum Staff Required", font=('Times 14 normal'))
    l9.place(x=25,y=140)

    l10 = Label(window,text=Minsta, font=('Times 14 italic bold'))
    l10.place(x=200,y=140)

    l11 = Label(window,text="Capacity", font=('Times 14 normal'))
    l11.place(x=225,y=140)
       
    l12 = Label(window,text=Capacity,font=('Times 14 italic bold'))
    l12.place(x=300,y=140)

    l13 = Label(window,text="Staff Assigned", font=('Times 14 normal'))
    l13.place(x=25,y=220)

    l14 = Label(window,text="Description", font=('Times 14 normal'))
    l14.place(x=25,y=340)
    
    l15 = Label(window,text="Daily Visits Range", font=('Times 14 normal'))
    l15.place(x=25,y=460)

    l16 = Label(window,text="--", font=('Times 14 normal'))
    l16.place(x=250,y=460)

    l17 = Label(window,text="Daily Revenue Range", font=('Times 14 normal'))
    l17.place(x=25,y=500)

    l18 = Label(window,text="--", font=('Times 14 normal'))
    l18.place(x=250,y=500)

    e16a_content = IntVar()
    e16a = Entry(window,width=3, bg='powder blue',textvariable=e16a_content)
    e16a.place(x=200,y=460)

    e16b_content = IntVar()
    e16b = Entry(window,width=3, bg='powder blue',textvariable=e16b_content)
    e16b.place(x=275,y=460)

    e18a_content = IntVar()
    e18a = Entry(window,width=3, bg='powder blue',textvariable=e18a_content)
    e18a.place(x=200,y=500)

    e18b_content = IntVar()
    e18b = Entry(window,width=3, bg='powder blue',textvariable=e18b_content)
    e18b.place(x=275,y=500)

    def selectItem1(event):
        selectitem.clear()
        item = tree1.selection()
        selectitem['values'] = []
        for i in item:
            selectitem['values'].append( tree1.item(i)['values'][0])

    tree1 = ttk.Treeview(window)
    tree1.place(x=150,y=180)
    vsb1 = ttk.Scrollbar(window, orient="vertical", command=tree1.yview)
    vsb1.place(x=400, y=180, height=120)
    tree1["show"] = 'headings'
    tree1.configure(yscrollcommand=vsb1.set,height=6)
    tree1["columns"]=("one")
    tree1.column("one", width=200)
    tree1.heading("one", text="Name",command=(lambda: None))
    
    tree1.bind('<ButtonRelease-1>', selectItem1)
    i = 0
    for item in allstaffs:
        tree1.insert("",i,item[0],values=(item))
        i = i + 1
    tree1.selection_set(staffs)
    tree1.focus_set()
    for staff in staffs:
        tree1.focus(staff)

    st2 = scrolledtext.ScrolledText(window, width=25, height=8,wrap=WORD,bd=8,)
    st2.place(x=150,y=300)
    st2.insert(INSERT,table_list[0][5])
    st2.config(state=DISABLED)

    b1 = Button(window,text="Filter", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: filter()))
    b1.place(x=25,y=540)

    b2 = Button(window,text="Update", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: update()))
    b2.place(x=275,y=540)

    b3 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: back()))
    b3.pack(side='bottom')

    def selectItem(event):
        pass

    tree = ttk.Treeview(window)
    tree.place(x=25,y=580)
    vsb = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    vsb.place(x=325, y=580, height=160)
    tree["show"] = 'headings'
    tree.configure(yscrollcommand=vsb.set,height=8)
    tree["columns"]=("one","two","three")
    tree.column("one", width=100)
    tree.column("two", width=100)
    tree.column("three",width=100)
    tree.heading("one", text="Date",command=(lambda: None))
    tree.heading("two", text="Daily Visits",command=(lambda:  None))
    tree.heading("three", text="Daily Revenue($)",command=(lambda: None))
    tree.bind('<ButtonRelease-1>', selectItem)
    tmp_list = []
    for item in table_list:
        if (item[9],item[10],item[11]) not in tmp_list:
            tree.insert("",'end',values=(item[9],item[10],item[11]))
        tmp_list.append((item[9],item[10],item[11]))
    window.mainloop()
#27 #! unassigned staffs,overlap
def WIN_man_create_event():
    db =DB()
    command = "SELECT CONCAT(fname,' ',lname) from user WHERE username in (SELECT eusername FROM employee WHERE etype='Staff')"
    allstaffs = db.search(command)
    selectitem = {}
            
    window = Tk()
    window.title("Manager Create Event")
    window.geometry('500x500')
    window.resizable(0, 0)
    window.configure(background="#fff")

    def create():
        name = e1_content.get()
        price = e2_content.get()
        cap = e3_content.get()
        minsta = e4_content.get()
        startdate = e5_content.get()
        enddate = e6_content.get()
        description = st1.get("1.0","end-1c")
        site = whos_site[0][0]
        print(selectitem['values']['values'])
        
        if None not in (name,price,cap,minsta,startdate,enddate,description,site) and startdate <= enddate:
            try:
                command = "INSERT INTO event SET description='" + description \
                    + "',minStaffReq='" + minsta \
                    + "',capacity='" + cap \
                    + "',price='" + price \
                    + "',enddate='" + enddate \
                    + "',eventname='" + name \
                    + "',eventstartdate='" + startdate \
                    + "',sitename='" + site + "'"
                db.insert(command)
                for staff in selectitem['values']['values']:
                    
                    command = "SELECT username FROM user WHERE CONCAT(fname,' ',lname)='" + staff + "'"
                    username = db.search(command)[0][0]
                    command = "SELECT employeeID FROM employee WHERE eusername='" + username + "'"
                    ID = db.search(command)[0][0]
                    command = "INSERT INTO assign_to SET employeeID='" + ID \
                            + "',eventname='" + name \
                            + "',eventstartdate='" + startdate \
                            + "',sitename='" + site + "'"
                    db.insert(command)
                tkinter.messagebox.showinfo('Good','Created an event!') 
            except:
                tkinter.messagebox.showwarning('Error','Cannot create this event!') 

    def back():
        window.destroy()
        WIN_man_manage_event()

    l0 = Label(window,text="Create Event", width=36,font=('Arial', 18, 'bold'))
    l0.grid(sticky='n')

    l1 = Label(window,text="Name", font=('Times 14 normal'))
    l1.place(x=25,y=60)
    
    l2 = Label(window,text="Price($)", font=('Times 14 normal'))
    l2.place(x=25,y=100)

    l3 = Label(window,text="Capacity", font=('Times 14 normal'))
    l3.place(x=150,y=100)

    l4 = Label(window,text="Minimum Staff Required", font=('Times 14 normal'))
    l4.place(x=275,y=100)
    
    l5 = Label(window,text="Start Date",font=('Times 14 normal'))
    l5.place(x=25,y=140)
    
    l6 = Label(window,text="End Date",font=('Times 14 normal'))
    l6.place(x=275,y=140)

    l7 = Label(window,text="Description", font=('Times 14 normal'))
    l7.place(x=25,y=220)

    l8 = Label(window,text="Assign Staff", font=('Times 14 normal'))
    l8.place(x=25,y=340)

    e1_content = StringVar()
    e1 = Entry(window,width=20, bg='powder blue',textvariable=e1_content)
    e1.place(x=125,y=60)

    e2_content = StringVar()
    e2 = Entry(window,width=3, bg='powder blue',textvariable=e2_content)
    e2.place(x=100,y=100)

    e3_content = StringVar()
    e3 = Entry(window,width=3, bg='powder blue',textvariable=e3_content)
    e3.place(x=225,y=100)

    e4_content = StringVar()
    e4 = Entry(window,width=3, bg='powder blue',textvariable=e4_content)
    e4.place(x=450,y=100)

    e5_content = StringVar()
    e5 = Entry(window,width=8, bg='powder blue',textvariable=e5_content)
    e5.place(x=125,y=140)

    e6_content = StringVar()
    e6 = Entry(window,width=8, bg='powder blue',textvariable=e6_content)
    e6.place(x=350,y=140)

    st1 = Text(window, width=43, height=6,wrap=WORD,bd=8)
    st1.place(x=125,y=180)
    st1.insert(INSERT,"""Something to be filled""")

    def selectItem(event):
        selectitem.clear()
        item = tree.selection()
        selectitem['values'] = []
        for i in item:
            selectitem['values'].append( tree.item(i)['values'][0])

    tree1 = ttk.Treeview(window)
    tree1.place(x=150,y=300)
    vsb1 = ttk.Scrollbar(window, orient="vertical", command=tree1.yview)
    vsb1.place(x=500, y=300, height=120)
    tree1["show"] = 'headings'
    tree1.configure(yscrollcommand=vsb1.set,height=6)
    tree1["columns"]=("one")
    tree1.column("one", width=300)
    tree1.heading("one", text="Name",command=(lambda: None))

    tree1.bind('<ButtonRelease-1>', selectItem)
    i = 0
    for item in allstaffs:
        tree1.insert("",i,item[0],values=(item))
        i = i+1


    b1 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: back()))
    b1.place(x=75,y=450)

    b2 = Button(window,text="Create", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: create()))
    b2.place(x=275,y=450)

    window.mainloop() 
#28 filter
def WIN_man_manage_staff():
    db = DB()
    command = "SELECT employeeID FROM employee WHERE eusername='" + username_login[0] + "'"
    ID = db.search(command)[0][0]
    command = "SELECT sitename FROM site WHERE employeeID='" + ID + "'"
    sites = db.search(command)[0][0]
    command = "SELECT * from manage_staff WHERE sitename='" + sites + "'"
    table_raw = db.search(command)
    table_list = []
    for row in table_raw:
        table_list.append(row)
    filtered_list = table_list[:]
                
    window = Tk()
    window.title("Manager Manage Staff")
    window.geometry('400x500')
    window.resizable(0, 0)
    window.configure(background="#fff")

    def filter():
        fname = e2_content.get()
        lname = e2_content.get()
        startdate = e4_content.get()
        enddate = e4_content.get()
        if fname != '' and lname == '':
            filtered_list.clear()
            for item in table_list:
                if fname in item[6]:
                    if item not in filtered_list:
                        filtered_list.append(item)
            tree.delete(*tree.get_children())
            for item in filtered_list:
                tree.insert("",'end',values=(item[6]+' '+item[7],item[8])) 
        elif fname == '' and lname != '':
            filtered_list.clear()
            for item in table_list:
                if lname in item[7]:
                    if item not in filtered_list:
                        filtered_list.append(item)
            tree.delete(*tree.get_children())
            for item in filtered_list:
                tree.insert("",'end',values=(item[6]+' '+item[7],item[8])) 
        elif fname != '' and lname != '':
            filtered_list.clear()
            for item in table_list:
                if lname in item[7] and fname in item[6]:
                    if item not in filtered_list:
                        filtered_list.append(item)
            tree.delete(*tree.get_children())
            for item in filtered_list:
                tree.insert("",'end',values=(item[6]+' '+item[7],item[8])) 
        elif startdate <= enddate and startdate != '' and enddate != '':
            startdate_date = datetime.date(int(startdate.split("-")[0]),int(startdate.split("-")[1]),int(startdate.split("-")[2]))
            enddate_date = datetime.date(int(enddate.split("-")[0]),int(enddate.split("-")[1]),int(enddate.split("-")[2]))
            filtered_list.clear()
            for item in table_list:   
                if (startdate_date <= item[2] and enddate_date >= item[2]) or (startdate_date <= item[3] and enddate_date >= item[2]):
                    if item not in filtered_list:
                        filtered_list.append(item)
            tree.delete(*tree.get_children())
            for item in filtered_list:
                tree.insert("",'end',values=(item[6]+' '+item[7],item[8]))

    def back():
        if view_sta[0] == 'man':
            window.destroy()
            WIN_FUN_man()
        elif view_sta[0] == 'manuser':
            window.destroy()
            WIN_FUN_man_and_vis()
        else: pass

    l0 = Label(window,text="Manage Staff", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    l1 = Label(window,text="Site", font=('Times', 14, 'normal'))
    l1.place(x=75,y=60)

    l2 = Label(window,text="First Name", font=('Times', 14, 'normal'))
    l2.place(x=25,y=100)

    l3 = Label(window,text="Last Name", font=('Times', 14, 'normal'))
    l3.place(x=200,y=100)

    l4 = Label(window,text="Start Date", font=('Times', 14, 'normal'))
    l4.place(x=25,y=140)

    l5 = Label(window,text="End Date", font=('Times', 14, 'normal'))
    l5.place(x=200,y=140)

    e2_content = StringVar()
    e2 = Entry(window,width=6, bg='powder blue',textvariable=e2_content)
    e2.place(x=125,y=100)

    e3_content = StringVar()
    e3 = Entry(window,width=6, bg='powder blue',textvariable=e3_content)
    e3.place(x=300,y=100)

    e4_content = StringVar()
    e4 = Entry(window,width=6, bg='powder blue',textvariable=e4_content)
    e4.place(x=125,y=140)

    e5_content = StringVar()
    e5 = Entry(window,width=6, bg='powder blue',textvariable=e5_content)
    e5.place(x=300,y=140)

    option1 = StringVar()
    o1 = ttk.Combobox(window,width=10, textvariable=option1)
    o1['values'] = ([sites])
    o1.place(x=125,y=60)
    o1.current(0)

    b1 = Button(window,text="Filter", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: filter()))
    b1.place(x=150,y=180)

    b2 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: back()))
    b2.place(x=150,y=450)

    tree = ttk.Treeview(window)
    tree.place(x=25,y=220)
    vsb = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    vsb.place(x=350, y=220, height=160)
    tree["show"] = 'headings'
    tree.configure(yscrollcommand=vsb.set,height=8)
    tree["columns"]=("one","two")
    tree.column("one", width=150)
    tree.column("two", width=150)
    tree.heading("one", text="Staff Name",command=(lambda: None))
    tree.heading("two", text="# Event Shifts",command=(lambda: None))
    # tree.bind('<ButtonRelease-1>', selectItem)
    for item in filtered_list:
        tree.insert("",'end',values=(item[6]+' '+item[7],item[8]))

    window.mainloop()
#29 #! need to be tested
def WIN_man_site_report():
    db = DB()
    command = "SELECT employeeID FROM employee WHERE eusername='" + username_login[0] + "'"
    ID = db.search(command)[0][0]
    command = "SELECT sitename FROM site WHERE employeeID='" + ID + "'"
    sites = db.search(command)[0][0]
    command = "SELECT `date`,`Event_count`,`Staff_count`,`Total_Visits`,`Total_Revenue` FROM site_report WHERE sitename='" + sites + "'"
    sitereport = db.search(command)
    table_list = []
    for row in sitereport:
        table_list.append(row)
    isreversed = [0]
    filtered_list = table_list[:]
    selectitem = {} 
    
    window = Tk()
    window.title("Manager Site Report")
    window.geometry('500x400')
    window.resizable(0, 0)
    window.configure(background="#fff")

    def filter():
        startdate = e1_content.get()
        enddate = e2_content.get()
        ecr_s = e4a_content.get()
        ecr_e = e4b_content.get()
        scr_s = e6a_content.get()
        scr_e = e6b_content.get()
        tvr_s = e8a_content.get()
        tvr_e = e8b_content.get()
        trr_s = e10a_content.get()
        trr_e = e10b_content.get()
        if startdate <= enddate and startdate != '' and enddate != '':
            startdate_date = datetime.date(int(startdate.split("-")[0]),int(startdate.split("-")[1]),int(startdate.split("-")[2]))
            enddate_date = datetime.date(int(enddate.split("-")[0]),int(enddate.split("-")[1]),int(enddate.split("-")[2]))
            filtered_list.clear()
            for item in table_list:   
                if startdate_date <= item[0] and enddate_date >= item[0]:
                    if item not in filtered_list:
                        filtered_list.append(item)
            tree.delete(*tree.get_children())
            for item in filtered_list:
                tree.insert("",'end',values=(item[0],item[1],item[2],item[3],item[4]))
        elif ecr_e != 0 and ecr_s != 0:
            filtered_list.clear()
            for item in table_list: 
                if ecr_s <= item[1] and ecr_e >= item[1]:
                    if item not in filtered_list:
                        filtered_list.append(item)
            tree.delete(*tree.get_children())
            for item in filtered_list:
                tree.insert("",'end',values=(item[0],item[1],item[2],item[3],item[4]))
        elif scr_s != 0 and scr_e != 0:
            filtered_list.clear()
            for item in table_list: 
                if scr_s <= item[2] and scr_e >= item[2]:
                    if item not in filtered_list:
                        filtered_list.append(item)
            tree.delete(*tree.get_children())
            for item in filtered_list:
                tree.insert("",'end',values=(item[0],item[1],item[2],item[3],item[4]))
        elif tvr_s != 0 and tvr_e != 0: 
            filtered_list.clear()
            for item in table_list: 
                if tvr_s <= item[3] and tvr_e >= item[3]:
                    if item not in filtered_list:
                        filtered_list.append(item)
            tree.delete(*tree.get_children())
            for item in filtered_list:
                tree.insert("",'end',values=(item[0],item[1],item[2],item[3],item[4]))
        elif trr_s != 0 and trr_e != 0: 
            filtered_list.clear()
            for item in table_list: 
                if trr_s <= item[4] and trr_e >= item[4]:
                    if item not in filtered_list:
                        filtered_list.append(item)
            tree.delete(*tree.get_children())
            for item in filtered_list:
                tree.insert("",'end',values=(item[0],item[1],item[2],item[3],item[4]))
        else:pass

    def navigation(value):
        site_daily_detail = selectitem['values']['values']
        if value == 1:
            window.destroy()
            WIN_man_daily_detail()

    def back():
        if view_site_report[0] == 'man':
            window.destroy()
            WIN_FUN_man()
        elif view_site_report[0] == 'manuser':
            window.destroy()
            WIN_FUN_man_and_vis()
        else: pass

    l0 = Label(window,text="Site Report", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    l1 = Label(window,text="Start Date", font=('Times', 14, 'normal'))
    l1.place(x=25,y=60)

    l2 = Label(window,text="End Date", font=('Times', 14, 'normal'))
    l2.place(x=300,y=60)

    l3 = Label(window,text="Event Count Range", font=('Times', 14, 'normal'))
    l3.place(x=25,y=100)

    l4 = Label(window,text="--", font=('Times', 14, 'normal'))
    l4.place(x=200,y=100)

    l5 = Label(window,text="Staff Count Range", font=('Times', 14, 'normal'))
    l5.place(x=250,y=100)

    l6 = Label(window,text="--", font=('Times', 14, 'normal'))
    l6.place(x=425,y=100)

    l7 = Label(window,text="Total Visits Range", font=('Times', 14, 'normal'))
    l7.place(x=25,y=140)

    l8 = Label(window,text="--", font=('Times', 14, 'normal'))
    l8.place(x=200,y=140)

    l9 = Label(window,text="Total Revenue Range", font=('Times', 14, 'normal'))
    l9.place(x=250,y=140)

    l10 = Label(window,text="--", font=('Times', 14, 'normal'))
    l10.place(x=425,y=140)

    e1_content = StringVar()
    e1 = Entry(window,width=10, bg='powder blue',textvariable=e1_content)
    e1.place(x=100,y=60)

    e2_content = StringVar()
    e2 = Entry(window,width=10, bg='powder blue',textvariable=e2_content)
    e2.place(x=375,y=60)

    e4a_content = IntVar()
    e4a = Entry(window,width=2, bg='powder blue',textvariable=e4a_content)
    e4a.place(x=170,y=100)

    e4b_content = IntVar()
    e4b = Entry(window,width=2, bg='powder blue',textvariable=e4b_content)
    e4b.place(x=215,y=100)

    e6a_content = IntVar()
    e6a = Entry(window,width=2, bg='powder blue',textvariable=e6a_content)
    e6a.place(x=395,y=100)

    e6b_content = IntVar()
    e6b = Entry(window,width=2, bg='powder blue',textvariable=e6b_content)
    e6b.place(x=440,y=100)

    e8a_content = IntVar()
    e8a = Entry(window,width=2, bg='powder blue',textvariable=e8a_content)
    e8a.place(x=170,y=140)

    e8b_content = IntVar()
    e8b = Entry(window,width=2, bg='powder blue',textvariable=e8b_content)
    e8b.place(x=215,y=140)

    e10a_content = IntVar()
    e10a = Entry(window,width=2, bg='powder blue',textvariable=e10a_content)
    e10a.place(x=395,y=140)

    e10b_content = IntVar()
    e10b = Entry(window,width=2, bg='powder blue',textvariable=e10b_content)
    e10b.place(x=440,y=140)

    b1 = Button(window,text="Filter", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: filter()))
    b1.place(x=50,y=180)

    b2 = Button(window,text="Daily Detail", width=12, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation(1)))
    b2.place(x=375,y=180)

    b3 = Button(window,text="Back", width=12, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: back()))
    b3.pack(side='bottom')

    def selectItem(event):
        item = tree.focus()
        selectitem['values'] = tree.item(item)

    tree = ttk.Treeview(window)
    tree.place(x=25,y=220)
    vsb = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    vsb.place(x=425, y=220, height=120)
    tree["show"] = 'headings'
    tree.configure(yscrollcommand=vsb.set,height=6)
    tree["columns"]=("one","two","three","four","five")
    tree.column("one", width=80)
    tree.column("two", width=80)
    tree.column("three",width=80)
    tree.column("four",width=80)
    tree.column("five",width=80)
    tree.heading("one", text="Date",command=(lambda: None))
    tree.heading("two", text="Event Count",command=(lambda: None))
    tree.heading("three", text="Staff Count",command=(lambda: None))
    tree.heading("four", text="Total Visits",command=(lambda: None))
    tree.heading("five", text="Total Revenue($)",command=(lambda: None))
    tree.bind('<ButtonRelease-1>', selectItem)
    for item in table_list:
        tree.insert("",'end',values=(item[0],item[1],item[2],item[3],item[4]))

    window.mainloop()
#30 #! datetime in daily detail
def WIN_man_daily_detail():
    db = DB()
    command = "SELECT employeeID FROM employee WHERE eusername='" + username_login[0] + "'"
    ID = db.search(command)[0][0]
    command = "SELECT sitename FROM site WHERE employeeID='" + ID + "'"
    sites = db.search(command)[0][0]
    command = "SELECT eventname FROM event WHERE sitename='" + sites + "'"
    eventinfo = db.search(command)
    events = []
    for event in eventinfo:
        events.append(event[0])
    # for event in 
    #!!!

    command = "SELECT * FROM daily_detail"
    dailydetail = db.search(command)
    table_list = []
    table_dic = {}
    for row in dailydetail:
        table_list.append(row)
    for row in table_list:
        if row[0] not in table_dic:
            table_dic[row[0]] = [row[0],[row[3]],row[6],row[5]]
        else:
            if row[3] not in table_dic[row[0]][1]:
                table_dic[row[0]][1].append(row[3])
    for value,item in table_dic.items():
        table_dic[value][1] = ','.join(item[1])
            
    window = Tk()
    window.title("Manager Daily Detail")
    window.geometry('400x300')
    window.resizable(0, 0)
    window.configure(background="#fff")

    def back():
        window.destroy()
        WIN_man_site_report()

    l0 = Label(window,text="Daily Detail", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    b1 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda:back()))
    b1.pack(side='bottom')

    tree = ttk.Treeview(window)
    tree.place(x=50,y=50)
    vsb = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    vsb.place(x=425, y=160, height=160)
    tree["show"] = 'headings'
    tree.configure(yscrollcommand=vsb.set,height=8)
    tree["columns"]=("one","two","three","four")
    tree.column("one", width=80)
    tree.column("two", width=80)
    tree.column("three",width=80)
    tree.column("four",width=80)
    tree.heading("one", text="Event Name",command=(lambda: None))
    tree.heading("two", text="Staff Name",command=(lambda:  None))
    tree.heading("three", text="Visits",command=(lambda:  None))
    tree.heading("four",text="Revenue($)",command=(lambda:  None))
    for value,item in table_dic.items():
        tree.insert("",'end',values=(item[0],item[1],item[2],item[3]))

    window.mainloop()
#31 display
def WIN_sta_view_schedule():
    db =DB()
    command = "SELECT employeeID FROM employee WHERE eusername='" + username_login[0] + "'"
    ID = db.search(command)[0][0]
    command = "SELECT * FROM view_schedule WHERE employeeID='" + ID + "'"
    schedule = db.search(command)
    table_dic = {}
    table_list = []
    for row in schedule:
        table_list.append(row)
    for row in table_list:
        if row[0] not in table_dic:
            table_dic[row[0]] = [row[0],row[1],row[2],[row[3]],row[6]]
        else:
            if row[3] not in  table_dic[row[0]][3]:
                table_dic[row[0]][3].append(row[3])
    for value,item in table_dic.items():
        table_dic[value][3] = ','.join(item[3])
    isreversed = [0]
    filtered_list = table_list[:]
    selectitem = {} 
              
    window = Tk()
    window.title("Staff View Schedule")
    window.geometry('500x400')
    window.resizable(0, 0)
    window.configure(background="#fff")

    def filter():
        pass
    
    def navigation():
        event_to_view[0] =  selectitem['values']['values'][0]
        window.destroy()
        WIN_sta_event_detail()

    def back():
        if view_schedule[0] == 'sta':
            window.destroy()
            WIN_FUN_sta()
        elif view_schedule[0] == 'stauser':
            window.destroy()
            WIN_FUN_sta_and_vis()
        else: pass

    l0 = Label(window,text="View Schedule", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    l1 = Label(window,text="First Name", font=('Times', 14, 'normal'))
    l1.place(x=25,y=60)

    l2 = Label(window,text="Last Name", font=('Times', 14, 'normal'))
    l2.place(x=250,y=60)

    l3 = Label(window,text="Start Date", font=('Times', 14, 'normal'))
    l3.place(x=25,y=100)

    l4 = Label(window,text="End Date", font=('Times', 14, 'normal'))
    l4.place(x=250,y=100)

    e1_content = StringVar()
    e1 = Entry(window,width=10, bg='powder blue',textvariable=e1_content)
    e1.place(x=125,y=60)

    e2_content = StringVar()
    e2 = Entry(window,width=10, bg='powder blue',textvariable=e2_content)
    e2.place(x=350,y=60)

    e3_content = StringVar()
    e3 = Entry(window,width=10, bg='powder blue',textvariable=e3_content)
    e3.place(x=125,y=100)

    e4_content = StringVar()
    e4 = Entry(window,width=10, bg='powder blue',textvariable=e4_content)
    e4.place(x=350,y=100)

    b1 = Button(window,text="Filter", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: filter()))
    b1.place(x=100,y=140)

    b2 = Button(window,text="View Event", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: navigation()))
    b2.place(x=275,y=140)

    b3 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: back()))
    b3.pack(side='bottom')

    def selectItem(event):
        item = tree.focus()
        selectitem['values'] = tree.item(item)

    tree = ttk.Treeview(window)
    tree.place(x=25,y=180)
    vsb = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    vsb.place(x=425, y=180, height=160)
    tree["show"] = 'headings'
    tree.configure(yscrollcommand=vsb.set,height=8)
    tree["columns"]=("one","two","three","four","five")
    tree.column("one", width=80)
    tree.column("two", width=80)
    tree.column("three",width=80)
    tree.column("four",width=80)
    tree.column("five",width=80)
    tree.heading("one", text="Event Name",command=(lambda: None))
    tree.heading("two", text="Site Name",command=(lambda: None))
    tree.heading("three", text="Start Date)",command=(lambda: None))
    tree.heading("four", text="End Date",command=(lambda: None))
    tree.heading("five", text="Staff Count",command=(lambda: None))
    tree.bind('<ButtonRelease-1>', selectItem)
    for value,item in table_dic.items():
        tree.insert("",'end',values=(item[0],item[3],item[1],item[2],item[4]))

    window.mainloop()
#32 p
def WIN_sta_event_detail():
    db = DB()
    #should we do db=DB for every function?

    #input should always be string
    #Event = "Bus Tour"  
    Event = Event_name  
    #Startdate = "2019-02-01"
    Startdate = Event_Start_date
    #sql_command_32 = "select * from event"

    sql_command_32_1 = "SELECT `event`.`eventname`,`event`.`sitename`, `event`.`enddate`,`event`.`eventstartdate`,`event`.`capacity`, `event`.`description`,`event`.`price`,`assign_to`.`employeeID`,CONCAT(`user`.`fname`,' ',`user`.`lname`) as Staff, `employee`.`eusername` FROM `event` JOIN `assign_to` ON `event`.`eventname` = `assign_to`.`eventname` AND `event`.`eventstartdate` = `assign_to`.`eventstartdate` JOIN `employee` ON `assign_to`.`employeeID` = `employee`.`employeeID` JOIN `user` ON `employee`.`eusername` = `user`.`username` where `event`.`eventname` = '"+str(Event)+"' and `event`.`eventstartdate` = '"+str(Startdate)+"'"
    #print(sql_command_32_1)
    detail_list = db.search(sql_command_32_1)
    #print(detail_list)
    #print("23")    
    window = Tk()
    window.title("Staff Event Detail")
    window.geometry('500x400')
    window.resizable(0, 0)
    window.configure(background="#fff")
    
    def days_between(d1, d2):
        d1 = datetime.strptime(d1, "%Y-%m-%d")
        d2 = datetime.strptime(d2, "%Y-%m-%d")
        return abs((d2 - d1).days)
    
    Durationdays= days_between(Startdate,str(detail_list[0][2]))
    Staffsassigned=[]
    Site = detail_list[0][1]
    Description= detail_list[0][5]

    Enddate = detail_list[0][2]
    Number_of_staff= len(detail_list)
    for i in range(Number_of_staff):
        Staffsassigned.append(detail_list[i][8])
    Capacity = detail_list[0][4]
    Price = detail_list[0][6]
    print(Staffsassigned)
    def back():
        window.destroy()
        WIN_sta_view_schedule()
    

    l0 = Label(window,text="Event Detail", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    l1 = Label(window,text="Event", font=('Times 14 normal'))
    l1.place(x=25,y=60)
    
    l2 = Label(window,text=Event, font=('Times 14 italic bold'))
    l2.place(x=100,y=60)

    l3 = Label(window,text="Site", font=('Times 14 normal'))
    l3.place(x=275,y=60)

    l4 = Label(window,text=Site, font=('Times 14 italic bold'))
    l4.place(x=325,y=60)
    
    l5 = Label(window,text="Start Date",font=('Times 14 normal'))
    l5.place(x=25,y=100)
    
    l6 = Label(window,text=Startdate,font=('Times 14 italic bold'))
    l6.place(x=100,y=100)

    l7 = Label(window,text="End Date", font=('Times 14 normal'))
    l7.place(x=200,y=100)

    l8 = Label(window,text=Enddate, font=('Times 14 italic bold'))
    l8.place(x=275,y=100)
    
    l9 = Label(window,text="Duration Days", font=('Times 14 normal'))
    l9.place(x=350,y=100)

    l10 = Label(window,text=Durationdays, font=('Times 14 italic bold'))
    l10.place(x=450,y=100)

    l11 = Label(window,text="Staffs Assigned", font=('Times 14 normal'))
    l11.place(x=25,y=140)
       
    #l12 = Label(window,text=Staffsassigned,font=('Times 14 italic bold'))
    #l12.place(x=125,y=140)

    l13 = Label(window,text="Capacity", font=('Times 14 normal'))
    l13.place(x=240,y=140)
    
    l14 = Label(window,text=Capacity, font=('Times 14 italic bold'))
    l14.place(x=315,y=140)

    l15 = Label(window,text="Price", font=('Times 14 normal'))
    l15.place(x=345,y=140)

    l16 = Label(window,text=Price, font=('Times 14 italic bold'))
    l16.place(x=400,y=140)
       
    l17 = Label(window,text="Description",font=('Times 14 italic bold'))
    l17.place(x=25,y=180)

    st1 = scrolledtext.ScrolledText(window, width=45, height=7,wrap=WORD,bd=8,)
    st1.place(x=125,y=180)
    st1.insert(INSERT,Description)
    st1.config(state=DISABLED)

    o1 = ttk.Combobox(window,width=10 )
    o1['values'] = tuple(Staffsassigned)
    o1.place(x=150,y=140)
    o1.current(0)
           
    b1 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: back()))
    b1.pack(side='bottom')

    window.mainloop() 
#33 p
def WIN_vis_explore_event():
    db = DB()
    sql_command_33_1 = "select sitename from site"
    site_list = db.search(sql_command_33_1)
    sql_command_33_2 = "SELECT DISTINCT  `eventname`, `sitename`,  `price`,`Tickets Remaining`,  `Total Visits`,  `My Visits` FROM  `explore_event`"
    table_raw=db.search(sql_command_33_2)
    print(table_raw)
    window = Tk()
    window.title("Explore Event")
    window.geometry('600x600')
    window.resizable(0, 0)
    window.configure(background="#fff")

    def back():
        window.destroy()
        WIN_FUN_vis()

    def filter(e1at,e1bt,e2t,e3at,e3bt,e4at,e4bt,e4ct,e4dt):
        print("sql_command_33_3")
        print(e1at,e1bt,e2t,e3at,e3bt,e4at,e4bt,e4ct,e4dt)

    l0 = Label(window,text="Explore Event", width=36,font=('Arial', 18, 'bold'))
    l0.grid(sticky='n')

    l1 = Label(window,text="Name", font=('Times 14 normal'))
    l1.place(x=10,y=60)

    l2 = Label(window,text="Description Keyword", font=('Times 14 normal'))
    l2.place(x=230,y=60)

    l3 = Label(window,text="Site Name", font=('Times 14 normal'))
    l3.place(x=10,y=100)

    l4 = Label(window,text="Start Date", font=('Times', 14, 'normal'))
    l4.place(x=10,y=140)

    l5 = Label(window,text="End Date", font=('Times', 14, 'normal'))
    l5.place(x=300,y=140)   

    l5 = Label(window,text="Daily Visits Range", font=('Times', 14, 'normal'))
    l5.place(x=10,y=180)

    l6 = Label(window,text="--", font=('Times', 14, 'normal'))
    l6.place(x=200,y=180)

    l7 = Label(window,text="Ticket Price Range", font=('Times', 14, 'normal'))
    l7.place(x=270,y=180)

    l8 = Label(window,text="--", font=('Times', 14, 'normal'))
    l8.place(x=470,y=180)

    b3 = Button(window,text="Back", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: back()))
    b3.place(x=200,y=550)

    e1a_content= StringVar()
    e1a = Entry(window,width=10, bg='powder blue',textvariable = e1a_content)
    e1a.place(x=150,y=60)

    e1b_content= StringVar()
    e1b = Entry(window,width=10, bg='powder blue',textvariable = e1b_content)
    e1b.place(x=450,y=60) 

    e2_content= StringVar()
    e2 = Entry(window,width=20, bg='powder blue', textvariable = e2_content)
    e2.place(x=150,y=140) 

    e3a_content= StringVar()
    e3a = Entry(window,width=20, bg='powder blue',textvariable = e3a_content)
    e3a.place(x=150,y=140)

    e3b_content= StringVar()
    e3b = Entry(window,width=20, bg='powder blue', textvariable = e3b_content)
    e3b.place(x=400,y=140)

    e4a_content= StringVar()
    e4a = Entry(window,width=4, bg='powder blue', textvariable = e4a_content)
    e4a.place(x=160,y=180) 

    e4b_content= StringVar()
    e4b = Entry(window,width=4, bg='powder blue', textvariable = e4b_content)
    e4b.place(x=230,y=180)

    e4c_content= StringVar()
    e4c = Entry(window,width=4, bg='powder blue', textvariable = e4c_content)
    e4c.place(x=430,y=180)

    e4d_content= StringVar()
    e4d = Entry(window,width=4, bg='powder blue',textvariable = e4d_content)
    e4d.place(x=500,y=180)
         

    chVarDis = IntVar()
    c1 = Checkbutton(window, text='Include Visited',variable=chVarDis)
    if True:
        c1.select()
    else:
        c1.deselect()
    c1.place(x=150,y=220)

    chVarDis2 = IntVar()
    c1 = Checkbutton(window, text='Include Sold out event',variable=chVarDis2)
    if True:
        c1.select()
    else:
        c1.deselect()
    c1.place(x=350,y=220)

    option1 = StringVar()
    o1 = ttk.Combobox(window,width=20, textvariable=option1)
    o1['values'] = tuple(site_list)
    o1.place(x=130,y=100)
    o1.current(0)
    tree = ttk.Treeview(window)
    tree.place(x=0,y=300)
    vsb = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    vsb.place(x=550, y=250, height=250)
    tree["show"] = 'headings'
    tree.configure(yscrollcommand=vsb.set,height=12)

    e1a_text=e1a_content.get()
    e1b_text=e1b_content.get()
    e2_text=e2_content.get()
    e3a_text=e3a_content.get()
    e3b_text=e3b_content.get()
    e4a_text=e4a_content.get()
    e4b_text=e4b_content.get()
    e4c_text=e4c_content.get()
    e4d_text=e4d_content.get()
    print(e1a_text)

    b1 = Button(window,text="Filter", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: filter()))
    b1.place(x=50,y=250)

    b2 = Button(window,text="Event Detail", width=12, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b2.place(x=375,y=250)

    tree["columns"]=("one","two","three","four","five","six")
    tree.column("one", width=100)
    tree.column("two", width=100)
    tree.column("three",width=100)
    tree.column("four",width=100)
    tree.column("five",width=100)
    tree.column("six",width=100)
    tree.heading("one", text="Event Name",command=(lambda: None))
    tree.heading("two", text="Site Name",command=(lambda: None))
    tree.heading("three", text="Ticket Price",command=(lambda: None))
    tree.heading("four",text="Ticket Remaining",command=(lambda: None))
    tree.heading("five",text="Total Visits",command=(lambda: None))
    tree.heading("six",text="My Visits",command=(lambda: None))


    window.mainloop() #34:
#34
def WIN_vis_event_detail():
    db = DB()
    #should we do db=DB for every function?
    visitor_username='mary.smith'
    #input should always be string
    Event = "Bus Tour"  
    #Event = Event_name  
    Start_Date = "2019-02-01"
    #Startdate = Event_Start_date
    sql_command_34_3 = "SELECT DISTINCT `eventname`,`sitename`,`eventstartdate`,`enddate`,`price`,`description`,`Tickets Remaining`FROM `visitor_event_detail` WHERE `eventname` = '"+str(Event)+"'and `eventstartdate` = '"+str(Start_Date)+"'  "
    #print(sql_command_32_1)
    detail_list= db.search(sql_command_34_3)
    #print(detail_list)
    #print("23")            
    window = Tk()
    window.title("Visitor Event Detail ")
    window.geometry('500x600')
    window.resizable(0, 0)
    window.configure(background="#fff")


    Site=detail_list[0][1]
    End_Date=detail_list[0][3]
    Ticket_Price=detail_list[0][4]
    Tickets_Remaining=detail_list[0][6]
    Description= detail_list[0][5]

    def log_visit():
        #print(e1_content.get())
        if not re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$',e1_content.get()):
            tkinter.messagebox.showwarning('Date Error','Not valid date!')
        #sql_command_34_4="INSERT INTO `visit_event` SET `eventname`='"+str(Event)+"', `eventstartdate`='"str()"', `sitename`='"+str(Inman Park)+"', `date`='"+str(e1_content)+"', `visitorusername`='"+visitor_username+"'"
        #db.insert(sql_command_34_4)
        #update query
    
    l0 = Label(window,text="Visitor Event Detail", width=36,font=('Arial', 18, 'bold'))
    l0.grid(sticky='n')

    l1 = Label(window,text="Event", font=('Times 12 normal'))
    l1.place(x=10,y=50)

    l2 = Label(window,text=Event,font=('Times 10 italic bold'))
    l2.place(x=70,y=50)

    l3 = Label(window,text="Site",font=('Times 12 normal'))
    l3.place(x=250,y=50)   

    l4 = Label(window,text=Site,font=('Times 10 italic bold'))
    l4.place(x=300,y=50)   

    l5 = Label(window,text="Start Date",font=('Times 12 normal'))
    l5.place(x=10,y=80)

    l6 = Label(window,text=Start_Date,font=('Times 10 italic bold'))
    l6.place(x=100,y=80)

    l7 = Label(window,text="End Date",font=('Times 10 normal'))
    l7.place(x=250,y=80)  

    l8 = Label(window,text=End_Date,font=('Times 10 italic bold'))
    l8.place(x=350,y=80)

    l9 = Label(window,text="Ticket Price($)",font=('Times 12 normal'))
    l9.place(x=10,y=120)   

    l10 = Label(window,text=Ticket_Price,font=('Times 10 italic bold'))
    l10.place(x=140,y=120) 

    l11 = Label(window,text="Tickets Remaining",font=('Times 10 normal'))
    l11.place(x=250,y=120)

    l12 = Label(window,text=Tickets_Remaining,font=('Times 10 italic bold'))
    l12.place(x=380,y=120)      

    l13 = Label(window,text="Description",font=('Times 12 normal'))
    l13.place(x=10,y=200)

    st1 = scrolledtext.ScrolledText(window, width=40, height=10,wrap=WORD,bd=8,)
    st1.place(x=125,y=200)
    st1.insert(INSERT,Description)
    st1.config(state=DISABLED)

    l15 = Label(window,text="Visit Date",font=('Times 10 italic bold'))
    l15.place(x=10,y=500)

    b1 = Button(window,text="Log Visit", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: log_visit()))
    b1.place(x=300,y=500)

    e1_content = StringVar()
    e1 = Entry(window,width=20, bg='powder blue',textvariable=e1_content)
    e1.place(x=150,y=500) 

    b2 = Button(window,text="Back", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b2.place(x=200,y=550)

    window.mainloop() 
#35
def WIN_vis_explore_site():
            
    window = Tk()
    window.title(" ")
    window.geometry('x')
    window.resizable(0, 0)
    window.configure(background="#fff")

    def back():
        if man_profile[0] == 'user':
            window.destroy()
            WIN_FUN_user()
        elif man_profile[0] == 'adm':
            window.destroy() 
            WIN_FUN_adm()           
        elif man_profile[0] == 'admuser':
            window.destroy()
            WIN_FUN_adm_and_vis()
        elif man_profile[0] == 'man':
            window.destroy()
            WIN_FUN_man()
        elif man_profile[0] == 'manuser':
            window.destroy()
            WIN_FUN_man_and_vis()
        elif man_profile[0] == 'sta':
            window.destroy()
            WIN_FUN_sta()
        elif man_profile[0] == 'stauser':
            window.destroy()
            WIN_FUN_sta_and_vis()
        elif man_profile[0] == 'vis':
            window.destroy()
            WIN_FUN_vis()
        else: pass

    l0 = Label(window,text="", width=36,font=('Arial', 18, 'bold'))
    l0.grid(sticky='n')

    b1 = Button(window,text="", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.grid(row=2,column=2)

    e1 = Entry(window,width=20, bg='powder blue')
    e1.place(x=150,y=60)

    t1 = Text(window,width=20, bg='white')
    t1.pack()

    window.mainloop()
#36
def WIN_vis_transit_detail():
            
    window = Tk()
    window.title(" ")
    window.geometry('x')
    window.resizable(0, 0)
    window.configure(background="#fff")

    def back():
        if man_profile[0] == 'user':
            window.destroy()
            WIN_FUN_user()
        elif man_profile[0] == 'adm':
            window.destroy() 
            WIN_FUN_adm()           
        elif man_profile[0] == 'admuser':
            window.destroy()
            WIN_FUN_adm_and_vis()
        elif man_profile[0] == 'man':
            window.destroy()
            WIN_FUN_man()
        elif man_profile[0] == 'manuser':
            window.destroy()
            WIN_FUN_man_and_vis()
        elif man_profile[0] == 'sta':
            window.destroy()
            WIN_FUN_sta()
        elif man_profile[0] == 'stauser':
            window.destroy()
            WIN_FUN_sta_and_vis()
        elif man_profile[0] == 'vis':
            window.destroy()
            WIN_FUN_vis()
        else: pass

    l0 = Label(window,text="", width=36,font=('Arial', 18, 'bold'))
    l0.grid(sticky='n')

    b1 = Button(window,text="", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.grid(row=2,column=2)

    e1 = Entry(window,width=20, bg='powder blue')
    e1.place(x=150,y=60)

    t1 = Text(window,width=20, bg='white')
    t1.pack()

    window.mainloop() 
#37 
def WIN_vis_site_detail():

    Site="Inman Park"
    Open_Everyday="Yes"
    Address = "Inman Park, Atlanta, GA 30307"

    window = Tk()
    window.title("Visitor Site Detail")
    window.geometry('600x300')
    window.resizable(0, 0)
    window.configure(background="#fff")

    l0 = Label(window,text="Site Detail", width=36,font=('Arial', 18, 'bold'))
    l0.grid(sticky='n')

    l1 = Label(window,text="Site", font=('Times 12 normal'))
    l1.place(x=10,y=50)

    l2 = Label(window,text=Site, font=('Times 12 italic'))
    l2.place(x=90,y=50)    

    l3 = Label(window,text="Open Everyday", font=('Times 12 normal'))
    l3.place(x=250,y=50)

    l4 = Label(window,text=Open_Everyday, font=('Times 12 italic'))
    l4.place(x=400,y=50)

    l5 = Label(window,text="Address", font=('Times 12 normal'))
    l5.place(x=10,y=100)

    l6 = Label(window,text=Address, font=('Times 12 italic'))
    l6.place(x=100,y=100) 

    l7 = Label(window,text="Visit Date", font=('Times 12 normal'))
    l7.place(x=100,y=180)       

    b1 = Button(window,text="Back", width=10, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.place(x=300,y=225)

    b2 = Button(window,text="Log Visit", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b2.place(x=450,y=180)

    e1 = Entry(window,width=20, bg='powder blue')
    e1.place(x=250,y=180)

    window.mainloop() 
#38 
def WIN_vis_visit_his():
            
    window = Tk()
    window.title(" ")
    window.geometry('x')
    window.resizable(0, 0)
    window.configure(background="#fff")

    def back():
        if man_profile[0] == 'user':
            window.destroy()
            WIN_FUN_user()
        elif man_profile[0] == 'adm':
            window.destroy() 
            WIN_FUN_adm()           
        elif man_profile[0] == 'admuser':
            window.destroy()
            WIN_FUN_adm_and_vis()
        elif man_profile[0] == 'man':
            window.destroy()
            WIN_FUN_man()
        elif man_profile[0] == 'manuser':
            window.destroy()
            WIN_FUN_man_and_vis()
        elif man_profile[0] == 'sta':
            window.destroy()
            WIN_FUN_sta()
        elif man_profile[0] == 'stauser':
            window.destroy()
            WIN_FUN_sta_and_vis()
        elif man_profile[0] == 'vis':
            window.destroy()
            WIN_FUN_vis()
        else: pass

    l0 = Label(window,text="", width=36,font=('Arial', 18, 'bold'))
    l0.grid(sticky='n')

    b1 = Button(window,text="", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.grid(row=2,column=2)

    e1 = Entry(window,width=20, bg='powder blue')
    e1.place(x=150,y=60)

    t1 = Text(window,width=20, bg='white')
    t1.pack()

    window.mainloop()

def main():

    # WIN_user_login()
    # WIN_regi_nav()
    # WIN_regi_user()
    # WIN_regi_vis()
    # WIN_regi_emp()
    # WIN_regi_emp_and_vis()
    # WIN_FUN_user()
    # WIN_FUN_adm()
    # WIN_FUN_adm_and_vis()
    # WIN_FUN_man()
    # WIN_FUN_man_and_vis()
    # WIN_FUN_sta()
    # WIN_FUN_sta_and_vis()
    # WIN_FUN_vis() 
    # WIN_take_transit()
    # WIN_transit_his()
    # WIN_emp_manage_profile()
    # WIN_adm_manage_user()
    # WIN_adm_manage_site()
    # WIN_adm_edit_site()
    # WIN_adm_create_site()
    # WIN_adm_manage_transit()   
    # WIN_adm_edit_transit()
    # WIN_adm_create_transit()
    # WIN_man_manage_event()
    # WIN_man_VE_event()
    # WIN_man_create_event()
    # WIN_man_manage_staff()
    # WIN_man_site_report()
    # WIN_man_daily_detail()
    WIN_sta_view_schedule()
    # WIN_sta_event_detail()
    # WIN_vis_explore_event()
    # WIN_vis_event_detail()
    # WIN_vis_explore_site()
    # WIN_vis_transit_detail()
    # WIN_vis_site_detail()
    # WIN_vis_visit_his()

if __name__ == '__main__':
    main()
    
