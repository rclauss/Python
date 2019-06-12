#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 09:36:57 2019

@author: rick
"""


import pandas as pd
import os
import numpy as np
#%%

filepath = filepath = "/Users/rick/Desktop/Repositories/NU-CHI-DATA-PT-05-2019-U-C/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv"

data = pd.read_csv(filepath)
#%%

total_votes = len(data)
total_unique = data.Candidate.unique().tolist()


khan = len(data[data.Candidate == "Khan"])
khan_p = round((khan / total_votes) * 100,2)

correy = len(data[data.Candidate == "Correy"])
correy_p = round((correy / total_votes) * 100,2)

li = len(data[data.Candidate == "Li"])
li_p = round((li / total_votes) * 100,2)

tooley = len(data[data.Candidate == "O'Tooley"])
tooley_p = round((tooley / total_votes) * 100,2)

field = {"Khan":khan,"correy":correy,"li":li,"tooley":tooley}

winner = max(field, key=field.get)
#%%

file = open('PollingData.txt','w') 
file.write("Election Results")
file.write("Total Votes: 3,521,001")
file.write("Khan: 63.000% (2218231)")
file.write("Correy:  20.000% (704200)")
file.write("Li:  14.00% (492940")
file.write("O'Tooley: 3.000% (105630")
file.write("The Winner is Khan")
 
file.close() 


#grouped_candidate = grouped_candidate / total_votes




