import os
import csv

election_data_path = os.path.join('Resources','election_data.csv')

#place holder for the count of votes
total_votes = 0

#placeholder for candidate names
candidate_names = []
#total
candidate_votes = []
#percent_votes = (candidate_votes/total_votes) * 100

with open(election_data_path, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidate_names = (row[2])

        if row[2] not in candidate_names:
            candidate_names.append(row[2])
            candidate_list = candidate_names.index(row[2])
            candidate_votes.append(1)
        else: 
            candidate_list = candidate_names.index(row[2])
            candidate_votes.append(1)

winner = max(candidate_votes)
candidate_list = candidate_votes.index(winner)
elected = candidate_list(winner)

print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
#print("--------------------------")
print(f"Winner: {elected}")
#print("--------------------------")