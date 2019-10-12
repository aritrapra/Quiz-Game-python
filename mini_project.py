#This project is devoloped by Aritra Pramanick
#A current CSE student who study in 2nd yaar Btech
#This devoloping work starts from 11th Octobar, 2019
#This project is devolop for collage project but full project and devoloped version will available on github. my github resporatorty URL was



#Importing all nececerry module

import tkinter as tk
from tkinter import *
import random, time








#this variable decleir for question no genarating
x = 0
#this is the question no for user
num = 0
#this counting question in question set
my_var = 0
#its declear to assign result
remarks = 0
#this variable declear total no of question in quiz
total_ques_in_quiz = 5
#this variable declear the marks per question
question_per_marks = 5
#its declear the time allowd per question
question_per_time = 1
#its calculate total quiz time
total_time = total_ques_in_quiz * question_per_time



#importing all RIGHT ANSWERS as an array
#importing answer containing txt file
right_answer1 = open("system/do_not_open.txt", "r")
#read and split as an array
right_answer = right_answer1.read().split(" ")
#close the file
right_answer1.close()
total_ques_quiz = total_ques_in_quiz - 1
#importing all questions and split it in array
question = open("system/dont.txt","r")
ques = question.read().split("\n")
question.close()

#count total question and store it to variable
total_ques = int(len(ques)/5)

#this functtion called when quiz time is up
def times_up():
    #declear global variable for changing globally
    global my_var,total_ques_quiz
    my_var = total_ques_quiz
    #called submit function to declear result
    submit()

#this function is write to desplay a counter value
def timer():
    #declear global variable
    global now_second,total_time
    #starting if condition with if time is up
    if(total_time == 0):
        times_up()
    #if there are some time left then show time and the counter
    else:
        #in this method we gain the "hours" value left in counter
        timer_hour = int(total_time/3600)
        #in this method we gain the "minutes" value left in counter
        timer_min = int((total_time - (timer_hour * 3600))/60)
        #in this method we gain the "seconds" value left in counter
        timer_sec = int(total_time - ((timer_hour*3600)+(timer_min*60)))
        #this try method called because string formating method is different in different version of python
        try:
            #this is for python version 3 and upper
            time_hour_for = "{0:0=2d}".format(timer_hour)
            time_min_for = "{0:0=2d}".format(timer_min)
            time_sec_for = "{0:0=2d}".format(timer_sec)

        except:
            #this is for python 2 and lower versions of python 3
            time_hour_for = "%02d"%timer_hour
            time_min_for = "%02d"%timer_min
            time_sec_for = "%02d"%timer_sec
        #make the string as an digital counter
        time_string = str(time_hour_for) + ":" + str(time_min_for) +  ":" + str(time_sec_for)
        clock_label.config(text = time_string)
        #decresement of time by 1 in a second
        total_time = total_time - 1
        clock_label.after(1000, timer)

#this function is made for gaining time system
def time_management():
    #globally declear value and gaining recent time
    global now_second
    recent_time = time.strftime("%H:%M:%S").split(":")
    now_minute = (int(recent_time[0]) * 60) + int(recent_time[1])
    now_second = (now_minute * 60) + int(recent_time[2])

#this function is assign with result pages start new quiz button value....and restating quiz for new user
def restart_quiz():
    global result_label,result_label_image,Start_new_quiz_btn,label_score,x,num,my_var,remarks,total_time,total_ques_quiz,question_per_time
    #destroying all label and buttons on the main window m
    result_label.destroy()
    result_label_image.destroy()
    Start_new_quiz_btn.destroy()
    label_score.destroy()
    #back all nececerry veriables to its initialize value
    x = 0
    num = 0
    my_var = 0
    remarks = 0
    total_time = total_ques_in_quiz * question_per_time
    #now we go back to the start page
    start_page_create()

