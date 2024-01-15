import pandas as pd
import gspread
from AllTime import allTimeDataFrame, allTimeRundownDataFrame
from ThreeMonths import threeMonthsDataFrame, threeMonthsRundownDataFrame
from LastMonth import lastMonthDataFrame, lastMonthRundownDataFrame

def main():
    # Loading credentials and authorizing gspread
    gc = gspread.service_account(filename = '/Users/santiagofernandez/eclipse/PersonalProjects/ImportantFiles/expensetracker-410304-47baf1ad714c.json')
    print("Service account created")

    # Call the all-time data frame
    allTimeDF = allTimeDataFrame(gc)

    # Call the all-time rundown data frame 
    allTimeRundownDataFrame(gc, allTimeDF)

    # Call the three months data frame 
    threeMonthsDF = threeMonthsDataFrame(gc)

    # Call the three months rundown data frame
    threeMonthsRundownDataFrame(gc, threeMonthsDF)

    # Call the last month data frame
    lastMonthDF = lastMonthDataFrame(gc)

    # Call the last month rundown data frame
    lastMonthRundownDataFrame(gc, lastMonthDF)


if __name__ == "__main__":
    main()