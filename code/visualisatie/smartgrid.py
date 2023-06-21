import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from matplotlib import cm
import numpy as np
import pandas as pd
import os
import json

def visualise(methode):

    cwd = os.getcwd()
    sep = os.sep
    pad = f'{sep}figures{sep}output.json'

    file = open(cwd + pad)
    data = json.load(file)

    colors = cm.rainbow(np.linspace(0, 1, len(data) - 1))

    # Grid parameters
    plt.rcParams["figure.figsize"] = [8.00, 6.00]
    plt.rcParams["figure.autolayout"] = True
    plt.grid()

    x_batterijen = []
    y_batterijen = []

    for i in range(1, len(data)):
        x_batterijen.append(int(data[i]['location'].split(',')[0]))
        y_batterijen.append(int(data[i]['location'].split(',')[1]))


    for i in range(len(x_batterijen)):
        plt.plot(x_batterijen[i], y_batterijen[i], marker='s', ls='none', ms=10, color=colors[i])

    for i in range(1, len(data)):
        color = colors[i - 1]
        for j in range(len(data[i]['houses'])):
            kabels = (data[i]['houses'][j]['cables'])
            huis = data[i]['houses'][j]['location'].split(',')
            if len(kabels) != 1:
                for k in range(len(kabels)):
                    try:
                        plt.plot([int(kabels[k].split(',')[0]), int(kabels[k + 1].split(',')[0])], [int(kabels[k].split(',')[1]), int(kabels[k + 1].split(',')[1])], color=color, linestyle='dotted')

                    except IndexError:
                        plt.plot(int(huis[0]), int(huis[1]), color=color, marker='p')
                        break
            else:
                plt.plot(int(huis[0]), int(huis[1]), color=color, marker='p')

    wijknummer = data[0]['district']
    plt.savefig(f"figures/smartgrid_{wijknummer}_{methode}.png")




