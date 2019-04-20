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
        if 'Employee' in etype[0]:
            username_tmp = str(username[0][0])
            print(username_tmp)
            command = "SELECT Em.etype FROM employee as Em " + "WHERE Em.eusername='" + username_tmp + "'"
            etype_emp = db.search(command)
            if 'Admin' in etype_emp[0]:
                WIN_FUN_adm()
            elif 'Manager' in etype_emp[0]:
                WIN_FUN_man()
            elif 'Staff' in  etype_emp[0]:
                WIN_FUN_sta()
        elif 'emplyee,visitor' in etype[0]:
            username_tmp = str(username[0][0])
            command = "SELECT Em.etype FROM employee as Em " + "WHERE Em.eusername='" + username_tmp + "'"
            etype_emp = db.search(command)
            if 'Admin' in etype_emp[0]:
                WIN_FUN_adm_and_vis()
            elif 'Manager' in etype_emp[0]:
                WIN_FUN_man_and_vis()
            elif 'Staff' in etype_emp[0]:
                WIN_FUN_sta_and_vis()
        elif 'User' in etype[0]:
            WIN_FUN_user()
        elif 'Visitor' in etype[0]:
            WIN_FUN_vis()

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
        WIN_regi_nav()
 
    b1 = Button(window, text="Login", width=6, height=2,bg='white',fg='grey',font=('Arial 9 bold'), command=(lambda: checkaccount()))
    b1.place(x=75,y=150)

    b2 = Button(window, text="Register", width=8, height=2,bg='white',fg='grey',font=('Arial 9 bold'), command=(lambda: register()))
    b2.place(x=250,y=150)

    window.mainloop()
