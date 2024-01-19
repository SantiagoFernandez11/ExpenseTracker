import pandas as pd
import gspread

def allTimeDataFrame(gc):
    # Setting the columns that will be read from the bank transaction CSV file and reading those columns into a dataframe object
    # showing all-time transactions
    use_cols = ["Date", "Name", "Memo","Amount"]
    allTimeDF = pd.read_csv('/Users/santiagofernandez/eclipse/PersonalProjects/ExpenseTracker/Chequing.CSV', usecols = use_cols)

    # Replace NaN values with an empty string or any other value
    allTimeDF = allTimeDF.fillna('')

    # Convert the date column to a pandas datetime object then sorting the dates from most recent at the top to oldest at the bottom
    allTimeDF['Date'] = pd.to_datetime(allTimeDF['Date'])
    allTimeDF_sorted = allTimeDF.sort_values(by='Date', ascending=False)

    # Convert datetime columns to string representation
    allTimeDF_sorted['Date'] = allTimeDF_sorted['Date'].dt.strftime('%Y-%m-%d')

    try:
        worksheet = gc.open('ExpenseTracker').worksheet('AllTime')
    except gspread.exceptions.SpreadsheetNotFound as e:
        print(f"Spreadsheet not found. Details: {e}")

    # Writing the dataframe to a sheet 
    worksheet.update([allTimeDF_sorted.columns.values.tolist()] + allTimeDF_sorted.values.tolist())

    return allTimeDF_sorted  # Return the DataFrame

def allTimeRundownDataFrame(gc, allTimeDF):

    # Amount that came into the account
    amountIn = allTimeDF[allTimeDF['Amount'] > 0]['Amount'].sum()

    # Amount going out of the account
    amountOut = allTimeDF[allTimeDF['Amount'] < 0]['Amount'].sum()

    # Cashflow
    cashFlow = allTimeDF['Amount'].sum()

    allTimeRundownDF = pd.DataFrame({'Amount In': [amountIn],
                        'Amount Out': [amountOut],
                        'Cashflow': [cashFlow]})
    
    try:
        worksheet = gc.open('ExpenseTracker').worksheet('AllTime')
        print("Worksheet is opened")
    except gspread.exceptions.SpreadsheetNotFound as e:
        print(f"Spreadsheet not found. Details: {e}")

    # Convert the dataframe to a list of lists
    values = allTimeRundownDF.values.tolist()

    # Add the dataframe's column headers
    values.insert(0, allTimeRundownDF.columns.tolist())

    start_cell = 'F1'

    # Update the worksheet with the DataFrame
    worksheet.update(start_cell, values, value_input_option='USER_ENTERED')



