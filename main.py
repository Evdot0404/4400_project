#! /usr/bin/python3
import flask
import sqlite3
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
import tkinter.messagebox
import re

class DB:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
        self.conn.execute("command")
        self.conn.commit()
    
    def __del__(self): #destructor
        self.conn.close()

    # Seach database
    def search(self):
        self.cursor.execute("command")
        rows = self.cursor.fetchall()
        return rows

    # Insert database
    def insert(self,args):
        self.conn.execute("command")
        self.conn.commit()

    # Update database
    def update(self,args):
        self.conn.execute("command")
        self.conn.commit()

    # Delete from database
    def delete(self,args):
        self.conn.execute("command")
        self.conn.commit()
# Mutural functions 
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

#1 s2
def WIN_user_login():
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
    # l1.grid(row=2, column=0)

    l2 = Label(window, text="Password",font=('Times 14 normal'))
    l2.place(x=25,y=100)
    # l2.grid(row=4, column=0)

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

    def checkaccount():
        email = e1_content.get()
        password = e2_content.get()
        #! Here, a list from database needed
        accounts = [('mcao42@gatech.edu','12345678')]
        if (email,password) in accounts:
            window.destroy()
            WIN_FUN_user()
        else: 
            tkinter.messagebox.showwarning('Invalid Account','Incorrect email and password combination!')

    def register():
        window.destroy()
        WIN_regi_nav()
    
    b1 = Button(window, text="Login", width=6, height=2,bg='white',fg='grey',font=('Arial 9 bold'), command=(lambda: checkaccount()))
    b1.place(x=75,y=150)

    b2 = Button(window, text="Register", width=8, height=2,bg='white',fg='grey',font=('Arial 9 bold'), command=(lambda: register()))
    b2.place(x=250,y=150)

    # Radiobutton()

    window.mainloop()
