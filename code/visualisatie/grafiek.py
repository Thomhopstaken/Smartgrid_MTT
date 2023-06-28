import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib import cm
import os


def histogram(wijknummer, soort):
    """Maakt een histogram en plot de normale verdeling van de gegeven dataset.

    In: data, wijknummer en aantal runs."""
    cwd = os.getcwd()
    sep = os.sep
    kleuren = cm.Set2(np.linspace(0, 1, 4))

    kmeans = pd.read_csv(
        cwd + (f'{sep}Huizen&Batterijen{sep}experiment'
               f'{sep}KMeans_{wijknummer}_experiment.csv'))['kosten']
    greedy = pd.read_csv(
        cwd + (f'{sep}Huizen&Batterijen{sep}experiment'
               f'{sep}Greedy_{wijknummer}_experiment.csv'))['kosten']
    random = pd.read_csv(
        cwd + (f'{sep}Huizen&Batterijen{sep}experiment'
               f'{sep}Random_{wijknummer}_experiment.csv'))['kosten']
    hillclimb = pd.read_csv(
        cwd + (f'{sep}Huizen&Batterijen{sep}experiment'
               f'{sep}Hill_{wijknummer}_experiment.csv'))['kosten']

    if soort == 'sub':
        fig, axs = plt.subplots(2, 2, figsize=(8, 8))
        plt.subplots_adjust(hspace=0.4)
        axs[0, 0].hist(kmeans, density=True, color='r', bins=1000)
        axs[0, 0].set_title('KMeans')
        axs[1, 0].hist(greedy, density=True, color='b', bins=1000)
        axs[1, 0].set_title('Greedy')
        axs[0, 1].hist(random, density=True, color='g', bins=1000)
        axs[0, 1].set_title('Random')
        axs[1, 1].hist(hillclimb, density=True, color='c', bins=1000)
        axs[1, 1].set_title('Hill Climber')

    if soort == 'hist':
        plt.hist(kmeans, density=True, color=kleuren[0], label='KMeans',
                 alpha=0.5,
                 bins=30)
        plt.hist(greedy, density=True, color=kleuren[1], label='Greedy',
                 alpha=0.5,
                 bins=30)
        plt.hist(random, density=True, color=kleuren[2], label='Random',
                 alpha=0.5,
                 bins=30)
        plt.hist(hillclimb, density=True, color=kleuren[3],
                 label='Hill Climber',
                 alpha=0.5, bins=30)
        sns.kdeplot(kmeans, linewidth=1)
        sns.kdeplot(greedy, linewidth=1)
        sns.kdeplot(random, linewidth=1)
        sns.kdeplot(hillclimb, linewidth=1)
        plt.legend(loc='upper right')

    plt.savefig(
        cwd + f'{sep}figures{sep}grafiek_wijk_{wijknummer}_{soort}', dpi=300)


def hill_climber_grafiek(bestand):
    """Maakt een grafiek van de kostenveranderingen
    tijdens de uitvoering van de Hill Climber.

    In: bestand met kostendata."""
    data = pd.read_csv(bestand)
    data['iteratie'] = range(1, len(data) + 1)

    plt.plot(data['iteratie'], data['kosten'])

    plt.title('Hill Climber')
    plt.ylabel('Kosten')
    plt.xlabel('Iteraties')

    plt.savefig('figures/grafiek_hillclimber')
