#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 16:47:51 2020

@author: carlyfabris
"""

import os
import csv
#defining variables

votes = []
candidates = {}
winner_count = 0

#opening election data
election_data_csv = os.path.join("Resources", "election_data.csv")
with open(election_data_csv) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter = ",")
#skip the first row because those are titles
    next(csvreader, None)
#adding all voter ids to a list and adding the candidates as keys in a dictionary
#each vote for a candidate will be a value of their respective key
    
    for record in csvreader:
        voterID = record[0]
        votes.append(voterID)
        cand = record[2]
#you must have an if statement here becuase you must start with an empty list to add
#the first vote too, but you don't want the list reset as empty each time
        if cand in candidates:
            candidates[cand].append(voterID)
        else:
            candidates[cand]= []
            candidates[cand].append(voterID)
        


#writing analysis data to console     
total_votes = len(votes)
print("Election Results")
print("----------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------")
for x, v in candidates.items():
    candidate_votes = len(v)
    vote_percent = round(candidate_votes/total_votes * 100, 2)
    print(f'{x}: {vote_percent}% votes: ({candidate_votes})') 
    if candidate_votes > winner_count:
        winner_count = candidate_votes
        winner_name = x
print("----------------------------------")
print(f'The winner is {winner_name}')
print("----------------------------------")
#exporting results to txt file

path = 'Analysis/CFK_PyPoll_Analysis.txt'
output_file = open(path, "w")
output_file.write("Election Results\n")
output_file.write("----------------------------------\n")
output_file.write(f"Total Votes: {total_votes}\n")
output_file.write(f"----------------------------------\n")
for x, v in candidates.items():
    candidate_votes = len(v)
    vote_percent = round(candidate_votes/total_votes * 100, 2)
    output_file.write(f'{x}: {vote_percent}% votes: ({candidate_votes})\n')
output_file.write(f'----------------------------------\n')
output_file.write(f'The winner is {winner_name}\n')
output_file.write("----------------------------------")
output_file.close()
