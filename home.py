from tkinter import *

top=Tk()
top.title("Celsuis to Fahrenheit converter")
top.geometry("600x400")
top.config(background="light blue")

def convort():
    try:
        temp_cel=float(p.get())
        fahrenheit=(temp_cel*9/5)+32
        aswer.config(text=f"Temprature In Fahrenheit:{fahrenheit:.1f}")
    except:
        aswer.config(text="please enter a valid number")



text = Label(top,
                text="Celsius --> Fahrenheit",font=("Times New Roman",30)).place(x=150,
                                        y=10)
enter= Label(top,
                     text="Enter Temperature in Celsius ",font=("Times New Roman",15),bd='3')
enter.place(x=30,
                                            y=140)
aswer=Label(top,
        text="Temperature In Fahrenheit Is:",font=("Times New Roman",15),bg="light blue")
aswer.place(x=80,
                                                                                y=180)

p= Entry(top,
                width=20,font=("Arial",18))
p.place(x=280, y=140)

submit=Button(top,
              text="Convert",font=("Arial",20),command=convort)
submit.place(x=200, y=250)

top.mainloop()
