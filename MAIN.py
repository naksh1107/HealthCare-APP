from tkinter import *
from PIL import ImageTk, Image
import pyttsx3
import view_my_profile
import appointmentFinal
import Pharmacy
import coronavirus_test
import speech_recognition as speech_recog
from tkinter import messagebox

app = Tk()
app.geometry('1000x600')
app.title('V-Care')
app.configure(bg = 'white')

banner = Image.open('banner.jpg')
banner = banner.resize((1000, 150), Image.ANTIALIAS)
banner = ImageTk.PhotoImage(banner)
banner_lbl = Label(app, image = banner)
banner_lbl.place(x = 0, y = 0)

logo = Image.open('logo_heart.png')
logo = logo.resize((120, 100), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
logo_lbl = Label(app, image = logo)
logo_lbl.place(x = 315, y = 0)

logo_title = Image.open('logo_title.png')
logo_title = logo_title.resize((280, 100), Image.ANTIALIAS)
logo_title = ImageTk.PhotoImage(logo_title)
logo_title_lbl = Label(app, image = logo_title)
logo_title_lbl.place(x = 438, y = 0)

logo_tag = Image.open('logo_tag.png')
logo_tag = logo_tag.resize((300, 40), Image.ANTIALIAS)
logo_tag = ImageTk.PhotoImage(logo_tag)
logo_tag_lbl = Label(app, image = logo_tag)
logo_tag_lbl.place(x = 439, y = 100)

def chatbot_AI():
    
    root = Toplevel(master = app)
    root.title('Virtual Assistant')
    root.geometry('600x500')
    root.iconbitmap('chat_bot_ico.ico')
    
    # Background and other images
    
    img_bg = Image.open("chat_bot_bg.png")
    img_bg = img_bg.resize((600, 450), Image.ANTIALIAS)
    bg_img = ImageTk.PhotoImage(img_bg)
    bg_img_lbl = Label(master = root, image = bg_img)
    bg_img_lbl.place(x = 0, y = 0)
    
    eva_logo_img = Image.open("e.v.a_logo.png")
    eva_logo_img = eva_logo_img.resize((200, 150), Image.ANTIALIAS)
    eva_logo = ImageTk.PhotoImage(eva_logo_img)
    eva = Label(master = root, image = eva_logo)
    eva.place(x = 30, y= 70)

    eva_speech_logo_img = Image.open("speech_bubble_eva.png")
    eva_speech_logo_img = eva_speech_logo_img.resize((300, 150), Image.ANTIALIAS)
    eva_speech_logo = ImageTk.PhotoImage(eva_speech_logo_img)
    eva_speech = Label(master = root, image = eva_speech_logo)
    eva_speech.place(x = 250, y= 10)


    user_logo_img = Image.open("user_logo.png") 
    user_logo_img = user_logo_img.resize((200, 150), Image.ANTIALIAS)
    user_logo = ImageTk.PhotoImage(user_logo_img)
    user = Label(master = root, image = user_logo)
    user.place(x = 350, y = 300)
    
    user_speech_logo_img = Image.open("speech_bubble_user.png")
    user_speech_logo_img = user_speech_logo_img.resize((300, 150), Image.ANTIALIAS)
    user_speech_logo = ImageTk.PhotoImage(user_speech_logo_img)
    user_speech = Label(master = root, image = user_speech_logo)
    user_speech.place(x = 20, y= 250)

    def send_command():
        
        Label(root,text="\n                                               \n                                           \n                                                                                 \n                                             ",bg='white').place(x = 30, y = 260)
        
        Label(root, text = text_entry.get(), bg = 'white', font = ('FixedSys', 16), wraplength = 250, justify = 'center').place(x = 30, y = 300)
        
        
        

        
    
        
        s= text_entry.get().lower()
        
        if 'hello' in s or 'hi' in s:
            
            engine.say('Welcome to V-Care! How may I help?')
            
            engine.runAndWait()
            
        elif 'help' in text_entry.get():
            Label(root, text = '1.View your profile\n2.Online coronavirus test\n3.Book an appointment\n 4.Online Pharmacy\n 5.View latest updates', bg = 'white', font = ('FixedSys', 16)).place(x = 260, y = 30)
            engine.say('The V-Care application offers the following services. Type in the respective service to avail it. View yor profile. Take an online coronavirus test. Book an appointment. Check out our online pharmacy. View the latest updates.')
            engine.runAndWait()

        elif 'profile' in s or '1'in s :
            view_my_profile.profile_view()
            
        elif 'coronavirus test' in s or '2' in s:
            coronavirus_test.online_questionnaire()

        elif 'pharmacy' in text_entry.get():
            Pharmacy.pharmacy()

        elif 'appointment' in text_entry.get():
            appointmentFinal.appointment()
            
            
            
        else:
            Label(root, text ="Please choose from one of the options given above", bg = 'white', font = ('FixedSys', 16), wraplength = 250, justify = 'center').place(x = 280, y = 50)
            engine.say("Please choose from one of the options given above")
            engine.runAndWait()
    
        text_entry.delete(0, END)
        
        
   
    
    # Text to speech

    engine = pyttsx3.init(driverName = 'sapi5')

    engine.setProperty('rate', 180)
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

    #engine.say("Hello there! I am your Virtual Assistant. I am here to attend to all your needs and help you to the best of my abilities. Type in help to get started on the V-Care application's services catalogue.")
    #engine.runAndWait()

    # Speech to text
    
    
    
    
    

   

    # Widget definitions
    
    text_entry = Entry(root, width = 30, borderwidth = 9, font = ('FixedSys', 18))
    text_entry.place(x = 0, y = 450)

    Button(root, text = "Send", borderwidth = 7, width = 11, height = 2, activebackground = 'light green', command = send_command).place(x = 500, y = 448)

    root.mainloop()

chatbot_btn = Image.open('chatbot.png')
chatbot_btn = chatbot_btn.resize((100,100), Image.ANTIALIAS)
chatbot_btn = ImageTk.PhotoImage(chatbot_btn)
chatbot_btn_wid = Button(app, image = chatbot_btn, borderwidth = 0, compound = CENTER, bg = 'white', command = chatbot_AI)
chatbot_btn_wid.image = chatbot_btn
chatbot_btn_wid.place(x = 900, y = 490)

def click1():
    view_my_profile.profile_view()

def click2():
    coronavirus_test.online_questionnaire()

def click3():
    Pharmacy.pharmacy()

def click4():
    appointmentFinal.appointment()
    
    
    
def lines_click():
    
    login = Image.open('login.png')
    login = login.resize((50, 50), Image.ANTIALIAS)
    login = ImageTk.PhotoImage(login)
    login_btn = Button(app, bg ='white', image = login, compound = LEFT, text = 'login/sign-up', font = ('FixedSys', 15), borderwidth = 2,command=click1)
    login_btn.image = login
    login_btn.place(x = 0, y = 160)
    
    test = Image.open('about_us.jpg')
    test = test.resize((50, 50), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(test)
    test_btn = Button(app, bg = 'white', image = test, compound = LEFT, text = 'coronavirus test', width = 220, font = ('FixedSys', 15), borderwidth = 2,command=click2)
    test_btn.image = test
    test_btn.place(x = 0, y = 460)
    
    appointment = Image.open('appointment.png')
    appointment = appointment.resize((50, 50), Image.ANTIALIAS)
    appointment = ImageTk.PhotoImage(appointment)
    appointment_btn = Button(app, bg = 'white', image = appointment, width = 153, compound = LEFT, text = 'Appointment', font = ('FixedSys', 15), borderwidth = 2,command=click4)
    appointment_btn.image = appointment
    appointment_btn.place(x = 0, y = 260)
    
    pharmacy = Image.open('pharmacy.jpg')
    pharmacy = pharmacy.resize((50, 50), Image.ANTIALIAS)
    pharmacy = ImageTk.PhotoImage(pharmacy)
    pharmacy_btn = Button(app, bg = 'white', image = pharmacy, width = 153, compound = LEFT, text = '  Pharmacy', font = ('FixedSys', 15), borderwidth = 2,command=click3)
    pharmacy_btn.image = pharmacy
    pharmacy_btn.place(x = 0, y = 360)
    
    
lines = Image.open('tabs_img.png')
lines = lines.resize((50, 50), Image.ANTIALIAS)
lines = ImageTk.PhotoImage(lines)
lines_btn = Button(app, bg = 'white', image = lines, compound = CENTER, borderwidth = 2, command = lines_click)
lines_btn.place(x = 0, y = 10)
    
update_1 = Image.open('alzheimers.png')
update_1 = update_1.resize((800, 240), Image.ANTIALIAS)
update_1 = ImageTk.PhotoImage(update_1)
update_1_lbl = Label(app, image = update_1, borderwidth = 15, relief = 'ridge')
update_1_lbl.place(x=170,y=150)

update_2 = Image.open('aids.png')
update_2 = update_2.resize((800, 240), Image.ANTIALIAS)
update_2 = ImageTk.PhotoImage(update_2)
update_2_lbl = Label(app, image = update_2, borderwidth = 15, relief = 'ridge')

update_3 = Image.open('diabetesday.jpg')
update_3 = update_3.resize((800, 240), Image.ANTIALIAS)
update_3 = ImageTk.PhotoImage(update_3)
update_3_lbl = Label(app, image = update_3, borderwidth = 15, relief = 'ridge')


l1=[update_2_lbl,update_3_lbl]
count=0

def lines_click2():
    global count
    
    if count==len(l1):
        count=0
    
        
    else:
        l1[count].place(x=170,y=150)
        count+=1
    
Button(app,text=">",font=('FixedSys', 16),width=5,command=lines_click2,).place(x=570,y=420)

app.mainloop()
