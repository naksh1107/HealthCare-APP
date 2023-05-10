from tkinter import *
global score
global lbl


def online_questionnaire():
    global lbl
    global score
    from tkinter import messagebox
    quest = Tk()
    quest.title("Coronavirus questionnaire")
    quest.geometry('840x730')

    Label(quest, text="Coronavirus questionnaire", font=("Comic Sans MS", 25, "bold underline")).place(x=185, y=0)
    Label(quest, text="Please respond to the following questions honestly as it help us provide \n a more accurate diagnosis", font=("Comic Sans MS", 16, "bold")).place(x=30, y=60)

    # This score is used to evaluate the risk at the end
    score = 0

    def final_result_yes():
        global score
        score += 1
        Button(quest, text="Yes", width=6, font=("Comic Sans MS", 17, "bold"), fg='white', bg='magenta', activebackground='light blue', borderwidth=7).place(x=270, y=250)
        if score == 4:
            messagebox.showwarning("High risk", "You have a very high risk of infection. It is advisable to a test immediately")
        elif 4 > score > 2:
            messagebox.showwarning("Moderate risk", "There is a moderate chance of infection. It is advisable to self quarantine for 14 days")
        else:
            messagebox.showinfo("No risk", "There is a very less chance of infection. Stay safe and remember to follow social distancing!")

    def final_result_no():
        Button(quest, text="No", width=6, font=("Comic Sans MS", 17, "bold"), fg='white', bg='green', activebackground='light blue', borderwidth=7).place(x=435, y=250)
        if score == 4:
            messagebox.showwarning("High risk", "You have a very high risk of infection. It is advisable to a test immediately")
        elif 4 > score > 2:
            messagebox.showwarning("Moderate risk", "There is a moderate chance of infection. It is advisable to self quarantine for 14 days")
        else:
            messagebox.showinfo("No risk", "There is a very less chance of infection. Stay safe and remember to follow social distancing!")

    def worker_meet_yes():
        global score
        Button(quest, text="Yes", width=7, font=("Comic Sans MS", 17, "bold"), fg='white', bg='magenta', activebackground='light blue', borderwidth=7, command=worker_meet_yes).place(x=250, y=600)
        score += 1
        Label(quest, text="Have you been in contact with any infected person?  ", font=("Comic Sans MS", 20, "bold")).place(x=40, y=180)
        Label(quest, text='                      \n                                        \n                      \n                    ').place(x=20, y=250)
        Label(quest, text='                            \n                                                                                      \n                                      \n').place(x=270, y=250)
        Button(quest, text="Yes", width=6, font=("Comic Sans MS", 17, "bold"), activebackground='light blue', borderwidth=7, command=final_result_yes).place(x=270, y=250)
        Button(quest, text="No", width=6, font=("Comic Sans MS", 17, "bold"), activebackground='light blue', borderwidth=7, command=final_result_no).place(x=435, y=250)
        Label(quest, text='                            \n                          \n                                    \n              ').place(x=150, y=250)
        Label(quest, text='                                       \n                            \n                         \n         ').place(x=538, y=250)

    def worker_meet_no():
        global score
        Button(quest, text="No", width=7, font=("Comic Sans MS", 17, "bold"), activebackground='light blue', bg='green', fg='white', borderwidth=7, command=worker_meet_no).place(x=400, y=600)
        Label(quest, text="Have you been in contact with any infected person?  ", font=("Comic Sans MS", 20, "bold")).place(x=40, y=180)
        Label(quest, text='                      \n                                        \n                      \n                    ').place(x=20, y=250)
        Label(quest, text='                            \n                                                                                      \n                                      \n').place(x=270, y=250)
        Button(quest, text="Yes", width=6, font=("Comic Sans MS", 17, "bold"), activebackground='light blue', borderwidth=7, command=final_result_yes).place(x=270, y=250)
        Button(quest, text="No", width=6, font=("Comic Sans MS", 17, "bold"), activebackground='light blue', borderwidth=7, command=final_result_no).place(x=435, y=250)
        Label(quest, text='                            \n                          \n                                    \n              ').place(x=150, y=250)
        Label(quest, text='                                       \n                            \n                         \n         ').place(x=538, y=250)
    global lbl

    def hotspot_city():
        global lbl
        lbl = Label(quest, text="Have you been to any hotspot city in the past month?", font=("Comic Sans MS", 20, "bold")).place(x=45, y=538)
        Button(quest, text="Yes", width=7, font=("Comic Sans MS", 17, "bold"), activebackground='light blue', borderwidth=7, command=worker_meet_yes).place(x=250, y=600)
        Button(quest, text="No", width=7, font=("Comic Sans MS", 17, "bold"), activebackground='light blue', borderwidth=7, command=worker_meet_no).place(x=400, y=600)

    def international_his_dia():
        global score
        Button(quest, text="Diabetes", font=("Comic Sans MS", 17, "bold"), activebackground='light blue', borderwidth=7, bg='magenta', fg='white').place(x=20, y=430)
        hotspot_city()
        score += 1

    def international_his_heart():
        global score
        Button(quest, text="Heart disease", font=("Comic Sans MS", 17, "bold"), activebackground='light blue', borderwidth=7, bg='magenta', fg='white').place(x=160, y=430)
        hotspot_city()
        score += 1

    def international_his_hyper():
        global score
        Button(quest, text="Hypertension", font=("Comic Sans MS", 17, "bold"), activebackground='light blue', borderwidth=7, bg='magenta', fg='white').place(x=360, y=430)
        hotspot_city()
        score += 1

    def international_his_lung():
        global score
        Button(quest, text="Lung disease", font=("Comic Sans MS", 17, "bold"), activebackground='light blue', borderwidth=7, bg='magenta', fg='white').place(x=550, y=430)
        hotspot_city()
        score += 1

    def none():
        Button(quest, text="None", font=("Comic Sans MS", 17, "bold"), activebackground='light blue', borderwidth=7, fg='white', bg='green').place(x=740, y=430)
        hotspot_city()

    def health_dis():
        Label(quest, text="Have you ever had any of these diseases before?", font=("Comic Sans MS", 20, "bold")).place(x=45, y=360)
        Button(quest, text="Diabetes", font=("Comic Sans MS", 17, "bold"), activebackground='light blue', borderwidth=7, command=international_his_dia).place(x=20, y=430)
        Button(quest, text="Heart disease", font=("Comic Sans MS", 17, "bold"), activebackground='light blue', borderwidth=7, command=international_his_heart).place(x=160, y=430)
        Button(quest, text="Hypertension", font=("Comic Sans MS", 17, "bold"), activebackground='light blue', borderwidth=7, command=international_his_hyper).place(x=360, y=430)
        Button(quest, text="Lung disease", font=("Comic Sans MS", 17, "bold"), activebackground='light blue', borderwidth=7, command=international_his_lung).place(x=550, y=430)
        Button(quest, text="None", font=("Comic Sans MS", 17, "bold"), activebackground='light blue', borderwidth=7, command=none).place(x=740, y=430)

    def cough():
        global score
        Button(quest, text="Cough", font=("Comic Sans MS", 17, "bold"), activebackground='light blue', borderwidth=7, bg='magenta', fg='white').place(x=50, y=250)
        health_dis()
        score += 1

    def fever():
        global score
        Button(quest, text="Fever", font=("Comic Sans MS", 17, "bold"), activebackground='light blue', borderwidth=7, bg='magenta', fg='white').place(x=160, y=250)
        health_dis()
        score += 1

    def breath():
        global score
        Button(quest, text="Breathing difficulty", font=("Comic Sans MS", 17, "bold"), activebackground='light blue', borderwidth=7, bg='magenta', fg='white').place(x=270, y=250)
        health_dis()
        score += 1

    def nota():
        Button(quest, text="None", font=("Comic Sans MS", 17, "bold"), activebackground='light blue', borderwidth=7, bg="green", fg='white').place(x=535, y=250)
        health_dis()

    Label(quest, text="Have you experienced any of the following symptoms?", font=("Comic Sans MS", 20, "bold")).place(x=40, y=180)
    Button(quest, text="Cough", font=("Comic Sans MS", 17, "bold"), activebackground='light blue', borderwidth=7, command=cough).place(x=50, y=250)
    Button(quest, text="Fever", font=("Comic Sans MS", 17, "bold"), activebackground='light blue', borderwidth=7, command=fever).place(x=160, y=250)
    Button(quest, text="Breathing difficulty", font=("Comic Sans MS", 17, "bold"), activebackground='light blue', borderwidth=7, command=breath).place(x=270, y=250)
    Button(quest, text="None", font=("Comic Sans MS", 17, "bold"), activebackground='light blue', borderwidth=7, command=nota).place(x=535, y=250)

    quest.mainloop()

