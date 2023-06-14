import pandas as pd
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
from matplotlib import cm
import numpy as np
import os

def kmeans_alg(wijknummer):
    cwd = os.getcwd()
    sep = os.sep
    pad = f'{sep}Huizen&Batterijen{sep}district_{wijknummer}{sep}district-{wijknummer}_houses.csv'
    df = pd.read_csv(cwd + os.path.normpath(pad), usecols=['x', 'y'])

    k = range(2, 11)
    # ssd = []
    # score = []
    #
    # for i in k:
    #     km = KMeans(n_clusters=i, n_init='auto', random_state=1).fit(df)
    #     ssd.append(km.inertia_)
    plt.rcParams["figure.figsize"] = [8.00, 6.00]
    plt.rcParams["figure.autolayout"] = True
    plt.grid()
    # print(ssd)
    # print(score)
    # plt.plot(k, ssd)
    # plt.show()

    colors = cm.rainbow(np.linspace(0, 1, len(k) + 1))
    for i in k:
        # Centroids vinden met k clusters
        km = KMeans(n_clusters=i, n_init='auto')
        print(km)
        label = km.fit_predict(df)

        filtered_labels = []
        for j in range(i):
            filtered_labels.append(df[label == j])

        centroids = km.cluster_centers_
        print(centroids)
        for l in range(i):
            plt.scatter(filtered_labels[l]['x'], filtered_labels[l]['y'], color=colors[l])
            plt.scatter(centroids[l][0], centroids[l][1], color='k')

        # plt.show()
        plt.savefig(f"figures/kmeans{i}.png")
        plt.clf()

