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

"""
sales = SHEET.worksheet("sales") # sales is the name of the first excel worksheet

data = sales.get_all_values()
print(data)
"""

def get_sales_data():
    """
    Get sales figures input from the user.
    """
    
    """
    #a
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here: ")
    # print(f"The data provided is {data_str}")
    sales_data = data_str.split(",") #split() method returns the broken up values as a list
    # print(sales_data)
    validate_data(sales_data) # calling the functin
    """
    #b repeat request/continue to repeate

    while True:
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: ")

        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("Data is valid!")
            break # the code will repeate it self until valid data and then break

    return sales_data


def validate_data(values):
    print(values)
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    (em: 1 -we check if there's exactly 6 values:
    2 -we check if all the values inside our data 
    can be converted into integers)
    """
    try:
        [int(value) for value in values] #2
        if len(values) != 6: #1
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        #b
        return False
    #b
    return True 


def update_sales_worksheet(data):
    """
    #c
    Update sales worksheet, add new row with the list data provided
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    #access sales worksheet from Google Sheet
    sales_worksheet.append_row(data)
    #adds new row to the end in the worksheet selected
    print("Sales worksheet updated successfully.\n")
    #user feedback and narrow down bugs



#b

data = get_sales_data()
# print(data)

#c
sales_data = [int(num) for num in data]
update_sales_worksheet(sales_data)

