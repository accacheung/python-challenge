import os
import csv

# Path to collect data from the Resources folder
budget_dataCSV = os.path.join("../Resources", 'budget_data.csv')

# Define the function and have it accept the 'budgetdata' as its sole parameter
def analysis(budgetdata):

# Find the total number of months included in the dataset
    totalmonths = len(budgetdata[0])

# Find the total net amount of "Profit/Losses"
    totalpl = int(budgetdata[1])
    
# Find the average change in "Porfit/Losses"
    

# Find the greatest increase in profits
    

# Find the greatest decrease in losses


# Print out results
    print(f"Total number of months: {str(totalmonths)}")
    print(f"Net Amount: {str(totalpl)}")
   

# Read in the CSV file
with open(budget_dataCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

