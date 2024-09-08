from tkinter import *
import random

windows = Tk()
windows.title("my  gui")


def hi_fun():
    randomrange = random.randint(1, 5)
    if randomrange == 1:
        e = "green"
        f = "green"
    elif randomrange == 2:
        e = "blue"
        f = "blue"
    elif randomrange == 3:
        e = "yellow"
        f = "yellow"
    elif randomrange == 4:
        e = "black"
        f = "black"
    else:
        e = "red"
        f = "red"
    display.config(text=e, fg="black", bg=f)


windows.option_add("*Font", "Helvetica 200")

btn1 = Button(windows, text="click me", command=hi_fun)
btn1.pack()
display = Label(windows, text="")
display.pack()

windows.mainloop()

"""
from tkinter import *


windows = Tk()
windows.title("my  gui")


def hi_fun():
    global change
    
    if change == False:
        display.config(text="green", fg="black", bg="green")
    else:
        display.config(text="red", fg="black", bg="red")
    change = not change

change = False
btn1 = Button(windows, text="click me", command=hi_fun)
btn1.pack()
display = Label(windows, text="red", fg="black", bg="red")
display.pack()
windows.mainloop()
"""
