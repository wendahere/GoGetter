import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import time
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
import os
import sys
import RPi.GPIO as GPIO
import MFRC522
import signal

UIDinput_global = 0

continue_reading = True

INSUFFICIENT_POINTS = -1
UID_NOT_FOUND = -2
SHEET_NOT_FOUND = -3

spreadSheetIDValue = "1uqCwaVqo4EV3DC4Ue8bpi4BdwVLwzTG1w_xq6YTyxEU"
logsSpreadSheetIDValue = "1EjQIPAZD2wDNJ44Ue6UK--fPk2RL3HKWNnnTnQ0xAjU"

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)

client = gspread.authorize(creds)



# Capture SIGINT for cleanup when the script is aborted
def end_read():
    print("Ending read.")
    continue_reading = False
    GPIO.cleanup()


# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print("Welcome to the MFRC522 data read")


def findUIDinSheet(sheet,UID):
    sheetData = sheet.get_all_records()

    i = 1
    dataMatched = False

    for dataSet in sheetData:
        UIDValue = dataSet["UID"]
        if (UIDValue == UID):
            return True

    return False

def findSheet(UID):
    #Get the list of sheets
    workbook = client.open("database")
    worksheet_list = workbook.worksheets() #list of all worksheets

    #start from sheet 1 to find UID excluding "Logs"

    for sheet in worksheet_list:
        # Ommit the "Logs" file
        if ("Log" not in sheet.title and "log" not in sheet.title):
            #If found Return sheet
            if ((findUIDinSheet(sheet, UID))):
                return sheet

    #If not found Return "-2"
    return UID_NOT_FOUND

def findRow(sheetData,UID): #output -> row number

    i = 1
    dataMatched = False

    for dataSet in sheetData:
        UIDValue = dataSet["UID"]
        if (UIDValue == UID):
            dataMatched = True
            break

        i = i + 1

    if (dataMatched):
        return i - 1

    else:  # Means UID does not match
        return UID_NOT_FOUND

def findDetails(sheetData,row): #output -> Dict with name, class, points
    return sheetData[row]

def getPoints(sheet, row, details):
    #Check if points is string, if string set to 0
    if (type(details["Points"]) == str):
        if(details["Points"] == ""):
            #Type string which is empty
            updateSheet(sheet, row, 0)
            return 0
        else:
            #Type string which is not empty
            updateSheet(sheet, row, 0)
            return 0
    elif (type(details["Points"]) == int):
        #Value is an integer
        return details["Points"]
    else:
        #Data is erronous
        updateSheet(sheet, row, 0)
        return 0

def deductPoints(points,pointstodeduct):
    if (points < pointstodeduct):
        return INSUFFICIENT_POINTS
    else:
        return points - pointstodeduct

