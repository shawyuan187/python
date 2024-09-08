from tkinter import *

windows = Tk()
windows.title("my first gui")


def hi_fun():
    print("hi")
    display.config(text="hi", fg="red", bg="blue")


def clear_fun():
    display.config(text="", fg="white", bg="white")


# create a button
btn1 = Button(windows, text="meeee", command=hi_fun)
btn1.pack()
btn2 = Button(windows, text="clear", command=clear_fun)
btn2.pack()
#############################creat 標籤#################################
# create a label and pack it
# fg = foreground color
# bg = background color
display = Label(windows, text="")
display.pack()

windows.mainloop()
