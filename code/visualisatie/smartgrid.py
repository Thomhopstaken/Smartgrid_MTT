import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import pandas as pd
import os


def visualise(wijknummer, wijk):
    cwd = os.getcwd()
    sep = os.sep
    pad2 = f'{sep}Huizen&Batterijen{sep}district_{wijknummer}{sep}district-{wijknummer}_batteries.csv'
    df = pd.read_csv(cwd + os.path.normpath(pad2))
    colors = ['b', 'y', 'r', 'c', 'm']
    positions = []
    for i in range(len(df)):
        positions.append(df.positie[i])
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


    # Scatter plot with x and y
    for i in range(len(wijk.batterijen)):
        plt.plot(x_pos[i], y_pos[i], marker='s', ls='none', ms=10, color=colors[i])

    batterij_coordinaten = []
    for batterij in wijk.batterijen:
        coord = (batterij.x_as, batterij.y_as)
        batterij_coordinaten.append(coord)



    for i in range(len(wijk.gelinkte_huizen)):
        index = wijk.batterijen.index(wijk.gelinkte_huizen[i].aangesloten)
        color = colors[index]
        for j in range(len(wijk.gelinkte_huizen[i].kabels)):
            kabel = wijk.gelinkte_huizen[i].kabels
            if len(kabel) != 1:
                try:
                    plt.plot([kabel[j][0], kabel[j+1][0]], [kabel[j][1], kabel[j+1][1]], color=color, linestyle='dotted')
                    # print(wijk.gelinkte_huizen[i].kabels[j][0], wijk.gelinkte_huizen[i].kabels[j+1][0])
                except IndexError:
                    plt.plot(wijk.gelinkte_huizen[i].x_as, wijk.gelinkte_huizen[i].y_as, color=color, marker='p')
                    break
            else:
                plt.plot(wijk.gelinkte_huizen[i].x_as,
                         wijk.gelinkte_huizen[i].y_as, color=color, marker='p')


    # Display the plot
    # plt.show()
    plt.savefig("figures/smartgrid.png")
