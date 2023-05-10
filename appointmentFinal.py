from tkinter import *
import mysql.connector
import random
from tkinter import messagebox

def appointment():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1269",database="mydb")
    cursor=mydb.cursor()

    root = Tk()
    root.geometry('700x600')
    root.title('Book an Appointment')

    variable = StringVar(root)
    variable.set("10:00 - 10:30")

    Label(root, text = 'V-Care', font = ('FixedSys', 40)).place(x = 150, y = 20)


    with open('doctor_names.txt') as file:
        doctor_names = file.readline().split(',')
        doctor = random.choice(doctor_names)

    global username
    Label(root, text = 'User Name', font = ('FixedSys', 20)).place(x = 50, y = 100)
    username = Entry(root, width = 38, borderwidth = 7, relief = 'sunken')
    username.place(x = 210, y = 105)

    menu = OptionMenu(root, variable, "10:00 - 10:30", "10:30 - 11:00", "11:00 - 11:30", "17:30 - 18:00", "18:00 - 18:30")
    Label(root, text = 'Time', font = ('FixedSys', 20)).place(x = 50, y = 180)
    menu.place(x = 150, y = 180)

    def click():
        global username
    

        query = f"SELECT CONCAT(F_NAME, L_NAME), PHONE_NUMBER, AGE, GENDER FROM SIGN_UP WHERE USERNAME = '{username.get()}'"

        cursor.execute(query)

        result = cursor.fetchone()
        print(result)

    

    
    


        Label(root, text = f'Name : {result[0]}', font = ('FixedSys', 20)).place(x = 50, y = 250)

        Label(root, text = f'Phone Number : {result[1]}', font = ('FixedSys', 20)).place(x = 50, y = 320)
    
        Label(root, text = f'Age : {result[2]}', font = ('FixedSys', 20)).place(x = 50, y = 390)

        Label(root, text = f'Gender : {result[3]}', font = ('FixedSys', 20)).place(x = 50, y = 460)

        mydb.close()

        Label(root, text =f"Your appointment has been confirmed\nwith '{doctor}'",font = ('FixedSys', 20),fg="red").place(x = 50, y = 530)

    Button(root, text = 'Submit', font = ('FixedSys', 20), borderwidth = 4,command=click).place(x = 500, y = 95)



