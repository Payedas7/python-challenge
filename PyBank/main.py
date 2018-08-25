"""----------------------------------------------------------------------------
Created on Mon Aug 20 17:39:11 2018
@author: payeldas
-------------------------------------------------------------------------------
# =============================================================================
# "The PyBank Challenge"
# =============================================================================

Task is to create a Python script that analyzes the records to calculate each of the following:
    
    * The total number of months included in the dataset

    * The total net amount of "Profit/Losses" over the entire period

    * The average change in "Profit/Losses" between months over the entire period

    * The greatest increase in profits (date and amount) over the entire period

    * The greatest decrease in losses (date and amount) over the entire period
----------------------------------------------------------------------------"""

import os
import csv
# =============================================================================
# opening the given CSV formatted file as 'csvfile' in this program and using  
# 'reader funtion reading the contents into 'csv_reader' 
# =============================================================================
pybankCSV = os.path.join("/Users/payeldas/python-challenge/PyBank/","Resources", "budget_data.csv")
with open(pybankCSV, 'r',encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)
# =============================================================================
# calculation of total number of months    
# =============================================================================
    month_total = 0
    for row in csv_reader:
        month_total += 1
    print(f"Total Months : {month_total}")
# =============================================================================
# reading the csvfile in dictionary mode to take the value of 'profit/losses' 
# and put it in a list called 'col_value'    
# =============================================================================
    col_value = []
    with open(pybankCSV, 'r',encoding='utf-8') as csvfile:
       reader_1 = csv.DictReader(csvfile)
       col_value = [(row['Profit/Losses']) for row in reader_1]
       print(col_value)
# =============================================================================
#   reading the csvfile in dictionary mode to take the value of 'Date' column in
#   a list called 'date_value'
# =============================================================================
    date_value = []     
    with open(pybankCSV, 'r',encoding='utf-8') as csvfile:
       reader_2 = csv.DictReader(csvfile)
       date_value = [(row['Date']) for row in reader_2]
       print(date_value)
# =============================================================================
# calculation of total net amount of "Profit/Losses" over the entire period    
# =============================================================================
    total_amount = 0
    for j in range(0,(len(col_value))):
        total_amount += int(col_value[j])
    print(f"Total : ${total_amount}")    
# =============================================================================
#  making a list named 'change_pf_ls' of values which are representing the 
#  change in 'Profit/Losses' between months 
#  over the entire period   
# =============================================================================
    change_pf_ls = []
    total_change = 0.00
    change_pf = 0
    #change_pf_ls.append(0)
    c = len(col_value) - 1
    for i in range(0,(len(col_value)-1)):
        change_pf = (float(col_value[i+1]) - float(col_value[i]))
        change_pf_ls.append(change_pf)
        total_change = total_change + change_pf
# =============================================================================
#  calculation of Average Change in "Profit/Losses" between months over the 
#  entire period      
# =============================================================================
    avg_change = round(float(total_change/(len(change_pf_ls))),2)
    print(f"Average  Change: ${avg_change}")
# =============================================================================
# calculation of greatest increase in profits (date and amount) over the entire 
# period   
# =============================================================================
    gr_inc_prof = max(change_pf_ls)
# =============================================================================
# taking "k" as an integer to hold the position of the max value that is stored 
# in another variable "x"
# using loop comprehension method the code is shorter to get that   
# =============================================================================
    for k in (k for k,x in enumerate(change_pf_ls) if x == gr_inc_prof):
        pos_1 = k
# =============================================================================
#   taking the Date value when the profit rises from the list of dates stored  
#   in the "date_value" list       
# =============================================================================
    date_inc_prof = date_value[k+1]    
    print(f"Greatest Increase in Profits: {date_inc_prof} (${gr_inc_prof})" )
# =============================================================================
#   calculation of greatest decrease in losses (date and amount) over the entire 
#   period  
# =============================================================================
    gr_dec_loss = min(change_pf_ls)
# =============================================================================
# taking "m" as an integer to hold the position of the max value that is stored 
# in another variable "y"
# using loop comprehension method the code is shorter to get that      
# =============================================================================
    for m in (m for m,y in enumerate(change_pf_ls) if y == gr_dec_loss):
        pos_2 = m
# =============================================================================
#  taking the Date value when the profit decreases from the list of dates stored  
#  in the "date_value" list    
# =============================================================================
    date_dec_loss = date_value[m+1]    
    print(f"Greatest Decrease in Profits: {date_dec_loss} (${gr_dec_loss})" )
    csvfile.close()

pybankTXT = os.path.join("/Users/payeldas/python-challenge/PyBank/","Resources","output.txt") 
with open(pybankTXT, 'w',encoding='utf-8') as outfile:
    a = '-' * 30
    outfile.write(f"Financial Analysis\n{a}")
    outfile.write(f"\nTotal Months : {month_total}\nAverage  Change: ${avg_change}\nGreatest Increase in Profits: {date_inc_prof} (${gr_inc_prof})\nGreatest Decrease in Profits: {date_dec_loss} (${gr_dec_loss})")
    outfile.close()
    
    
    
    
    
    
    
    
    
    