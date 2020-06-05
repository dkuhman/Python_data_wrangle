#This script provides examples for using the Pandas package in Python
#Created by: Daniel Kuhman
#Last updated: 2020-06-04
#GitHub: https://github.com/dkuhman

import pandas as pd

#Load data from .csv file
data = pd.read_csv('data/city_weather_2019.csv')

#You print data - head(n) specifies to print the first n rows
print(data.head(5))

#Read the column names (column headers) using .columns
print(data.columns)

#Read data from a specific column
print(data['city'])

#Specify which rows to pull from a specific column
#This will pull rows 0-9 from column 'city'
print(data['city'][0:10])

#Select specific columns
#Note that the columns selected will be in the order in which they were selected
new_data = data[['city', 'week_day', 'date', 'time1', 'temp_low1', 'temp_high1']]
print(new_data)

#Print a specific row by index using iloc (iloc = integer location)
#This will print data of all columns in 'data' row 0 (first row)
print(data.iloc[0])
#You can also print multiple rows by index
print(data.iloc[0:10])

#Filter rows by condition
#This will return only the rows in 'data' where column 'city' is 'birmingham'
bhm_data = data.loc[data['city'] == 'birmingham']
print(bhm_data.head(5))
#You can add multiple conditions to filter on
#Note that conditions must be separated by parentheses
bhm_mon_data = data.loc[(data['city'] == 'birmingham') & (data['week_day'] == 'Mon')]
print(bhm_mon_data.head(5))
#You can also run conditionals on numeric bhm_data
bhm_mon_data = data.loc[(data['city'] == 'birmingham') & (data['week_day'] == 'Mon') & (data['temp_high1'] > 60)]
print(bhm_mon_data.head(5))
#Note that when filtering, the old index remains. To reset a new index:
#By default, the function keeps the old index as a column, but you can add drop=True to remove it
bhm_mon_data = bhm_mon_data.reset_index(drop=True)
print(bhm_mon_data.head(5))

#Sort rows by value; by default, the sort goes from high to low - add ascending=False to reverse this
print(bhm_data.sort_values('temp_high1', ascending=False))

#Drop columns
data = data.drop(columns=['NA1','NA2','NA3','NA4','NA5','NA6','NA7','NA8'])
print(data)

#Add a column with values that rely on values in existing columns
#This will create a new column in 'data' that is the average of all high temperatures for each row
data['avg_high'] = (data['temp_high1'] + data['temp_high2'] + data['temp_high3'] + data['temp_high4'])/4
print(data['avg_high'])

#Alter rows based on condition
#Change city from birmingham to chicago in all rows where city == birmingham
data.loc[data['city'] == 'birmingham', 'city'] = 'chicago'
print(data)
#Add a new column with conditional row data
data.loc[data['avg_high'] > 80, 'hot_or_cold'] = 'hot'
data.loc[data['avg_high'] < 80, 'hot_or_cold'] = 'cold'
print(data)

#Group rows of data by similar values
#Get average temperature across all days for each city in the dataset
#The describe() fnction gives you basic statistic info, including mean, std, min, max, etc.
print(data.groupby('city').describe())
#You can also pass a list into groupby() to group on multiple levels
print(data.groupby(['city', 'week_day']).describe())

#Save to a new file
#By default, the new file will include an index column as column 0 in the saved file.
#You can change this by including index=False
data.to_csv('data.csv', index=False)
