##### Pulls finance data from Google Sheets #####
# Importing libraries
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# define the scope
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('finance-tracker-access.json', scope)

# authorize the clientsheet
client = gspread.authorize(creds)

# get the instance of the Spreadsheet
sheet = client.open('Finance Tracker')

# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(1)
sheets_all = sheet_instance.get_all_records()

print(sheets_all)
