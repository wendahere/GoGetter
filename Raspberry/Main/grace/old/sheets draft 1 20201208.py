import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)

client = gspread.authorize(creds)

sheet = client.open("database").sheet1

data=sheet.get_all_records()

column = sheet.col_values(3)
row = sheet.row_values(3)
cell = sheet.cell(1,2).value


#insertRow = ["hello", 5, "red", "blue"]
#sheet.add_rows(insertRow, 4)  # Insert the list as a row at index 4

#sheet.update_cell(2,2, "CHANGED")  # Update one cell

pprint(row)

# /* sheetsID 1uqCwaVqo4EV3DC4Ue8bpi4BdwVLwzTG1w_xq6YTyxEU
# api key=AIzaSyDoQGn2-znSaFRPN9Ks_ZUWyXL4NxMKIEY */