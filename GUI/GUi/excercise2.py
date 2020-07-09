from tkinter import *


window=Tk()

window.geometry("644x444")
window.title("Change dimensios")
Label(text="width ").grid()
Label(text="height ").grid(row=1)

w=IntVar()
h=IntVar()
Entry(window,textvariable=w).grid(row=0,column=1)
Entry(window,textvariable=h).grid(row=1,column=1)
k=window.geometry(f"{w}x{h}")
def k():
    wd=w.get()
    ht=h.get()
    window.geometry(f"{wd}x{ht}")

Button(window,text="Change dimensions",command=k).grid()

window.mainloop()