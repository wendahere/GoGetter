import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

spreadSheetIDValue = "1uqCwaVqo4EV3DC4Ue8bpi4BdwVLwzTG1w_xq6YTyxEU"

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)

#service = build('drive', 'v4', credentials=creds)

client = gspread.authorize(creds)

sheet = client.open("database").sheet1

data = sheet.get_all_records()

UIDInput = int(input("Please enter UID: "))

#check if UID is number

#what is the total columns for google sheet?

totalRows = len(data) + 1

#totalRows = 1

#for dataSet in data:
#    totalRows = totalRows + 1

#data_range = sheet.get_data_range()
#rows = data.
#rows = data_range.get_rows()

#range_names = [
    # Range names ...
#]
#result = service.spreadsheets().values().batchGet(
#    spreadsheetId=spreadSheetIDValue, ranges=range_names).execute()
#ranges = result.get('valueRanges', [])
#print('{0} ranges retrieved.'.format(len(ranges)))

#print("Number of rows: ")
#print(totalRows)

i = 1
dataMatched = False

for dataSet in data:
    UIDValue = dataSet["UID"]
    if (UIDValue == UIDInput):
        dataMatched = True
        break

    i = i + 1

if (dataMatched):
    rowToEdit = i - 1

    name = data[rowToEdit]["Name"]
    points = data[rowToEdit]["Points"]


    print(f"{name} has {points} points")
    deductPoints = int(input("Please input how many points to deduct: "))

    while deductPoints > points:
        print(f"{name} has {points} points")
        deductPoints = int(input("Error! Please input how many points to deduct (Less than or equal to how many points he/she has): "))

    updatedPoints = points - deductPoints

    print(f"Points left: {updatedPoints}")

    #edit points
    sheet.update_cell(rowToEdit + 2,4, updatedPoints)  # Update points (2 is to match the row, 4 is the "points" column)


else: #Means UID does not match
    rowToEdit = 0


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