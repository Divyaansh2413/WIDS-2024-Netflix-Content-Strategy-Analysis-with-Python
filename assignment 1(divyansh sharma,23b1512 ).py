import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

df=pd.read_csv('chess.csv')

#Highest Elo Identify the player with the highest Elo rating in the dataset.

elo_values = df['ELO'].to_numpy()
max_elo = np.max(elo_values)
max_index = np.argmax(elo_values)
name=df['Name'].to_numpy()
print("Maximum Elo:", max_elo)
print("name of the palyer with highest elo rating: ",name[max_index])


#Top 10 Players With Highest Elo List the top 10 players with the highest Elo ratings.

sorted_elo = np.sort(elo_values)[::-1]
a=0
while(a<10):
    for i in range(440):
        if sorted_elo[a]==elo_values[i]:
            print(name[i])
            a=a+1
            break
    
#Time Trend of Top 10's Average Elo Each Year Plot how the average Elo of the top 10 players has changed over the years.

years = df['Date'].unique()

average_elo = []

for j in range(22):
    a=0
    b=0    
    for i in range(20*j,20+20*j):
        a=a+elo_values[i]
    b=a/20
    average_elo.append(b)
plt.plot(years, average_elo)
plt.show()

#Time Trend for Number of Players Above 2750 Elo Visualize the trend for the number of players exceeding 2750 Elo each year.

players_above_2750 = []

for j in range(22):
    a=0
    for i in range(20*j,20+20*j):
        if elo_values[i]>2750:
            a=a+1
    players_above_2750.append(a)   
plt.plot(years, players_above_2750)
plt.show()

#Time Trend of Top 10's Average Age Each Year Analyze the change in the average age of the top 10 players year by year.

top10_average= []
age=df['Age'].to_numpy()

for j in range(22):
    a=0
    b=0
    for i in range(20*j,10+20*j):
        a=a+age[i]
    b=a/10
    top10_average.append(b)    

plt.plot(years, top10_average)
plt.show()       

#Time Trend for Number of Players Under 25 Years Old in Top 10 Observe how the number of top 10 players under 25 years of age has changed over the years.

top10_under_25=[]

for j in range(22):
    a=0
    for i in range(20*j,10+20*j):
        if age[i]<25:
            a=a+1
    top10_under_25.append(a)
plt.plot(years, top10_under_25)
plt.show()   

#Time Trend of Magnus Carlsen's Elo Track Magnus Carlsen's Elo rating over time

magnus_elo= []

for j in range(22):
    a=0
    for i in range(20*j,20+20*j):
        if name[i]=="Carlsen":
            a=elo_values[i]
            magnus_elo.append(a)
            break
        elif i==19+20*j:
            magnus_elo.append(0)
            
plt.plot(years, magnus_elo)
plt.show()      