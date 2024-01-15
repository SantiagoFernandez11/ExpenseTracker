import gspread
import pandas as pd
from datetime import datetime, timedelta

def threeMonthsDataFrame(gc):
    # Setting the columns that will be read from the bank transaction CSV file and reading those columns into a dataframe object
    # showing the last three months's transactions
    use_cols = ["Date", "Name", "Memo","Amount"]
    threeMonthsDF = pd.read_csv('/Users/santiagofernandez/eclipse/PersonalProjects/ExpenseTracker/Chequing.CSV', usecols = use_cols)

    # Convert the date column to a pandas datetime object then sorting the dates from most recent at the top to oldest at the bottom
    threeMonthsDF['Date'] = pd.to_datetime(threeMonthsDF['Date'])   
    threeMonthsDF_sorted = threeMonthsDF.sort_values(by='Date', ascending=False)   

    #Finding the date three months ago
    three_months_ago = datetime.now() - timedelta(days=90)

    # Filter the rows based on the date column
    threeMonthsDF_sorted = threeMonthsDF_sorted[threeMonthsDF_sorted['Date'] >= three_months_ago]

    # Convert datetime columns to string representation
    threeMonthsDF_sorted['Date'] = threeMonthsDF_sorted['Date'].dt.strftime('%Y-%m-%d')
    threeMonthsDF_sorted = threeMonthsDF_sorted.fillna('')

    try:
        worksheet = gc.open('ExpenseTracker').worksheet('ThreeMonths')
    except gspread.exceptions.SpreadsheetNotFound as e:
        print(f"Spreadsheet not found. Details: {e}")

    # Writing the dataframe to a sheet 
    worksheet.update([threeMonthsDF_sorted.columns.values.tolist()] + threeMonthsDF_sorted.values.tolist())

    # Return the DataFrame
    return threeMonthsDF_sorted

def threeMonthsRundownDataFrame(gc, threeMonthsDF):
    # Amount that came into the account
    amountIn = threeMonthsDF[threeMonthsDF['Amount'] > 0]['Amount'].sum()

    # Amount going out of the account
    amountOut = threeMonthsDF[threeMonthsDF['Amount'] < 0]['Amount'].sum()

    # Cashflow
    cashFlow = threeMonthsDF['Amount'].sum()

    threeMonthsRundownDF = pd.DataFrame({'Amount In': [amountIn],
                        'Amount Out': [amountOut],
                        'Cashflow': [cashFlow]})
    
    try:
        worksheet = gc.open('ExpenseTracker').worksheet('ThreeMonths')
        print("Second worksheet is opened")
    except gspread.exceptions.SpreadsheetNotFound as e:
        print(f"Spreadsheet not found. Details: {e}")

    # Convert the dataframe to a list of lists
    values = threeMonthsRundownDF.values.tolist()

    # Add the dataframe's column headers
    values.insert(0, threeMonthsRundownDF.columns.tolist())

    start_cell = 'F1'

    # Update the worksheet with the DataFrame
    worksheet.update(start_cell, values, value_input_option='USER_ENTERED')