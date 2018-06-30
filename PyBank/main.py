import os
import csv

# Path to collect data from the Resources folder
budgetCSV = os.path.join('Resources', 'budget_data.csv')
# Path to create new text file for results
PyBankResults = os.path.join('PyBankResults.txt')


# Define and set variables
Totalmonths = 0
PreviousPL = 0
ChangeinRevenue = []
GreatestIncrease = ["", 0]
GreatestDecrease = ["", 99999999]
TotalPL = 0

# Read in CSV file
with open(budgetCSV, 'r') as csvfile:
    csvfile = csv.DictReader(csvfile)

    for row in csvfile:

        # Track the total
        Totalmonths = Totalmonths + 1
        TotalPL = TotalPL + int(row["Revenue"])

        # Track the revenue change
        ChangeperYear = int(row["Revenue"]) - PreviousPL
        PreviousPL  = int(row["Revenue"])
        ChangeinRevenue = ChangeinRevenue + [ChangeperYear]
        
        # Calculate the greatest increase
        if (ChangeperYear > GreatestIncrease[1]):
            GreatestIncrease[0] = row["Date"]
            GreatestIncrease[1] = ChangeperYear

        # Calculate the greatest decrease
        if (ChangeperYear < GreatestDecrease[1]):
            GreatestDecrease[0] = row["Date"]
            GreatestDecrease[1] = ChangeperYear

# Calculate the Average Revenue Change
    for Averagechange in range(len(ChangeinRevenue)):
        Averagechange = sum(ChangeinRevenue) / len(ChangeinRevenue)

output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {Totalmonths}\n"
    f"Total: ${TotalPL}\n"
    f"Average Change: ${Averagechange}\n"
    f"Greatest Increase in Profits: {GreatestIncrease[0]} (${GreatestIncrease[1]})\n"
    f"Greatest Decrease in Profits: {GreatestDecrease[0]} (${GreatestDecrease[1]})\n")

print(output)

# Export text file
with open(PyBankResults, "w") as txt_file:
    txt_file.write(output)