#this function create start page
def start_page_create():
    global Logo_image,logo_label, head_label,Quiz_startbtn,term_label,total_ques_in_quiz,question_per_marks
    m.config(
        background="#ffffff"
    )#set main window background colour to white
    #load logo image from file
    Logo_image = PhotoImage(file="images/logo.png")
    logo_label = Label(
        m,
        image=Logo_image,
        border=0,
        justify="center",
    )#create logo label
    logo_label.pack(pady=(30, 10))#pack logo label
    head_label = Label(
        m,
        text="Quiz Game",
        font=("Comic sans MS", 24, "bold"),
        background="#ffffff",
        justify="center",
    ) #create head label
    head_label.pack(pady=(0, 10))

    quiz_start_logo = PhotoImage(file="images/start_quiz.png")
    Quiz_startbtn = Button(
        m,
        image=quiz_start_logo,
        border=0,
        background="#ffffff",
        command=start_btnpress
    ) #this create start quiz button
    Quiz_startbtn.pack(pady=30)
    #assign the image with that button
    Quiz_startbtn.image = quiz_start_logo

    term_label = Label(
        m,
        text="Rules for this Quiz Game\n"
             "*This game have " + str(total_ques_in_quiz) + " questions and each question have " + str(question_per_marks) + " marks\n"
             "You have " + str(total_time/60) + " minute to answer this questions\n"
             "*Cheak before submiting your answer\n"
             "*Answer's are not changeable after submiting.\n"
             "*After submiting answers result will be shown in main window",
        background="blue",
        width=580,
        justify="center",
    ) #tearms and condition label create
    term_label.pack(padx=10)

#this function is for save new question
def save_question():
    global qtn_enty,qtn_enty_op2,qtn_enty_op1,qtn_enty_op3,qtn_enty_op,answer_var
    #save Question in question.txt file in append mode
    save_string = "\n" + qtn_enty.get() + "\n" + qtn_enty_op.get() + "\n" + qtn_enty_op1.get() + "\n" + qtn_enty_op2.get() +"\n" + qtn_enty_op3.get()
    save_to_file = open("system/dont.txt", "a")
    save_to_file.write(save_string)
    save_to_file.close()
    #save Answers in answer.txt file in append mode
    answer_file = open("system/do_not_open.txt", "a")
    answer_file.write(" " + str(answer_var.get()))
    answer_file.close()

#this function is for creating a new question entry window
def question_entry():
    global qtn_enty,qtn_enty_op2,qtn_enty_op1,qtn_enty_op3,qtn_enty_op,answer_var
    n = Tk() #creating main window
    n.geometry("600x700") #define size of the window
    n.resizable(0,0)#define its no resizeable
    n.wm_iconbitmap("images/logo_official.ico")
    n.title("New question entry point")
    answer_var = IntVar() #define variable for collect answers
    answer_var = (-1)
    #crerating label for question entry
    question_entry_label = Label(
        n,
        text = "question entry point",
        font = ("bold",30)
    )

    question_entry_label.pack()
    #question add label
    question_entry_label_small = Label(
        n,
        text= "Enter Question",
        font = ("bold",16)
    )
    question_entry_label_small.place(x=50,y=70)
    #question add entry
    qtn_enty = Entry(
        n,
        width =30,
        font = (16)

    )
    qtn_enty.pack(padx=220,pady=(22,39))
    #answer option 1 label
    question_entry_label_small_0 = Label(
        n,
        text="Enter Option 1",
        font=("bold", 16)
    )
    question_entry_label_small_0.place(x=50, y=170)
    #radiobutton for collect answer
    save_answer1 = Radiobutton(
        n,
        value=0,
        variable=answer_var,
    )
    save_answer1.place(x=200, y=173)
    #entry wiget to get option value
    qtn_enty_op = Entry(
        n,
        width=30,
        font=(16)

    )
    qtn_enty_op.pack(padx=220, pady=34)
    #answer option 2 label
    question_entry_label_small_1 = Label(
        n,
        text="Enter Option 2",
        font=("bold", 16)
    )
    question_entry_label_small_1.place(x=50, y=270)
    #radiobutton for collect answer
    save_answer2 = Radiobutton(
        n,
        value=1,
        variable=answer_var,
    )
    save_answer2.place(x=200, y=273)
    #entry wiget to get option value
    qtn_enty_op1 = Entry(
        n,
        width=30,
        font=(16)

    )
    qtn_enty_op1.pack(padx=220, pady=37)
    #answer option 3 label
    question_entry_label_small_2= Label(
        n,
        text="Enter Option 3",
        font=("bold", 16)
    )
    question_entry_label_small_2.place(x=50, y=370)
    #radiobutton for collect answer
    save_answer3 = Radiobutton(
        n,
        value=2,
        variable=answer_var,
    )
    save_answer3.place(x=200, y=373)
    #entry wiget to get option value
    qtn_enty_op2 = Entry(
        n,
        width=30,
        font=(16)

    )
    qtn_enty_op2.pack(padx=220, pady=37)
    #answer option 4 label
    question_entry_label_small_3 = Label(
        n,
        text="Enter option 4",
        font=("bold", 16)
    )
    question_entry_label_small_3.place(x=50, y=470)
    #radiobutton for collect answer
    save_answer4 = Radiobutton(
        n,
        value=3,
        variable=answer_var,
    )
    save_answer4.place(x=200, y=473)
    #entry wiget to get option value
    qtn_enty_op3 = Entry(
        n,
        width=30,
        font=(16)

    )
    qtn_enty_op3.pack(padx=220, pady=37)
    #creating save button for add question
    question_entry_btn = Button(
        n,
        text = "save",
        command = save_question

    )
    question_entry_btn.place(x = 400,y=570)
    n.mainloop()

