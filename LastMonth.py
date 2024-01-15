import gspread
import pandas as pd
from datetime import datetime, timedelta

def lastMonthDataFrame(gc):
    # Setting the columns that will be read from the bank transaction CSV file and reading those columns into a dataframe object
    # showing the last month's transactions
    use_cols = ["Date", "Name", "Memo","Amount"]
    lastMonthDF = pd.read_csv('/Users/santiagofernandez/eclipse/PersonalProjects/ExpenseTracker/Chequing.CSV', usecols = use_cols)

    # Convert the date column to a pandas datetime object
    lastMonthDF['Date'] = pd.to_datetime(lastMonthDF['Date'])   
    lastMonthDF_sorted = lastMonthDF.sort_values(by='Date', ascending=False)   

    #Finding the date one month ago
    one_month_ago = datetime.now() - timedelta(days=30)

    # Filter the rows based on the date column
    lastMonthDF_sorted = lastMonthDF_sorted[lastMonthDF_sorted['Date'] >= one_month_ago]

    # Convert datetime columns to string representation
    lastMonthDF_sorted['Date'] = lastMonthDF_sorted['Date'].dt.strftime('%Y-%m-%d')
    lastMonthDF_sorted = lastMonthDF_sorted.fillna('')

    try:
        worksheet = gc.open('ExpenseTracker').worksheet('LastMonth')
    except gspread.exceptions.SpreadsheetNotFound as e:
        print(f"Spreadsheet not found. Details: {e}")

    # Writing the dataframe to a sheet 
    worksheet.update([lastMonthDF_sorted.columns.values.tolist()] + lastMonthDF_sorted.values.tolist())

    # Return the DataFrame
    return lastMonthDF_sorted

def lastMonthRundownDataFrame(gc, lastMonthDF):
    # Amount that came into the account
    amountIn = lastMonthDF[lastMonthDF['Amount'] > 0]['Amount'].sum()

    # Amount going out of the account
    amountOut = lastMonthDF[lastMonthDF['Amount'] < 0]['Amount'].sum()

    # Cashflow
    cashFlow = lastMonthDF['Amount'].sum()

    lastMonthRundownDF = pd.DataFrame({'Amount In': [amountIn],
                        'Amount Out': [amountOut],
                        'Cashflow': [cashFlow]})
    
    try:
        worksheet = gc.open('ExpenseTracker').worksheet('LastMonth')
        print("Third worksheet is opened")
    except gspread.exceptions.SpreadsheetNotFound as e:
        print(f"Spreadsheet not found. Details: {e}")

    # Convert the dataframe to a list of lists
    values = lastMonthRundownDF.values.tolist()

    # Add the dataframe's column headers
    values.insert(0, lastMonthRundownDF.columns.tolist())

    start_cell = 'F1'

    # Update the worksheet with the DataFrame
    worksheet.update(start_cell, values, value_input_option='USER_ENTERED')