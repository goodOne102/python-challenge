# Python Homework - PyBank

import os
import csv
import numpy as np

csvpath = os.path.join('..', 'PyBank','budget_data.csv')
output_path = os.path.join("..", "output", "pyBank.txt")

#Array of all data
pyBankData = []
#List array of only profit
pyMoney = []
# List array of differences of profit/loss by month
pyDifference = []
# List array for outfile *** come back to this ** not used yet but this has to be the better way to write variables to file for consumption
pyBankResultsPrinted = []


netTotal = 0
averageProfitLoss = 0
totalSize = len(pyBankData)


with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    
    for row in csvreader:
        
        # Add all csv data into list array
        pyBankData.append(row)

# Add all profit/loss for net total
for i in pyBankData:

    netTotal = netTotal + int(i[1])
    #print(netTotal)

# Create list array with only money for profit/loss    
for n in pyBankData:
    #print(n)
    
    pyMoney.append(int([n][0][1]))
    
    #print("pyMoney",pyMoney)
    

totalMonths = (len(pyBankData))

# create a list of the differences between each data entry 
pyDifference = np.diff(pyMoney) 

# calculate the average change over the entire dataset for profit/loss
averageProfitLoss = ((np.sum(pyDifference)) / (totalMonths-1))

# locate the greaest increase in the list of differences
locateGreatestIncrease = int(np.argmax(pyDifference))
    # print (locateGreatestIncrease)
    # print ((pyBankData[locateGreatestIncrease+1][0]), max(pyDifference))

#locate the greatest decrease in losses between each data entry
locateGreatestDecrease = int(np.argmin(pyDifference))
    # print(locateGreatestDecrease)
    # print ((pyBankData[locateGreatestDecrease+1][0]), min(pyDifference))


# check for pyBankResultsPrinted = [] as array list or possibly dict for output to file 
with open("pyBank.txt","w") as pyBankResults:
    pyBankResults.write("-----------------------------\n")
    pyBankResults.write("Total Months: ")
    pyBankResults.write(str(totalMonths))
    pyBankResults.write("\nTotal: $")
    pyBankResults.write(str(netTotal))
    pyBankResults.write("\nAverage Change: $")
    pyBankResults.write(str(averageProfitLoss))
    pyBankResults.write("\nGreatest Increase in Profits: ")
    pyBankResults.write(str(pyBankData[locateGreatestIncrease+1][0]))
    pyBankResults.write("  ")
    pyBankResults.write(str(max(pyDifference)))
    
    pyBankResults.write("\nGreatest Decrease in Profits: ")
    pyBankResults.write(str(pyBankData[locateGreatestDecrease+1][0]))
    pyBankResults.write("  ")
    pyBankResults.write(str(min(pyDifference)))        

# print(pyBankResults)

print("-----------------------------")
print("Total Months: ", totalMonths)
print("Total: $", netTotal)
print("Average Change: $", round(averageProfitLoss))
print("Greatest Increase in Profits: ", (pyBankData[locateGreatestIncrease+1][0]),"  $", max(pyDifference))
print("Greatest Decrease in Profits: ", (pyBankData[locateGreatestDecrease+1][0]), "  $", min(pyDifference))
