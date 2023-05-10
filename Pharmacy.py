from tkinter import *
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image

def pharmacy():
    root=Tk()
    root.title("Online Pharmacy")
    root.geometry("500x300")

    '''bg=ImageTk.PhotoImage(Image.open("pharmacy1.png"))
    piclabel=Label(master=root,image=bg)
    piclabel.place(x=0,y=0,relwidth=1,relheight=1)'''

    '''img_bg = Image.open("pharmacy1.png")
    img_bg = img_bg.resize((500, 300), Image.ANTIALIAS)
    bg_img = ImageTk.PhotoImage(img_bg)
    bg_img_lbl = Label(master = root, image = bg_img)
    bg_img_lbl.place(x = 0, y = 0)'''


    TOP=Toplevel()

    wrapper1=LabelFrame(TOP)

    my_canvas=Canvas(wrapper1)
    my_canvas.pack(side=LEFT,fill="both",expand="yes")


    sbar=ttk.Scrollbar(wrapper1,orient="vertical",command=my_canvas.yview)
    sbar.pack(side=RIGHT,fill="y")

    frame3=Frame(my_canvas)
    my_canvas.create_window((150,0),window=frame3,anchor="nw")
                        
    wrapper1.pack(fill="both",expand="yes",padx=10,pady=10)

    my_menu=Menu(TOP)
    TOP.config(menu=my_menu)



    TOP.title("Cart")
    
    TOP.geometry("500x500")

    TOP.withdraw()
    
    global addnum
    addnum=0
    global cst
    cst=0
    total=0
    a=''
    li1=[]

    def disable_event():
        pass

    TOP.protocol("WM_DELETE_WINDOW", disable_event)


    #function to search


    def search():
        try:
        
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="1269",database="mydb")
            cursor=mydb.cursor()
            sql=f"select * from pharmacy where Name='{Name.get()}'"
            cursor.execute(sql)
            result=cursor.fetchone()
            MedicineID.set(result[0])
            Manufacturer.set(result[2])
            Pharmalogical_Category.set(result[3])
            Dosage_form.set(result[4])
            Availability.set(result[5])
            cost.set(result[6])
            e.configure(state='disabled')
            e1.configure(state='disabled')
            e2.configure(state='disabled')
            e3.configure(state='disabled')
            e4.configure(state='disabled')
            e5.configure(state='disabled')
            e6.configure(state='disabled')
        
            mydb.close()
        except :
            messagebox.showinfo('Not Found','Search not found!')
            refresh()

        
#function to clear

        
    def refresh():
        Name.set('')
        MedicineID.set('')
        Manufacturer.set('')
        Pharmalogical_Category.set('')
        Dosage_form.set('')
        Availability.set('')
        cost.set('')
        e.configure(state='normal')
        e1.configure(state='normal')
        e2.configure(state='normal')
        e3.configure(state='normal')
        e4.configure(state='normal')
        e5.configure(state='normal')
        e6.configure(state='disabled')
        e7.delete(0,END)
        if b3["state"]=="disabled":
             b3["state"]="active"
        else:
            b3["state"]="normal"
    
       
    

#cart function
    
    def cart():
    


        my_canvas.configure(yscrollcommand=sbar.set)
        my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion=(0,0,0,10000)))

    
    
        TOP.deiconify()


    

