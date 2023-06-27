import json
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import cm
import numpy as np
import os

matplotlib.use('Agg')


def visualisatie(methode: str, wijk_nummer: int) -> None:
    """Maakt een visuele weergave van het smartgrid
    volgens de opgegeven methode en wijknummer.

    In: type algoritme en wijknummer."""
    cwd = os.getcwd()
    sep = os.sep
    pad = f'{sep}figures{sep}{methode}_{wijk_nummer}_output.json'

    bestand = open(cwd + pad)
    data = json.load(bestand)

    kleuren = cm.Set2(np.linspace(0, 1, len(data) - 1))

    # Grid parameters
    plt.rcParams["figure.figsize"] = [8.00, 6.00]
    plt.rcParams["figure.autolayout"] = True
    plt.grid()

    # Coördinaten van de batterijen
    x_batterijen = []
    y_batterijen = []

    # Laad batterij coördinaten in
    for i in range(1, len(data)):
        x_batterijen.append(int(data[i]['location'].split(',')[0]))
        y_batterijen.append(int(data[i]['location'].split(',')[1]))

    # Plot de batterijen
    for i in range(len(x_batterijen)):
        plt.plot(x_batterijen[i], y_batterijen[i], marker='s', ls='none',
                 ms=10, color=kleuren[i])

    # Plot de huizen en kabels
    for i in range(1, len(data)):
        kleur = kleuren[i - 1]

        # Plot de kabels van het huis naar de batterij
        for j in range(len(data[i]['houses'])):
            kabels = (data[i]['houses'][j]['cables'])
            huis = data[i]['houses'][j]['location'].split(',')

            # Plot de kabels als er meer dan één is
            if len(kabels) != 1:
                for k in range(len(kabels) - 1):
                    plt.plot([int(kabels[k].split(',')[0]),
                              int(kabels[k + 1].split(',')[0])],
                             [int(kabels[k].split(',')[1]),
                              int(kabels[k + 1].split(',')[1])],
                             color=kleur, linestyle='dotted')

            # Plot het huis
            plt.plot(int(huis[0]), int(huis[1]), color=kleur,
                     marker='p')

    wijknummer = data[0]['district']
    plt.savefig(f"figures/smartgrid_{wijknummer}_{methode}.png")
    plt.clf()


def vernieuw_grids():
    methods = ["Greedy", "Hill", "KMeans", "Random"]
    wijken = range(1, 4)
    for method in methods:
        for wijk in wijken:
            visualisatie(method, wijk)
