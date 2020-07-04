#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 16:40:57 2020

@author: carlyfabris
"""
import os
import csv
num_of_months = set()
profit = []
daily_changes = []
maximum = 0
minimum = 0
max_date = "test"
min_date = "test"
daily_change = 0
last_profit = 0
go_flag = True
budget_data_csv = os.path.join("Resources", "budget_data.csv")
with open(budget_data_csv) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter = ",")
#skip the first row because those are titles
    next(csvreader, None)
# adding each item in a column to its respective list/set
    
    for record in csvreader:
        months = record[0]
        daily_profit = int(record[1])
        num_of_months.add(months)
        profit.append(daily_profit)
# comparing the profit to the previous month to determine change in profit.
#adding change of profit to a list
#Boolean necessary so the first difference (cell1 - 0) isn't included in avg calculations
        if go_flag == False:
            daily_change = daily_profit- last_profit
            daily_changes.append(daily_change)
        last_profit = daily_profit
 #determining the max change and assigning the day on which this occurs       
        
        if daily_change > maximum:
            maximum = daily_change
            max_date = months
        if daily_change < minimum:
            minimum = daily_change
            min_date = months
        go_flag = False

        
#Print statement of Analysis to console
        
print("Financial Analysis")
print("---------------------------------------------")
print(f"Total Months: {len(num_of_months)}")
#calculate total profit
total_profit = sum(profit)
print(f"The total profit is: {total_profit}")
#calculate average daily change
avg_daily_change = sum(daily_changes)/len(daily_changes)
print(f'Average Change: {round(avg_daily_change, 2)}')
print(f'Greatest increase in profits: {max_date} {maximum}')
print(f'Greatest decrease in profits: {min_date} {minimum}')



#write Analysis to a text file
path = 'Analysis/CFK_Analysis.txt'
output_file = open(path, "w")
output_file.write("Financial Analysis\n")
output_file.write("---------------------------------------------\n")
output_file.write(f"Total Months: {len(num_of_months)}\n")
output_file.write(f"The total profit is: {total_profit}\n")
output_file.write(f'Average Change: {round(avg_daily_change, 2)}\n')
output_file.write(f'Greatest increase in profits: {max_date} {maximum}\n')
output_file.write(f'Greatest decrease in profits: {min_date} {minimum}\n')
output_file.close()


    

