import csv

votes_data="Resources/election_data.csv"
row_count=0
ind_vote_count={}

# Open the CSV file
with open(votes_data,'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    # skip Header row
    next(reader)

    # row count for months
    for row in reader:
        row_count +=1
        candidate=row[2]

        if candidate in ind_vote_count:
            ind_vote_count[candidate]+=1

        else:
            ind_vote_count[candidate]=1
   
#print the analysis results
print("Election Results")
print("_________________________________")
print("Total Votes:",row_count)
print("_________________________________")

for candidate, votes in ind_vote_count.items():
    print(f"{candidate}:{round(votes/row_count*100,3)}% ({votes})")

print("_________________________________")

winner=max(ind_vote_count)
print(winner)