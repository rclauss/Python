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
main_data


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

df_bubble
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

urban_df
suburban_df
rural_df

#%%
# Make sure all of the sizes will be visible -- but not too big
urban_size = urban_df['Driver Count per City'] * 6
suburban_size = suburban_df['Driver Count per City'] * 6
rural_size = rural_df['Driver Count per City'] * 6

#  Create a graph for each one because the coloring is easier this way
ax1 = urban_df.plot(kind='scatter', x='Total Number of Rides (Per City)', y='Average Fare ($)', s=urban_size, color='lightblue', edgecolor='black', alpha=0.7, label='Urban')    

ax2 = suburban_df.plot(kind='scatter', x='Total Number of Rides (Per City)', y='Average Fare ($)', s=suburban_size, color='gold', edgecolor='black', alpha=0.7, ax=ax1, label='Suburban')    

ax3 = rural_df.plot(kind='scatter', x='Total Number of Rides (Per City)', y='Average Fare ($)', s=rural_size, color='lightcoral', edgecolor='black', alpha=0.7, ax=ax1, label='Rural')

# Plot formatting
plt.grid()
plt.title('Ride Sharing Data Compare')
plt.xlabel('Total Number of Rides (Per City)')
plt.ylabel('Average Fare ($)')
plt.show()
#%%

city_type = city_data.set_index("city")
city_type = city_type['type']

pie_df = ride_data.join(city_type, on='city')

pie_df_urban = pie_df.loc[pie_df['type'] == 'Urban', :]
pie_df_suburban = pie_df.loc[pie_df['type'] == 'Suburban', :]
pie_df_rural = pie_df.loc[pie_df['type'] == 'Rural', :]


pie_df_urban = pie_df_urban.groupby('type')
pie_df_suburban = pie_df_suburban.groupby('type')
pie_df_rural = pie_df_rural.groupby('type')

#Set up configs for the pie chart
explode = [0.1, 0.1, 0.1]
text = {'fontsize' : 15}
wedge = {'edgecolor' : 'black'}


fare_urban = pie_df_urban['fare'].sum()
fare_suburban = pie_df_suburban['fare'].sum()
fare_rural = pie_df_rural['fare'].sum()

fare_labels = ['Urban', 'Suburban', 'Rural']
fare_totals = pd.Series([fare_urban, fare_suburban, fare_rural])
fare_colors = ['lightblue', 'gold', 'lightcoral']

plt.axis("equal")
plt.title('% of Total Fares by City Type', y=1.80, fontsize=15)
plt.pie(fare_totals, radius=3, textprops=text, wedgeprops=wedge, labels=fare_labels, explode=explode, colors=fare_colors,
        autopct="%1.1f%%", shadow=True, startangle=70)
plt.show()
#%%

rides_urban = pie_df_urban['fare'].count()
rides_suburban = pie_df_suburban['fare'].count()
rides_rural = pie_df_rural['fare'].count()
#%%
rides_labels = ['Urban', 'Suburban', 'Rural']
rides_totals = pd.Series([rides_urban, rides_suburban, rides_rural])

plt.axis("equal")
plt.title('% of Total Rides by City Type', y=1.80, fontsize=15)

plt.pie(rides_totals, radius=3, textprops=text, wedgeprops=wedge, labels=rides_labels, explode=explode, colors=fare_colors, autopct="%1.1f%%", shadow=True, startangle=70)
plt.show()
#%%


drivers_df = city_data.groupby('type')
drivers_total = drivers_df['driver_count'].sum()

drivers_labels = ['Urban', 'Suburban', 'Rural']
drivers_totals = [drivers_total['Urban'], drivers_total['Suburban'], drivers_total['Rural']]
drivers_colors = ['lightblue', 'gold', 'lightcoral']

plt.axis("equal")
plt.title('% of Total Drivers by City Type', y=1.80, fontsize=15)
plt.pie(drivers_totals, radius=3, textprops=text, wedgeprops=wedge, labels=drivers_labels, explode=explode, colors=drivers_colors,
        autopct="%1.1f%%", shadow=True, startangle=40)
plt.show()

##adding comment to test vi
## adding second commment to test remote push
