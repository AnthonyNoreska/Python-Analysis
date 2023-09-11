#Import the necessary libraries
import csv
import os

#Load the CSV data into a list of dictionaries

csv_file_path = r'C:\Users\Admin\Documents\GitHub\Python-Analysis\PyPoll\Resources\election_data.csv'

data = [row for row in csv.DictReader(open(csv_file_path, 'r', newline=''))]
my_report = open("PyPoll\Analysis\Poll_Analysis.txt", "w")

#Define the names of the columns: #Ballot ID,County,Candidate
Ballot_ID = "Ballot ID"
County = "County"
Candidate = "Candidate"

#Initialize variables and dictionaries to count the total votes as well as store the candidates and their corresponding votes
total_votes = 0
candidate_list = {}
candidate_votes = {}

winning_candidate = ""
max_votes = 0


#Initialize a for loop to iterate through each row of data
for row in data:

    total_votes +=1 

    candidate_name = row["Candidate"]

    if candidate_name not in candidate_list:

        candidate_list[candidate_name] = 0

    if candidate_name in candidate_votes:

        candidate_votes[candidate_name] += 1

    else:
        candidate_votes[candidate_name] = 1
    
#Define a function to calculate and format the percentages    
def percentage_calc():

    percentages = []


    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
    
        percentages.append(f"{candidate}: {percentage:.3f}% ({votes})")
    return "\n".join(percentages)


#Initialize a for loop to find the winning candidate
for candidate, votes in candidate_votes.items():
    if votes > max_votes:
        max_votes = votes
        winning_candidate = candidate
   



percentage = percentage_calc()




# Create a formatted output string for the election results
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
my_report.write(output)