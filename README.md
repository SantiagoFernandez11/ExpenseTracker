This is a personal project I took on to better keep track of my bank 
account's expenses. 

The code is simple, it utilizes pandas and gspread libraries to upload 
multiple data frames to a Google sheet. The first worksheet has all time 
transactions on one data frame and the second one that's printed to the 
right of it has a simple rundown of those transactions: amount in, amount 
out, cashflow. These data frames have been customized to improve 
efficiency when reading; the transactions are sorted by their "Date" 
column, ordering it from most recent at the top and the oldest at the 
bottom. As for the rundown data frame, the calculations are all done in 
the python code. This process is duplicated on the following two 
worksheets, showing all transactions from the last three months and its 
rundown, then the last month and its respective rundown.