#this function is made for reviewing the answer get from the user
def reviewer():
    global num, answerss,my_var,remarks,ques_set,right_answer
    #starting if condition and configuring true if user answewr and Right answer matched
    if(answerss.get() == int(right_answer[ques_set[my_var]])):
        #increment of right answer no
        remarks = remarks + 1

#this function create and show result page
def result():
    global remarks,question_per_marks,total_ques_in_quiz,question_per_marks,result_label,result_label_image,Start_new_quiz_btn,label_score
    #count total marks obtained
    marks = remarks * question_per_marks
    #load all result page image
    excelent_image = PhotoImage(file="images/excelent.png")
    ordinary_image = PhotoImage(file="images/ordinary.png")
    fail_image = PhotoImage(file="images/fail.png")
    #changing the background color
    m.config(
        background = "#8BE2FF"
    )
    #create result lebel
    result_label = Label(
        m,
        text= "you got " + str(question_per_marks * remarks),
        background = "#8BE2FF",
        font = ("bold",30)
    )
    result_label.pack()
    #creating result label image
    result_label_image = Label(
        m,
        border=0
    )
    result_label_image.pack()

    #its calculate the percentage of marks
    total_marks = total_ques_in_quiz*question_per_marks
    remark_percent_st1 = 100/total_marks
    remark_percent = remark_percent_st1 * marks

    #if marks is greater then equal to 80.0 show some result
    if(remark_percent >= 80.0):
        #configure result label and result label image
        result_label_image.config(image=excelent_image)
        result_label_image.image = excelent_image
        label_score = Label(
            m,
            text="Wow carry on",
            background="#8BE2FF",
            font=('bold', 30)
        )
        label_score.pack()
    #if marks is greater then equal to  50.0 then show some result
    elif(remark_percent > 50.0):
        #configureing result window
        result_label_image.config(image=ordinary_image)
        result_label_image.image = ordinary_image
        label_score = Label(
            m,
            text = "you need to do better",
            background = "#8BE2FF",
            font = ('bold', 30)
        )
        label_score.pack()
    else:
        result_label_image.config(image=fail_image)
        result_label_image.image = fail_image
        label_score = Label(
            m,
            text="Dont sad, next time you do better",
            background="#8BE2FF",
            font=('bold', 26)
        )
        label_score.pack()
    #crteating start new quiz button
    new_quiz_logo = PhotoImage(file="images/start_new_quiz.png")
    Start_new_quiz_btn = Button(
        m,
        image = new_quiz_logo,
        command = restart_quiz
    )
    Start_new_quiz_btn.place(x=530,y=520)
    Start_new_quiz_btn.image = new_quiz_logo

#this function genarate random question number for user
def question_no_genarator():
    global ques_set,ques,x,total_ques,total_ques_quiz
    #get a empty question set
    ques_set = [0]
    #run while loop to get random no one by one
    while(len(ques_set)<=total_ques_quiz):
        value = random.randint(0,total_ques-1)
        #if value is already in set the skip it
        if(value in ques_set):
            continue
        #otherwise add it to question set
        else:
            ques_set.append(value)
            x += 1

