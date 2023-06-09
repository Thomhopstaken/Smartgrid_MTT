from matplotlib import pyplot as plt
import pandas as pd
from district import District
from smartgrid import huis_checker

wijknummer = input('Wijk 1, 2 of 3: ')
colors = ['b', 'y', 'r', 'c', 'm']

# maak een district aan.
wijk = District(wijknummer)


df = pd.read_csv(
    r'C:\Users\thmic\OneDrive\Documents\GitHub\Smartgrid_MTT\Huizen&Batterijen\district_1\district-1_houses.csv')

df2 = pd.read_csv(
    r'C:\Users\thmic\OneDrive\Documents\GitHub\Smartgrid_MTT\Huizen&Batterijen\district_1\district-1_batteries.csv')
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


def route_cable(wijk, batterij, huis):
    cursor_x, cursor_y = batterij.x_as, batterij.y_as
    while cursor_x < huis.x_as:
        huis.lay_cable((cursor_x), (cursor_y))
        cursor_x += 1
    while cursor_x > huis.x_as:
        huis.lay_cable((cursor_x), (cursor_y))
        cursor_x -= 1
    while cursor_y < huis.y_as:
        huis.lay_cable((cursor_x), (cursor_y))
        cursor_y += 1
    while cursor_y > huis.y_as:
        huis.lay_cable((cursor_x), (cursor_y))
        cursor_y -= 1
    huis.lay_cable((cursor_x), (cursor_y))
    wijk.creer_connectie(batterij, huis)

while len(wijk.losse_huizen) > 0:
    for batterij in wijk.batterijen:
        for huis in wijk.losse_huizen:
            if huis_checker(huis, batterij):
                # batterij.gebruik += huis.maxoutput
                wijk.huis_linken(huis.huis_id)
                route_cable(wijk, batterij, huis)

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
