import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

df=pd.read_csv('GlobalLandTemperaturesByCountry.csv')

#Display the first 10 rows and use .info()/.describe() method to examine statistical information and the structure of the dataset.

print("First 10 rows of the dataset:")
print(df.head(10))

print("\nDataset Information:")
print(df.info())

print("\nStatistical Description:")
print(df.describe(include='all'))

#Handle Missing Values

print(df.isnull().sum())
df2 = df.fillna({ 'AverageTemperature': df['AverageTemperature'].mean(),
                 'AverageTemperatureUncertainty': df['AverageTemperatureUncertainty'].mean()})

df3=df.dropna(how='any')


#Parse the Date Column

df2['dt'] = pd.to_datetime(df2['dt'])


df2['Year'] = df2['dt'].dt.year
df2['Month'] = df2['dt'].dt.month
df2['Day'] = df2['dt'].dt.day 
print(df2)


#Check for Data Consistency

#Filter Data Based on Uncertainty

filtered_df = df2[df2['AverageTemperatureUncertainty'] <= 2.0]
print(filtered_df)
print(df2.shape)
print(filtered_df.shape)

#Filter Data Based on Uncertainty

print(df2)

yearly_trends = df2.groupby('Year').agg({
    'AverageTemperature': 'mean',
    'AverageTemperatureUncertainty': 'mean'
}).reset_index()


plt.errorbar(yearly_trends['Year'], yearly_trends['AverageTemperature'], 
             yerr=yearly_trends['AverageTemperatureUncertainty'], fmt='o-', color='blue', ecolor='red', capsize=3)
plt.title("Average Temperature Trend with Uncertainty")
plt.xlabel("Year")
plt.ylabel("Average Temperature (°C)")
plt.grid()
plt.show()


#Analyze Trends in Uncertainty

plt.plot(yearly_trends['Year'], yearly_trends['AverageTemperatureUncertainty'], marker='o', color='blue')
plt.title("Trend of Temperature Uncertainty Over Time")
plt.xlabel("Year")
plt.ylabel("Average Uncertainty (°C)")
plt.grid()
plt.show()
#the average uncertainity decreases over time because of increased accuracy of the measurement and availability of data over time. At first the uncertainity maybe be low because of less availabilty of data and icrease further


#Identify High-Uncertainty and Inconsistent Periods

AverageTemperatureUncertainty_std=yearly_trends['AverageTemperatureUncertainty'].std()
AverageTemperatureUncertainty_mean=yearly_trends['AverageTemperatureUncertainty'].mean()
df4 = df2[df2['AverageTemperatureUncertainty'] >= AverageTemperatureUncertainty_mean+AverageTemperatureUncertainty_std]
print(df4['Year'])
df5 = df2[df2['AverageTemperatureUncertainty'] <= AverageTemperatureUncertainty_mean-AverageTemperatureUncertainty_std]
print(df5['Year'])
#reason for outliers:Sparse or low-quality data.Measurement limitations in earlier years.Regional variations or extreme weather events.


df2.to_csv('cleaned_temperatures.csv', index=False)
print("\nCleaned dataset saved as 'cleaned_temperatures.csv'.")