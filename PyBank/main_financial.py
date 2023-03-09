import csv

#assign variables
budget_data="Resources/budget_data.csv"
row_count=0
total=0
lastyear_profit=0
profit_changes=[]
greatest_increase_amount=0
greatest_increase_date=""
greatest_decrease_date=""
greatest_decrease_amount=0


# Open the CSV file
with open(budget_data,'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    # skip Header row
    next(reader)

    # row count for months
    for row in reader:
        row_count +=1
        total += int(row[1])

        # create profit change list and calculate change in profit/loss
        if row_count > 1:
            yearly_change = int(row[1]) - previous_profit
            profit_changes.append(yearly_change)

            #find greatest increase date and amount
            if yearly_change > greatest_increase_amount:
                greatest_increase_amount = yearly_change
                greatest_increase_date = row[0]

            #find greatest decrease date and amount
            if yearly_change < greatest_decrease_amount:
                greatest_decrease_amount = yearly_change
                greatest_decrease_date = row[0]

        #total change in profit/loss
        previous_profit = int(row[1])

# average profit/loss change
avg_change = sum(profit_changes)/len(profit_changes)

#print the analysis results
print("Financial Analysis")
print("_________________________________")
print("Total Months:",row_count)
print(f"Total: ${total}")
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")

#export analysis to text file
with open("analysis/financial_analysis.txt", "w") as output_file:
    
    # Write the analysis results to the text file
    output_file.write("Financial Analysis\n")
    output_file.write("_________________________________\n")
    output_file.write(f"Total Months: {row_count}\n")
    output_file.write(f"Total: ${total}\n")
    output_file.write(f"Average Change: ${avg_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})\n")

# Print message to confirm that the export was complete
print("Analysis results exported to financial_analysis.txt")
