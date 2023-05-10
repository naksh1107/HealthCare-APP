global select
global priv_pass
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image

message=''
def profile_view():
    
    # root canvas definition
    my_prof = Tk()
    my_prof.title("V-Care")
    my_prof.geometry('1000x700')
    

    # login interface
    Label(my_prof, text="My Profile", font=("Fixedsys", 57, "bold underline")).place(x=300, y=0)
    Label(my_prof, text="Sign in to continue", font=("Fixedsys", 30)).place(x=310, y=120)

    Label(my_prof, text = "username: ", font = ("Fixedsys", 30)).place(x = 130, y = 230)
    username = Entry(my_prof, width = 50, borderwidth = 5)
    username.place(x = 330, y = 245)
    Label(my_prof, text = "password: ", font = ("Fixedsys", 29)).place(x = 130, y = 320)
    password = Entry(my_prof, show = "*", width = 50, borderwidth = 5)
    password.place(x = 330, y = 335)

    def change_pass():
        ch_pass = Tk()
        ch_pass.title("Change password")
        ch_pass.geometry('400x500')

        Label(ch_pass, text = "Username: ", font = ("Fixedsys", 23)).place(x = 10, y = 10)
        ch_user = Entry(ch_pass, width = 30, borderwidth = 5)
        ch_user.place(x = 60, y = 70)
        Label(ch_pass, text = "Old password: ", font = ("Fixedsys", 23)).place(x = 10, y = 110)
        ch_old_pass = Entry(ch_pass, width = 30, borderwidth = 5)
        ch_old_pass.place(x = 60, y = 160)
        Label(ch_pass, text="New password: ", font=("Fixedsys", 23)).place(x=10, y=210)
        ch_new_pass = Entry(ch_pass, width = 30, borderwidth = 5)
        ch_new_pass.place(x = 60, y = 260)
        Label(ch_pass, text="Confirm new password: ", font=("Fixedsys", 23)).place(x=10, y=310)
        ch_confirm_new_pass = Entry(ch_pass, width = 30, borderwidth = 5)
        ch_confirm_new_pass.place(x = 60, y = 360)

        Button(ch_pass, text = "Exit window", borderwidth = 6, activebackground = "magenta", command = ch_pass.quit).place(x = 10, y = 430)

        # noinspection PyBroadException
        def submit():
            import mysql.connector as sqltor
            mycon = sqltor.connect(host="localhost", user="root", password="toor", database="v_care")
            cursor = mycon.cursor()

            try:
                check_str = "select username, password from sign_up where username = '{}'".format(ch_user.get())
                cursor.execute(check_str)
                data = cursor.fetchall()
                old_pass = data[0][1]

                check_str = "update sign_up set password = '{}' where username = '{}'".format(ch_new_pass.get(), ch_user.get())
                cursor.execute(check_str)
                mycon.commit()
                
                if ch_old_pass.get() != data[0][1]:
                    messagebox.showerror(title = 'Incorrect password', message = 'The old password which you have given for this email id is incorrect. Please try again')
                    
                elif ch_new_pass.get() != ch_confirm_new_pass.get():
                    messagebox.showerror(title = 'Passwords do not match', message = 'The two passwords do not match. Please try again')
                    
                elif ch_new_pass.get() == '' or ch_confirm_new_pass.get() == '':
                    messagebox.askretrycancel(title = 'Empty fields', message = 'PLease fill the passwords fields')
                    
                elif ch_new_pass.get() == ch_old_pass.get():
                    messagebox.showwarning(title = 'Same password', message = 'New password cannot be the same as old password')
                    
                else:
                    messagebox.showinfo("Password change successful", "Your password has been changed from {} to {}".format(old_pass, ch_new_pass.get()))

            except:
                messagebox.showerror("Invalid details", "The details you have provided are invalid")

            mycon.close()

        Button(ch_pass, text="change password", font=("Fixedsys", 15), borderwidth=6, command=submit).place(x=240, y=430)

    Button(my_prof, text = "change password", font = ("Fixedsys", 15), borderwidth = 6, command = change_pass).place(x = 520, y = 410)
    

    def forgot_passwd():
        frgt_pass = tkinter.Tk()
        frgt_pass.title("Forgot password")
        frgt_pass.geometry('500x500')

        Label(frgt_pass, text = "Enter your username: ", font = ("Fixedsys", 23)).place(x = 10, y = 20)
        check_user = Entry(frgt_pass, width = 40, borderwidth = 5)
        check_user.place(x = 15, y = 70)

        Label(frgt_pass, text = "Enter your phone number: ", font = ("Fixedsys", 23)).place(x = 10, y = 120)
        check_ph_no = Entry(frgt_pass, width = 40, borderwidth = 5)
        check_ph_no.place(x = 15, y = 170)

        Label(frgt_pass, text = "Enter your pincode: ", font = ("Fixedsys", 23)).place(x = 10, y = 220)
        check_pin_code = Entry(frgt_pass, width = 40, borderwidth = 5)
        check_pin_code.place(x = 15, y = 280)

        Label(frgt_pass, text = "Enter your retrieval username: ", font = ("Fixedsys", 23)).place(x = 10, y = 330)
        check_ret_user = Entry(frgt_pass, width = 40, borderwidth = 5)
        check_ret_user.place(x = 15, y = 390)

        Button(frgt_pass, height = 2, borderwidth = 7, text = "Exit window", activebackground = "magenta", command = frgt_pass.quit).place(x = 10, y = 440)

        def submit_frgt():
            import mysql.connector as sqltor
            mycon = sqltor.connect(host = "localhost", user = "root", password = "toor", database = "v_care")
            cursor = mycon.cursor()

            try:
                check_str = "select username, password, ph_no, pin_code, retrieval_email_id from sign_up where username = '{}'".format(check_user.get())
                cursor.execute(check_str)
                data = cursor.fetchall()
                
                if check_ph_no.get() != data[0][2]:
                    messagebox.showerror(title = 'Invalid phone number', message = 'The phone number which you have provided for this email is incorrect. Please try again')
                    
                elif check_pin_code.get() != data[0][3]:
                    messagebox.showerror(title = 'Invalid pin code', message = 'The pin code which you have provided for this email is incorect. Please try again')
                    
                elif check_ret_user.get() != data[0][4]:
                    messagebox.showerror(title = 'Invalid retrieval user id', message = 'The retrieval user id which you have provided for this email is incorrect. Please try again')
                
                else:
                    messagebox.showinfo("Password found!", "Your account password is {}".format(data[0][1]))

            except:
                messagebox.showerror("Invalid details", "The details that you have provided are invalid")

            mycon.close()

        Button(frgt_pass, width = 12, height = 2, borderwidth = 7, text = "Submit", command = submit_frgt).place(x = 390, y = 440)


    Button(my_prof, text = "Forgot password?", borderwidth = 6, font = ("Fixedsys", 15), command = forgot_passwd).place(x = 270, y = 410)

    # This pass will determine whether or not the user has privileges to access the user access services
    priv_pass = 0

    # button functions
    def clicked_next():
        # MySQL connection
        import mysql.connector as sqltor
        mycon = sqltor.connect(host = "localhost", user = "root", password = "toor", database = "v_care")
    
        cursor = mycon.cursor()

        check_str = "select password from sign_up where username = '{}';".format(username.get())
        cursor.execute(check_str)
        data = cursor.fetchall()

        try:
            if password.get() == data[0][0]:
                messagebox.showinfo("Connection successful", "You have successfully logged into your account")
                global priv_pass
                priv_pass = 1

            elif password.get() != data[0][0]:
                messagebox.showerror("Incorrect password", "The password you have entered is incorrect. Click on 'forgot password' to retrieve your password")

        except:
            messagebox.showerror("Incorrect user-id/password", "The username or password that you have given is invalid")
            from tkinter import END
            username.delete(0, END)
            password.delete(0, END)

        mycon.close()

    def clicked_sign_up():
        sign_up = Tk()
        sign_up.title("Create new profile")
        sign_up.geometry('700x700')

        note_bk = ttk.Notebook(sign_up)
        note_bk.place(x = 110, y = 0)

        frame_pers_details = Frame(note_bk, width = 500, height = 500)
        frame_user_details = Frame(note_bk, width = 500, height = 500)
        frame_medic_details = Frame(note_bk, width = 500, height = 500)

        frame_pers_details.place(x = 200, y = 0)
        frame_user_details.place(x = 200, y = 0)
        frame_medic_details.place(x = 200, y = 0)

        note_bk.add(frame_pers_details, text = "Personal details")
        note_bk.add(frame_user_details, text = "User details")
        note_bk.add(frame_medic_details, text = "Medical details")


        Button(sign_up, height = 2, width = 10, text = "Exit window", command = sign_up.quit, activebackground = "magenta", font = ("bold", 15), borderwidth = 5).place(x = 550, y = 630)


        # personal details
        Label(frame_pers_details, text = "First Name: ", font = ("Times New Roman", 22)).place(x = 20, y = 20)
        f_name = Entry(frame_pers_details, width = 44, borderwidth = 5)
        f_name.place(x = 180, y = 30)

        Label(frame_pers_details, text="Last Name: ", font=("Times New Roman", 22)).place(x = 19, y = 100)
        l_name = Entry(frame_pers_details, width = 44, borderwidth = 5)
        l_name.place(x = 180, y = 111)


        Label(frame_pers_details, text="Gender: ", font=("Times New Roman", 22)).place(x = 20, y = 180)
        choice = StringVar()
        OptionMenu(frame_pers_details, choice, "Male", "Female", "Others").place(x = 140, y = 186)
        choice.set(choice.get())

        Label(frame_pers_details, text = "Age: ", font=("Times New Roman", 22)).place(x = 250, y = 180)
        age = Entry(frame_pers_details, width = 21, borderwidth = 5)
        age.place(x = 315, y = 190)

        Label(frame_pers_details, text = "Phone Number: ", font=("Times New Roman", 22)).place(x = 20, y = 260)
        ph_no = Entry(frame_pers_details, width = 37, borderwidth = 5)
        ph_no.place(x = 220, y = 270)

        Label(frame_pers_details, text = "Address: ", font=("Times New Roman", 22)).place(x = 20, y = 345)
        add = Entry(frame_pers_details, width = 50, borderwidth = 5)
        add.place(x = 139, y = 355)

        Label(frame_pers_details, text = "Pin-Code: ", font=("Times New Roman", 22)).place(x = 20, y = 430)
        pin = Entry(frame_pers_details, width = 46, borderwidth = 5)
        pin.place(x = 160, y = 440)

        # user details
        Label(frame_user_details, text = "Username: ", font=("Times New Roman", 22)).place(x = 20, y = 20)
        user = Entry(frame_user_details, width = 44, borderwidth = 5)
        user.place(x = 180, y = 30)

        Label(frame_user_details, text = "Password: ", font=("Times New Roman", 22)).place(x = 20, y = 100)
        passwd = Entry(frame_user_details, width = 44, borderwidth = 5)
        passwd.place(x = 180, y = 108)

        Label(frame_user_details, text = "Confirm password: ", font=("Times New Roman", 22)).place(x = 20, y = 175)
        confirm_passwd = Entry(frame_user_details, width = 29, borderwidth = 5)
        confirm_passwd.place(x = 270, y = 183)

        Label(frame_user_details, text = "Retrieval username: ", font = ("Times New Roman", 22)).place(x = 20, y = 250)
        ret_email_id = Entry(frame_user_details, width = 30, borderwidth = 5)
        ret_email_id.place(x = 270, y = 260)

        # medical details
        Label(frame_medic_details, text = "Family doctor's name: ", font = ("Times New Roman", 22)).place(x = 20, y = 20)
        fam_doc_name = Entry(frame_medic_details, width = 31, borderwidth = 5)
        fam_doc_name.place(x = 290, y = 30)

       

        def yes_click():
            global select
            select = "YES"
            Button(frame_medic_details, height=2, width=6, borderwidth=3, bg = "light green", text="Yes", activebackground="green", command=yes_click).place(x = 20, y = 270)

        def no_click():
            global select
            select = "NO"
            Button(frame_medic_details, height=2, width=6, borderwidth=3, bg = "magenta", text="No", activebackground="red", command=no_click).place(x=200, y=270)

        Label(frame_medic_details, text = "Are you currently under medication? ", font = ("Times New Roman", 22)).place(x = 19, y = 210)
        Button(frame_medic_details, height = 2, width = 6, borderwidth = 3, text = "Yes", activebackground = "green", command = yes_click).place(x = 20, y = 270)
        Button(frame_medic_details, height = 2, width = 6, borderwidth = 3, text = "No", activebackground = "red", command = no_click).place(x = 200, y = 270)

        group = StringVar()
        Label(frame_medic_details, text = "Blood Group: ", font = ("Times New Roman", 22)).place(x = 19, y = 350)
        OptionMenu(frame_medic_details, group, "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-").place(x = 200, y = 355)
        choice.set(choice.get())

        Label(frame_medic_details, text = "Allergies: ", font = ("Times New Roman", 22)).place(x = 20, y = 440)
        allergy = Entry(frame_medic_details, width = 55, borderwidth = 5)
        allergy.place(x = 150, y = 450)

        # submit button
        def submit():
            # exception and error handling at front end

            for ch1 in f_name.get():
                if type(ch1) == type(1):
                    messagebox.showerror("Invalid name", "The first name which has been given is invalid")
            for ch2 in l_name.get():
                if type(ch2) == type(1):
                    messagebox.showerror("Invalid name", "The last name which has been given is invalid")
            try:
                int(age.get())
            except:
                messagebox.showerror("Invalid age", "The age which has been given is invalid")
            try:
                int(pin.get())
            except:
                messagebox.showerror("Invalid pincode", "The pincode which has been given is invalid")
            try:
                int(ph_no.get())
            except:
                messagebox.showerror("Invalid phone number", "The phone number which has been given is invalid")
            if len(ph_no.get()) != 10:
                messagebox.showerror("Invalid phone number", "The phone number which has been given is invalid")
            elif len(pin.get()) != 6:
                messagebox.showerror("Invalid pin code", "The pin code that has been given is invalid")

            elif passwd.get() != confirm_passwd.get():
                messagebox.showerror("Invalid password", "Passwords do not match")


            # MySQL connection to database
            import mysql.connector as sqltor
            mycon = sqltor.connect(host = "localhost", user = "root", password = "1269", database = "mydb")
            cursor = mycon.cursor()
            
            
            insert_str="select username from sign_up"
            cursor.execute(insert_str)
            val=cursor.fetchall()
            print(val)
            if tuple(user.get()) in val:
                messagebox.showerror("invalid username", "username already exists please choose another one")

            

            else:
                
            


                try:
                    insert_str = "insert into sign_up values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(f_name.get().upper(), l_name.get().upper(), user.get(),passwd.get(),choice.get().upper(), age.get(),ph_no.get(), add.get().upper(), pin.get(), ret_email_id.get(), fam_doc_name.get().upper(), group.get().upper())
                    cursor.execute(insert_str)
            
                    mycon.commit()

                except:
                    messagebox.showerror("Invalid details", "Some details have not been filled. Please fill all details and try again.")
                

                else:
                    messagebox.showinfo("Successful!", "Your account was created successfully!")

            mycon.close()

        Button(sign_up, text = "Submit", borderwidth = 5, font = ("Times New Roman", 20), activebackground = "light green", command = submit).place(x = 320, y = 550)


    # next button
    Button(my_prof, width = 10, height = 1, text = "Next", activebackground = "light blue", font = ("Times New Roman", 20), highlightcolor = "light blue", borderwidth = 7, command = clicked_next).place(x = 680, y = 500)


    # link to create_new_account
    Button(my_prof, height = 1, text = "Sign up", font = ("Times New Roman", 20), activebackground = "light green", borderwidth = 7, command = clicked_sign_up).place(x = 200, y = 500)

    # Exit window button
    

    
    my_prof.mainloop()