#2 s2
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
#3
def WIN_regi_user():

    geometry = '600x' + str(len(newemail)*40+300)
    
    window = Tk()
    window.title("Register User")
    window.geometry(geometry)
    window.resizable(0, 0)
    window.configure(background="#fff")

    def confirmpwd():
        if len(e3_content.get()) < 8 :
            tkinter.messagebox.showwarning('Password Error','Password should at least 8 characters')
        
        if e3_content.get() != e5_content.get():
            tkinter.messagebox.showwarning('Not same password','Incorrect confirmed password, try again!')

    def checkusername():
        #! username list from database needed
        usernames = ['Mingming','Priyam']
        if e2_content.get() in usernames:
            tkinter.messagebox.showwarning('Existed Username','The username exists, try another username!')

    def checkemail():
        #! username list from database needed
        emails = ['mcao42@gatech.edu']
        #! email format
        if not re.match(r'^[0-9a-zA-Z]+@{1}[0-9a-zA-Z]+\.{1}[0-9a-zA-Z]+',e6_content.get()):
            tkinter.messagebox.showwarning('Email Error','Not valid email!')
        elif e6_content.get() in emails:
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
        confirmpwd()
        checkusername()
        window.destroy()
        WIN_user_login()

    def addemail():
        checkemail()
        window.destroy()
        WIN_regi_user()

    def removeemail(email):
        # print(email)
        newemail.remove(email)
        window.destroy()
        WIN_regi_user()

    def back():
        window.destroy()
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
#4
def WIN_regi_vis():

    geometry = '600x' + str(len(newemail_vis)*40+300)
    
    window = Tk()
    window.title("Register Visitor")
    window.geometry(geometry)
    window.resizable(0, 0)
    window.configure(background="#fff")

    def confirmpwd():
        if len(e3_content.get()) < 8 :
            tkinter.messagebox.showwarning('Password Error','Password should at least 8 characters')
        
        if e3_content.get() != e5_content.get():
            tkinter.messagebox.showwarning('Not same password','Incorrect confirmed password, try again!')

    def checkusername():
        #! username list from database needed
        usernames = ['Mingming','Priyam']
        if e2_content.get() in usernames:
            tkinter.messagebox.showwarning('Existed Username','The username exists, try another username!')

    def checkemail():
        #! username list from database needed
        emails = ['mcao42@gatech.edu']
        #! email format
        if not re.match(r'^[0-9a-zA-Z]+@{1}[0-9a-zA-Z]+\.{1}[0-9a-zA-Z]+',e6_content.get()):
            tkinter.messagebox.showwarning('Email Error','Not valid email!')
        elif e6_content.get() in emails:
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
        confirmpwd()
        checkusername()
        window.destroy()
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
#5
def WIN_regi_emp():

    geometry = '600x' + str(len(newemail_emp)*40+400)

    window = Tk()
    window.title("Register Employee")
    window.geometry(geometry)
    window.resizable(0, 0)
    window.configure(background="#fff")


    def confirmpwd():
        if len(e3_content.get()) < 8 :
            tkinter.messagebox.showwarning('Password Error','Password should at least 8 characters')
        
        if e3_content.get() != e5_content.get():
            tkinter.messagebox.showwarning('Not same password','Incorrect confirmed password, try again!')

    def checkusername():
        #! username list from database needed
        usernames = ['Mingming','Priyam']
        if e2_content.get() in usernames:
            tkinter.messagebox.showwarning('Existed Username','The username exists, try another username!')

    def checkemail():
        #! username list from database needed
        emails = ['mcao42@gatech.edu']
        #! email format
        if not re.match(r'^[0-9a-zA-Z]+@{1}[0-9a-zA-Z]+\.{1}[0-9a-zA-Z]+',e6_content.get()):
            tkinter.messagebox.showwarning('Email Error','Not valid email!')
        elif e6_content.get() in emails:
            tkinter.messagebox.showwarning('Existed Email','The email exists, try another email!')
        else:
            newemail_emp.append(e6_content.get())

    def checkphone():
        #! phone list from database needed
        phones = ['123456789']
        if e8_content.get() == '':
            tkinter.messagebox.showwarning('Phone Error','Phone should not be none')  
        elif not re.match('^[0-9]{9}',e8_content.get()):
            tkinter.messagebox.showwarning('Phone Error','Not valid phone!')
        elif e8_content.get() in phones:
            tkinter.messagebox.showwarning('Existed Phone','The phone exists, try another phone!')

    def checkzipcode():
        if e12_content.get() == '':
            tkinter.messagebox.showwarning('Zipcode Error','Zipcode should not be none')  
        elif not re.match('^[0-9]{5}',e12_content.get()):
            tkinter.messagebox.showwarning('Zipcode Error','Not valid zipcode!')

    def register_checks():
        if e1_content.get() == '':
            tkinter.messagebox.showwarning('First Name Error','First Name should not be none')
        if e4_content.get() == '':
            tkinter.messagebox.showwarning('Last Name Error','Last Name should not be none')
        if e2_content.get() == '':
            tkinter.messagebox.showwarning('Username Error','Username should not be none')  
        if len(newemail_emp) == 0:
            tkinter.messagebox.showwarning('Email Error','Email should not be none')  
        confirmpwd()
        checkphone()
        checkusername()
        if e10_content.get() == '':
            tkinter.messagebox.showwarning('City Error','City should not be none')  
        checkzipcode()
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
    o11['values'] = ('AL','AZ','AR','CA','GA') # More states should be involved
    o11.place(x=250,y=220)
    o11.current(0)

    b3 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: back()))
    b3.place(x=175,y=350+len(newemail_emp)*40)

    b4 = Button(window,text="Register", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda:register_checks()))
    b4.place(x=325,y=350+len(newemail_emp)*40)

    b6add = Button(window,text="Add", width=6, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: addemail()))
    b6add.place(x=400,y=e6y)

    window.mainloop()
