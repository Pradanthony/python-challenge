import csv

#filepath and variables
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

    #find each candidate vote counts
        if candidate in ind_vote_count:
            ind_vote_count[candidate]+=1

        else:
            ind_vote_count[candidate]=1
   
#print the total vote count
print("Election Results")
print("_________________________________")
print("Total Votes: ",row_count)
print("_________________________________")

#loop to print each candidate vote count in table since ind)vote)count is dictionary
for candidate, votes in ind_vote_count.items():
    print(f"{candidate}: {round(votes/row_count*100,3)}% ({votes})")
print("_________________________________")

#print winner name
winner=max(ind_vote_count,key=ind_vote_count.get)
print("Winner:", winner)
print("_________________________________")

#export to text file
with open("analysis/vote_analysis.txt","w")as output_file:
    output_file.write("Election Results")
    output_file.write("_________________________________")
    output_file.write("Total Votes: "+str(row_count))
    output_file.write("_________________________________")
    for candidate, votes in ind_vote_count.items():
        output_file.write(f"{candidate}:{round(votes/row_count*100,3)}% ({votes})")
    output_file.write("_________________________________")
    winner=max(ind_vote_count,key=ind_vote_count.get)
    output_file.write("Winner: "+str(winner))
    output_file.write("_________________________________")

print("vote analysis result exported to text file successfully")

