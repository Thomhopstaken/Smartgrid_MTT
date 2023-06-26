import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import os

cwd = os.getcwd()
sep = os.sep
kleuren = cm.Set2(np.linspace(0, 1, 4))


def histogram():
    kmeans = pd.read_csv('KMeans_3_experiment.csv')
    greedy = pd.read_csv('Greedy_3_experiment.csv')
    random = pd.read_csv('Random_3_experiment.csv')
    hillclimb = pd.read_csv('Hill_3_experiment.csv')


    # gemiddelde = np.mean(data)
    # standaard_af = np.std(data)
    #
    # fig, axs = plt.subplots(2, 2)
    # axs[0, 0].hist(kmeans, density=True, color='r', bins=1000)
    # axs[0, 0].set_title('KMeans')
    # axs[1, 0].hist(greedy, density=True, color='b', bins=1000)
    # axs[1, 0].set_title('Greedy')
    # axs[0, 1].hist(random, density=True, color='g', bins=1000)
    # axs[0, 1].set_title('Random')
    # axs[1, 1].hist(hillclimb, density=True, color='c', bins=1000)
    # axs[1, 1].set_title('Hill Climber')

    plt.hist(kmeans, density=True, color=kleuren[0], label='KMeans', alpha=0.5, bins=50)
    plt.hist(greedy, density=True, color=kleuren[1], label='Greedy', alpha=0.5, bins=50)
    plt.hist(random, density=True, color=kleuren[2], label='Random', alpha=0.5, bins=50)
    plt.hist(hillclimb, density=True, color=kleuren[3], label='Hill Climber', alpha=0.5, bins=50)
    sns.kdeplot(kmeans, linewidth=2)
    sns.kdeplot(greedy, linewidth=2)
    sns.kdeplot(random, linewidth=2)
    sns.kdeplot(hillclimb, linewidth=2)

    plt.legend(loc='upper right')
    plt.show()


if __name__ == '__main__':
    histogram()
