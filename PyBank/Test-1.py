import os
import csv

# Path to collect data from the Resources folder
budgetdataCSV = os.path.join('..', 'Resources', 'budget_data.csv')

# Define the function and have it accept the 'budgetdata' as its sole parameter
def analysis(budgetdata):

# Find the total number of months included in the dataset
    totalmonths = len(budget_data[0])
    print(totalmonths)

# Find the total net amount of "Profit/Losses"
    totalpl = sum(int(budgetdata[1])
    print(totalpl)


avechange = totalpl/totalmonths
 print(f"Average Change: {str(avechange)}")
