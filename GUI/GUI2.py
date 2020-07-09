from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.title("Second GUI")

root.geometry("500x400")

f1=Frame(root,bg="grey")
f1.pack(side=TOP)

f2=Frame(root,bg="grey",borderwidth=3,relief=SUNKEN)
f2.pack(anchor="nw")

label=Label(f1,text="Any Form",font="Times 20 italic")
label.pack(fill='x')

label2=Label(f2,text="""Skywatchers along a narrow band from west Africa to the Arabian Peninsula, 
India and southern China will witness on Sunday a dramatic “ring of fire” solar eclipse.
The partial phase of the eclipse will begin at 9.16 am. 
The annular phase will start at 10.19 am and end at 2.02 pm. 
The partial phase of the eclipse will end at 3.04 pm, the Ministry of Earth Sciences said.
“Close to noon, for a small belt in north India the eclipse will turn into a beautiful annular 
(ring-shaped) one since the Moon is not close enough to cover the Sun completely,” 
the Astronomical Society of India said on Saturday.""",font="Times 20 bold")
label2.pack()

photo=ImageTk.PhotoImage(Image.open("gui.jpg"))
photo1=ImageTk.PhotoImage(Image.open("eclipse.jpg"))

label3=Label(f2,image=photo)
label3.pack(anchor='nw')

label4=Label(f2,image=photo1)
label4.pack(side=TOP)

root.mainloop()