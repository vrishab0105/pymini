from tkinter import *
from tkinter import messagebox
from random import *
word_list=['Python','keybord','class','object','print','variable','pointer','while','for','do while',
           'elif','def','function','method','mainloop','input','int','float','pass','string','Tuple']
timeleft=60
def timer():
    global timeleft
    if timeleft>0:
        timeleft-=1
        lab_tcount.config(text=timeleft)
        lab_tcount.after(1000,timer)
    else:
        ent_inp.config(state=DISABLED)
        result=correct-wrong
        lab_instruction.config(text=f"Correct:{correct}\n wrong:{wrong}\n result:{result}")
        res=messagebox.askyesno('Confoirm','Do you want to play again')
        if res==True:
            i=0
            timeleft=60
            lab_wcount.config(text='0')
            lab_tcount.config(text='60')
            ent_inp.config(state=NORMAL)
            lab_instruction.config(text='Type word and hit enter')
i=0
correct,wrong=0,0
def check(event):
    global i,correct,wrong
    i+=1
    lab_wcount.config(text=i)
    if timeleft==60:
        timer()
    if ent_inp.get()==lab_wordlist['text']:
        correct+=1
    else:
        wrong+=1
    shuffle(word_list)
    lab_wordlist.config(text=word_list[0])
    ent_inp.delete(0,END)
    lab_instruction.config(text='')
    


root=Tk()
root.title("Check Word")

root.geometry("600x600+30+20")
f=("Arial",20,"bold")
root.iconbitmap("logo.ico")
root.config(bg="black")

lab_title=Label(root,text="Check word typing speed",font=f,fg="white",bg="black")
lab_title.place(x=150,y=20)

shuffle(word_list)
lab_wordlist=Label(root,text=word_list[0],font=("Arial",25,"bold"),fg="green",
                   bg="black")
lab_wordlist.place(x=250,y=200,anchor=CENTER)#to place at center in label

lab_word=Label(root,text="words",font=f,fg="white",bg="black")
lab_wcount=Label(root,text="0",font=f,fg="white",bg="black")
lab_word.place(x=50,y=110)
lab_wcount.place(x=60,y=150)


lab_time=Label(root,text="time",font=f,fg="white",bg="black")
lab_tcount=Label(root,text="60",font=f,fg="white",bg="black")
lab_time.place(x=500,y=110)
lab_tcount.place(x=510,y=150)


ent_inp=Entry(root,font=f,bd=5,justify=CENTER)
ent_inp.place(x=150,y=250)
ent_inp.focus_set()

lab_instruction=Label(root,text="Type word and hit enter",
                      font=("chiller",19,"bold"),fg="Red",bg="black")
lab_instruction.place(x=270,y=350,anchor=CENTER)

root.bind('<Return>',check)


mainloop()

