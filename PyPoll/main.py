import os
import csv
from collections import Counter

# Path to collect data from the Resources folder
VoteCSV = os.path.join('Resources', 'election_data.csv')
# Path to create new text file for results
PyPollResults = os.path.join('PyPollResults.txt')

#Read in CSV file
with open(VoteCSV, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #Skipping header row in CSV
    next(csvreader, None)

    # Using Counter() to count total number of votes 
    VotesCount = Counter() 
    # Complete list of candidates who received votes
    CandidateList = [] 
    # Percentage of votes for each candidate won
    PercentageVotes = [] 
    # Winner
    Winner = [] 
    # answers print
    answer = []


    for row in csvreader: 
        CandidateList.append(row[2])

    TotalVotes = len(CandidateList)

    for name in CandidateList:
        VotesCount[name] += 1

    Winner = max(zip(VotesCount.values(), VotesCount.keys())) 
    names = tuple(VotesCount.keys())
    Votesper = tuple(VotesCount.values())

    for x in Votesper:
        PercentageVotes.append((int(x)/TotalVotes)*100)
    
    answer.append('Election Results')
    answer.append('-----------------------')
    answer.append('Total Votes: ' + str(TotalVotes))
    answer.append('-----------------------')
    for x in range(len(names)):
        answer.append(names[x] + ': ' + str(round(PercentageVotes[x],1)) + '% ' + '(' + str(Votesper[x]) + ')')
    answer.append('-----------------------')
    answer.append('Winner: ' + Winner[1])
    answer.append('-----------------------')

    print("\n".join((answer)))

with open(PyPollResults, 'w') as txtfile:
    txtfile.write('\n'.join(answer))
