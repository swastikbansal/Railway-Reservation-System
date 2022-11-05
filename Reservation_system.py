import tkinter
from tkinter import ttk
from tkinter.constants import END
import tkcalendar
from tkinter import messagebox
import mysql.connector
import datetime
import time

#--------------MySQL connection---------------#

try:
    # Connecting to Database
    mycon=mysql.connector.connect(
    host="bvhnwga1g3mpezf6mrai-mysql.services.clever-cloud.com",
    user="uhnntwwvt4dmdiqw",
    password="CDDNlY1wxJBQMoeUD8nf",
    database="bvhnwga1g3mpezf6mrai")

    cur = mycon.cursor()# Creating an Object for working in Database
    mycon.autocommit=True

    if mycon.is_connected():# Checking Connection
        print("Connection Successfull !!!!!")     
        current_datetime=datetime.date.today()# Storing Current Date of Current Day        

        # Storing Dates of next 7 days w.r.t 'current_datetime'
        d1=str(current_datetime+datetime.timedelta(days=1))
        d2=str(current_datetime+datetime.timedelta(days=2))
        d3=str(current_datetime+datetime.timedelta(days=3))
        d4=str(current_datetime+datetime.timedelta(days=4))
        d5=str(current_datetime+datetime.timedelta(days=5))
        d6=str(current_datetime+datetime.timedelta(days=6))
        d7=str(current_datetime+datetime.timedelta(days=7))

        date_list=[d1,d2,d3,d4,d5,d6,d7]

        # Updating Dates of specific Days column in 'schedule' table
        for date in date_list:
            day=(date_list.index(date)+1)
            cur.execute("UPDATE schedule SET Date='{}' WHERE Day={}".format(date,day))

        #-------GUI window--------------#
        main_win=tkinter.Tk()
        main_win.title("Welcome")
        main_win.iconphoto(True,tkinter.PhotoImage(file='Project Setup\Images\locomotive.png'))
        main_win.resizable(False,False)
        main_win.geometry("500x220")

        h_frame = tkinter.Frame(main_win,relief="ridge",bd=10,bg="white")
        h_frame.grid(row = 0,column = 0,pady = 10)
        h = tkinter.Label(h_frame,text = "Railway Reservation System",font = ("Maiandra GD",30),bg = "White")
        h.grid()

        rail_img = tkinter.PhotoImage(file = "Project Setup/Images/locomotive_b.png")

        #---Variables for storing Signup details------#
        user_create_mobile=tkinter.StringVar()
        user_create_email=tkinter.StringVar()
        user_create_username=tkinter.StringVar()
        user_create_password=tkinter.StringVar()
        user_create_firstname=tkinter.StringVar()
        user_create_lastname=tkinter.StringVar()
        user_create_dob=tkinter.StringVar()
        #----------------------Images-----------------------#
        #Adding Images for buttons
        book_img = tkinter.PhotoImage(file = "Project Setup/Images/book_icon_b.png")
        cancel_img = tkinter.PhotoImage(file = "Project Setup/Images/delete_icon_b.png")
        show_img = tkinter.PhotoImage(file = "Project Setup/Images/show_icon_b.png")
        #----------------Variables for storing Search details------------------#
        from_station=tkinter.StringVar()
        from_station.set("Select a Station")

        to_station=tkinter.StringVar()
        to_station.set("Select a Station")

        current_user=tkinter.StringVar()
        current_user_password=tkinter.StringVar()
        current_user_email=tkinter.StringVar()
        current_user_wallet=tkinter.IntVar()
        current_user_name=tkinter.StringVar()
        current_reservation_date=tkinter.StringVar()
        current_reservation_day=tkinter.StringVar()
        current_class=tkinter.StringVar()
        #-------------Variables for storing cancel details--------#
        cancel_reservation_date=tkinter.StringVar()
        cancel_class=tkinter.StringVar()
        cancel_t_seats=tkinter.IntVar()
        cancel_t_name=tkinter.StringVar()        
        #-----------Login page--------#
        def login_page():
            # Construction of login Page
            main_win.geometry("300x220")
            main_win.title("Login")

            #-------------------Heading Frame----------------------#
            h_frame=tkinter.Frame(main_win,relief="ridge",bd=10,bg="white")
            h_frame.grid(row=0,column=0,columnspan=2)
            h=tkinter.Label(h_frame,text="Login",font=("Maiandra GD",20),bg="white")
            h.grid(padx=100,pady=2)
            #-----------------Data Frame------------------------------#
            frame2=tkinter.Frame(main_win)
            frame2.grid(row=1,column=0,pady=20)

            u_label=tkinter.Label(frame2,text="Username : ")
            u_label.grid(row=0,column=0,padx=5,pady=10)
            login_page.u_entry=tkinter.Entry(frame2,width=20,justify="center")
            login_page.u_entry.focus()
            login_page.u_entry.grid(row=0,column=1,padx=5,pady=5)

            pswd_label=tkinter.Label(frame2,text="Password : ")
            pswd_label.grid(row=1,column=0)
            login_page.pswd_entry=tkinter.Entry(frame2,width=20,justify="center",show="*")
            login_page.pswd_entry.grid(row=1,column=1,padx=5,pady=5)
            #--------------Button Frame------------------------------------#
            frame3=tkinter.Frame(main_win)
            frame3.grid(row=2,column=0)

            def check_and_continue():#  This button will check if the user exists or not
                cur.execute("SELECT Username,Password FROM users")
                data_retrieved=cur.fetchall()#storing username and password from database
                
                username_entered=login_page.u_entry.get()#username entered in entry box
                password_entered=login_page.pswd_entry.get()#password entered in entry box            

                if username_entered=="" or password_entered=="":
                    messagebox.showerror("No Data Entered","Please fill all the fields!")
                else:
                    if (username_entered,password_entered) in data_retrieved:
                        messagebox.showinfo("Success","You have Logged In Successfully.")
                        global user_t
                        cur.execute("SELECT User_Type FROM users WHERE Username = '{}' AND Password = '{}' ".format(username_entered,password_entered))
                        user_t = cur.fetchall()                   
                        cur.execute("SELECT F_name,L_name,Email FROM users WHERE Username='{}'".format(username_entered))
                        f_l_email_wallet=cur.fetchall()
                        
                        f_name=f_l_email_wallet[0][0]
                        l_name=f_l_email_wallet[0][1]
                        name=f_name+" "+l_name
                        email=f_l_email_wallet[0][2]
                                                
                        current_user_name.set(name)
                        current_user.set(username_entered)
                        current_user_password.set(password_entered)
                        current_user_email.set(email)
                        
                        login_page.u_entry.config(state="disabled")
                        login_page.pswd_entry.config(state="disabled")
                        login_page.con.config(state="disabled")
                        login_page.c_account.config(state="disabled")         
                        loginMenu()                        
                    else:
                        messagebox.showerror("User not found","Username or Password is wrong")

            login_page.con=tkinter.Button(frame3,text="Continue",bd=3,command=check_and_continue)
            login_page.con.grid(row=0,column=0,padx=25,pady=10)
            # After clicking on this button check and continue function runs

            login_page.c_account=tkinter.Button(frame3,text="Create Account",bd=3,command=sign_up_page)
            login_page.c_account.grid(row=0,column=1,padx=25)
            # If user wants to create an account sign up button will bring him to sign up page

        def sign_up_page():            
            sign_up_win=tkinter.Toplevel(main_win)
            sign_up_win.geometry("410x500")
            sign_up_win.resizable(False,False)
            sign_up_win.title("Create Account")
            sign_up_win.grab_set()            

            #-----------Heading Frame------------------#
            h_frame=tkinter.Frame(sign_up_win,relief="ridge",bd=10)
            h_frame.grid(row=0,column=0)
            h=tkinter.Label(h_frame,text="Create Account",font=("Book Antiqua",20),bg="white")
            h.grid(padx=100,pady=2)
            #--------------Details Frame----------------------#
            details_frame=tkinter.Frame(sign_up_win)
            details_frame.grid(row=1,column=0)

            mobile_no_l=tkinter.Label(details_frame,text="Mobile Number : ")      
            mobile_no_l.grid(row=0,column=0,padx=5,pady=10)
            user_create_mobile.set("")
            mobile_no_e=tkinter.Entry(details_frame,width=20,justify="center",textvariable=user_create_mobile)
            mobile_no_e.config(state="normal")
            mobile_no_e.grid(row=0,column=1)

            email_l=tkinter.Label(details_frame,text="Email Address : ")
            email_l.grid(row=1,column=0,padx=5,pady=10,sticky='w')
            user_create_email.set("")
            email_e=tkinter.Entry(details_frame,width=20,justify="center",textvariable=user_create_email)
            email_e.config(state="normal")
            email_e.grid(row=1,column=1)

            def check_database():
                cur.execute("SELECT Mobile_no FROM users")
                database_mobile=cur.fetchall()

                cur.execute("SELECT Email FROM users")
                database_email=cur.fetchall()

                mobile_no=user_create_mobile.get()
                email=user_create_email.get()

                if mobile_no=="" or email=="":
                    messagebox.showerror("Empty box","Please fill all the fields")
                elif mobile_no.isdigit()==False or len(mobile_no)!=10 or mobile_no[0] not in ["9","8","7","6"]:
                    messagebox.showerror("Invalid Mobile Number","Please enter a valid mobile number")
                else:
                    if ((mobile_no,) in database_mobile) or ((email,) in database_email):
                        messagebox.showerror("Existing User","User with same Mobile Number or Email already has an account")
                    else:
                        mobile_no_e.config(state="disabled")
                        email_e.config(state="disabled")
                        username_e.config(state="normal")
                        password_e.config(state="normal")
                        first_name_e.config(state="normal")
                        last_name_e.config(state="normal")
                        choose.config(state="normal")
                        submit.config(state="normal")
            
            check=tkinter.Button(details_frame,text="Check",command=check_database)
            check.grid(row=1,column=2,padx=10)

            username_l=tkinter.Label(details_frame,text="Username : ")
            username_l.grid(row=2,column=0,padx=5,pady=10,sticky='w')
            user_create_username.set("")
            username_e=tkinter.Entry(details_frame,width=20,justify="center",textvariable=user_create_username)
            username_e.config(state="disabled")
            username_e.grid(row=2,column=1)

            password_l=tkinter.Label(details_frame,text="Password : ")
            password_l.grid(row=3,column=0,padx=5,pady=10,sticky='w')
            user_create_password.set("")
            password_e=tkinter.Entry(details_frame,width=20,justify="center",textvariable=user_create_password)
            password_e.config(state="disabled")
            password_e.grid(row=3,column=1)

            first_name_l=tkinter.Label(details_frame,text="First Name : ")
            first_name_l.grid(row=4,column=0,padx=5,pady=10,sticky='w')
            user_create_firstname.set("")
            first_name_e=tkinter.Entry(details_frame,width=20,justify="center",textvariable=user_create_firstname)
            first_name_e.config(state="disabled")
            first_name_e.grid(row=4,column=1)

            last_name_l=tkinter.Label(details_frame,text="Last Name : ")
            last_name_l.grid(row=5,column=0,padx=5,pady=10,sticky='w')
            user_create_lastname.set("")
            last_name_e=tkinter.Entry(details_frame,width=20,justify="center",textvariable=user_create_lastname)
            last_name_e.config(state="disabled")
            last_name_e.grid(row=5,column=1)

            dob_l=tkinter.Label(details_frame,text="Date Of Birth : ")
            dob_l.grid(row=6,column=0,padx=5,pady=10,sticky='w',columnspan=2)

            date_l=tkinter.Label(details_frame)
            date_l.grid(row=6,column=1,padx=5,pady=10)
            user_create_dob.set("")          

            def choose_date():
                date_picker=tkinter.Toplevel(sign_up_win)
                date_picker.resizable(False,False)
                date_picker.title("Date Picker")
                date_picker.grab_set()
                dob_e=tkcalendar.Calendar(date_picker,selectmode='day',year=2000,month=1,day=1)                
                dob_e.pack()

                def picked():
                    date_l.config(text=dob_e.get_date())
                    user_create_dob.set(dob_e.get_date())                    
                    date_picker.destroy()
                
                ok=tkinter.Button(date_picker,text="OK",bd=5,command=picked)
                ok.pack(pady=10)           
            
            choose=tkinter.Button(details_frame,text="Choose Date",command=choose_date)
            choose.config(state="disabled")
            choose.grid(row=6,column=2)
            #------------frame for submit button----------------#
            b_frame=tkinter.Frame(sign_up_win)
            b_frame.grid(row=2,column=0)

            def submit_details():
                m=user_create_mobile.get()
                e=user_create_email.get()
                u=user_create_username.get()
                p=user_create_password.get()
                f_n=user_create_firstname.get()
                l_n=user_create_lastname.get()
                dob=user_create_dob.get()
                
                if u and p and f_n and l_n and dob:
                    cur.execute("SELECT Username FROM users WHERE Username='{}'".format(u))
                    data=cur.fetchall()
                    if data!=[]:
                        messagebox.showerror("Username exists","This Username already Exists!")
                    else:
                        cur.execute("SELECT F_name FROM users WHERE F_name='{}'".format(f_n))
                        data=cur.fetchall()
                        if data!=[]:
                            messagebox.showerror("Account Exists","You already have an account please try to login")
                        else:
                            if f_n.isalpha() and l_n.isalpha() and u.isspace()==False:
                                cur.execute("INSERT INTO users(Username,F_name,L_name,Mobile_no,Email,Password,DOB) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(u,f_n,l_n,m,e,p,dob))
                                messagebox.showinfo("Registered","Your account has been created successfully and now you can Login")
                                sign_up_win.destroy()                            
                            else:
                                messagebox.showerror("Invalid Character","All the fields must contain their respective characters only!")
                else:
                    messagebox.showerror("Data Entry","Please fill all the fields!!")

            submit=tkinter.Button(b_frame,text="SUBMIT",width=30,bd=6,font=30,command=submit_details)
            submit.config(state="disabled")
            submit.grid(row=0,column=0,padx=10,pady=30)

            def back():
                sign_up_win.destroy()

            back_b=tkinter.Button(b_frame,text="<--- Go Back to Login",bd=6,command=back)
            back_b.grid(row=1,column=0,sticky='w')

        def loginMenu():
            global menu_win
            menu_win = tkinter.Toplevel(main_win)
            menu_win.grab_set()
            menu_win.title("Menu")
            menu_win.resizable(False,False)
            menu_win.geometry("450x200")
            #---------------- 

            if user_t == [('Admin',)]:
                
                def reset():
                    q=messagebox.askyesno("Confirm Reset","Do you really want to reset the Data?")
                    if q==True:
                        messagebox.showwarning("WARNING","Do not Perform any actions while we reset the data")
                        progress_win=tkinter.Toplevel(menu_win)
                        progress_win.title("Reset Data")
                        progress_win.resizable(False,False)
                        progress_win.grab_set() 
                                                
                        def reset_data():                            
                            
                            l1.config(text="Deleting all Bookings")
                            progress_win.update_idletasks()
                            time.sleep(3)                  
                            cur.execute("DELETE FROM booking")
                            
                            for i in range(1,8):
                                day="day{}".format(i)                                
                                l1.config(text="Resetting Seats available on "+day)
                                bar['value']+=14
                                progress_win.update_idletasks()                                
                                
                                for j in range(1,7):
                                    cur.execute("SELECT Train_name,1AC,2AC,3AC,2S,SL,CC FROM trains WHERE Train_no={}".format(j))
                                    data=cur.fetchall()                                    
                                    
                                    t_name=data[0][0]
                                    _1ac=data[0][1]
                                    _2ac=data[0][2]
                                    _3ac=data[0][3]
                                    _2s=data[0][4]
                                    _sl=data[0][5]
                                    _cc=data[0][6]                            

                                    cur.execute("UPDATE {} SET {}={} WHERE Class='1AC'".format(day,t_name,_1ac))
                                    cur.execute("UPDATE {} SET {}={} WHERE Class='2AC'".format(day,t_name,_2ac))
                                    cur.execute("UPDATE {} SET {}={} WHERE Class='3AC'".format(day,t_name,_3ac))
                                    cur.execute("UPDATE {} SET {}={} WHERE Class='2S'".format(day,t_name,_2s))
                                    cur.execute("UPDATE {} SET {}={} WHERE Class='SL'".format(day,t_name,_sl))
                                    cur.execute("UPDATE {} SET {}={} WHERE Class='CC'".format(day,t_name,_cc))
                            progress_win.destroy()
                            messagebox.showinfo("Reset Complete","The Data has been successfully Reset")
                            

                        l1=tkinter.Label(progress_win,text="",background="white")
                        l1.pack(pady=15)

                        l2=tkinter.Label(progress_win,text="WARNING : Do not perform any Actions!\nPlease Wait...",background="white",foreground="red")
                        l2.pack(pady=10)

                        bar=ttk.Progressbar(progress_win,length=300,orient="horizontal",mode='determinate')
                        bar.pack(pady=20,padx=20)

                        progress_win.update_idletasks()
                        
                        reset_data()
                
                reset_b = tkinter.Button(menu_win,text = "RESET",bd = 4,width = 10,command=reset)
                reset_b.grid(row = 2 ,column=2)

            #Seacrching/Booking Train
            search_l = tkinter.Label(menu_win,text="Book\nTicket",font = ("Consolas",13))
            search_l.grid(row = 1,column=0,sticky="n")
            search=tkinter.Button(menu_win,image = book_img,bd=5,font=("Consolas",12),height = 90,width=100,command=book_train,borderwidth=0)
            search.grid(row =0,column = 0,pady=5,padx = 20) 

            #Cancelling Train
            cancel_l = tkinter.Label(menu_win,text="Cancel\nTicket",font = ("Consolas",13))
            cancel_l.grid(row = 1,column=1,sticky="n")
            cancel=tkinter.Button(menu_win,bd=5,image = cancel_img,font=("Consolas",12),height = 90,width=100,command=cancel_page,borderwidth=0)
            cancel.grid(row =0,column = 1,pady=5,padx = 20,) 

            #Showing Ticket
            show_l = tkinter.Label(menu_win,text="Show\nTicket",font = ("Consolas",13))
            show_l.grid(row = 1,column=2,sticky="n")
            show=tkinter.Button(menu_win,image = show_img,bd=5,font=("Consolas",12),height = 90,width=100,command=show_bookings,borderwidth=0)
            show.grid(row =0,column = 2,pady=5,padx = 20)    

            #Wallet
            wallet_b  = tkinter.Button(menu_win,text = "Wallet",font = ("Consolas",12),bd = 6,width = 15,command = wallet)
            wallet_b.grid(row = 2,column= 1)             
            
            def logout():                
                menu_win.destroy()
                
                login_page.u_entry.config(state='normal')
                login_page.u_entry.delete(0,END)
                login_page.pswd_entry.config(state="normal")
                login_page.pswd_entry.delete(0,END)
                login_page.con.config(state="normal")
                login_page.c_account.config(state="normal")
                
            #Log Out Button
            log_out = tkinter.Button(menu_win,text = "Log Out",bd = 4,font = ("Consolas",8),width = 12,command=logout)
            log_out.grid(row = 2, column = 0,pady = 10)
        
        def book_train():
            
            booking_win=tkinter.Toplevel(menu_win)
            booking_win.resizable(False,False)
            booking_win.title("Search Train")
            booking_win.grab_set()            
            
            #-------------------Heading Frame----------------------#
            h_frame=tkinter.Frame(booking_win,relief="ridge",bd=10,bg="white")
            h_frame.grid(row=0,column=0)
            h=tkinter.Label(h_frame,text="SEARCH TRAIN",font=("Maiandra GD",20),bg="white")
            h.grid(padx=142,pady=2)
            # ------------------data Frame----------------------------#
            d_frame=tkinter.Frame(booking_win)
            d_frame.grid(row=1,column=0)

            from_l=tkinter.Label(d_frame,text="From : ",font=("Consolas",15))
            from_l.grid(row=0,column=0,padx=10,pady=10)
            l=["Bhopal - BPL","Jhansi - JHS","Agra Cantt - AGC","New Delhi - NDLS"]
            from_e=tkinter.OptionMenu(d_frame,from_station,*l)
            from_e.grid(row=0,column=1)

            to_l=tkinter.Label(d_frame,text="To : ",font=("Consolas",15))
            to_l.grid(row=1,column=0,padx=10,pady=10)    
            to_e=tkinter.OptionMenu(d_frame,to_station,*l)
            to_e.grid(row=1,column=1)

            def search():
                start=from_station.get()
                end=to_station.get()        
                
                if start=="Select a Station" or end=="Select a Station":
                    messagebox.showerror("No Station","No Station Selected")
                elif start==end:
                    messagebox.showerror("Same Station","Start and End Stations must be different")        
                else:
                    h_frame.destroy()
                    d_frame.destroy()
                    search_b.destroy()
                    show_trains()
            
            def show_trains():
                start=from_station.get()
                end=to_station.get()
                r1=start.split("-")[1]                
                r2=end.split("-")[1]
                
                route1=start+"_"+end
                route2=end+"_"+start    

                cur.execute("SELECT Train_no,Train_name,Timing FROM trains WHERE Route='{}' OR Route='{}'".format(route1,route2))
                train_no_train_name_train_timing=cur.fetchall()
                train_no=train_no_train_name_train_timing[0][0]
                train_name=train_no_train_name_train_timing[0][1]
                train_timing=train_no_train_name_train_timing[0][2]
                
                cur.execute("SELECT Day,Date FROM schedule WHERE {} = '{}' OR '{}'".format(train_name,route1,route2))
                day_date=cur.fetchall()                

                day1=day_date[0][0]
                date1=day_date[0][1]
                day2=day_date[1][0]
                date2=day_date[1][1]

                cur.execute("SELECT {} FROM day{}".format(train_name,day1))
                class_data=cur.fetchall() 
               
                d1_1ac=class_data[0][0]
                d1_2ac=class_data[1][0]
                d1_2s=class_data[2][0]
                d1_3ac=class_data[3][0]
                d1_cc=class_data[4][0]
                d1_sl=class_data[5][0]

                cur.execute("SELECT {} FROM day{}".format(train_name,day2))
                class_data=cur.fetchall()
                
                d2_1ac=class_data[0][0]
                d2_2ac=class_data[1][0]
                d2_2s=class_data[2][0]
                d2_3ac=class_data[3][0]
                d2_cc=class_data[4][0]
                d2_sl=class_data[5][0]
                
                f1=tkinter.Frame(booking_win)
                f1.grid(row=0,column=0,columnspan=2,pady=10,padx=30)

                l1=tkinter.Label(f1,text="{} ({})".format(train_name,train_no),font=("Bookman Old Style",25),fg="blue")
                l1.grid(row=0,column=0,sticky='w')
                l2=tkinter.Label(f1,text="{}".format(r1+" --->"+r2),font=("Consolas",20))
                l2.grid(row=1,column=0,columnspan=2,pady=5)
                l3=tkinter.Label(f1,text="Timing : {}".format(train_timing),font=10)
                l3.grid(row=2,column=0,sticky='w',pady=5)

                #seperator
                s=ttk.Separator(booking_win,orient="horizontal")
                s.grid(row=1,column=0,sticky="ew",pady=5,columnspan=2)

                c_l=tkinter.Label(booking_win,text="The train has the following schedule for this route\nChoose the appropriate schedule for you",font=("Maiandra GD",20))
                c_l.grid(row=2,column=0)

                f2=tkinter.Frame(booking_win)
                f2.grid(row=3,column=0,columnspan=2)

                def s1_b():
                    current_reservation_day.set(day1)
                    current_reservation_date.set(date1)
                    c_l.destroy()
                    f2.destroy()
                    b.destroy()

                    date_l=tkinter.Label(booking_win,text="Date\n{}".format(date1),font=("Maiandra GD",20))
                    date_l.grid(row=2,column=0,pady=10,columnspan=2)

                    seat_frame=tkinter.Frame(booking_win,relief="groove",bd=10)
                    seat_frame.grid(row=3,column=0,padx=300)
                    
                    if d1_1ac!=0:
                        r1=tkinter.Radiobutton(seat_frame,text="1 AC - \u20B9 1500 per seat",variable=current_class,value="1AC",font=10)
                        r1.grid(sticky='w')
                        r1.select()           
                    
                    if d1_2ac!=0:
                        r2=tkinter.Radiobutton(seat_frame,text="2 AC - \u20B9 1000 per seat",variable=current_class,value="2AC",font=10)
                        r2.grid(sticky='w')
                        r2.select()
                    
                    if d1_3ac!=0:
                        r3=tkinter.Radiobutton(seat_frame,text="3 AC - \u20B9 800 per seat",variable=current_class,value="3AC",font=10)
                        r3.grid(sticky='w')
                        r3.select()
                    
                    if d1_sl!=0:
                        r4=tkinter.Radiobutton(seat_frame,text="SL    - \u20B9 600 per seat",variable=current_class,value="SL",font=10)
                        r4.grid(sticky='w')
                        r4.select()
                    
                    if d1_2s!=0:
                        r5=tkinter.Radiobutton(seat_frame,text="2S    - \u20B9 500 per seat",variable=current_class,value="2S",font=10)
                        r5.grid(sticky='w')
                        r5.select()
                    
                    if d1_cc!=0:
                        r6=tkinter.Radiobutton(seat_frame,text="CC    - \u20B9 900 per seat",variable=current_class,value="CC",font=10)
                        r6.grid(sticky='w')
                        r6.select()

                    book=tkinter.Button(seat_frame,text="Book",command=verify)
                    book.grid(row=3,column=1,padx=10)

                    def another_schedule():
                        date_l.destroy()
                        seat_frame.destroy()
                        another_s.destroy()
                        show_trains()
                    another_s=tkinter.Button(booking_win,text="<-- Choose another date",command=another_schedule)
                    another_s.grid(pady=20)                  
                    
                s1=tkinter.Button(f2,font=15,bd=8,width=30,text="Date : {}\n\n1AC : {}\t\t\tSL : {}\n\n2AC : {}\t\t\t2S : {}\n\n3AC : {}\t\t\tCC : {}".format(date1,d1_1ac,d1_sl,d1_2ac,d1_2s,d1_3ac,d1_cc),command=s1_b)
                if d1_1ac==d1_2ac==d1_3ac==d1_sl==d1_2s==d1_cc==0:
                    s1.config(state='disabled')
                s1.grid(pady=10) 

                def s2_b():
                    current_reservation_day.set(day2)
                    current_reservation_date.set(date2)
                    c_l.destroy()
                    f2.destroy()
                    b.destroy()

                    date_l=tkinter.Label(booking_win,text="Date\n{}".format(date2),font=("Maiandra GD",20))
                    date_l.grid(row=2,column=0,pady=10,columnspan=2)

                    seat_frame=tkinter.Frame(booking_win,relief="groove",bd=10)
                    seat_frame.grid(row=3,column=0,padx=300)
                    
                    if d2_1ac!=0:
                        r1=tkinter.Radiobutton(seat_frame,text="1 AC - \u20B9 1500 per seat",variable=current_class,value="1AC",font=10)
                        r1.grid(sticky='w')
                        r1.select()           
                    
                    if d2_2ac!=0:
                        r2=tkinter.Radiobutton(seat_frame,text="2 AC - \u20B9 1000 per seat",variable=current_class,value="2AC",font=10)
                        r2.grid(sticky='w')
                        r2.select()
                    
                    if d2_3ac!=0:
                        r3=tkinter.Radiobutton(seat_frame,text="3 AC - \u20B9 800 per seat",variable=current_class,value="3AC",font=10)
                        r3.grid(sticky='w')
                        r3.select()
                    
                    if d2_sl!=0:
                        r4=tkinter.Radiobutton(seat_frame,text="SL     - \u20B9 600 per seat",variable=current_class,value="SL",font=10)
                        r4.grid(sticky='w')
                        r4.select()
                    
                    if d2_2s!=0:
                        r5=tkinter.Radiobutton(seat_frame,text="2S    - \u20B9 500 per seat",variable=current_class,value="2S",font=10)
                        r5.grid(sticky='w')
                        r5.select()
                    
                    if d2_cc!=0:
                        r6=tkinter.Radiobutton(seat_frame,text="CC    - \u20B9 900 per seat",variable=current_class,value="CC",font=10)
                        r6.grid(sticky='w')
                        r6.select()

                    book=tkinter.Button(seat_frame,text="Book",command=verify)
                    book.grid(row=3,column=1,padx=10)   

                    def another_schedule():
                        date_l.destroy()
                        seat_frame.destroy()
                        another_s.destroy()
                        show_trains()
                    another_s=tkinter.Button(booking_win,text="<-- Choose another date",command=another_schedule)
                    another_s.grid(pady=20)      
                                
                s2=tkinter.Button(f2,font=15,bd=8,width=30,text="Date  : {}\n\n1AC : {}\t\t\tSL : {}\n\n2AC : {}\t\t\t2S : {}\n\n3AC : {}\t\t\tCC : {}".format(date2,d2_1ac,d2_sl,d2_2ac,d2_2s,d2_3ac,d2_cc),command=s2_b)
                if d2_1ac==d2_2ac==d2_3ac==d2_sl==d2_2s==d2_cc==0:
                    s2.config(state="disabled")
                s2.grid(pady=10) 

                def book(money):
                        c_user=current_user_name.get()
                        c_day=current_reservation_day.get()
                        c_date=current_reservation_date.get()   
                        start_st=route1.split("_")[0]
                        end_st=route1.split("_")[1]

                        c_class=current_class.get()

                        cur.execute("SELECT * FROM booking")
                        table_empty=cur.fetchall()
                        
                        if table_empty==[]:
                            cur.execute("INSERT INTO booking(PNR_no,Username,Journey_date,Start_Station,End_Station,Train_no,Train_name,Class,Seats,Price) VALUES(1560684294,'{}','{}','{}','{}',{},'{}','{}',{},{})".format(c_user,c_date,start_st,end_st,train_no,train_name,c_class,seats,money))
                        else:
                            cur.execute("INSERT INTO booking(Username,Journey_date,Start_Station,End_Station,Train_no,Train_name,Class,Seats,Price) VALUES('{}','{}','{}','{}',{},'{}','{}',{},{})".format(c_user,c_date,start_st,end_st,train_no,train_name,c_class,seats,money))
                        cur.execute("UPDATE day{} SET {}={}-{} WHERE Class='{}'".format(c_day,train_name,train_name,seats,c_class))
                        messagebox.showinfo("Confirmed Booking","Your Seat has been Reserved Successfully\n\nHappy Journey")
                        saveFile()

                def verify():
                    verify_win=tkinter.Toplevel(booking_win)
                    verify_win.title("Verification")
                    verify_win.geometry("416x190")
                    verify_win.resizable(False,False)
                    verify_win.grab_set()

                    seat_wallet_frame=tkinter.Frame(verify_win,borderwidth=5,relief="groove")
                    seat_wallet_frame.grid(row=0,column=0,columnspan=2)                    

                    cur.execute("SELECT Price FROM seat_price WHERE Class='{}'".format(current_class.get()))
                    seat_price=cur.fetchall()[0][0]                    
                    
                    seat_type_price=tkinter.Label(seat_wallet_frame,text="Class : {}\nRate : {}".format(current_class.get(),seat_price),font=("Maindra GD",20),foreground="blue")
                    seat_type_price.grid(row=0,column=0,padx=20)
                    
                    cur.execute("SELECT Wallet FROM users WHERE Username='{}'".format(current_user.get()))
                    wallet_money=cur.fetchall()[0][0]
                    
                    wallet_l=tkinter.Label(seat_wallet_frame,text="Wallet Money\n\u20B9 {}".format(wallet_money),font=("Maiandra GD",20),foreground="blue")
                    wallet_l.grid(row=0,column=1,padx=20)

                    no_passengers_l=tkinter.Label(verify_win,text="Number of Passengers : ",font=20)
                    no_passengers_l.grid(row=1,column=0,pady=20)

                    no_passengers_e=tkinter.Entry(verify_win)
                    no_passengers_e.grid(row=1,column=1)

                    b_frame=tkinter.Frame(verify_win)
                    b_frame.grid(row=2,column=0,columnspan=2)

                    def check():
                        global seats
                        seats=no_passengers_e.get() 
                        verify_win.geometry("416x212")                       

                        if seats!="" and seats.isdigit():                            
                            seats=int(seats)
                            cur.execute("SELECT {} FROM day{} WHERE Class='{}'".format(train_name,current_reservation_day.get(),current_class.get()))
                            avai_seats=cur.fetchall()[0][0]
                            
                            if seats>avai_seats:
                                messagebox.showerror("Seats Unavailable","There are only {} seats available".format(avai_seats))
                            else:
                                no_passengers_l.destroy()
                                no_passengers_e.destroy()
                                b_frame.destroy()
                                new_frame=tkinter.Frame(verify_win)
                                new_frame.grid(row=1,column=0,pady=20)

                                passenger_l=tkinter.Label(seat_wallet_frame,text="Passengers : {}".format(seats),font=20)
                                passenger_l.grid(row=1,column=0,sticky="w",padx=20)

                                t_fare_l=tkinter.Label(seat_wallet_frame,text="Total Fare : \u20B9 {}".format(seats*seat_price),font=20)
                                t_fare_l.grid(row=1,column=1,sticky="e",padx=20)

                                tkinter.Label(new_frame,text="Email : ",font=20).grid(row=0,column=0,sticky="w",pady=10)
                                tkinter.Label(new_frame,text="Password : ",font=20).grid(row=1,column=0,sticky="w")
                                email_e=tkinter.Entry(new_frame)
                                email_e.grid(row=0,column=1)
                                pswd_e=tkinter.Entry(new_frame,show="*")
                                pswd_e.grid(row=1,column=1)

                                def confirm_booking():
                                    if (email_e.get()!=current_user_email.get()) or (pswd_e.get()!=current_user_password.get()):
                                        messagebox.showerror("Incorrect","The Details Entered are Incorrect!\n\tPlease Check")
                                    elif wallet_money<(seats*seat_price):
                                        messagebox.showerror("Not Enough Money","You don't have enough money in your wallet\nPlease add the Money and try later")
                                    else:
                                        cur.execute("UPDATE users SET Wallet=Wallet-{} WHERE Email='{}'".format(seat_price*seats,email_e.get()))
                                        messagebox.showinfo("Money Deducted","\u20B9 {} has been deducted from your wallet".format(seat_price*seats))
                                        book(seats*seat_price)
                                        
                                        verify_win.destroy()
                                        booking_win.destroy()                                        

                                confirm=tkinter.Button(verify_win,text="Confirm Booking",command=confirm_booking)
                                confirm.grid(row=1,column=1)

                                verify_win.update_idletasks()               
                                
                        else:
                            messagebox.showerror("Value Error","No of Passengers must be a Number")

                    check_b=tkinter.Button(b_frame,text="Check Seats",command=check)
                    check_b.grid(pady=10)

                    verify_win.update_idletasks()                    

                def saveFile():
                    cur.execute("SELECT * FROM booking WHERE Username = '{}' AND Journey_date='{}'".format(current_user_name.get(),current_reservation_date.get()))
                    data = cur.fetchall()
                    
                    file_name = current_reservation_date.get()
                    file = open("tickets\\"+file_name+".txt","w")
                    with file:
                        pnr = str(data[-1][0])
                        username = data[-1][1]
                        doj = data[-1][2]
                        start_station = data[-1][3]   
                        end_station = data[-1][4]
                        train_no = str(data[-1][5])
                        train_name = data[-1][6] 
                        Class  = data[-1][7]
                        seats = str(data[-1][8])
                        price = str(data[-1][9])                                    
                        
                        header = ["PNR No. : "+pnr+"\n" ,"Username : "+username+"\n" ,"Date of Journey : "+doj+"\n" ,"Start Station : "+start_station+"\n" ,"End Station : "+end_station+"\n" ,"Train No. : "+train_no+"\n" ,"Train Name : "+train_name+"\n" ,"Class : "+Class+"\n" ,"No. of Seats : "+seats+"\n" ,"Total Price : "+price+"\n" ]
                        file.writelines(header)

                        messagebox.showinfo("File Saved","Ticket saved to File Successfully.\nSaved Data in "+file_name+".txt")

                def back():
                    booking_win.destroy()
                    book_train()
                b=tkinter.Button(booking_win,text="<----- Select another station",command=back)
                b.grid()
            search_b=tkinter.Button(booking_win,text="SEARCH",bd=5,font=("Consolas",10),width=10,command=search)
            search_b.grid(pady=20) 

        def cancel_page():

            cancel_win = tkinter.Toplevel(menu_win)
            cancel_win.geometry("400x230")
            cancel_win.resizable(False,False)
            cancel_win.title("Cancel Ticket")
            cancel_win.grab_set()

            username = current_user_name.get()

            def fetch(): 
                
                pnr = pnr_no.get()
                 
                if pnr.isdigit():
                     
                    cur.execute("SELECT * FROM booking WHERE Username = '{}' and PNR_no = {}".format(username,pnr))
                    data = cur.fetchall()             

                    if data != []:
                        cancel_win.geometry("400x470")
                        pnr_entry.config(state="disabled")
                        check_button.config(state="disabled")
                        cancel_button.config(state="normal")

                        u_name=data[0][1]
                        r_date=data[0][2]
                        global total_price
                        total_price = data[0][-1]
                        
                        cancel_reservation_date.set(r_date)
                        start_st=data[0][3]
                        end_st=data[0][4]
                        t_no=data[0][5]
                        t_name=data[0][6]
                        cancel_t_name.set(t_name)
                        seat_class=data[0][7]
                        cancel_class.set(seat_class)
                        t_seats=data[0][8]
                        cancel_t_seats.set(t_seats)
                        
                        l=tkinter.Label(ticket_detail_frame,text="Username : {}\n\nJourney Date : {}\n\nStart : {}\n\nEnd : {}\n\nTrain No. : {}\n\nTrain Name : {}\n\nClass : {}\n\nSeats : {}".format(u_name,r_date,start_st,end_st,t_no,t_name,seat_class,t_seats),font=15)
                        l.grid()                        
                    else:
                        messagebox.showerror("Invalid PNR","Ticket not Found.\nEnter Correct PNR Number.")
                else:
                    messagebox.showerror("Invalid PNR","PNR number should only contain digits")


            def cancelTicket():
                ans=messagebox.askquestion("Confirm Cancelling","Do you want to cancel the ticket?")
                if ans=="yes":
                    cur.execute("SELECT Day FROM schedule WHERE Date='{}'".format(cancel_reservation_date.get()))
                    day=cur.fetchall()[0][0]
                    
                    t_name=cancel_t_name.get()
                    c_class=cancel_class.get()
                    c_seat=cancel_t_seats.get()
        
                    reduced_price = (total_price*25)/100
                    final_price = total_price-reduced_price 
                    money_to_return=final_price
                    cur.execute("UPDATE day{} SET {} ={}+{} WHERE Class='{}'".format(day,t_name,t_name,c_seat,c_class))
                    cur.execute("DELETE FROM booking WHERE PNR_no={}".format(pnr_no.get()))
                    
                    messagebox.showinfo("Ticket cancelled","Ticket Cancelled Successfully")
                    
                    cur.execute("UPDATE users SET Wallet=Wallet+{} WHERE Username='{}'".format(money_to_return,current_user.get()))
                    messagebox.showinfo("Money Returned","\u20B9 {} has been returned to your Wallet".format(money_to_return))
                    cancel_win.destroy()
                else:
                    cancel_win.destroy()

            #-------------------------Heading Frame----------------------
            h_frame = tkinter.Frame(cancel_win,relief="ridge",bd=10,bg="white")    
            h_frame.grid(row = 0,column = 0,columnspan=3)
            h = tkinter.Label(h_frame,text = "Cancel Ticket",font = ("Maiandra GD",20),bg = "White")
            h.grid(padx = 110,pady = 2)

            pnr_label = tkinter.Label(cancel_win,text = "PNR No.",font = 11)
            pnr_label.grid(row = 1,column= 0,pady = 30)

            pnr_no = tkinter.StringVar()
            pnr_entry = tkinter.Entry(cancel_win,textvariable = pnr_no,bd = 4,width = 40)
            pnr_entry.grid(row=1,column=1,pady = 30)

            check_button = tkinter.Button(cancel_win,text = "Check",command = fetch )
            check_button.grid(row = 1 ,column = 2)

            ticket_detail_frame=tkinter.Frame(cancel_win)
            ticket_detail_frame.grid(row=2,column=1)

            cancel_button = tkinter.Button(cancel_win,text = "CANCEL TICKET",bd = 5,font = 15,state = "disabled",command=cancelTicket)
            cancel_button.grid(column=1,pady=5)

        def show_bookings():
            name = current_user_name.get()
            cur.execute("SELECT * FROM booking WHERE Username = '{}'".format(name))  
            data = cur.fetchall()

            if data != []:
                #Main Window
                show_win = tkinter.Toplevel(menu_win)
                show_win.geometry("1500x350")
                show_win.resizable(False,False)
                show_win.title("Show Ticket")
                show_win.grab_set()

                h_frame = tkinter.Frame(show_win,relief="ridge",bd=10,bg="white")    
                h_frame.grid(row = 0,column = 0,columnspan=8,pady = 10)
                h = tkinter.Label(h_frame,text = "Your Bookings",font = ("Maiandra GD",30),bg = "White")
                h.grid(padx = 503,pady = 15)

                table_f = tkinter.Frame(show_win)
                table_f.grid() 

                total_rows = len(data)
                total_columns = len(data[0])

                header = ["PNR No.","Passenger","Journey Date","Start Station","End Station","Train No.","Train Name","Class","Seats"]
                for i in range(1):
                    for j in range(9):
                        e = tkinter.Entry(table_f, width=15, fg='blue',font=('Arial',15,'bold'))
                        e.grid(row = i+1,column=j)
                        e.insert(0,header[j])
                        
                for i in range(total_rows):
                    for j in range(total_columns):  
                            e = tkinter.Entry(table_f, width=15, fg='blue',font=('Arial',15,'bold'))
                            e.grid(row=i+2, column=j)
                            e.insert(0,data[i][j])

                def back_to_menu():
                    show_win.destroy()
                back_b = tkinter.Button(show_win,text = "<---- Back To Menu Page",font = 15,command=back_to_menu)
                back_b.grid(pady=20)            
            else :
                messagebox.showinfo("No Tickets", "No Tickets Booked Till Now.")
        
        def wallet():
            username  = current_user.get()
            password = current_user_password.get()
            cur.execute("SELECT Wallet FROM users WHERE Username = '{}' AND Password = '{}'".format(username,password))
            data = cur.fetchall()
            current_money=data[0][0]
            
            #wallet Window
            wallet_win = tkinter.Toplevel(menu_win)
            wallet_win.grab_set()
            wallet_win.title("Wallet")
            wallet_win.resizable(False,False)
            wallet_win.geometry("350x170")
            
            current_l = tkinter.Label(wallet_win,text = "Current money in your wallet : ",font=("Consolas",15))
            current_l.grid(column=0,row=0)
        
            money_l = tkinter.Label(wallet_win,text = "\u20B9 "+str(current_money),font=("Consolas",17))
            money_l.grid(column=0,row=1)         

            #Add Money Function
            def add_money():
                l = tkinter.Label(wallet_win,text = "Enter the money you want to add :")
                l.grid(row=3,column=0)
                
                money_var=tkinter.StringVar()
                money_e = tkinter.Entry(wallet_win,bd = 3,textvariable=money_var)
                money_e.grid(row=4,column=0)
                                
                #Authentiacte Function 
                def authenticate():
                    money_to_add=money_var.get()
                    if money_to_add != "" and money_to_add.isdigit():
                        if  int(money_to_add)<=10000:
                            ad_money =  int(money_to_add)
                            #Authentication Window
                            authenticate_win = tkinter.Toplevel(wallet_win)
                            authenticate_win.grab_set()
                            authenticate_win.title("Verify")
                            authenticate_win.resizable(False,False)
                            authenticate_win.geometry("280x120")

                            cur.execute("SELECT Email,Password FROM users WHERE Username = '{}' AND Password = '{}'".format(username,password))
                            auth_data = cur.fetchall()

                            #Email_ID
                            email_id_l = tkinter.Label(authenticate_win,text = "Email-ID : ",font=("Consolas",15))
                            email_id_l.grid(row = 0,column=0)
                            email_id_e = tkinter.Entry(authenticate_win,bd = 5)
                            email_id_e.grid(row = 0,column=1)
                            
                            #Password 
                            pswd_l = tkinter.Label(authenticate_win,text = "Password : ",font=("Consolas",15))
                            pswd_l.grid(row = 1,column=0)
                            pswd_e = tkinter.Entry(authenticate_win,bd = 5,show="*")
                            pswd_e.grid(row = 1,column=1)

                            #Authententicate
                            def check() :
                                #Entered Email_id And Password 
                                email_id = email_id_e.get()
                                pswd = pswd_e.get()

                                #Real Email_ID and Password
                                cur_email_id = auth_data[0][0]
                                cur_pass = auth_data[0][1]

                                #Authenticating
                                if (email_id,pswd) == (cur_email_id,cur_pass):
                                    authenticate_win.destroy()
                                    wallet_win.focus()
                                    total_money = current_money + ad_money
                                    
                                    cur.execute("UPDATE users SET Wallet = {} WHERE (Email = '{}')".format(total_money,cur_email_id))
                                    messagebox.showinfo("Successfull","Authentication Succesfull.\nMoney Added Successfully.")
                                    wallet_win.destroy()
                                    
                                else:
                                    messagebox.showerror("Invalid","Invalid Email-ID and Password")
                            auth_f = tkinter.Frame(authenticate_win)
                            auth_f.grid(columnspan=2)

                            auth_b = tkinter.Button(auth_f,width = 20,text = "Verify",font=("Consolas",13),command = check,bd = 4)
                            auth_b.grid(pady = 20)                          
                    
                        else:
                            messagebox.showerror("Huge Amount","You can only add \u20B9 10,000 at a time")                    
                    else:
                        messagebox.showerror("Invalid Input","The Amount of Money you want to add must be a Number")
                
                add_b.config(command=authenticate)

            add_b = tkinter.Button(wallet_win,text = "Add Money",font=("Consolas"),command=add_money)
            add_b.grid(column=0,row=5)

        def next():
            h_frame.destroy()
            go.destroy()
            login_page()
        go = tkinter.Button(main_win,image=rail_img,font = 15,borderwidth= 5,command=next,width=160)
        go.grid()# After clicking on the Train(GO) button login page opens

        main_win.mainloop()
except:
    messagebox.showerror("Connection Lost","Sorry but we can't connect to the server at the moment\nPlease try Later....")