def updateSheet(sheet,row,points):
    sheet.update_cell(row + 2, 4, points)  # Update points (2 is to match the row, 4 is the "points" column)
    sheet.update_cell(row + 2, 5, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

def findSheetWithNameLogs(name):
    # Get the list of sheets
    workbook = client.open("Logs")
    worksheet_list = workbook.worksheets()  # list of all worksheets

    # start from sheet 1 to find UID excluding "Logs"

    for sheet in worksheet_list:
        if (sheet.title == name):
            # If found Return sheet
            return sheet

    # If not found Return "SHEET_NOT_FOUND"
    return SHEET_NOT_FOUND

def updateLogs(UID, details, pointsRemaining, pointsToDeduct):
    #Find current month & year
    month = datetime.now().strftime("%m")
    year = datetime.now().strftime("%Y")

    #Concentate Logs with month and year
    logsName = "Logs " + str(month) + "/" + str(year)

    #Find the logs sheet (If cannot file, create new sheet)
    #Checking for sheet
    logsSheet  = findSheetWithNameLogs(logsName)

    if (logsSheet == SHEET_NOT_FOUND):
        # Creating new sheet
        workbook = client.open("Logs")
        workbook.add_worksheet(logsName, 500, 500)

        logsSheet = findSheetWithNameLogs(logsName)

        # Update the title

        # Updating Date
        logsSheet.update_cell(1, 1, "Date Updated")

        # Updating UID
        logsSheet.update_cell(1, 2, "UID")

        # Updating Name
        logsSheet.update_cell(1, 3, "Name")

        # Updating Class
        logsSheet.update_cell(1, 4, "Class")

        # Updating Year
        logsSheet.update_cell(1, 5, "Year")

        # Updating Points
        logsSheet.update_cell(1, 6, "Points (+/-)")

        # Updating Remaining Points
        logsSheet.update_cell(1, 7, "Remaining Points")

        # Updating the logs
        updateLogsData(logsSheet, UID, details, pointsRemaining, pointsToDeduct)
    else:
        # Updating the logs
        updateLogsData(logsSheet, UID, details, pointsRemaining, pointsToDeduct)

def updateLogsData(sheet, UID, details, pointsRemaining, pointsToDeduct):
    #Get list of all data in logs
    sheetsData = sheet.get_all_records()

    #Check for non occupied row
    i = 1

    for rowData in sheetsData:
        i  = i + 1

    #Updating Date
    sheet.update_cell(i + 1, 1, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    #Updating UID
    sheet.update_cell(i + 1, 2, UID)

    #Updating Name
    sheet.update_cell(i + 1, 3, details["Name"])

    #Updating Class
    sheet.update_cell(i + 1, 4, details["Class"])

    #Updating Year
    sheet.update_cell(i + 1, 5, str(findSheet(UID))[12:18]) #YEAR HERE

    #Updating Points
    changedPoints = "-" + str(pointsToDeduct)
    sheet.update_cell(i + 1, 6, changedPoints)

    #Updating Remaining Points
    sheet.update_cell(i + 1, 7, pointsRemaining)

def elseif(number):
    if (number == "1"):
        print("Column 1")  # GPIO Motor Control put here

    elif (number == "2"):
        print("Column 2")

    elif (number == "3"):
        print("Column 3")

    elif (number == "4"):
        print("Column 4")

    elif (number == "5"):
        print("Column 5")
    else:
        print("Invalid Selection")
        lbl.configure(text="Invalid Selection")
        window.update()
        time.sleep(5)
        resetDisplay()


def switch(select):
    #select = str(input("Enter Letter Followed by Number: "))  # Input Keypad, letter then number and press enter
    letter = select[0]
    number = select[1]

    if (letter == 'a' and points >= 100):
        print("Row A")
        # LEDRowA()
        elseif(number)
        return 100
    elif (letter == 'b' and points >= 60):
        print("Row B")
        # LEDRowB()
        elseif(number)
        return 60
    elif (letter == 'c' and points >= 40):
        print("Row C")
        # LEDRowC()
        elseif(number)
        return 40
    elif (points < 40):
        print("Insufficient Points")
        lbl.configure(text="Insufficient Points")
        window.update()
        time.sleep(5)
        resetDisplay()
    else:
        print("Invalid Selection")
        lbl.configure(text="Insufficient Points")
        window.update()
        time.sleep(5)
        resetDisplay()

window = Tk()

window.title("G2G0 Vending Machine")

window.geometry('1000x100')
window.attributes("-fullscreen", True)


blank = Label(window, text=" ")
blank.grid(column=0, row=3)

lbl = Label(window, text="Please Tap your card", font=("Arial Bold", 50))

lbl.grid(column=1, row=4)

selectiontext = Label(window, text="Input your selection", font=("Arial Bold", 30))

selectiontext.grid(column=1, row=5)

txt = Entry(window,width=100)

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
    pointstodeduct = int(switch(select))
    print(UIDinput)
    
    if (type(UIDinput) == int):
                sheet = findSheet(UIDinput)
                print(UIDinput)
                if (sheet == UID_NOT_FOUND):
                    print("User not found, please try again.")
                    lbl.configure(text="User not found")
                    window.update()
                    time.sleep(5)
                    resetDisplay()
                else:
                    # Open sheet
                        # workingSheet = client.open("database").worksheet(sheet)
                        sheetsData = sheet.get_all_records()

                        row = findRow(sheetsData, UIDinput)
                        details = findDetails(sheetsData, row)
                        points = getPoints(sheet, row, details)
                        remainingPoints = points - pointstodeduct

                        # Update details if any error to the points
                        details = findDetails(sheetsData, row)
                        if (remainingPoints == INSUFFICIENT_POINTS):
                            # INSUFFICIENT_POINTS
                            print("Insufficient Points")
                            lbl.configure(text="Insufficient Points")
                            window.update()
                            time.sleep(5)
                            resetDisplay()
                            
                        else:
                            # Update database
                            updateSheet(sheet, row, remainingPoints)
                            updateLogs(UIDinput, details, remainingPoints, pointstodeduct)
                            #print(f"The updated points: {remainingPoints}")
                            bartxt.configure(text="Updated Points: "+str(remainingPoints))
                            bar['value'] = points
                            window.update()
                            time.sleep(5)
                            resetDisplay()

btn = Button(window, text="Enter", command=runClick)

btn.grid(column=1, row=7)

txt.bind('<Return>', runClick)


nametxt = Label(window, text="Name:", font=("Arial Bold", 30) )
nametxt.grid(column=1, row=8)

bartxt = Label(window, text="Points:", font=("Arial Bold", 30) )
bartxt.grid(column=1, row=10)

style = ttk.Style()

style.theme_use('default')

style.configure("black.Horizontal.TProgressbar", background='green')

bar = Progressbar(window, length=500, style='black.Horizontal.TProgressbar')

points = 0

bar['value'] = 0

bar.grid(column=1, row=11)

def resetDisplay():
    bartxt.configure(text="Points: ")
    bar['value'] = 0
    nametxt.configure(text="Name: ")
    lbl.configure(text="Please tap your card")
    window.update()
    #os.execv(__file__, sys.argv)
    os.execv(sys.executable, ['python'] + sys.argv) #reset program

def resetDisplayEscape(self):
    bartxt.configure(text="Points: ")
    bar['value'] = 0
    nametxt.configure(text="Name: ")
    lbl.configure(text="Please tap your card")
    window.update()
    #os.execv(__file__, sys.argv)
    os.execv(sys.executable, ['python'] + sys.argv) #reset program

window.bind("<Escape>", resetDisplayEscape) #Esc to quit   
                 
try:
    window.update_idletasks()
    txt.focus()
    window.update()
    window.update_idletasks()
    
    while continue_reading:
        window.update()
        window.update_idletasks()

        # Scan for cards
        (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        # If a card is found
        if status == MIFAREReader.MI_OK:
            print("Card detected")

        # Get the UID of the card
        (status, uid) = MIFAREReader.MFRC522_Anticoll()

        # If we have the UID, continue
        if status == MIFAREReader.MI_OK:
            # Print UID
            print("Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3]))
            UIDinput=int(str(uid[0]) + str(uid[1]) + str(uid[2]) + str(uid[3]))
            print(UIDinput)
            print(type(UIDinput))
            
            UIDinput_global = UIDinput
            
            # This is the default key for authentication
            key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
            # Select the scanned tag
            MIFAREReader.MFRC522_SelectTag(uid)
            # Authenticate
            status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)
            if (type(UIDinput) == int):
                sheet = findSheet(UIDinput)
                print(UIDinput)
                if (sheet == UID_NOT_FOUND):
                    print("User not found, please try again.")
                else:
                    # Open sheet
                        # workingSheet = client.open("database").worksheet(sheet)
                        sheetsData = sheet.get_all_records()

                        row = findRow(sheetsData, UIDinput)
                        details = findDetails(sheetsData, row)
                        points = getPoints(sheet, row, details)

                        # Update details if any error to the points
                        details = findDetails(sheetsData, row)
                        
                        name = "Name: "+details["Name"] #using dict details)
                        nametxt.configure(text=name)
                        barpoints="Points: "+str(points)
                        bartxt.configure(text=barpoints)
                        bar['value'] = points
                        
                        
                        window.update() #update window
                        

                        print(details)
                        
except ValueError:
# Handle the exception
    print('Error')
    window.update()

