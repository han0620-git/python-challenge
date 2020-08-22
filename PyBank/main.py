import csv
import os

# filename = "budget_data.csv"
# path = "Resources"
# infile = os.path.join(path, filename)

infile = os.path.join("Resources", "budget_data.csv")

outfile = os.path.join("analysis", "pybank.txt")


monthsTotal = 0
netTotal = 0
previousBudget = 0
changeTotal = 0
greatestIncrease = 0
greatestDecrease = 0
greatestIncreaseDate = ""
greatestDecreaseDate = ""

with open(infile) as csvFile:
   
    csvFile.readline()

    rows = csv.reader(csvFile)
    changeCount = 0
    change = 0

    for row in rows:
        monthsTotal += 1
        currentBudget = int(row[1])
        netTotal += currentBudget

        if previousBudget != 0:
            change = currentBudget - previousBudget
            changeTotal += change
            changeCount += 1
            print(change)

        previousBudget = currentBudget

        if change > greatestIncrease:
            greatestIncrease = change
            greatestIncreaseDate = row[0]

        if change < greatestDecrease:
            greatestDecrease = change
            greatestDecreaseDate = row[0]

    print(f"change count: {changeCount}")
    print(f"total of changes: {changeTotal}")
   

# print(monthsTotal)
# print(netTotal)
# print(greatestIncreaseDate,greatestIncrease)
# print(greatestDecreaseDate,greatestDecrease)

# def print_results(results):
#     print(results)

output = f"""
Financial Analysis
----------------------------
Total Months: {monthsTotal}
Total: ${netTotal:,}
Average  Change: ${changeTotal/changeCount:.2f}
Greatest Increase in Profits: {greatestIncreaseDate} (${greatestIncrease:,})
Greatest Decrease in Profits: {greatestDecreaseDate} (${greatestDecrease:,})
"""



print(output)


with open(outfile, 'w') as outputFile:
    outputFile.write(output)
