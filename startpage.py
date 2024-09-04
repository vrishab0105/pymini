from tkinter import *
from PIL import Image, ImageTk
import subprocess
import sys

slidershow = ''
count = 0
validuser = 0

def slider():
    global slidershow, count
    text = "Welcome to typing master"
    if count >= len(text):
        count = 0
        slidershow = ''
    slidershow = slidershow + text[count]
    lab_title.config(text=slidershow)
    lab_title.after(250, slider)
    count += 1

def gamestart():
    if sys.platform.startswith('win'):
        subprocess.Popen([sys.executable, "typingame.py"], creationflags=subprocess.CREATE_NO_WINDOW)
    else:
        subprocess.Popen([sys.executable, "typingame.py"])

def wordcheck():
    if sys.platform.startswith('win'):
        subprocess.Popen([sys.executable, "wordcheck.py"], creationflags=subprocess.CREATE_NO_WINDOW)
    else:
        subprocess.Popen([sys.executable, "wordcheck.py"])


root = Tk()
root.title("Typing Master")
root.geometry("600x600+400+10")
root.iconbitmap("logo.ico")
# Load background image
bg_image = Image.open("blackspeed.jfif")# Replace "path_to_your_image.jpg" with the actual path to your image
bg_image = bg_image.resize((600, 600), Image.LANCZOS)  # Use Image.LANCZOS for antialiasing
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
f = ("Arial", 20, "bold")



lab_title = Label(root, text='', font=f,fg='White', bg="black")
lab_title.pack(pady=20)
slider()

lab_data=Label(root,text='35.Ganesh Suryawanshi \n26.Vrishab shenvi \n23.Kshitij Satpute',font=("Arial", 12, "italic"),fg='White', bg="black")
lab_data.pack(pady=20)

ph_icon=Image.open("logotm.png")
ph_icon =ph_icon.resize((190, 190), Image.LANCZOS)
lo_photo = ImageTk.PhotoImage(ph_icon)
lo_label = Label(root, image=lo_photo)
lo_label.place(x=210, y=180)

lab_wordcheck = Button(root, text="Word check", font=f, bg="blue", command=wordcheck)
lab_wordcheck.place(x=310, y=420)

lab_game = Button(root, text="  Game  ", font=f, bg="blue", command=gamestart)
lab_game.place(x=140, y=420)

root.mainloop()
