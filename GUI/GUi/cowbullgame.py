from tkinter import *
import random
num=random.randrange(1000,9999,3)

window=Tk()

window.geometry("344x244")
window.title("CowbullGame")
Label(text="Guess The Number",font="lucida 20 bold").pack()
Label(text="Enter the number here").pack()
var=StringVar()
Entry(window,textvariable=var).pack()
def game():
    try:
        k=str(num)
        #print(num)
        num_1=[int(i) for i in k] 
        cow=0
        user_input=var.get()
        if len(user_input)!=4:
            print("write a 4 digit number plz!")
        a=[int(i) for i in user_input]
        cow=0
        bull=0
        for i in range(4):
            if num_1[i]==a[i]:
                cow+=1
        num_2=set(num_1)
        a_1=set(a)
        lst=num_2.intersection(a_1)
        lst=list(lst)
        bull=len(lst)-cow
        print("cow=",cow)
        print("bull=",bull)
        if cow==4:
            print("congrats!!") 
        else:
            print("try again!")
    except:
        print("Write a number plz!")
        print("Try again!")
Button(text="Try it!",command=game).pack(pady=15)
window.mainloop()