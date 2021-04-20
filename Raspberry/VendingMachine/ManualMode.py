import time
import RPi.GPIO as gpio
# from datetime import datetime
from tkinter import *
import tkinter as tk
from tkinter.ttk import Progressbar
from tkinter import ttk
import os
import sys
# import MFRC522
# import signal
# import subprocess

# Points setup

tier_1 = 40
tier_2 = 60
tier_3 = 100

# 24V Setup
DCPin1 = 35 # Row 1
DCPin2 = 33 # Row 2
DCPin3 = 31 # Row 3


def gpioSetup():
    gpio.setmode(gpio.BOARD)

    # GND setup
    gpio.setup(37, gpio.OUT) # Column 1
    gpio.setup(38, gpio.OUT) # Column 2
    gpio.setup(36, gpio.OUT) # Column 3
    gpio.setup(32, gpio.OUT) # Column 4
    gpio.setup(26, gpio.OUT) # Column 5



gpioSetup()

def motorOff(): # turn all motor output OFF
    gpio.setmode(gpio.BOARD)
    gpio.output(37, False)
    gpio.output(38, False)
    gpio.output(36, False)
    gpio.output(32, False)
    gpio.output(26, False)


def motorStop(): # turn all motor output OFF
    gpio.setmode(gpio.BOARD)
    gpio.setup(37, gpio.OUT) # Column 1
    gpio.setup(38, gpio.OUT) # Column 2
    gpio.setup(36, gpio.OUT) # Column 3
    gpio.setup(32, gpio.OUT) # Column 4
    gpio.setup(26, gpio.OUT) # Column 5
    gpio.output(37, False)
    gpio.output(38, False)
    gpio.output(36, False)
    gpio.output(32, False)
    gpio.output(26, False)
    gpio.cleanup()
    txt.delete(0)
    txt.delete(0)

motorOff() # Initial state for motor is OFF

UIDinput_global = 1



def elseif(column):
    if (column == "a"):
        print("Column A")  # GPIO Motor Control put here
        # waitPrizeAudio.play()
        gpio.output(37, True)
        time.sleep(2.35)
        motorStop()
        print("stopped")


    elif (column == "b"):
        print("Column B")
        # waitPrizeAudio.play()
        gpio.output(38, True)
        time.sleep(2.35)
        motorStop()


    elif (column == "c"):
        print("Column C")
        # waitPrizeAudio.play()
        gpio.output(36, True)
        time.sleep(2.35)
        motorStop()


    elif (column == "d"):
        print("Column D")
        # waitPrizeAudio.play()
        gpio.output(32, True)
        time.sleep(2.35)
        motorStop()


    elif (column == "e"):
        print("Column E")
        # waitPrizeAudio.play()
        gpio.output(26, True)
        time.sleep(2.35)
        motorStop()


    else:
        print("Invalid Selection")
        lbl.configure(text="Invalid Selection")
        window.update()
        time.sleep(5)


    txt.focus()

def switch(select):
    # select = str(input("Enter Letter Followed by Number: "))  # Input Keypad, letter then number and press enter
    row = select[0]
    column = select[1]
    gpioSetup()

    if (row == '3'):
        print("Row 3")
        # LEDRowA()
        gpio.setup(DCPin3, gpio.OUT) # Row 3

        elseif(column)

        return tier_3

    elif (row == '2'):
        print("Row 2")
        # LEDRowB()
        gpio.setup(DCPin2, gpio.OUT) # Row 2
        elseif(column)
        return tier_2

    elif (row == '1'):
        print("Row 1")
        # LEDRowC()
        gpio.setup(DCPin1, gpio.OUT) # Row 1
        elseif(column)
        return tier_1

    else:
        print("Invalid Selection")
        lbl.configure(text="Invalid Selection")
        window.update()
        # notEnoughPointsAudio.play()
        time.sleep(5)
        

window = tk.Tk()

window.title("G2G0 Vending Machine")

window.geometry('1000x100')
window.attributes("-fullscreen", True)

window.configure(background= 'white')

blank = Label(window, text="Ctrl to Exit")
blank.grid(column=0, row=3)

lbl = Label(window, text="G2G0 Vending Machine", font=("Arial Bold", 50))

lbl.grid(column=1, row=4)

lbl.configure(background= 'white')

selectiontext = Label(window, text="Manual Mode", font=("Arial Bold", 30))

selectiontext.grid(column=1, row=5)

selectiontext.configure(background= 'white')

large_font = ('Verdana',50)

txt = Entry(window,width=10,font=large_font)

txt.grid(column=1, row=6)

def runClick(i):
    clicked(UIDinput_global)

def clicked(UIDinput, event=None):
    if (UIDinput == 0):
        return

    res = "Selection: " + txt.get()
    lbl.configure(text= res)
    txt.focus()
    select = str(txt.get())
    switch(select)


def close(event=None):
    window.destroy()

#btn = Button(window, text="Enter", command=runClick)

#btn.grid(column=1, row=7)

ctrl = Button(window, text="Exit", command=close)

ctrl.grid(column=0, row=0)

txt.bind('<Return>', runClick)

nametxt = Label(window, text="Teachers only!", font=("Arial Bold", 30), background= 'white' )
nametxt.grid(column=1, row=8)


# bartxt = Label(window, text="Points:", font=("Arial Bold", 80) )
# bartxt.grid(column=1, row=10)

style = ttk.Style()

style.theme_use('default')

style.configure("TProgressbar", background='yellow', thickness=100)

bar = Progressbar(window, length=500, style='black.Horizontal.TProgressbar')

points = 100

bar['value'] = 100

bar.grid(column=1, row=11)




def resetDisplay():
    motorStop()
    # os.execv(sys.argv[0], sys.argv)
    # os.execv(__file__, sys.argv)
    # os.execv(sys.executable, ['python'] + sys.argv) # reset program
    #  os.execv('/home/pi/Desktop/VendingMachine/ManualMode.py', [''])
    # os.execl(sys.executable, sys.executable, *sys.argv)
    os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)
    # os.execv(sys.executable,
    #         [sys.executable, os.path.join(sys.path[0], __file__)] + sys.argv[1:])


def clear(self):
    motorStop()
    txt.delete(0)
    txt.delete(0)
    txt.delete(0)


window.bind("<Escape>", clear) # Esc to reset
window.bind('<Control_L>', close)



try:
    window.update_idletasks()
    txt.focus()
    window.update()
    window.update_idletasks()


except ValueError:
# Handle the exception
    print('Error')
    window.update()
