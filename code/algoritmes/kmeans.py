import pandas as pd
from code.helpers import csv_writer, helpers
from sklearn.cluster import KMeans
import random
import copy



## Make a maak_clusters function an use that to create csv etc.

def gebruik_clusters(wijk, k):
    wijk_nummer = wijk.wijk
    pad = helpers.data_pad(wijk_nummer, 'houses')
    df_coords = pd.read_csv(pad, usecols=['x', 'y'])
    df_output = pd.read_csv(pad, usecols=['maxoutput'])
    df_combined = pd.read_csv(pad)


    cluster_outputs = [9999, 9999]
    while not max(cluster_outputs) <= 1800:
        km = KMeans(n_clusters=k, n_init='auto')
        cluster_id = km.fit_predict(df_coords)

        filtered_output = []
        filtered_combined = []
        for i in range(k):
            filtered_output.append(df_output[cluster_id == i])
            filtered_combined.append(df_combined[cluster_id == i])
        centroids = km.cluster_centers_
        cluster_outputs = []
        cluster_cents = []
        for i in range(k):
            cluster_outputs.append(sum(filtered_output[i]["maxoutput"]))
            cluster_cents.append(
                f'{round(centroids[i][0])}, {round(centroids[i][1])}')

        batterijen = kies_batterij(cluster_outputs)
        csv_writer.Write_csv(f'Huizen&Batterijen/k_means/batterij_{k}.csv').batterij(batterijen, cluster_cents)



    wijk.laad_batterijen(
        helpers.data_pad(wijk_nummer, k, kmeans=True), 5000)

    return filtered_combined

def kmeans_alg(wijk, k=5):
    wijk_buffer = copy.deepcopy(wijk)
    filtered_huizen = gebruik_clusters(wijk_buffer, k)
    wijk_nummer = wijk_buffer.wijk

    # goedkoopste_run = [0, 9999999]
    # goedkoopste_wijk = None
    # run_lijst = []

    for i in range(k):
        csv_writer.Write_csv(
            f'Huizen&Batterijen/k_means/batterij_{k}_cluster_{i}.csv').huizen(filtered_huizen[i])

    for i in range(k):

        wijk_buffer.laad_huizen(
            helpers.data_pad(wijk_nummer, k, i, huizen=True))
        # Vermijd overlap tussen batterij en huizen
        random.shuffle(wijk_buffer.losse_huizen)
        for huis in wijk_buffer.losse_huizen:
            if wijk_buffer.batterijen[i].x_as == huis.x_as and \
                    wijk_buffer.batterijen[i].y_as == huis.y_as:
                wijk_buffer.batterijen[i].x_as += 1
        # Alle losse huizen aan batterij verbinden
        while len(wijk_buffer.losse_huizen) > 0:
            for huis in wijk_buffer.losse_huizen:
                wijk_buffer.leg_route(wijk_buffer.batterijen[i], huis)
    return wijk_buffer

def kies_batterij(outputs):
    batterijen = []
    bat_cat = [450, 900, 1800]
    for i in range(len(outputs)):
        for j in range(len(bat_cat)):
            if outputs[i] > bat_cat[j]:
                continue
            batterijen.append(bat_cat[j])
            break

    # optimaal capaciteit:
    # batterijen = [1800, 1800, 1800, 1800, 1800, ]
    # index = outputs.index(min(outputs))
    # batterijen[index] = 450
    return batterijen
