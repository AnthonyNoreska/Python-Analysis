#Import the necessary libraries
import csv
import os

#Load the CSV data into a list of dictionaries
data = [row for row in csv.DictReader(open(r'PyPoll\Resources\election_data.csv', 'r', newline=''))]

#Define the names of the columns: #Ballot ID,County,Candidate
Ballot_ID = "Ballot ID"
County = "County"
Candidate = "Candidate"

total_votes = 0
candidate_list = {}
candidate_votes = {}

winning_candidate = ""
max_votes = 0

for row in data:

    total_votes +=1 

    candidate_name = row["Candidate"]

    if candidate_name not in candidate_list:

        candidate_list[candidate_name] = 0

    if candidate_name in candidate_votes:

        candidate_votes[candidate_name] += 1

    else:
        candidate_votes[candidate_name] = 1
    

def percentage_calc():

    percentages = []


    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
    
        percentages.append(f"{candidate}: {percentage:.3f}% ({votes})")
    return "\n".join(percentages)



for candidate, votes in candidate_votes.items():
    if votes > max_votes:
        max_votes = votes
        winning_candidate = candidate
   



percentage = percentage_calc()





output = f'''
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{percentage}
-------------------------
Winner: {winning_candidate}
-------------------------
'''
print(output)
