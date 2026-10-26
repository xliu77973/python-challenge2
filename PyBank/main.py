import os
import csv

# path to csv file
csv_path = os.path.join("PyBank", "Resources", "budget_data.csv")

# lists to store data
dates = []
profits_loses = []

# skkip the header and read the data
with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        dates.append(row[0])
        profits_loses.append(int(row[1]))

# Total month
total_months = len(dates)

# Net total amount of profits/loses
net_total = sum(profits_loses)

# Monthly changes - in huaman language: the monthly change comparing to the previous month
# Then the average of those changes.
changes = []
change_dates = []

for i in range(1, len(profits_loses)):
    monthly_change = profits_loses[i] - profits_loses[i - 1]
    changes.append(monthly_change)
    change_dates.append(dates[i])

# average change
average_change = sum(changes) / len(changes)

# Greatest increase in profits and the date of that increase
greatest_increase = max(changes)
greatest_increase_date = change_dates[changes.index(greatest_increase)]

#Greatest decrease in profits and the date of that decrease
greatest_decrease = min(changes)
greatest_decrease_date = change_dates[changes.index(greatest_decrease)]

# Output the results
analysis = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})"
)

# Print to terminal
print(analysis)

# Export to text file
output_path = os.path.join(
    "PyBank",
    "analysis",
    "financial_analysis.txt"
)

with open(output_path, "w") as txt_file:
    txt_file.write(analysis)

print(f"\nResults saved to {output_path}")