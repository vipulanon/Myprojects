from tkinter import *


window=Tk()
window.title("scrollbar")
window.geometry("544x244")
s=Scrollbar(window)
s.pack(side=RIGHT,fill=Y)
#tt="Government of India is taking all \nnecessary steps to ensure that we are prepared \nwell to face the challenge and\n threat posed by the growing \npandemic of COVID-19 the Corona Virus.\n With active support of \nthe people of India, we have \nbeen able to contain the spread of\n the Virus in our country. \nThe most important factor in\n preventing the spread of the \nVirus locally is to empower the\n citizens with the right \ninformation and taking precautions as per \nthe advisories being issued by Ministry\n of Health & Family Welfare.\n"
#L=Label(window,textvariable=tt,font="Times 15 italic",yscrollcommand=s.set).pack(fill="both")
#L=Text(window,yscrollcommand=s.set).pack(fill="both")
#s.config(command=L.yview)

window.mainloop()