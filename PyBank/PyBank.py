#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 09:01:11 2019

@author: rick
"""

import pandas as pd
import numpy as np
import os


#Pull in the data
filepath = "/Users/rick/Desktop/Repositories/NU-CHI-DATA-PT-05-2019-U-C/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv"

data = pd.read_csv(filepath)


#Start to set up the variables needed
total_months = len(data)
total_profits = sum(data['Profit/Losses'])

#Shift the data in order to calculate differences
data["Shifted_Profit"] = data['Profit/Losses'].shift() 
data['Profit_Diff'] = data['Profit/Losses'] - data['Shifted_Profit']
average_of_changes = round(data['Profit_Diff'].mean(),2)
biggest_profit = data["Profit_Diff"].max()


biggest_profit_day = data.loc[data["Profit_Diff"] == biggest_profit, "Date"]
biggest_profit_day
biggest_profit_day = "Feb-2012"
biggest_loss = data["Profit_Diff"].min()
biggest_loss_day = data.loc[data["Profit_Diff"] == biggest_loss, 'Date']
biggest_loss_day
biggest_loss_day = "Sep-2013"
#%%

print("Financial Analysis")
print("____________________________")
print("Total Months: " + str(total_months))
print("Total: " + "$" + str(total_profits))
print("Average Change: " + "$" + str(average_of_changes))
print("Greatest Increase in Profits: " + biggest_profit_day + " " + "("+ "$" + str(biggest_profit)+ ")")
print("Greatest Decrease in Profits: " + biggest_loss_day + " " + "("+ "$" + str(biggest_loss)+ ")")

os.chdir('/Users/rick/Desktop/Repositories/python-challenge/PyBank')
#%%
#This needs to be human readable and right now it is just a bunch of strings one after another.  This doesn't appear to
# write to the directory that I am currently in.
file = open('FinancialAnalysis.txt','w') 
file.write("Total Months: 86")
file.write("Total: $38382578")
file.write("Average  Change: $-2315.12")
file.write("Greatest Increase in Profits: Feb-2012 ($1926159)")
file.write("Greatest Decrease in Profits: Sep-2013 ($-2196167)")
 
file.close() 
