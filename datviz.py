import numpy as np
import matplotlib.pyplot as plt

labels = 'USA', 'CAN', 'NOR', 'URS', 'FIN', 'SWE', 'GER', 'SUI', 'AUT', 'RUS'
sizes = [650,623,454,437,432,430,357,282,277,260]


fig1, ax1 = plt.subplots()
plt.title("Canada Verses The Top 10 Countries in Medal Countries: All Time")
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

labels = 'USA', 'CAN', 'NOR', 'FIN', 'SWE', 'GER', 'SUI', 'AUT', 'RUS'
sizes = [64,89,35,33,54,35,32,26,67]


fig5, ax5 = plt.subplots()
plt.title("Canada Verses The Top 10 Countries in Medal Countries: 2014")
ax5.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax5.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

labels = 'USA', 'CAN', 'NOR', 'FIN', 'SWE', 'GER', 'SUI', 'AUT', 'RUS'
sizes = [97,90,39,49,18,53,12,25,24]


fig5, ax5 = plt.subplots()
plt.title("Canada Verses The Top 10 Countries in Medal Countries: 2010")
ax5.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax5.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


x = np.arange(10)
bronzemedals = [166,106,126,92,220,176,96,131,102,78]

fig, ax =plt.subplots()
plt.bar(x,bronzemedals)
plt.xticks(x,('USA','CAN','NOR','URS','FIN','SWE','GER','SUI','AUT','RUS'))
plt.title('Canada Verse Top 10 Countries: Bronze')
plt.xlabel('Countries')
plt.ylabel('Bronze Medals')


x = np.arange(10)
silvermedals = [318,203,170,96,146,128,125,76,97,89]

fig, ax =plt.subplots()
plt.bar(x,silvermedals)
plt.xticks(x,('USA','CAN','NOR','URS','FIN','SWE','GER','SUI','AUT','RUS'))
plt.title('Canada Verse Top 10 Countries: Silver')
plt.xlabel('Countries')
plt.ylabel('Silver Medals')

x = np.arange(10)
goldmedals = [166,314,158,249,66,126,136,76,97,93]

fig, ax =plt.subplots()
plt.bar(x,goldmedals)
plt.xticks(x,('USA','CAN','NOR','URS','FIN','SWE','GER','SUI','AUT','RUS'))
plt.title('Canada Verse Top 10 Countries: Gold')
plt.xlabel('Countries')
plt.ylabel('Gold Medals')
