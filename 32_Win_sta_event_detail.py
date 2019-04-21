def WIN_sta_event_detail(Event_name,Event_Start_date):
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
