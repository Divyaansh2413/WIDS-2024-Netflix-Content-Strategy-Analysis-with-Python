import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('AB_NYC_2019.csv')

#Data Exploration and Summary

print(f'Number of rows: {df.shape[0]}')
print(f'Number of columns: {df.shape[1]}')

categorical_columns = df.select_dtypes(include=['object', 'category']).columns.tolist()
numerical_columns = df.select_dtypes(include=['number']).columns.tolist()

print("Categorical Columns:", categorical_columns)
print("Numerical Columns:", numerical_columns)


plt.subplot(1,3,1)
plt.scatter(df['latitude'],df['price'])
plt.title('Price vs Latitude')
plt.xlabel('Latitude')
plt.ylabel('Price')

plt.subplot(1,3,2)
plt.scatter(df['latitude'],df['number_of_reviews'])
plt.xlabel('Latitude')
plt.ylabel('number_of_reviews')

plt.subplot(1,3,3)
plt.scatter(df['latitude'],df['availability_365'])
plt.xlabel('Latitude')
plt.ylabel('availability_365')
plt.show()

plt.subplot(1, 3, 1)
plt.hist(df['price'], bins=30, color='blue')
plt.title('Frequency of Price')
plt.xlabel('Price')
plt.ylabel('Frequency')

plt.subplot(1, 3, 2)
plt.hist(df['number_of_reviews'], bins=30, color='green')
plt.title('Frequency of Number of Reviews')
plt.xlabel('Number of Reviews')
plt.ylabel('Frequency')

plt.subplot(1, 3, 3)
plt.hist(df['availability_365'], bins=30, color='orange')
plt.title('Frequency of Availability (365 days)')
plt.xlabel('Availability (days)')
plt.ylabel('Frequency')

plt.show()


#Data Cleaning

#missing values
missing_values = df.isnull().sum()
print(missing_values)

df['name'] = df['name'].fillna('Name not available')
df['host_name']=df['host_name'].fillna('Anonymmous')
df['reviews_per_month']=df['reviews_per_month'].fillna(0)
df['last_review']=df['last_review'].fillna('Did nott got any visit')

 



#Categorical Data Processing

# occurrences of each category in 'neighbourhood_group'
neighbourhood_group_dist = df['neighbourhood_group'].value_counts()

#  occurrences of each category in 'room_type'
room_type_dist = df['room_type'].value_counts()


plt.subplot(1, 2, 1)
plt.bar(neighbourhood_group_dist.index, neighbourhood_group_dist.values, color='skyblue')
plt.title('Distribution of Neighbourhood Groups')
plt.xlabel('Neighbourhood Group')
plt.ylabel('Count')

# Plot for Room Types
plt.subplot(1, 2, 2)
plt.bar(room_type_dist.index, room_type_dist.values, color='orange')
plt.title('Distribution of Room Types')
plt.xlabel('Room Type')
plt.ylabel('Count')
plt.show()
 
#Encode categorical variables




#Visualize the popularity of room types across neighborhoods.

# Group data by 'neighbourhood_group' and 'room_type', then calculate counts
room_type_popularity = df.groupby(['neighbourhood_group', 'room_type']).size().unstack()

room_type_popularity.plot(kind='bar', stacked=False)
plt.title('Popularity of Room Types Across Neighbourhood Groups')
plt.xlabel('Neighbourhood Group')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.legend(title='Room Type')
plt.show()

#print(room_type_popularity)

#Outlier Detection and Handling

plt.subplot(1, 2, 1)
plt.hist(df['price'], bins=100)
plt.xlabel('Price')
plt.ylabel('Frequency')


plt.subplot(1, 2, 2)
plt.boxplot(df['price'], vert=False, patch_artist=True)
plt.xlabel('Price')
plt.show()

Q1=df['price'].quantile(0.25)
Q3=df['price'].quantile(0.75)
IQR=Q3-Q1
max=Q3+2*IQR
min=Q1-1.5*IQR
df2=df[(df['price'] > min) & (df['price'] < max)]

#after removing the outliers, analyzing the data of price 
plt.subplot(1, 2, 1)
plt.hist(df2['price'], bins=100)
plt.xlabel('Price')
plt.ylabel('Frequency')


plt.subplot(1, 2, 2)
plt.boxplot(df2['price'], vert=False, patch_artist=True)
plt.xlabel('Price')
plt.show()


#Date Transformation

df['last_review'] = pd.to_datetime(df['last_review'],errors='coerce')


df['Year'] = df['last_review'].dt.year
df['Month'] = df['last_review'].dt.month
df['Day'] = df['last_review'].dt.day 
print(df)

#advanced analysis