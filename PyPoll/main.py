#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Created on Fri Aug 24 01:24:37 2018
@author: payeldas
-------------------------------------------------------------------------------
# =============================================================================
# "The PyPoll Challenge"
# =============================================================================

Task is to create a Python script that analyzes the votes and calculates each of the following:

    * The total number of votes cast

    * A complete list of candidates who received votes

    * The percentage of votes each candidate won

    * The total number of votes each candidate won

    * The winner of the election based on popular vote.
----------------------------------------------------------------------------"""
import os
import csv
# =============================================================================
# opening the given CSV formatted file as 'csvfile' in this program and using  
# 'reader funtion reading the contents into 'csv_reader' 
# =============================================================================
pypollCSV = os.path.join("/Users/payeldas/python-challenge/PyPoll/","Resources", "election_data.csv")
with open(pypollCSV, 'r',encoding='utf-8') as csvfile:
   csv_reader = csv.reader(csvfile, delimiter=',')
   csv_header = next(csv_reader)
# =============================================================================
# taking all the data from the csv file to a list named 
# 'data_value", for easy to analyse data   
# =============================================================================
   data_value = []
   data_value = [row for row in csv_reader]
   #print(len(data_value))
# =============================================================================
#  calculation of total vote counted by counting the number of rows or different voter ids  
# =============================================================================
   vote_total = len(data_value)
   print(f"Total Votes:  {vote_total}")
# =============================================================================
#  making a list of candidate column into a list named 'candidates'  
# =============================================================================
   candidates = list(set((row[2]) for row in data_value))
# =============================================================================
#  complete list of candidates who received votes
# =============================================================================
   print(candidates)
   
   vote_count = {} #creating a dict to hold candidate name as key and values are the 
                   #total vote received and percentage of vote counts corresponding to the
                   #candidate 
   winner_count = {} #creating a dict to hold candidates name as the key and the 
                     #total vote received as the value 
# =============================================================================
#   loop to update key and value pairs to the above mentioned dictionary                   
# =============================================================================
   for i in range (len(candidates)):
       y = len([row[2] for row in data_value if row[2] == candidates[i]])
       x = round(((y/vote_total)*100),2)
       vote_count.update({candidates[i]:[x,y]})
       winner_count.update({candidates[i]:y})
   print(vote_count)
# =============================================================================
#  A complete list of candidates who received votes
#  The percentage of votes each candidate won
#  The total number of votes each candidate won  
# =============================================================================
   from operator import itemgetter 
   for key, (value1, value2) in sorted(vote_count.items(), key = itemgetter(1), reverse = True):
    print(f"{key}: {value1}00% ({value2})")
# =============================================================================
#   The winner of the election based on popular vote 
# =============================================================================
   max_value1 = max(winner_count.values())  # maximum value
   #max_value2 = max(vote_count.values())
   max_keys = [key for key, value in winner_count.items() if value == max_value1] # getting all keys containing the `maximum`
   print(f"Winner: {max_keys[0]}") 
   csvfile.close()
# =============================================================================
# taking outputs to export to a text file with the results   
# =============================================================================
pybankTXT = os.path.join("/Users/payeldas/python-challenge/PyPoll/","Resources","output.txt") 
with open(pybankTXT, 'w',encoding='utf-8') as outfile:
    a = '-' * 30
    outfile.write(f"Election Results\n{a}\n")
    outfile.write(f"Total Votes:  {vote_total}\n{a}\n")
    from operator import itemgetter 
    for key, (value1, value2) in sorted(vote_count.items(), key = itemgetter(1), reverse = True):
     outfile.write(f"{key}: {value1}00% ({value2})\n")
    outfile.write(f"{a}\nWinner: {max_keys[0]}\n{a}\n") 
    outfile.close()
 