#this function is assign to answer submit button
def submit():
    global answerss,ques_set,num,question_label,radiobtn,radiobtn3,radiobtn1,radiobtn2,submit_btn,total_ques_in_quiz,my_var,remarks,clock_label
    #destroying all labels and images and buttons
    question_label.destroy()
    radiobtn.destroy()
    radiobtn1.destroy()
    radiobtn2.destroy()
    radiobtn3.destroy()
    submit_btn.destroy()

    #cheak if the user answer all the question
    if(my_var == total_ques_quiz):
        #this statement is for review last question
        if (answerss.get() == right_answer[ques_set[my_var-1]]):
            remarks = remarks + 1
        reviewer()
        #now quiz is end and show the result page
        result()
        #destroying the counter label
        clock_label.destroy()
    #else review the answer and go to the next question
    else:
        reviewer()
        my_var = my_var + 1
        #starting quiz and get next question
        start_quiz()

#this function start the quiz
def start_quiz():
    global  answerss,num,question_label,radiobtn,radiobtn3,radiobtn1,radiobtn2,submit_btn,my_var,clock_label,now_second
    num = ques_set[my_var] * 5
    #configure main window background
    m.config(
        bg = "#43d4d9"
    )
    #create question label
    question_label = Label(
        m,
        text = ques[num],
        bg = "#43d4d9",
        font = ("bold",24)
    )
    question_label.pack(pady = 50)
    answerss = IntVar()   #create variable to get answer from user

    #creating radio button 1
    radiobtn = Radiobutton(
        m,
        text = ques[num+1],
        value = 0,
        variable = answerss,
        bg="#addcde",
        width = 50,
        height = 2,
        font = (20)
    )
    radiobtn.pack(pady = 10)
    #creating radio button 2
    radiobtn1 = Radiobutton(
        m,
        text=ques[num+2],
        value = 1,
        variable=answerss,
        bg="#addcde",
        width=50,
        height=2,
        font=(20)
    )
    radiobtn1.pack(pady = 10)
    #creating radio button 3
    radiobtn2 = Radiobutton(
        m,
        text=ques[num+3],
        value = 2,
        variable=answerss,
        bg="#addcde",
        width=50,
        height=2,
        font=(20)
    )
    radiobtn2.pack(pady = 10)
    #creating radio button 4
    radiobtn3 = Radiobutton(
        m,
        text=ques[num+4],
        value = 3,
        variable=answerss,
        bg="#addcde",
        width=50,
        height=2,
        font=(20)
    )
    radiobtn3.pack(pady = 20)
    #CREATING SUBMIT LOGO
    Submit_logo = PhotoImage(file="images/submit.png")
    submit_btn = Button(
        m,
        image=Submit_logo,
        command = submit
    )
    submit_btn.pack()
    #assigning image to the button
    submit_btn.image = Submit_logo

#this function is called to initializing quiz start
def start_btnpress():
    global logo_label,head_label,Quiz_startbtn,term_label,clock_label
    #destroying all available labels and images and buttons
    logo_label.destroy()
    head_label.destroy()
    Quiz_startbtn.destroy()
    term_label.destroy()
    #Create counter label
    clock_label = Label(
        m,
        bg="#000000",
        fg="#ffffff",
        font = ("bold",30)
    )
    clock_label.place(x=540,y=0)
    timer()
    #called the start quiz function to start quiz
    start_quiz()






#creating main window
m = tk.Tk()
#name the main window
m.title("mini project by Aritra Pramanick")
#define window size
m.geometry("700x600")
m.wm_iconbitmap("images/logo_official.ico")
#set it to not resizeable
m.resizable(0,0)
#creating menus
menu = Menu(
    m
)
m.config(menu=menu)

sub_menu = Menu(menu)
menu.add_cascade(label="question_entry",menu = sub_menu)
sub_menu.add_cascade(label="question_entry",command= question_entry)
start_page_create()
question_no_genarator()
#the mainloop function to end the tkinter loop
m.mainloop()