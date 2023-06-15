import pandas as pd
from code.klassen import district
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
from matplotlib import cm
from code.visualisatie import smartgrid
import numpy as np
import csv
import os

def kmeans_alg(wijknummer):
    cwd = os.getcwd()
    sep = os.sep
    pad = f'{sep}Huizen&Batterijen{sep}district_{wijknummer}{sep}district-{wijknummer}_houses.csv'
    df_coords = pd.read_csv(cwd + os.path.normpath(pad), usecols=['x', 'y'])
    df_output = pd.read_csv(cwd + os.path.normpath(pad), usecols=['maxoutput'])
    df_combined = pd.read_csv(cwd + os.path.normpath(pad))

    k = range(2, 11)
    plt.rcParams["figure.figsize"] = [8.00, 6.00]
    plt.rcParams["figure.autolayout"] = True
    plt.grid()

    colors = cm.rainbow(np.linspace(0, 1, len(k) + 3))

    for i in k:
        # wijk = district.District(wijk_kiezen, aantal_runs, laad_batterij=False)
        # Centroids vinden met k clusters
        km = KMeans(n_clusters=i, n_init='auto')
        # print(km)
        label = km.fit_predict(df_coords)

        filtered_labels = []
        filtered_output = []
        filtered_combined = []
        for j in range(i):
            filtered_labels.append(df_coords[label == j])
            filtered_output.append(df_output[label == j])
            filtered_combined.append(df_combined[label == j])
        # print(filtered_labels)
        centroids = km.cluster_centers_


        # print(centroids)
        outputs = []
        cluster_cents = []
        for l in range(i):
            plt.scatter(filtered_labels[l]['x'], filtered_labels[l]['y'], color=colors[l])
            plt.scatter(centroids[l][0], centroids[l][1], color='k')
            # print(f'sum of output for {i} clusters: {sum(filtered_output[l]["maxoutput"])}')
            outputs.append(sum(filtered_output[l]["maxoutput"]))
            cluster_cents.append(f'{round(centroids[l][0])}, {round(centroids[l][1])}')

        if max(outputs) <= 1800:
            # print(outputs)
            # plt.show()
            plt.savefig(f"figures/k_means/kmeans{i}.png")
            batterijen = batterij_keuze(outputs)
            write_csv_batterij(f'Huizen&Batterijen/k_means/batterij_{i}.csv', batterijen, cluster_cents)
            for m in range(len(filtered_output)):
                write_csv_huizen(f'Huizen&Batterijen/k_means/batterij_{i}_cluster_{m}.csv', filtered_combined[m])
            wijk = district.District(wijknummer, i, False, False)
            wijk.laad_batterijen(wijk.data_pad(wijknummer, i, kmeans=True))

            for n in range(i):
                wijk.laad_huizen(wijk.data_pad(wijknummer, i, n, huizen=True))
                for huis in wijk.losse_huizen:
                    wijk.leg_route(wijk.batterijen[n], huis)
            plt.clf()
            smartgrid.visualise(i, wijk, k_means=True, k=k)



        plt.clf()
        plt.rcParams["figure.figsize"] = [8.00, 6.00]
        plt.rcParams["figure.autolayout"] = True
        plt.grid()

    # print(cluster_cents)

def write_csv_batterij(filename, batterijen, centroids):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["positie", "capaciteit"]
        writer.writerow(field)
        for i in range(len(batterijen)):
            writer.writerow([centroids[i], batterijen[i]])

def write_csv_huizen(filename, huizen):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["x", "y", "maxoutput"]
        writer.writerow(field)
        for ind in huizen.index:
            writer.writerow([huizen['x'][ind], huizen['y'][ind], huizen['maxoutput'][ind]])

def batterij_keuze(outputs):
    batterijen = []
    bat_cat = [450, 900, 1800]
    for i in range(len(outputs)):
        for j in range(len(bat_cat)):
            if outputs[i] > bat_cat[j]:
                continue
            batterijen.append(bat_cat[j])
            break
    return batterijen
