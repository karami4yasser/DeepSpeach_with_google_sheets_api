import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("your_sheet_name").sheet1  # tape your sheet's name

#data = sheet.get_all_records()

#row = sheet.row_values(1)  # Get a specific row
#col = sheet.col_values(3)  # Get a specific column
#cell = sheet.cell(row_number,column_number).value
print(cell)  # Get the value of a specific cell

#sheet.add_rows(insertRow)  # Insert the list as a row at index 4

sheet.update_cell(1000,26, 2)  # Update one cell

cell = sheet.cell(1000,26).value
print(cell)
#numRows = sheet.row_count  # Get the number of rows in the sheet