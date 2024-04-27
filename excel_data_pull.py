# -------------- Pulling data from test Excel sheet and analyzing -------------- #
# Importing libraries
import pandas as pd
#import numpy as np


# Gets all categories from the data
def get_categories(df, colname='Category'):
    categories = df[colname].drop_duplicates()                # Gets categories & removes duplicates
    categories = categories.reset_index(drop=True)            # Resets index (which gets changed after removing dupes)
    return categories


# Extract entries matching selected category
def ext_category(df, category):
    return df[df.Category.isin([category])]     # Checks if entry matches category, returns if yes


# Get total income/spending of selected entries
def selected_spending(df):
    expense = sum(df[df['Income/Expense'] == 'E']['Amount'])
    income = sum(df[df['Income/Expense'] == 'I']['Amount'])
    total = income - expense
    return income, expense, total


# Calculates the current account balance of selected account
def account_balance(df, account):
    transaction_amounts = df[df['Account'] == account]
    _, _, balance = selected_spending(transaction_amounts)
    return round(balance, 2)


def get_accounts(df, colname='Account'):
    accounts = df[colname].drop_duplicates()  # Gets categories & removes duplicates
    accounts = accounts.reset_index(drop=True)  # Resets index (which gets changed after removing dupes)
    return accounts


# Defining constants
filename = 'finance_tracker_demo.xlsx'

# Getting data from Excel file
raw_transactions = pd.read_excel(filename, sheet_name='Transactions')

# Asking user for input to choose tasks
print('Hello! Welcome to CoinTrail. Please select the task you wish to perform.')
task_sel = input(
    '''
    1. List all accounts.
    2. List all categories.
    3. Show the transaction summary of a selected category.
    4. Check the current balance of an account.
    '''
)

# Showing selected task & running
print(f'You have selected task {task_sel}.')
if task_sel == '1':
    accs = get_accounts(raw_transactions)
    print(f'Your saved accounts are: \n{accs}')
elif task_sel == '2':
    cats = get_categories(raw_transactions)
    print(f'Available categories are: \n{cats}')
elif task_sel == '3':
    selected_cat = input('Which category\'s spending do you want to see?\n')
    inc, exp, tot = selected_spending(ext_category(raw_transactions, selected_cat))
    print(f'''
    The transaction summary for category {selected_cat} is: 
    Income: {inc}  |  Expenses: {exp}  |  Total: {tot}
    ''')
elif task_sel == '4':
    selected_account = input('Which account would you like to see?\n')
    bal = account_balance(raw_transactions, selected_account)
    print(f'{selected_account}\'s balance: ', bal)
