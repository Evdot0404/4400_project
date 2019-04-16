#! /usr/bin/python3
import flask
import sqlite3
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

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
#1
def WIN_user_login():
    # import turtle
    # def hello():
    #     turtle.write("Hello world", align='center', font=('Arial', 18, 'normal'))

    # Initialization
    window = Tk()
    window.title("User Login")
    window.geometry('400x200')
    window.configure(background="#fff")

    # canvas = turtle.ScrolledCanvas(window)
    # canvas.pack(side=LEFT)
    # screen = turtle.TurtleScreen(canvas)
    # turtle = turtle.RawPen(screen, visible=False)

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
    e1 = Entry(window,width=20, bg='powder blue')
    e1.place(x=150,y=60)
    # e1.focus_set()

    e2 = Entry(window,width=20, bg='powder blue')
    e2.place(x=150,y=100)
    # e2.focus_set()

    def hello(text):
        e1.delete(0,END)
        # e1.insert(0,text)
        tkinter.messagebox.showinfo("Example",e1.get())
        # exit()

    def hi():
        tkinter.messagebox.showinfo("Example","hi")
        exit()
        # print("hi")
    # Buttons
    b1 = Button(window, text="Login", width=6, height=2,bg='white',fg='grey',font=('Arial 9 bold'), command=(lambda: hello("test")))
    b1.place(x=75,y=150)
    # b1.grid(row=12, column=1) padx,pady

    b2 = Button(window, text="Register", width=8, height=2,bg='white',fg='grey',font=('Arial 9 bold'), command=(lambda: tkinter.messagebox.showwarning("yes","this is wrong")))
    b2.place(x=250,y=150)
    # b2.grid(row=12, column=2)

    # Radiobutton()

    window.mainloop()
