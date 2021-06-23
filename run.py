import gspread  
# import entire gspread library so that we can access any function, class or method within it
from google.oauth2.service_account import Credentials 
"""
imports the Credentials class, which is part of the service_account function from Google auth library
"""
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
# the scope lists the APIs that the program should access in order to run
# SCOPE_variable_ with capital letter = constant, that shouldn't changed.

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("love_sandwiches") # love_sandwiches name of spreadsheet_excel. Spreadsheet is a collection of one or more worksheets

sales = SHEET.worksheet("sales") # sales is the name of the first excel worksheet

data = sales.get_all_values()
print(data)



