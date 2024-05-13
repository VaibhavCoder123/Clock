

from tkinter import*
from tkinter.ttk import*
import colorsys as cs
from random import randint
from time import strftime, time

root = Tk()
root.title("Clock")


def color_convert(rgb):
    return "#%02x%02x%02x" % rgb 

lable = Label(root, font=("ds-digital", 80), background = "black",foreground="#00FF00")
# lable = Label(root, font=("ds-digital", 80), background = "black", foreground="#00FF00")

def ticktock():
    a = int(time())
    rand_number = randint(0,255)
    print(((((a+rand_number)%255), ((a-rand_number)%255),((a+rand_number)%255))))
    string = strftime('%H:%M:%S %p')
    lable.config(text=string, foreground=color_convert((((a+rand_number)%255), ((a-rand_number)%255),((a+rand_number)%255))) )
    lable.after(100, ticktock)

lable.pack(anchor='center')
ticktock()

mainloop()