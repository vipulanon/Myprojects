from tkinter import *
from PIL import Image,ImageTk
import os
import datetime


root=Tk()

w=500
h=400
#width x length
root.geometry("500x400")
root.title("Newspaper")
date=datetime.date.today()
d2 = date.strftime("%d %B, %Y")
#min size-width,length
root.minsize(300,150)

label1=Label(text="The Hindu Times",font="Times 20 bold")
label1.pack()
label2=Label(text=str(d2),font="Times 7 bold")
label2.pack(side="left",anchor="nw")
c1=Canvas(root,width=w,height=h)
c1.pack()
c1.create_image(0,200)

#max-length-width,length
#root.maxsize(1200,800)

#label
#label1=Label(text="Ready!",borderwidth=3,relief=SUNKEN,padx=22)
#label1.pack(side=BOTTOM)

'''#image in labels using tkinter
photo=PhotoImage(file="1.png")
label2=Label(image=photo)
label2.pack()'''
#important packing labels
'''fill-X and Y
padx and pady-padding 
anchor-"nw","ne"
side-TOP,BOTTOM,LEFT,RIGHT
'''
'''
#image using pillow
image=Image.open("gui.jpg")
photo=ImageTk.PhotoImage(image)

label3=Label(image=photo)
label3.pack()
'''
#important label options
'''text-add the text
bg-background
fg-foreground
font-sets the font
padx=x padding
pady=y padding
relief=border styling=SUNKEN,RAISED,GROOVE,RIDGED'''


#event loop
root.mainloop()