#2
def WIN_regi_nav():

    window = Tk()
    window.title("Register Navigation")
    window.geometry('250x250')
    window.configure(background="#fff")

    l0 = Label(window,text="Register Navigation", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    b1 = Button(window,text="User Only", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.place(x=75,y=60)

    b2 = Button(window,text="Visitor Only", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b2.place(x=75,y=90)

    b3 = Button(window,text="Employee Only", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b3.place(x=75,y=120)

    b4 = Button(window,text="Employee-Visitor", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b4.place(x=75,y=150)

    b5 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b5.place(x=75,y=180)

    window.mainloop()
#3
def WIN_regi_user():
    
    window = Tk()
    window.title("Register User")
    window.geometry('600x300')
    window.resizable(0, 0)
    window.configure(background="#fff")

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
    
    l5 = Label(window,text="Comfirm Password",font=('Times 14 normal'))
    l5.place(x=275,y=140)

    l6 = Label(window,text="Email", font=('Times 14 normal'))
    l6.place(x=25,y=180)
 
    e1 = Entry(window,width=14, bg='powder blue')
    e1.place(x=120,y=60)

    e2 = Entry(window,width=14, bg='powder blue')
    e2.place(x=120,y=100)

    e3 = Entry(window,width=14, bg='powder blue')
    e3.place(x=120,y=140)

    e4 = Entry(window,width=14, bg='powder blue')
    e4.place(x=400,y=60)

    e5 = Entry(window,width=14, bg='powder blue')
    e5.place(x=400,y=140)

    # e6 = Entry(window,width=14, bg='powder blue')
    # e6.place(x=400,y=140)

    # b1 = Button(window,text="Remove", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    # b1.grid(row=2,column=2)

    # b2 = Button(window,text="Add", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    # b2.place(x=75,y=90)

    b3 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b3.place(x=175,y=250)

    b4 = Button(window,text="Register", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b4.place(x=325,y=250)

    window.mainloop()
#4
def WIN_regi_vis():
        
    window = Tk()
    window.title("Register Visitor")
    window.geometry('600x300')
    window.resizable(0, 0)
    window.configure(background="#fff")

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
    
    l5 = Label(window,text="Comfirm Password",font=('Times 14 normal'))
    l5.place(x=275,y=140)

    l6 = Label(window,text="Email", font=('Times 14 normal'))
    l6.place(x=25,y=180)
 
    e1 = Entry(window,width=14, bg='powder blue')
    e1.place(x=120,y=60)

    e2 = Entry(window,width=14, bg='powder blue')
    e2.place(x=120,y=100)

    e3 = Entry(window,width=14, bg='powder blue')
    e3.place(x=120,y=140)

    e4 = Entry(window,width=14, bg='powder blue')
    e4.place(x=400,y=60)

    e5 = Entry(window,width=14, bg='powder blue')
    e5.place(x=400,y=140)

    # e6 = Entry(window,width=14, bg='powder blue')
    # e6.place(x=400,y=140)

    # b1 = Button(window,text="Remove", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    # b1.grid(row=2,column=2)

    # b2 = Button(window,text="Add", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    # b2.place(x=75,y=90)

    b3 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b3.place(x=175,y=250)

    b4 = Button(window,text="Register", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b4.place(x=325,y=250)

    window.mainloop()
#5
def WIN_regi_emp():
        
    window = Tk()
    window.title("Register Employee")
    window.geometry('600x400')
    window.resizable(0, 0)
    window.configure(background="#fff")

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
 
    e1 = Entry(window,width=14, bg='powder blue')
    e1.place(x=120,y=60)

    e2 = Entry(window,width=14, bg='powder blue')
    e2.place(x=120,y=100)

    e3 = Entry(window,width=14, bg='powder blue')
    e3.place(x=120,y=140)

    e4 = Entry(window,width=14, bg='powder blue')
    e4.place(x=400,y=60)

    e5 = Entry(window,width=14, bg='powder blue')
    e5.place(x=400,y=140)

    e8 = Entry(window,width=14, bg='powder blue')
    e8.place(x=120,y=180)

    e9 = Entry(window,width=14, bg='powder blue')
    e9.place(x=400,y=180)

    e10 = Entry(window,width=6, bg='powder blue')
    e10.place(x=120,y=220)

    e12 = Entry(window,width=14, bg='powder blue')
    e12.place(x=400,y=220)

    option7 = StringVar()
    o7 = ttk.Combobox(window,width=12, textvariable=option7)
    o7['values'] = ('Manager','Staff')
    o7.place(x=400,y=100)
    o7.current(0)

    option11 = StringVar()
    o11 = ttk.Combobox(window,width=4, textvariable=option11)
    o11['values'] = ('GA') # More states should be involved
    o11.place(x=250,y=220)
    o11.current(0)
    # e6 = Entry(window,width=14, bg='powder blue')
    # e6.place(x=400,y=140)

    # b1 = Button(window,text="Remove", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    # b1.grid(row=2,column=2)

    # b2 = Button(window,text="Add", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    # b2.place(x=75,y=90)

    b3 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b3.place(x=175,y=350)

    b4 = Button(window,text="Register", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b4.place(x=325,y=350)

    window.mainloop()
#6
def WIN_regi_emp_and_vis():
         
    window = Tk()
    window.title("Register Employee-Visitor")
    window.geometry('600x400')
    window.resizable(0, 0)
    window.configure(background="#fff")

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
 
    e1 = Entry(window,width=14, bg='powder blue')
    e1.place(x=120,y=60)

    e2 = Entry(window,width=14, bg='powder blue')
    e2.place(x=120,y=100)

    e3 = Entry(window,width=14, bg='powder blue')
    e3.place(x=120,y=140)

    e4 = Entry(window,width=14, bg='powder blue')
    e4.place(x=400,y=60)

    e5 = Entry(window,width=14, bg='powder blue')
    e5.place(x=400,y=140)

    e8 = Entry(window,width=14, bg='powder blue')
    e8.place(x=120,y=180)

    e9 = Entry(window,width=14, bg='powder blue')
    e9.place(x=400,y=180)

    e10 = Entry(window,width=6, bg='powder blue')
    e10.place(x=120,y=220)

    e12 = Entry(window,width=14, bg='powder blue')
    e12.place(x=400,y=220)

    option7 = StringVar()
    o7 = ttk.Combobox(window,width=12, textvariable=option7)
    o7['values'] = ('Manager','Staff')
    o7.place(x=400,y=100)
    o7.current(0)

    option11 = StringVar()
    o11 = ttk.Combobox(window,width=4, textvariable=option11)
    o11['values'] = ('GA') # More states should be involved
    o11.place(x=250,y=220)
    o11.current(0)
    # e6 = Entry(window,width=14, bg='powder blue')
    # e6.place(x=400,y=140)

    # b1 = Button(window,text="Remove", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    # b1.grid(row=2,column=2)

    # b2 = Button(window,text="Add", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    # b2.place(x=75,y=90)

    b3 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b3.place(x=175,y=350)

    b4 = Button(window,text="Register", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b4.place(x=325,y=350)

    window.mainloop()
#7
def WIN_FUN_user():
 
    window = Tk()
    window.title("User Functionality")
    window.geometry('250x175')
    window.configure(background="#fff")

    l0 = Label(window,text="User Functionality", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    b1 = Button(window,text="Take Transit", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.place(x=75,y=60)

    b2 = Button(window,text="View Transit History", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b2.place(x=75,y=90)

    b3 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b3.place(x=75,y=120)

    window.mainloop()
#8
def WIN_FUN_adm():
 
    window = Tk()
    window.title("Administrator Functionality")
    window.geometry('250x300')
    window.configure(background="#fff")

    l0 = Label(window,text="Administrator Functionality", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    b1 = Button(window,text="Manage Profile", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.place(x=75,y=60)

    b2 = Button(window,text="Manage User", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b2.place(x=75,y=90)

    b3 = Button(window,text="Manage Transit", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b3.place(x=75,y=120)

    b4 = Button(window,text="Manage Site", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b4.place(x=75,y=150)

    b5 = Button(window,text="Take Transit", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b5.place(x=75,y=180)

    b6 = Button(window,text="View Transit History", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b6.place(x=75,y=210)

    b7 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b7.place(x=75,y=240)

    window.mainloop()
#9
def WIN_FUN_adm_and_vis():

    window = Tk()
    window.title("Administrator-Visitor Functionality")
    window.geometry('250x400')
    window.configure(background="#fff")

    l0 = Label(window,text="Administrator Functionality", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    b1 = Button(window,text="Manage Profile", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.place(x=75,y=60)

    b2 = Button(window,text="Manage User", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b2.place(x=75,y=90)

    b3 = Button(window,text="Manage Transit", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b3.place(x=75,y=120)

    b4 = Button(window,text="Manage Site", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b4.place(x=75,y=150)

    b5 = Button(window,text="Take Transit", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b5.place(x=75,y=180)

    b6 = Button(window,text="Explore Site", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b6.place(x=75,y=210)

    b7 = Button(window,text="Explore Event", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b7.place(x=75,y=240)

    b8 = Button(window,text="View Transit History", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b8.place(x=75,y=270)

    b9 = Button(window,text="View Visit History", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b9.place(x=75,y=300)

    b10 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b10.place(x=75,y=330)

    window.mainloop()
#10    
def WIN_FUN_man():
  
    window = Tk()
    window.title("Manager Functionality")
    window.geometry('250x300')
    window.configure(background="#fff")

    l0 = Label(window,text="Manager Functionality", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    b1 = Button(window,text="Manage Profile", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.place(x=75,y=60)

    b2 = Button(window,text="Manage Event", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b2.place(x=75,y=90)

    b3 = Button(window,text="View Site Report", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b3.place(x=75,y=120)

    b4 = Button(window,text="View Staff", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b4.place(x=75,y=150)

    b5 = Button(window,text="Take Transit", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b5.place(x=75,y=180)

    b6 = Button(window,text="View Transit History", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b6.place(x=75,y=210)

    b7 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b7.place(x=75,y=240)

    window.mainloop()
#11
def WIN_FUN_man_and_vis():

    window = Tk()
    window.title("Manager-Visitor Functionality")
    window.geometry('250x400')
    window.configure(background="#fff")

    l0 = Label(window,text="Manager Functionality", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    b1 = Button(window,text="Manage Profile", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.place(x=75,y=60)

    b2 = Button(window,text="Manage Event", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b2.place(x=75,y=90)

    b3 = Button(window,text="View Staff", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b3.place(x=75,y=120)

    b4 = Button(window,text="View Site Report", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b4.place(x=75,y=150)

    b5 = Button(window,text="Explore Site", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b5.place(x=75,y=180)

    b6 = Button(window,text="Explore Event", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b6.place(x=75,y=210)

    b7 = Button(window,text="Take Transit", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b7.place(x=75,y=240)

    b8 = Button(window,text="View Transit History", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b8.place(x=75,y=270)

    b9 = Button(window,text="View Visit History", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b9.place(x=75,y=300)

    b10 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b10.place(x=75,y=330)

    window.mainloop()
#12
def WIN_FUN_sta():
  
    window = Tk()
    window.title("Staff Functionality")
    window.geometry('250x250')
    window.configure(background="#fff")

    l0 = Label(window,text="Staff Functionality", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    b1 = Button(window,text="Manage Profile", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.place(x=75,y=60)

    b2 = Button(window,text="View Schedule", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b2.place(x=75,y=90)

    b3 = Button(window,text="Take Tansit", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b3.place(x=75,y=120)

    b4 = Button(window,text="View Transit History", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b4.place(x=75,y=150)

    b5 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b5.place(x=75,y=180)

    window.mainloop()
#13
def WIN_FUN_sta_and_vis():

    window = Tk()
    window.title("Staff-Visitor Functionality")
    window.geometry('250x320')
    window.configure(background="#fff")

    l0 = Label(window,text="Staff Functionality", width=36,font=('Arial', 18, 'bold'))
    l0.pack(side='top')

    b1 = Button(window,text="Manage Profile", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.place(x=75,y=60)

    b2 = Button(window,text="View Schedule", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b2.place(x=75,y=90)

    b3 = Button(window,text="Explore Event", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b3.place(x=75,y=120)

    b4 = Button(window,text="Explore Site", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b4.place(x=75,y=150)

    b5 = Button(window,text="Take Transit", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b5.place(x=75,y=180)

    b6 = Button(window,text="View Visit History", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b6.place(x=75,y=210)

    b7 = Button(window,text="View Transit History", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b7.place(x=75,y=240)

    b8 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
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

    b1 = Button(window,text="Explore Event", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.place(x=75,y=60)

    b2 = Button(window,text="Explore Site", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b2.place(x=75,y=90)

    b3 = Button(window,text="View Visit History", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b3.place(x=75,y=120)

    b4 = Button(window,text="Take Transit", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b4.place(x=75,y=150)

    b5 = Button(window,text="View Transit History", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b5.place(x=75,y=180)

    b6 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b6.place(x=75,y=210)

    window.mainloop()
#15
def WIN_take_transit():
           
    window = Tk()
    window.title("User Take Transit")
    window.geometry('500x500')
    window.resizable(0, 0)
    window.configure(background="#fff")

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

    e1 = Entry(window,width=3, bg='powder blue')
    e1.place(x=120,y=100)

    e2 = Entry(window,width=3, bg='powder blue')
    e2.place(x=200,y=100)

    e3 = Entry(window,width=8, bg='powder blue')
    e3.place(x=250,y=450)

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
    b1.place(x=300,y=100)

    b2 = Button(window,text="Back", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b2.place(x=50,y=450)

    b3 = Button(window,text="Log Transit", width=16, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
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
    window.geometry('400x300')
    window.resizable(0, 0)
    window.configure(background="#fff")

    l0 = Label(window,text="Edit Site", width=36,font=('Arial', 18, 'bold'))
    l0.grid(sticky='n')

    l1 = Label(window,text="Name", font=('Times 14 normal'))
    l1.place(x=25,y=60)
    
    l2 = Label(window,text="Zipcode", font=('Times 14 normal'))
    l2.place(x=200,y=60)

    l3 = Label(window,text="Address", font=('Times 14 normal'))
    l3.place(x=25,y=100)

    l4 = Label(window,text="Manager", font=('Times 14 normal'))
    l4.place(x=25,y=140)

    option4 = StringVar()
    o4 = ttk.Combobox(window,width=10, textvariable=option4)
    o4['values'] = ('Manager_name')
    o4.place(x=300,y=140)
    o4.current(0)

    chVarDis = IntVar()
    c1 = Checkbutton(window, text='Open Everyday',variable=chVarDis)
    if True:
        c1.select()
    else:
        c1.deselect()
    c1.place(x=250,y=325)

    b1 = Button(window,text="Filter", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b1.place(x=25,y=100)

    b2 = Button(window,text="Approve", width=14, height=2,bg='pink',fg='grey',font=('Arial 9 bold'), command=(lambda: None))
    b2.place(x=350,y=100)

    window.mainloop()

def WIN_adm_create_site():
            
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

def WIN_adm_manage_transit():
            
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

def WIN_adm_edit_transit():
            
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

def WIN_adm_create_transit():
            
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

def WIN_man_manage_event():
            
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

def WIN_man_VE_event():
            
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

def WIN_man_create_event():
            
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

def WIN_man_manage_staff():
            
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

def WIN_man_site_report():
            
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

def WIN_man_daily_detail():
            
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

def WIN_sta_view_schedule():
            
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

def WIN_sta_event_detail():
            
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
    # WIN_FUN_man_and_vis()
    # WIN_FUN_sta()
    # WIN_FUN_sta_and_vis()
    # WIN_FUN_vis() 
    # WIN_take_transit()
    # WIN_transit_his()
    # WIN_emp_manage_profile()
    # WIN_adm_manage_user()
    # WIN_adm_manage_site()
    WIN_adm_edit_site()

if __name__ == '__main__':
    main()
    
