from tkinter import *
window=Tk()
window.title("Newspaper")
window.geometry("1255x933")
window.minsize(1255,933)
window.maxsize(1255,933)
t = Frame(window,width=100)
t.pack()
lo=Label(t,text="Aashutosh Express News",font="Comic-Sans-MS 30 bold")
lo.pack(anchor="center")
ko=Label(t,text="1st May,2020",font="Verdana 9 italic")
ko.pack()
x=Frame(window,width=40)
x.pack(anchor="n",side=LEFT,fill=NONE)
'''
p=PhotoImage(file="1.png")
p1=Label(x,image=p)
p1.pack()

w=PhotoImage(file="Can you answer it _.png")
w1 = Label(x,image=w)
w1.pack(side=BOTTOM,pady=50)
w2=PhotoImage(file="Peroidic tale.png")
w3 = Label(x,image=w2)
w3.pack()'''

horse=Frame(window,width=1900,height=1000)
horse.pack(anchor="s")

text=Label(horse,text="""Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.

Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment.
Older people, and those with underlying medical problems like cardiovascular disease, diabetes, chronic respiratory disease, and cancer are more likely to develop serious illness.

The best way to prevent and slow down transmission is be well informed about the COVID-19 virus, the disease it causes and how it spreads.
Protect yourself and others from infection by washing your hands or using an alcohol based rub frequently and not touching your face. 

The COVID-19 virus spreads primarily through droplets of saliva or discharge from the nose when an infected person coughs or sneezes
 ,so it’s important that you also practice respiratory etiquette (for example, by coughing into a flexed elbow).

At this time, there are no specific vaccines or treatments for COVID-19. However, there are many ongoing clinical trials evaluating potential treatments. 
WHO will continue to provide updated information as soon as clinical findings become available.

Stay informed:

Protect yourself: advice for the public
Myth busters
Questions and answers
Situation reports
All information on the COVID-19 outbreak
COVID-19 affects different people in different ways. Most infected people will develop mild to moderate illness and recover without hospitalization.

Most common symptoms of Coronavirus are:

fever.
dry cough.
tiredness.
Less common symptoms:

aches and pains.
sore throat.
diarrhoea.
conjunctivitis.
headache.
loss of taste or smell.
a rash on skin, or discolouration of fingers or toes.
Serious symptoms:

difficulty breathing or shortness of breath.
chest pain or pressure.
loss of speech or movement.
Seek immediate medical attention if you have serious symptoms.  Always call before visiting your doctor or health facility. 

People with mild symptoms who are otherwise healthy should manage their symptoms at home. 

On average it takes 5–6 days from when someone is infected with the virus for symptoms to show, however it can take up to 14 days.""",borderwidth=10,relief=SUNKEN)
text.pack()

window.mainloop()