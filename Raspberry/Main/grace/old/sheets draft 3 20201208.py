import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

INSUFFICIENT_POINTS = -1
UID_NOT_FOUND = -2

spreadSheetIDValue = "1uqCwaVqo4EV3DC4Ue8bpi4BdwVLwzTG1w_xq6YTyxEU"

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)

client = gspread.authorize(creds)

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

UID = int(input("Please input UID: ")) #make sure UID is a valid code

#Make sure UID is valid, check type
if (type(UID) == int):
    sheet = findSheet(UID)

    if (sheet == UID_NOT_FOUND):
        print("User not found, please try again.")
    else:
        # Open sheet
        # workingSheet = client.open("database").worksheet(sheet)
        sheetsData = sheet.get_all_records()

        row = findRow(sheetsData, UID)
        details = findDetails(sheetsData, row)
        points = getPoints(sheet, row, details)

        print(details)

        pointstodeduct = int(
            input("Please input points to deduct: "))  # make sure that the points that is deducted is vaild

        remainingPoints = deductPoints(points, pointstodeduct)

        if (remainingPoints == INSUFFICIENT_POINTS):
            # INSUFFICIENT_POINTS
            print("Insufficient Points")
        else:
            # Update database
            updateSheet(sheet, row, remainingPoints)

            print(f"The updated points: {remainingPoints}")
else: #UID is not integer value





#data[rownumber].dict

#print(indexValue)

#for i in data:

#for i in range(totalRows):
#    cellValue = sheet.cell(i+1, 1).value
#    print(cellValue)
#    if (UIDInput == cellValue):
#        print(cellValue)
#        break


#print(rows)

#for loop to check though all the columns and stop at the correct UID, if not say there is an invaild UID

#if vaild UID, save the row number

#display the information of the user

#get the person to input the value to minus from the database

#check input to minus is a number, and check that it is at least more or equal to the number in the database

#if ok, then use the number in the database and minus from the input.

#update the database with the new result, and let the user know the operation is successful, and show result. (Display)

#dispese prize

#go back to the normal screen

column = sheet.col_values(3)
row = sheet.row_values(3)
cell = sheet.cell(1,2).value


#insertRow = ["hello", 5, "red", "blue"]
#sheet.add_rows(insertRow, 4)  # Insert the list as a row at index 4

#sheet.update_cell(2,2, "CHANGED")  # Update one cell

#pprint(row)

# /* sheetsID 1uqCwaVqo4EV3DC4Ue8bpi4BdwVLwzTG1w_xq6YTyxEU
# api key=AIzaSyDoQGn2-znSaFRPN9Ks_ZUWyXL4NxMKIEY */