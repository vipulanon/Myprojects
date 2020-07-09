from tkinter import *

def getvals():
    print(f"The value of user is {fnamevalue.get()}")
    print(f"The value of password is {lnamevalue.get()}")

    with open("records.txt", "a") as f:
        f.write(f"{fnamevalue.get(), lnamevalue.get()}\n")

root = Tk()

root.geometry("500x400")

Label(root, text="Dance Club", fg = "green", font = "verdana 24 bold").grid(row = 0, column = 5, pady = 5)
fname = Label(root, text = "First Name")
lname = Label(root, text = "Last Name")

fname.grid(row = 1, pady = 5)
lname.grid(row = 2, pady = 5)

fnamevalue = StringVar()
lnamevalue = StringVar()

fnameentry = Entry(root, textvariable = fnamevalue)
lnameentry = Entry(root, textvariable = lnamevalue)

fnameentry.grid(row = 1, column = 1, pady = 5, padx = 10)
lnameentry.grid(row = 2, column = 1, pady = 5, padx = 10)

Button(text = "Submit", bg = "grey", command = getvals).grid(pady = 5)

root.mainloop()

