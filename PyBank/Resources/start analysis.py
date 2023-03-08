import csv

budget_data="Resources/budget_data.csv"
row_count=0
total=0

# Open the CSV file
with open(budget_data,'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    # skip Header row
    next(reader)

    # row count for months
    for row in reader:
        row_count +=1
        total += int(row[1])

print("Financial Analysis")
print("_________________________________")
print("Total Months:",row_count)
print(f"Total: ${total}")




