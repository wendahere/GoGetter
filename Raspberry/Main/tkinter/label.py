from tkinter import *
#import tkinter as tk
from tkinter.ttk import Progressbar

from tkinter import ttk
import time
# import RPi.GPIO as GPIO
# from mfrc522 import SimpleMFRC522

# reader = SimpleMFRC522()

window = Tk()

window.title("G2G0 Vending Machine")

window.geometry('1000x500')

blank = Label(window, text=" ")
blank.grid(column=0, row=3)

lbl = Label(window, text="Please Tap your card", font=("Arial Bold", 50))

lbl.grid(column=1, row=4)

selectiontext = Label(window, text="Input your selection", font=("Arial Bold", 30))

selectiontext.grid(column=1, row=5)

txt = Entry(window,width=100)

txt.grid(column=1, row=6)

def clicked(event=None):
    res = "Selection: " + txt.get()
    lbl.configure(text= res)
    print(txt.get())
    txt.focus()

btn = Button(window, text="Enter", command=clicked)

btn.grid(column=1, row=7)

txt.bind('<Return>', clicked)

#txt = Entry(window,width=10, state='disabled')

# txt.focus()

bartxt = Label(window, text="Points:", font=("Arial Bold", 30) )
bartxt.grid(column=1, row=10)

style = ttk.Style()

style.theme_use('default')

style.configure("black.Horizontal.TProgressbar", background='green')

bar = Progressbar(window, length=500, style='black.Horizontal.TProgressbar')

points = 0

bar['value'] = points

bar.grid(column=1, row=11)

window.mainloop()