import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import RPi.GPIO as GPIO
import MFRC522
import signal

continue_reading = True

INSUFFICIENT_POINTS = -1
UID_NOT_FOUND = -2
SHEET_NOT_FOUND = -3

spreadSheetIDValue = "1uqCwaVqo4EV3DC4Ue8bpi4BdwVLwzTG1w_xq6YTyxEU"
logsSpreadSheetIDValue = "1EjQIPAZD2wDNJ44Ue6UK--fPk2RL3HKWNnnTnQ0xAjU"

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)

client = gspread.authorize(creds)

# !/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Copyright 2014,2018 Mario Gomez <mario.gomez@teubi.co>
#
#    This file is part of MFRC522-Python
#    MFRC522-Python is a simple Python implementation for
#    the MFRC522 NFC Card Reader for the Raspberry Pi.
#
#    MFRC522-Python is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    MFRC522-Python is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with MFRC522-Python.  If not, see <http://www.gnu.org/licenses/>.
#




# Capture SIGINT for cleanup when the script is aborted
def end_read():
    print("Ending read.")
    continue_reading = False
    GPIO.cleanup()


# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print("Welcome to the MFRC522 data read")
# print ("Press Ctrl-C to stop.")

# This loop keeps checking for chips. If one is near it will get the UID and authenticate



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


def switch(points):
    select = str(input("Enter Letter Followed by Number: "))  # Input Keypad, letter then number and press enter
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
        return 0
    else:
        print("Invalid Selection")
        return 0



while continue_reading:

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
        end_read()
        # This is the default key for authentication
        key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)
        # Authenticate
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)
        if (type(UIDinput) == int):
            sheet = findSheet(UIDinput)
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

            print(details)

            pointstodeduct = int(
                switch(points))
            #    input("Please input points to deduct: "))  # make sure that the points that is deducted is vaild

            remainingPoints = deductPoints(points, pointstodeduct)

            if (remainingPoints == INSUFFICIENT_POINTS):
                # INSUFFICIENT_POINTS
                print("Insufficient Points")
            else:
                # Update database
                updateSheet(sheet, row, remainingPoints)
                updateLogs(UIDinput, details, remainingPoints, pointstodeduct)

                print(f"The updated points: {remainingPoints}")
        # else: #UID is not integer value

