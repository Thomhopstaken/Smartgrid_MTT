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



    for k_hat in k:
        colors = cm.rainbow(np.linspace(0, 1, len(range(k_hat))))
        # wijk = district.District(wijk_kiezen, aantal_runs, laad_batterij=False)
        # Centroids vinden met k clusters
        km = KMeans(n_clusters=k_hat, n_init='auto')
        # print(km)
        label = km.fit_predict(df_coords)

        filtered_labels = []
        filtered_output = []
        filtered_combined = []
        for i in range(k_hat):
            filtered_labels.append(df_coords[label == i])
            filtered_output.append(df_output[label == i])
            filtered_combined.append(df_combined[label == i])
        # print(filtered_labels)
        centroids = km.cluster_centers_


        # print(centroids)
        outputs = []
        cluster_cents = []
        for i in range(k_hat):
            plt.scatter(filtered_labels[i]['x'], filtered_labels[i]['y'], color=colors[i])
            plt.scatter(centroids[i][0], centroids[i][1], color='k')
            # print(f'sum of output for {i} clusters: {sum(filtered_output[i]["maxoutput"])}')
            outputs.append(sum(filtered_output[i]["maxoutput"]))
            cluster_cents.append(f'{round(centroids[i][0])}, {round(centroids[i][1])}')

        if max(outputs) <= 1800:
            # print(outputs)
            # plt.show()
            plt.savefig(f"figures/k_means/kmeans{k_hat}.png")
            batterijen = batterij_keuze(outputs)
            write_csv_batterij(f'Huizen&Batterijen/k_means/batterij_{k_hat}.csv', batterijen, cluster_cents)
            for i in range(len(filtered_output)):
                write_csv_huizen(f'Huizen&Batterijen/k_means/batterij_{k_hat}_cluster_{i}.csv', filtered_combined[i])
            wijk = district.District(wijknummer, k_hat, False, False)
            wijk.laad_batterijen(wijk.data_pad(wijknummer, k_hat, kmeans=True))

            for i in range(k_hat):
                wijk.laad_huizen(wijk.data_pad(wijknummer, k_hat, i, huizen=True))
                for huis in wijk.losse_huizen:
                    wijk.leg_route(wijk.batterijen[i], huis)
                # print(f'1: {len(wijk.losse_huizen)}')
                # print(f'2: {len(wijk.gelinkte_huizen)}')
            plt.clf()
            smartgrid.visualise(k_hat, wijk, k_means=True, k=k_hat)



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
