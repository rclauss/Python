#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 12:03:03 2019

@author: rick
"""
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#%%

ride_data = pd.read_csv("ride_data.csv")
city_data = pd.read_csv("city_data.csv")

#%%

# Merge everthing into one dataset

main_data = city_data.merge(ride_data, on='city', how='left')


#%%

#Create new df to manipulate to keep main_data clean
grouped_main_data = main_data

# Groupby object to use for calculations
per_city = grouped_main_data.groupby("city")
#%%

avg_fare = round(per_city["fare"].mean(),2)

total_rides = per_city["ride_id"].count()

driver_count = city_data.set_index("city")["driver_count"]

types = main_data.drop_duplicates(subset='city', keep='first').set_index('city')["type"]
#%%

df_bubble = pd.concat([avg_fare, total_rides, driver_count,types], axis = 1, sort=False)
#%%
df_bubble = df_bubble.rename(columns={'fare' : 'Average Fare ($)',
                                   'ride_id' : 'Total Number of Rides (Per City)',
                                   'driver_count' : 'Driver Count per City',
                                   'type' : 'City Types'})
#%%
# Dataframe by city type
urban_df = df_bubble.loc[df_bubble['City Types'] == 'Urban', :]
suburban_df = df_bubble.loc[df_bubble['City Types'] == 'Suburban', :]
rural_df = df_bubble.loc[df_bubble['City Types'] == 'Rural', :]

#%%
urban_size = urban_df['Driver Count per City'] * 6
suburban_size = suburban_df['Driver Count per City'] * 6
rural_size = rural_df['Driver Count per City'] * 6

ax1 = urban_df.plot(kind='scatter', x='Total Number of Rides (Per City)', y='Average Fare ($)', s=urban_size, color='lightblue', edgecolor='black', alpha=0.7, label='Urban')    
ax2 = suburban_df.plot(kind='scatter', x='Total Number of Rides (Per City)', y='Average Fare ($)', s=suburban_size, color='gold', edgecolor='black', alpha=0.7, ax=ax1, label='Suburban')    
ax3 = rural_df.plot(kind='scatter', x='Total Number of Rides (Per City)', y='Average Fare ($)', s=rural_size, color='lightcoral', edgecolor='black', alpha=0.7, ax=ax1, label='Rural')

# Plot formatting
plt.grid()
plt.title('Ride Sharing Data Compare')
plt.xlabel('Total Number of Rides (Per City)')
plt.ylabel('Average Fare ($)')



