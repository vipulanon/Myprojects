from tkinter import *
from PIL import Image,ImageTk




window=Tk()

def getval():
    print("NAme:",name.get())
    print("Age:",age.get())
    print("E_mail:",email.get())
    print("password:",password.get())

    with open("Form.txt","a") as f:
        f.write(f"Name: {name.get()}\nAge: {age.get()}\nemail: {email.get()}\n\n")
    return 0

window.geometry("700x500")
window.title("Form")
label1=Label(text="Name").grid()
label2=Label(text="Age").grid(row=1)
label3=Label(text="E-mail").grid(row=2)
label2=Label(text="Password").grid(row=3)

name=StringVar()
age=StringVar()
email=StringVar()
password=StringVar()

name_entry=Entry(window,textvariable=name).grid(row=0,column=1)
age_entry=Entry(window,textvariable=age).grid(row=1,column=1)
email_entry=Entry(window,textvariable=email).grid(row=2,column=1)
password_entry=Entry(window,textvariable=password).grid(row=3,column=1)

b1=Button(window,text="Submit",command=getval).grid()

window.mainloop()