#6
def WIN_regi_emp_and_vis():

    geometry = '600x' + str(len(newemail_emp_and_vis)*40+400)

    window = Tk()
    window.title("Register Employee-Visitor")
    window.geometry(geometry)
    window.resizable(0, 0)
    window.configure(background="#fff")


    def confirmpwd():
        if len(e3_content.get()) < 8 :
            tkinter.messagebox.showwarning('Password Error','Password should at least 8 characters')
        
        if e3_content.get() != e5_content.get():
            tkinter.messagebox.showwarning('Not same password','Incorrect confirmed password, try again!')

    def checkusername():
        #! username list from database needed
        usernames = ['Mingming','Priyam']
        if e2_content.get() in usernames:
            tkinter.messagebox.showwarning('Existed Username','The username exists, try another username!')

    def checkemail():
        #! username list from database needed
        emails = ['mcao42@gatech.edu']
        #! email format
        if not re.match(r'^[0-9a-zA-Z]+@{1}[0-9a-zA-Z]+\.{1}[0-9a-zA-Z]+',e6_content.get()):
            tkinter.messagebox.showwarning('Email Error','Not valid email!')
        elif e6_content.get() in emails:
            tkinter.messagebox.showwarning('Existed Email','The email exists, try another email!')
        else:
            newemail_emp_and_vis.append(e6_content.get())

    def checkphone():
        #! phone list from database needed
        phones = ['123456789']
        if e8_content.get() == '':
            tkinter.messagebox.showwarning('Phone Error','Phone should not be none')  
        elif not re.match('^[0-9]{9}',e8_content.get()):
            tkinter.messagebox.showwarning('Phone Error','Not valid phone!')
        elif e8_content.get() in phones:
            tkinter.messagebox.showwarning('Existed Phone','The phone exists, try another phone!')

    def checkzipcode():
        if e12_content.get() == '':
            tkinter.messagebox.showwarning('Zipcode Error','Zipcode should not be none')  
        elif not re.match('^[0-9]{5}',e12_content.get()):
            tkinter.messagebox.showwarning('Zipcode Error','Not valid zipcode!')

    def register_checks():
        if e1_content.get() == '':
            tkinter.messagebox.showwarning('First Name Error','First Name should not be none')
        if e4_content.get() == '':
            tkinter.messagebox.showwarning('Last Name Error','Last Name should not be none')
        if e2_content.get() == '':
            tkinter.messagebox.showwarning('Username Error','Username should not be none')  
        if len(newemail_emp) == 0:
            tkinter.messagebox.showwarning('Email Error','Email should not be none')  
        confirmpwd()
        checkphone()
        checkusername()
        if e10_content.get() == '':
            tkinter.messagebox.showwarning('City Error','City should not be none')  
        checkzipcode()
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
    o11['values'] = ('AL','AZ','AR','CA','GA') # More states should be involved
    o11.place(x=250,y=220)
    o11.current(0)

    b3 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: back()))
    b3.place(x=175,y=350+len(newemail_emp_and_vis)*40)

    b4 = Button(window,text="Register", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda:register_checks()))
    b4.place(x=325,y=350+len(newemail_emp_and_vis)*40)

    b6add = Button(window,text="Add", width=6, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: addemail()))
    b6add.place(x=400,y=e6y)

    window.mainloop()
#7
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
#8
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
#9
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
#10    
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
#11
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
#12
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
#13
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
#14
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
#15
def WIN_take_transit():

    window = Tk()
    window.title("User Take Transit")
    window.geometry('500x500')
    window.resizable(0, 0)
    window.configure(background="#fff")

    def filter():
        start = e1_content.get()
        end = e2_content.get()
        
    def logtransit():
        if not re.match(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$',e3_content.get()):
            tkinter.messagebox.showwarning('Date Error','Not valid date!')            
        else:
            transitdate = e3_content.get()
        
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
    o1['values'] = ('InmanPark')
    o1.place(x=125,y=60)
    o1.current(0)

    option2 = StringVar()
    o2 = ttk.Combobox(window,width=8, textvariable=option2)
    o2['values'] = ('--ALL--','MARTA','Bus','Bike') # More states should be involved
    o2.place(x=350,y=60)
    o2.current(0)

    b1 = Button(window,text="Filter", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: filter()))
    b1.place(x=300,y=100)

    b2 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: back()))
    b2.place(x=50,y=450)

    b3 = Button(window,text="Log Transit", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: logtransit()))
    b3.place(x=350,y=450)

    window.mainloop()

    #The table
