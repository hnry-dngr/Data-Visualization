# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 09:40:49 2023

@author: HP
"""
import pandas as pd
import matplotlib.pyplot as plt


# Question1:
# Load the dataset into a data frame using Python.

data = "C:/Users/HP/Downloads/Africa_climate_change.csv"
dataset = pd.read_csv(data)

# Question2:
# Clean the data as needed.

#---Handling Missing Data in Pandas
missing = dataset.isnull().sum().sum() # counting the NAN

# Finding the mean of all the columns affected by the NAN
t_avg = dataset.loc[:, ["TAVG"]].mean() 
t_max = dataset.loc[:, ["TMAX"]].mean()
t_min = dataset.loc[:, ["TMIN"]].mean()
t_prcp = dataset.loc[:, ["PRCP"]].mean()

# filling the NAN with thier columns mean Using .fillna() to Fill Missing Data
dataset["TAVG"] = dataset["TAVG"].fillna(77.0298)
dataset["TMAX"] = dataset["TMAX"].fillna(88.714)
dataset["TMIN"] = dataset["TMIN"].fillna(65.5483)
dataset["PRCP"] = dataset["PRCP"].fillna(0.121)

#---Working with Duplicate Data in Pandas

# Identifying Duplicate Records in a Pandas DataFrame and Counting
duplicate = (dataset.duplicated().sum())
# Removing Duplicate Data in a Pandas DataFrame
dataset.drop_duplicates(inplace = True)

#---Cleaning Strings in Pandas by Trimming Whitespace from a Pandas Column
dataset["COUNTRY"].str.strip()

#---Changing String Case in Pandas by Changing Text to Title Case.
dataset["COUNTRY"].str.title()


# Converting date column to the date and time format
dataset["DATE"] = pd.to_datetime(dataset["DATE"], errors='coerce')

# Handling missing or incorrect values
dataset["DATE"].fillna(pd.to_datetime('today'), inplace=True)

# Removing the time part from a Date coulmn in Pandas
dataset["DATE"] = dataset["DATE"].dt.date

# Question3:
# Plot a line chart to show the average temperature fluctuations in Tunisia and Cameroon. Interpret the results.
fig, ax = plt.subplots(figsize=(10, 6))
x_country = dataset[(dataset["COUNTRY"]=="Tunisia")| (dataset["COUNTRY"]=="Cameroon")]
x_country.plot(x="COUNTRY", y="TAVG", kind='line')
plt.title("Average Temperature Fluctuations")
plt.xlabel("Countrys")
plt.ylabel("Average Temperature")
plt.show()

# Question4
# Zoom in to only include data between 1980 and 2005, try to customize the axes labels.

x_country["DATE"] = pd.to_datetime(x_country["DATE"], errors='coerce')
x_country = x_country.reset_index()

# # Filter data for the years between 1980 and 2005
x_zoom = x_country.loc[0:69088]

# Group by country and calculate the average temperature for each year
avg_temp_by_country = x_zoom.groupby(['COUNTRY', x_zoom["DATE"].dt.year])["TAVG"].mean().unstack()


# Plot the line chart
avg_temp_by_country.plot(ax = ax, marker ='o')
plt.title('Average Temperature Fluctuations (1980-2005)')
plt.xlabel('Year')
plt.ylabel('Average Temperature')
plt.legend(title='Country')
plt.show()

# Question5
# Create Histograms to show temperature distribution in Senegal between [1980,2000] and [2000,2023] (in the same figure). Describe the obtained results.

dataset["DATE"] = pd.to_datetime(dataset["DATE"], errors='coerce')

# filtering the dataset
dataset["DATE"].fillna(pd.to_datetime('today'), inplace=True)

dataset["DATE"] = dataset["DATE"].dt.date

senegal_1 = dataset[(dataset['COUNTRY'] == 'Senegal')]
senegal_1["DATE"] = pd.to_datetime(senegal_1["DATE"], errors='coerce')
senegal_1 = senegal_1.reset_index()
sen_1 =  senegal_1.loc[0:89175]

senegal_1 = dataset[(dataset['COUNTRY'] == 'Senegal')]
senegal_1["DATE"] = pd.to_datetime(senegal_1["DATE"], errors='coerce')
senegal_1 = senegal_1.reset_index()
sen_2 =  senegal_1.loc[85423:181512]

# Plot histogramsin Senegal between [1980,2000]
sen_1["TAVG"].plot.hist(bins = 10, edgecolor = "black", color = "skyblue")
plt.title('Temperature Distribution in Senegal Between [1980,2000]')
plt.xlabel('Temperature')
plt.ylabel('Frequency')
plt.show()

# Plot histogramsin Senegal between [2000,2023]
sen_2["TAVG"].plot.hist(bins = 10, edgecolor = "black", color = "skyblue")
plt.title('Temperature Distribution in Senegal Between [2000,2023]')
plt.xlabel('Temperature')
plt.ylabel('Frequency')
plt.show()

# Question6
# Select the best chart to show the Average temperature per country.
# Plot a bar chart for average temperature per country
# Group by country and calculate the average temperature
avg_temp_by_gen_country = dataset.groupby('COUNTRY')['TAVG'].mean().sort_values(ascending=False)
# Plot the bar chart
avg_temp_by_gen_country.plot.bar(x ="COUNTRY", y ="TAVG" , color='skyblue')
plt.title('Average Temperature Per Country')
plt.xlabel('Country')
plt.ylabel('Average Temperature')
plt.xticks(rotation=45, ha='right')
plt.show()

