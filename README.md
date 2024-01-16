This is a personal project I took on to better keep track of my bank 
account's expenses while learning how to use Google API and the pandas library.
This project also helped me further practice bash and using git commands in particular. 

The code is simple, it utilizes pandas and gspread libraries to upload data frames to
multiple worksheets on a Google sheet project.

The first worksheet has all-time transactions on one data frame and the second data frame 
is the "Rundown data frame", it's printed on the right side and has a simple rundown of the 
transactions: amount in, amount out, cash flow. The rundown data frame calculations are all
done in the Python code files named "AllTime.py", "ThreeMonths.py", and "LastMonth.py" respectively.

These data frames have been customized to improve efficiency when reading; the transactions are 
sorted by their "Date" column, ordering each transaction from the most recent at the top and the oldest
at the bottom. This process is duplicated on the following two worksheets, showing all transactions 
from the last three months and their rundown, then the last month and its respective rundown.

1) To properly copy and run this code if you'd like, there are a few things that you must do:
  - create a Google project with your Google developer account
  - enable Google Sheets and Google Drive API
  - create a service account and copy its JSON file to a secure folder on your desktop
    - make sure to copy the file's path when loading credentials and authorizing gspread on line 8 of main.py

2) Once that's all set, make sure to open a Google Sheets project and share it with the service account you 
made in step 1
  - Open three worksheets in your project, if you want to name them something specific go ahead, but make sure
  to change the worksheet names in the code

3) Download your bank statements directly from your bank account as a CSV file
   - when creating the data frames in the code, make sure to copy the correct path to your CSV files
   - use_cols = ["Date", "Name", "Memo","Amount"], these are the columns we will be selecting to use from the CSV
     file; however, if your CSV file uses different names, make sure to change that (e.g. instead of "Memo" it has "Type")
     
     
