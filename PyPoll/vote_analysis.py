import csv

votes_data="Resources/election_data.csv"
row_count=0

# Open the CSV file
with open(votes_data,'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    # skip Header row
    next(reader)

    # row count for months
    for row in reader:
        row_count +=1
   
#print the analysis results
print("Election Results")
print("_________________________________")
print("Total Votes:",row_count)
print("_________________________________")