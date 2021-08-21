from telebot import *
from tkinter import *
from time import *
from tkmacosx import *
import webbrowser as web


oop_bot=TeleBot("1877813721:AAGrGmPdLXNRnXLqYBeiF6DdkbMEDqM4wng")
sp_link="https://meet.google.com/lookup/gt4oj7cfe5?authuser=1&hs=179"
oop_link="trying to get the link ):"
micro_link="https://meet.google.com/tgd-xuvm-brn?hs=122&authuser=0"
math_link="http://meet.google.com/ope-azax-qsg"

start_time=time()

have_link=False
def open_micro_link():
    web.open(micro_link)
def open_oop_link():
    web.open(oop_link)
def open_sp_link():
    web.open(sp_link)
def open_math_link():
    web.open(math_link)


# def set_oop_link():
#     def get_oop(a):
#      if "meet.google.com" in a:
#         oop_link = a
#         print(oop_link)
#         oop_bot.stop_polling()
#         oop_bot.stop_bot()
#         have_link=True
#
#     @oop_bot.message_handler(func= lambda m:True)
#     def oop(message):
#         oop_bot.reply_to(message,message.text)
#         print("message:",message.text)
#         get_oop(message.text)
#         # oop_bot.reply_to(message,get_oop(message.text))
#     if time()-start_time<4:
#         oop_bot.polling(none_stop=True,interval=3,timeout=20)



routine={
    "Sat":{690:"micro",780:"sp",870:"math"},
    "Sun":{600:"oop",690:"numerical"},
    "Mon":{690:"numerical",870:"micro"},
    "Tue":False,
    "Wed":{600:"math",690:"oop"},
    "Thu":False,
    "Fri":False
}


all_time=ctime().split()
today=all_time[0]
temp=all_time[3].split(":")
t=int(temp[0])*60+int(temp[1])

#today = "Sun"
#t=601
cls=True
tClass={}
nowClass="it's not any class time"
for i in routine:
    if i == today:
        if routine[i]==False:
            cls=False
        else:
            for j in routine[i]:
                #print(j, routine[i][j])
                tClass[j]=routine[i][j]
                if j+90>t and j<=t:
                    nowClass=routine[i][j]

if nowClass=='oop':
    @oop_bot.message_handler(regexp="meet.google.com")
    def oop(message):
       global oop_link
       oop_link=message.text
       oop_bot.stop_polling()
    oop_bot.polling(timeout=4)





root=Tk()
root.geometry("800x400")
root.configure(bg='#faefcf')
Label(root,bg='#faefcf').grid(row=0,column=0,columnspan=6)
Label(root,text="Time:",font="Helvetica 40 bold",fg="red").grid(row=1,column=0,padx=10,pady=10)
Label(root,text="10:00",font="Helvetica 40 bold",fg="red").grid(row=1,column=1,padx=10,pady=10)
Label(root,text="11:30",font="Helvetica 40 bold",fg="red").grid(row=1,column=2,padx=10,pady=10)
Label(root,text="1:00",font="Helvetica 40 bold",fg="red").grid(row=1,column=3,padx=10,pady=10)
Label(root,text="2:30",font="Helvetica 40 bold",fg="red").grid(row=1,column=4,padx=10,pady=10)
Label(root,text="Today's class:",font="Helvetica 25 bold",fg="red").grid(row=2,column=0,padx=10,pady=10)
if cls==False:
    Label(root,text="there is no class today!",font="helvetica 25 bold",fg="red").grid(row=2,column=1,padx=10,pady=10,columnspan=3)
else:
    for i in tClass:
        if i==600:
            Label(root,text=tClass[i],font="helvetica 25 bold",fg="red").grid(row=2,column=1,padx=10,pady=10)
        elif i==690:
            Label(root,text=tClass[i],font="helvetica 25 bold",fg="red").grid(row=2,column=2,padx=10,pady=10)
        elif i==780:
            Label(root,text=tClass[i],font="helvetica 25 bold",fg="red").grid(row=2,column=3,padx=10,pady=10)
        elif i==870:
            Label(root,text=tClass[i],font="helvetica 25 bold",fg="red").grid(row=2,column=4,padx=10,pady=10)

Label(root,text="Class on going:",font="Helvetica 25 bold",fg="red").grid(row=3,column=0,padx=10,pady=10)
Label(root,text=nowClass,font="Helvetica 25 bold",fg="red").grid(row=3,column=1,padx=10,pady=10,columnspan=3)


if nowClass!="it's not any class time":
    Label(root, text="Class Link:", font="Helvetica 25 bold", fg="red").grid(row=4, column=0, padx=10, pady=10)
    if nowClass=="oop" :
        #set_oop_link()
        print("oop link:",oop_link)
        if have_link:
            Button(root,text="open link!",font="helvetica 25 bold",fg="green",bg="black",borderless=1,command=open_oop_link).grid(row=4,column=1,padx=10,pady=10,columnspan=2)
        else :
            Label(root,text=oop_link,font="helvetica 25 bold",fg="red").grid(row=4,column=1,padx=10,pady=10,columnspan=3)
    if nowClass=="sp" :
        Button(root,text="open link!",font="helvetica 25 bold",fg="green",bg="black",borderless=1,command=open_sp_link).grid(row=4,column=1,padx=10,pady=10,columnspan=2)

    if nowClass=="micro":
        Button(root, text="open link!", font="helvetica 25 bold", fg="green", bg="black",borderless=1,command=open_micro_link).grid(row=4, column=1, padx=10,
                                                                                               pady=10, columnspan=2)
    if nowClass=="math":
        Button(root, text="open link!", font="helvetica 25 bold", fg="green", bg="black",borderless=1,command=open_math_link).grid(row=4, column=1, padx=10,pady=10,columnspan=2)




root.mainloop()
print("final oop link:",oop_link)