#function to add items to the cart
    
    def add():
        global frame2,addnum,total,cst,a

        if e.get()=="":
           messagebox.showerror("Error","No search added")        

        elif e5.get()=='no':
            messagebox.showerror('Not available','Sorry!,This product is not available right now')  
     
   
        elif e7.get()=='':
            messagebox.showerror('Error','No quantity added')

        
    
    
        else:
            #creating labels in the new window
            r1="Medicine Name: "+ e.get()
            r2="MedicineID: "+ e1.get()
            r3="Manufacturer: "+ e2.get()
            r4="Pharmalogical_Category: "+ e3.get()
            r5="Dosage_form: "+ e4.get()
            r6="Availability: "+ e5.get()
            r7="Cost: "+e6.get()
            r8="Quantity: "+e7.get()

        

       

            #frame2
            frame2=LabelFrame(frame3,text="Item Details:",bd=5,font=10)
            frame2.pack()
       
                    
            lab1=Label(frame2,text=r1)
            lab2=Label(frame2,text=r2)
            lab3=Label(frame2,text=r3)
            lab4=Label(frame2,text=r4)
            lab5=Label(frame2,text=r5)
            lab6=Label(frame2,text=r6)
            lab7=Label(frame2,text=r7)
            lab8=Label(frame2,text=r8)
        

                    
            lab1.pack(anchor=W)
            lab2.pack(anchor=W)
            lab3.pack(anchor=W)
            lab4.pack(anchor=W)
            lab5.pack(anchor=W)
            lab6.pack(anchor=W)
            lab7.pack(anchor=W)
            lab8.pack(anchor=W)
       
        
           
            addnum=addnum+1
            
            messagebox.showinfo('Success','Item has been added to Cart')
            b3["state"]="disabled"
        

            c=e6.get()[3:]
            for i in c:
                if i=='/' :
                    a=c.index('/')

                    b=c[0:a]
                    total=int(e7.get())*int(b)
                
                
                    li1.append(total)
                    print(li1)
                    
                    break
            
            print(total)
            cst=cst+total
            print(cst)
        
            
        



        
    def delete():
    
    
    
    

        def remove():
            if e0.get()=="":
            
                messagebox.showerror('Error','No item specified')
            else:
                try:
                
            
                    frame3.winfo_children()[int(e0.get())-1].destroy()
                    global cst
                    cst=cst-li1[int(e0.get())-1]
            
                    l0.destroy()
                    e0.destroy()
                    b0.destroy()
            

                except:
                    messagebox.showerror('Error','Item not present ')
                
            
            
            
    
        l0=Label(TOP,text="Enter below the number of item u want to delete:")
        e0=Entry(TOP)
    
        b0=Button(TOP,text="Delete",command=remove)
        l0.pack()
        e0.pack()
        b0.pack()
    
    
        
        return

    def place():
        def order():
        
            CL.destroy()
            b10.destroy()
            TOP2=Toplevel()
            TOP2.title("Bill")
    
            TOP2.geometry("200x200")
    
        CL=Label(TOP,text="Total Cost="+str(cst))
    
        CL.pack()
        b10=Button(TOP,text="Place Order",command=order)
        b10.pack()
    
    

#adding a frame

    frame=LabelFrame(root,text="Medicine details:",background="white")
    frame.grid(row=2,column=2)

#defining column names

    Name=StringVar()
    MedicineID=StringVar()
    Manufacturer=StringVar()
    Pharmalogical_Category=StringVar()
    Dosage_form=StringVar()
    Availability=StringVar()
    cost=StringVar()


#making thelabels and input fields


    l1=Label(root,text='')
    e=Entry(root,textvariable=Name,width=50,bd=7)
    e.insert(0,"Enter the medicine you want to search for")
    l2=Label(frame,text='MedicineID:',bg="white")
    e1=Entry(frame,textvariable=MedicineID,width=25,bd=3)
    l3=Label(frame,text='Manufacturer:',bg="white")
    e2=Entry(frame,textvariable=Manufacturer,width=25,bd=3)
    l4=Label(frame,text='Pharmalogical_Category:',bg="white")
    e3=Entry(frame,textvariable=Pharmalogical_Category,width=25,bd=3)
    l5=Label(frame,text='Dosage_form:',bg="white")
    e4=Entry(frame,textvariable=Dosage_form,width=25,bd=3)
    l6=Label(frame,text='Availability:',bg="white")
    e5=Entry(frame,textvariable=Availability,width=25,bd=3)
    l7=Label(frame,text='Cost:',bg="white")
    e6=Entry(frame,textvariable=cost,width=25,bd=3)
    l8=Label(frame,text="Enter the quantity you want:",bg="white")
    e7=Entry(frame,width=10,bd=3)
    b1=Button(root,text='Search',command=search)
    b2=Button(root,text='Refresh',command=refresh)
    b3=Button(root,text="Add To Cart",command=add)
    b4=Button(root,text="Cart",command=cart)


    Bmenu=Menu(my_menu)
    my_menu.add_cascade(label="Proceed to Buy",menu=Bmenu)
    Bmenu.add_command(label="Place Order",command=place)



    Dmenu=Menu(my_menu)
    my_menu.add_cascade(label="Delete" ,menu=Dmenu)
    Dmenu.add_command(label="Delete an Item",command=delete)





    #placing the labels and input fields


    l1.grid(row=1,column=1)
    e.grid(row=1,column=2)
    l2.grid(row=2,column=2)
    e1.grid(row=2,column=3)
    l3.grid(row=3,column=2)
    e2.grid(row=3,column=3)
    l4.grid(row=4,column=2)
    e3.grid(row=4,column=3)
    l5.grid(row=5,column=2)
    e4.grid(row=5,column=3)
    l6.grid(row=6,column=2)
    e5.grid(row=6,column=3)
    l7.grid(row=7,column=2)
    e6.grid(row=7,column=3)
    l8.grid(row=8,column=2)
    e7.grid(row=8,column=3)
    b1.grid(row=1,column=3)
    b2.grid(row=1,column=0)
    b3.grid(row=9,column=2)
    b4.grid(row=1,column=5)



    root.mainloop()





    
    
    
    
        

        
