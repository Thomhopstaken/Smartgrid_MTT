from matplotlib import pyplot as plt
import pandas as pd
from district import District

import os
import sys
sys.path.append('../..')
from algoritmes import random
from algoritmes import greedy

wijknummer = input('Wijk 1, 2 of 3: ')
colors = ['b', 'y', 'r', 'c', 'm']

# maak een district aan.
wijk = District(wijknummer)

path = os.getcwd()
parent = os.path.dirname(path)

file_path = f'{parent}\Huizen&Batterijen\district_{wijknummer}'
df = pd.read_csv(file_path + f'/district-{wijknummer}_houses.csv')

df2 = pd.read_csv(file_path + f'/district-'+wijknummer+'_batteries.csv')
positions = []
for i in range(len(df2)):
    positions.append(df2.positie[i])
x_pos = []
y_pos = []
for pos in positions:
    pos = pos.split(",")
    x_pos.append(int(pos[0]))
    y_pos.append(int(pos[1]))


# Set the figure size
plt.rcParams["figure.figsize"] = [8.00, 6.00]
plt.rcParams["figure.autolayout"] = True
plt.grid()

# List of data points
x = df.x
y = df.y

# Scatter plot with x and y
plt.scatter(x, y, color='blue', marker='p')
for i in range(len(wijk.batterijen)):
    plt.plot(x_pos[i], y_pos[i], marker='s', ls='none', ms=10, color=colors[i])


greedy.greedy_alg(wijk)

for i in range(len(wijk.gelinkte_huizen)):
    color = colors[i % len(colors)]
    for j in range(len(wijk.gelinkte_huizen[i].kabels)):
        kabel= wijk.gelinkte_huizen[i].kabels
        try:
            plt.plot([kabel[j][0], kabel[j+1][0]], [kabel[j][1], kabel[j+1][1]], color=color)
            # print(wijk.gelinkte_huizen[i].kabels[j][0], wijk.gelinkte_huizen[i].kabels[j+1][0])
        except IndexError:
            break

# Display the plot
plt.show()