#16
def WIN_transit_his():
           
    window = Tk()
    window.title("User Transit History")
    window.geometry('500x500')
    window.resizable(0, 0)
    window.configure(background="#fff")

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

    e1 = Entry(window,width=6, bg='powder blue')
    e1.place(x=75,y=100)

    e2 = Entry(window,width=6, bg='powder blue')
    e2.place(x=225,y=100)

    e3 = Entry(window,width=6, bg='powder blue')
    e3.place(x=375,y=100)

    option1 = StringVar()
    o1 = ttk.Combobox(window,width=10, textvariable=option1)
    o1['values'] = ('InmanPark')
    o1.place(x=125,y=60)
    o1.current(0)

    option2 = StringVar()
    o2 = ttk.Combobox(window,width=8, textvariable=option2)
    o2['values'] = ('--ALL--') # More states should be involved
    o2.place(x=350,y=60)
    o2.current(0)

    b1 = Button(window,text="Filter", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.place(x=200,y=150)

    b2 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b2.place(x=200,y=450)


    window.mainloop()

    #The table
#17
def WIN_emp_manage_profile():
        
    window = Tk()
    window.title("Employee Manage Profile")
    window.geometry('600x400')
    window.resizable(0, 0)
    window.configure(background="#fff")

    Username = 'Ming'
    Sitename = 'Inman Park'
    Employeeid = '123456789'
    Address = '100 East Main Street, Seattle, WA 12345'

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
 
    e1 = Entry(window,width=14, bg='powder blue')
    e1.place(x=120,y=60)

    e2 = Entry(window,width=14, bg='powder blue')
    e2.place(x=400,y=60)

    e9 = Entry(window,width=14, bg='powder blue')
    e9.place(x=400,y=140)

    # e12 = Entry(window,width=14, bg='powder blue')
    # e12.place(x=400,y=220)

    chVarDis = IntVar()
    c1 = Checkbutton(window, text='Visitor Account',variable=chVarDis)
    if True:
        c1.select()
    else:
        c1.deselect()
    c1.place(x=250,y=325)

    b3 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b3.place(x=175,y=350)

    b4 = Button(window,text="Register", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b4.place(x=325,y=350)

    window.mainloop()
#18
def WIN_adm_manage_user():
        
    window = Tk()
    window.title("Administrator Manage User")
    window.geometry('600x400')
    window.resizable(0, 0)
    window.configure(background="#fff")

    l0 = Label(window,text="Manage User", width=36,font=('Arial', 18, 'bold'))
    l0.place(x=100,y=0)

    l1 = Label(window,text="Username", font=('Times 14 normal'))
    l1.place(x=25,y=60)
    
    l2 = Label(window,text="Type", font=('Times 14 normal'))
    l2.place(x=250,y=60)

    l3 = Label(window,text="Status", font=('Times 14 normal'))
    l3.place(x=425,y=60)
 
    e1 = Entry(window,width=10, bg='powder blue')
    e1.place(x=120,y=60)

    option2 = StringVar()
    o2 = ttk.Combobox(window,width=8, textvariable=option2)
    o2['values'] = ('Manager','Staff')
    o2.place(x=300,y=60)
    o2.current(0)

    option3 = StringVar()
    o3 = ttk.Combobox(window,width=6, textvariable=option3)
    o3['values'] = ('--ALL--') # More states should be involved
    o3.place(x=475,y=60)
    o3.current(0)

    b1 = Button(window,text="Filter", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.place(x=25,y=100)

    b2 = Button(window,text="Approve", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b2.place(x=350,y=100)

    b3 = Button(window,text="Decline", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b3.place(x=450,y=100)

    b4 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b4.place(x=250,y=350)

    window.mainloop()
#19
def WIN_adm_manage_site():
            
    window = Tk()
    window.title("Administrator Manage Site")
    window.geometry('500x400')
    window.resizable(0, 0)
    window.configure(background="#fff")

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
    o1['values'] = ('--ALL--')
    o1.place(x=100,y=60)
    o1.current(0)

    option2 = StringVar()
    o2 = ttk.Combobox(window,width=8, textvariable=option2)
    o2['values'] = ('--ALL--')
    o2.place(x=350,y=60)
    o2.current(0)

    option3 = StringVar()
    o3 = ttk.Combobox(window,width=6, textvariable=option3)
    o3['values'] = ('No','Yes') # More states should be involved
    o3.place(x=275,y=100)
    o3.current(0)

    b1 = Button(window,text="Filter", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.place(x=25,y=140)

    b2 = Button(window,text="Create", width=12, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b2.place(x=200,y=140)

    b3 = Button(window,text="Edit", width=12, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b3.place(x=300,y=140)

    b4 = Button(window,text="Delete", width=12, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b4.place(x=400,y=140)

    b5 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b5.place(x=200,y=350)

    window.mainloop()
#20
def WIN_adm_edit_site():

    window = Tk()
    window.title("Administrator Edit Site")
    window.geometry('400x250')
    window.resizable(0, 0)
    window.configure(background="#fff")

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

    e1 = Entry(window,width=10, bg='powder blue')
    e1.place(x=100,y=60)

    e2 = Entry(window,width=8, bg='powder blue')
    e2.place(x=300,y=60)

    e3 = Entry(window,width=26, bg='powder blue')
    e3.place(x=100,y=100)

    option4 = StringVar()
    o4 = ttk.Combobox(window,width=12, textvariable=option4)
    o4['values'] = ('Manager_name')
    o4.place(x=100,y=140)
    o4.current(0)

    chVarDis = IntVar()
    c1 = Checkbutton(window, text='Open Everyday',variable=chVarDis)
    if True:
        c1.select()
    else:
        c1.deselect()
    c1.place(x=250,y=140)

    b1 = Button(window,text="Back", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.place(x=25,y=200)

    b2 = Button(window,text="Update", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b2.place(x=275,y=200)

    window.mainloop()   
#21
def WIN_adm_create_site():
 
    window = Tk()
    window.title("Administrator Create Site")
    window.geometry('400x250')
    window.resizable(0, 0)
    window.configure(background="#fff")

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

    e1 = Entry(window,width=10, bg='powder blue')
    e1.place(x=100,y=60)

    e2 = Entry(window,width=8, bg='powder blue')
    e2.place(x=300,y=60)

    e3 = Entry(window,width=26, bg='powder blue')
    e3.place(x=100,y=100)

    option4 = StringVar()
    o4 = ttk.Combobox(window,width=12, textvariable=option4)
    o4['values'] = ('Manager_name')
    o4.place(x=100,y=140)
    o4.current(0)

    chVarDis = IntVar()
    c1 = Checkbutton(window, text='Open Everyday',variable=chVarDis)
    if True:
        c1.select()
    else:
        c1.deselect()
    c1.place(x=250,y=140)

    b1 = Button(window,text="Back", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.place(x=25,y=200)

    b2 = Button(window,text="Create", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b2.place(x=275,y=200)

    window.mainloop()   
#22
def WIN_adm_manage_transit():
            
    window = Tk()
    window.title("Administrator Manage Transit")
    window.geometry('500x400')
    window.resizable(0, 0)
    window.configure(background="#fff")

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

    e5a = Entry(window,width=3, bg='powder blue')
    e5a.place(x=350,y=100)

    e5b = Entry(window,width=3, bg='powder blue')
    e5b.place(x=425,y=100)

    e2 = Entry(window,width=14, bg='powder blue')
    e2.place(x=350,y=60)

    option1 = StringVar()
    o1 = ttk.Combobox(window,width=10, textvariable=option1)
    o1['values'] = ('--ALL--')
    o1.place(x=125,y=60)
    o1.current(0)

    option3 = StringVar()
    o3 = ttk.Combobox(window,width=8, textvariable=option3)
    o3['values'] = ('Inman Park') # More states should be involved
    o3.place(x=125,y=100)
    o3.current(0)

    b1 = Button(window,text="Filter", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.place(x=25,y=140)

    b2 = Button(window,text="Create", width=12, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b2.place(x=200,y=140)

    b3 = Button(window,text="Edit", width=12, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b3.place(x=300,y=140)

    b4 = Button(window,text="Delete", width=12, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b4.place(x=400,y=140)

    b5 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b5.place(x=200,y=350)

    window.mainloop()
#23
def WIN_adm_edit_transit():
            
    window = Tk()
    window.title("Administrator Edit Transit")
    window.geometry('400x300')
    window.resizable(0, 0)
    window.configure(background="#fff")

    # spin = Spinbox(window, values=('A','B'),width=5, bd=8)
    # spin.place(x=0,y=0)

    Transit_type = "Bus"

    l0 = Label(window,text="Edit Transit", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    l1 = Label(window,text="Transport Type", font=('Times', 14, 'normal'))
    l1.place(x=25,y=60)

    l2 = Label(window,text=Transit_type, font=('Times', 14, 'italic','bold'))
    l2.place(x=125,y=60)

    l3 = Label(window,text="Route", font=('Times', 14, 'normal'))
    l3.place(x=175,y=60)

    l4 = Label(window,text="Price($)", font=('Times', 14, 'normal'))
    l4.place(x=275,y=60)

    l5 = Label(window,text="Connected Sites", font=('Times', 14, 'normal'))
    l5.place(x=25,y=140)

    e1 = Entry(window,width=3, bg='powder blue')
    e1.place(x=225,y=60)

    e2 = Entry(window,width=3, bg='powder blue')
    e2.place(x=325,y=60)

    # For now, it's fixed
    st1 = scrolledtext.ScrolledText(window, width=20, height=8,wrap=WORD,bd=8,)
    st1.place(x=200,y=100)
    st1.insert(INSERT,"""Something to be filled""")
    st1.config(state=DISABLED)

    b1 = Button(window,text="Back", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.place(x=25,y=250)

    b2 = Button(window,text="Update", width=12, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b2.place(x=300,y=250)

    window.mainloop() 
#24
def WIN_adm_create_transit():
                 
    window = Tk()
    window.title("Administrator Create Transit")
    window.geometry('400x300')
    window.resizable(0, 0)
    window.configure(background="#fff")

    # spin = Spinbox(window, values=('A','B'),width=5, bd=8)
    # spin.place(x=0,y=0)

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

    e1 = Entry(window,width=3, bg='powder blue')
    e1.place(x=250,y=60)

    e2 = Entry(window,width=3, bg='powder blue')
    e2.place(x=350,y=60)

    option1 = StringVar()
    o1 = ttk.Combobox(window,width=5, textvariable=option1)
    o1['values'] = ('MARTA')
    o1.place(x=125,y=60)
    o1.current(0)
    # For now, it's fixed
    st1 = scrolledtext.ScrolledText(window, width=20, height=8,wrap=WORD,bd=8,)
    st1.place(x=200,y=100)
    st1.insert(INSERT,"""Something to be filled""")
    st1.config(state=DISABLED)

    b1 = Button(window,text="Back", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.place(x=25,y=250)

    b2 = Button(window,text="Create", width=12, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b2.place(x=300,y=250)

    window.mainloop() 
#25
def WIN_man_manage_event():
            
    window = Tk()
    window.title("Manager Manage Event")
    window.geometry('500x500')
    window.resizable(0, 0)
    window.configure(background="#fff")

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

    e1 = Entry(window,width=10, bg='powder blue')
    e1.place(x=100,y=60)

    e2 = Entry(window,width=8, bg='powder blue')
    e2.place(x=400,y=60)

    e3 = Entry(window,width=14, bg='powder blue')
    e3.place(x=100,y=100)

    e4 = Entry(window,width=14, bg='powder blue')
    e4.place(x=350,y=100)

    e6a = Entry(window,width=3, bg='powder blue')
    e6a.place(x=135,y=140)

    e6b = Entry(window,width=3, bg='powder blue')
    e6b.place(x=190,y=140)

    e8a = Entry(window,width=3, bg='powder blue')
    e8a.place(x=385,y=140)

    e8b = Entry(window,width=3, bg='powder blue')
    e8b.place(x=440,y=140)

    e10a = Entry(window,width=3, bg='powder blue')
    e10a.place(x=260,y=180)

    e10b = Entry(window,width=3, bg='powder blue')
    e10b.place(x=315,y=180)

    b1 = Button(window,text="Filter", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.place(x=25,y=220)

    b2 = Button(window,text="Create", width=12, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b2.place(x=200,y=220)

    b3 = Button(window,text="Edit", width=12, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b3.place(x=300,y=220)

    b4 = Button(window,text="Delete", width=12, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b4.place(x=400,y=220)

    b5 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b5.place(x=200,y=450)

    window.mainloop()
#26
def WIN_man_VE_event():
            
    window = Tk()
    window.title("Manager View/Edit Event")
    window.geometry('400x800')
    window.resizable(0, 0)
    window.configure(background="#fff")

    Eventname = 'Bus Tour'
    Price = '25'
    Startdate = '2019-02-01'
    Enddate = '2019-02-01'
    Minsta = '4'
    Capacity = '100'

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
    l10.place(x=100,y=140)

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

    e16a = Entry(window,width=3, bg='powder blue')
    e16a.place(x=200,y=460)

    e16b = Entry(window,width=3, bg='powder blue')
    e16b.place(x=275,y=460)

    e18a = Entry(window,width=3, bg='powder blue')
    e18a.place(x=200,y=500)

    e18b = Entry(window,width=3, bg='powder blue')
    e18b.place(x=275,y=500)

    st1 = scrolledtext.ScrolledText(window, width=25, height=8,wrap=WORD,bd=8,)
    st1.place(x=150,y=180)
    st1.insert(INSERT,"""Something to be filled""")
    st1.config(state=DISABLED)

    st2 = scrolledtext.ScrolledText(window, width=25, height=8,wrap=WORD,bd=8,)
    st2.place(x=150,y=300)
    st2.insert(INSERT,"""Something to be filled""")
    st2.config(state=DISABLED)

    b1 = Button(window,text="Filter", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.place(x=25,y=540)

    b2 = Button(window,text="Update", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b2.place(x=275,y=540)

    b3 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b3.pack(side='bottom')

    window.mainloop()
#27
def WIN_man_create_event():
            
    window = Tk()
    window.title("Manager Create Event")
    window.geometry('500x500')
    window.resizable(0, 0)
    window.configure(background="#fff")

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

    e1 = Entry(window,width=20, bg='powder blue')
    e1.place(x=125,y=60)

    e2 = Entry(window,width=3, bg='powder blue')
    e2.place(x=100,y=100)

    e3 = Entry(window,width=3, bg='powder blue')
    e3.place(x=225,y=100)

    e4 = Entry(window,width=3, bg='powder blue')
    e4.place(x=450,y=100)

    e5 = Entry(window,width=8, bg='powder blue')
    e5.place(x=125,y=140)

    e6 = Entry(window,width=8, bg='powder blue')
    e6.place(x=350,y=140)

    st1 = scrolledtext.ScrolledText(window, width=45, height=7,wrap=WORD,bd=8,)
    st1.place(x=125,y=180)
    st1.insert(INSERT,"""Something to be filled""")
    st1.config(state=DISABLED)

    st2 = scrolledtext.ScrolledText(window, width=45, height=7,wrap=WORD,bd=8,)
    st2.place(x=125,y=300)
    st2.insert(INSERT,"""Something to be filled""")
    st2.config(state=DISABLED)

    b1 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.place(x=75,y=450)

    b2 = Button(window,text="Create", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b2.place(x=275,y=450)

    window.mainloop() 
#28
def WIN_man_manage_staff():
                      
    window = Tk()
    window.title("Manager Manage Staff")
    window.geometry('400x500')
    window.resizable(0, 0)
    window.configure(background="#fff")

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

    e2 = Entry(window,width=6, bg='powder blue')
    e2.place(x=125,y=100)

    e3 = Entry(window,width=6, bg='powder blue')
    e3.place(x=300,y=100)

    e4 = Entry(window,width=6, bg='powder blue')
    e4.place(x=125,y=140)

    e5 = Entry(window,width=6, bg='powder blue')
    e5.place(x=300,y=140)

    option1 = StringVar()
    o1 = ttk.Combobox(window,width=10, textvariable=option1)
    o1['values'] = ('InmanPark')
    o1.place(x=125,y=60)
    o1.current(0)

    b1 = Button(window,text="Filter", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.place(x=150,y=180)

    b2 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b2.place(x=150,y=450)

    window.mainloop()
#29
def WIN_man_site_report():
            
    window = Tk()
    window.title("Manager Site Report")
    window.geometry('500x400')
    window.resizable(0, 0)
    window.configure(background="#fff")

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

    e1 = Entry(window,width=10, bg='powder blue')
    e1.place(x=100,y=60)

    e2 = Entry(window,width=10, bg='powder blue')
    e2.place(x=375,y=60)

    e4a = Entry(window,width=2, bg='powder blue')
    e4a.place(x=170,y=100)

    e4b = Entry(window,width=2, bg='powder blue')
    e4b.place(x=215,y=100)

    e6a = Entry(window,width=2, bg='powder blue')
    e6a.place(x=395,y=100)

    e6b = Entry(window,width=2, bg='powder blue')
    e6b.place(x=440,y=100)

    e8a = Entry(window,width=2, bg='powder blue')
    e8a.place(x=170,y=140)

    e8b = Entry(window,width=2, bg='powder blue')
    e8b.place(x=215,y=140)

    e10a = Entry(window,width=2, bg='powder blue')
    e10a.place(x=395,y=140)

    e10b = Entry(window,width=2, bg='powder blue')
    e10b.place(x=440,y=140)

    b1 = Button(window,text="Filter", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.place(x=50,y=180)

    b2 = Button(window,text="Daily Detail", width=12, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b2.place(x=375,y=180)

    b3 = Button(window,text="Back", width=12, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b3.pack(side='bottom')

    window.mainloop()
#30
def WIN_man_daily_detail():
            
    window = Tk()
    window.title("Manager Daily Detail")
    window.geometry('400x300')
    window.resizable(0, 0)
    window.configure(background="#fff")

    l0 = Label(window,text="Daily Detail", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    b1 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.pack(side='bottom')

    window.mainloop()
#31
def WIN_sta_view_schedule():
                       
    window = Tk()
    window.title("Staff View Schedule")
    window.geometry('500x400')
    window.resizable(0, 0)
    window.configure(background="#fff")

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

    e1 = Entry(window,width=10, bg='powder blue')
    e1.place(x=125,y=60)

    e2 = Entry(window,width=10, bg='powder blue')
    e2.place(x=350,y=60)

    e3 = Entry(window,width=10, bg='powder blue')
    e3.place(x=125,y=100)

    e4 = Entry(window,width=10, bg='powder blue')
    e4.place(x=350,y=100)

    b1 = Button(window,text="Filter", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.place(x=100,y=140)

    b2 = Button(window,text="View Event", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b2.place(x=275,y=140)

    b3 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b3.pack(side='bottom')

    window.mainloop()
#32
def WIN_sta_event_detail():
            
    window = Tk()
    window.title("Staff Event Detail")
    window.geometry('500x400')
    window.resizable(0, 0)
    window.configure(background="#fff")

    Event = "Arboretum Walking Tour"
    Site = "Inman Park"
    Startdate = "2019-02-02"
    Enddate = "2019-02-02"
    Durationdays = "1"
    Staffsassigned = "Alice Smith"
    Capacity = "20"
    Price = "0"

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
       
    l12 = Label(window,text=Staffsassigned,font=('Times 14 italic bold'))
    l12.place(x=125,y=140)

    l13 = Label(window,text="Capacity", font=('Times 14 normal'))
    l13.place(x=210,y=140)
    
    l14 = Label(window,text=Capacity, font=('Times 14 italic bold'))
    l14.place(x=275,y=140)

    l15 = Label(window,text="Price", font=('Times 14 normal'))
    l15.place(x=345,y=140)

    l16 = Label(window,text=Price, font=('Times 14 italic bold'))
    l16.place(x=400,y=140)
       
    l17 = Label(window,text="Description",font=('Times 14 italic bold'))
    l17.place(x=25,y=180)

    st1 = scrolledtext.ScrolledText(window, width=45, height=7,wrap=WORD,bd=8,)
    st1.place(x=125,y=180)
    st1.insert(INSERT,"""Something to be filled""")
    st1.config(state=DISABLED)
           
    b1 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.pack(side='bottom')

    window.mainloop() 
#33
def WIN_vis_explore_event():
            
    window = Tk()
    window.title(" ")
    window.geometry('x')
    window.resizable(0, 0)
    window.configure(background="#fff")

    l0 = Label(window,text="", width=36,font=('Arial', 18, 'bold'))
    l0.grid(sticky='n')

    b1 = Button(window,text="", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.grid(row=2,column=2)

    e1 = Entry(window,width=20, bg='powder blue')
    e1.place(x=150,y=60)

    t1 = Text(window,width=20, bg='white')
    t1.pack()

    window.mainloop() 

def WIN_vis_event_detail():
            
    window = Tk()
    window.title(" ")
    window.geometry('x')
    window.resizable(0, 0)
    window.configure(background="#fff")

    l0 = Label(window,text="", width=36,font=('Arial', 18, 'bold'))
    l0.grid(sticky='n')

    b1 = Button(window,text="", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.grid(row=2,column=2)

    e1 = Entry(window,width=20, bg='powder blue')
    e1.place(x=150,y=60)

    t1 = Text(window,width=20, bg='white')
    t1.pack()

    window.mainloop() 

def WIN_vis_explore_site():
            
    window = Tk()
    window.title(" ")
    window.geometry('x')
    window.resizable(0, 0)
    window.configure(background="#fff")

    l0 = Label(window,text="", width=36,font=('Arial', 18, 'bold'))
    l0.grid(sticky='n')

    b1 = Button(window,text="", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.grid(row=2,column=2)

    e1 = Entry(window,width=20, bg='powder blue')
    e1.place(x=150,y=60)

    t1 = Text(window,width=20, bg='white')
    t1.pack()

    window.mainloop()

def WIN_vis_transit_detail():
            
    window = Tk()
    window.title(" ")
    window.geometry('x')
    window.resizable(0, 0)
    window.configure(background="#fff")

    l0 = Label(window,text="", width=36,font=('Arial', 18, 'bold'))
    l0.grid(sticky='n')

    b1 = Button(window,text="", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.grid(row=2,column=2)

    e1 = Entry(window,width=20, bg='powder blue')
    e1.place(x=150,y=60)

    t1 = Text(window,width=20, bg='white')
    t1.pack()

    window.mainloop() 

def WIN_vis_site_detail():
            
    window = Tk()
    window.title(" ")
    window.geometry('x')
    window.resizable(0, 0)
    window.configure(background="#fff")

    l0 = Label(window,text="", width=36,font=('Arial', 18, 'bold'))
    l0.grid(sticky='n')

    b1 = Button(window,text="", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.grid(row=2,column=2)

    e1 = Entry(window,width=20, bg='powder blue')
    e1.place(x=150,y=60)

    t1 = Text(window,width=20, bg='white')
    t1.pack()

    window.mainloop() 

def WIN_vis_visit_his():
            
    window = Tk()
    window.title(" ")
    window.geometry('x')
    window.resizable(0, 0)
    window.configure(background="#fff")

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
    # db = DB()

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
    WIN_FUN_man_and_vis()
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
    # WIN_sta_view_schedule()
    # WIN_sta_event_detail()
    # WIN_vis_explore_event()
    # WIN_vis_event_detail()
    # WIN_vis_explore_site()
    # WIN_vis_transit_detail()
    # WIN_vis_site_detail()
    # WIN_vis_visit_his()

if __name__ == '__main__':
    main()
    
