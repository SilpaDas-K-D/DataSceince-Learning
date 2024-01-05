# read a csv file and answer the questions

'''
 1. What was max temperature in newyork in the month of january?
 2. On which days did it rain?
 3. What was the average speed of wind during the month?
'''

import pandas as pd

import pandas as pd
df = pd.read_csv('/Users/silpadaskd/downloads/nyc_weather.csv')

print("maximum temperature in january",df['Temperature'].max())

print("the days that rains are ",df['EST'][df['Events']=='Rain'])

print("the avergae windspeed" ,df['WindSpeedMPH'].mean()) # here we also include NA values 

# to remove Na, and replace it with zeros

df.fillna(0,inplace=True)

print("the avergae windspeed" ,df['WindSpeedMPH'].mean())
