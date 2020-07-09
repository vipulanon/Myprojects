from tkinter import *
import tkinter.messagebox as tmsg

window = Tk()
window.title("Rate our food")
window.geometry("444x300")

def display():
    with open("ratings.txt",'a') as f:
        f.write(f"{slider1.get()} out of 10\n")
    
    tmsg.showinfo("Than you!","Thanks for rating our food")

Label(text="how was the food, please rate our food",font="Times 15 italic").pack()
slider1=Scale(window, from_ = 0,to=10,orient=HORIZONTAL)
slider1.pack()
Button(window,text="Submit",command=display).pack()

window.mainloop()