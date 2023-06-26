import copy
from code.helpers import csv_writer, helpers
import pandas as pd
from sklearn.cluster import KMeans
import random


def gebruik_clusters(wijk: object, k: int) -> list:
    """Vind clusters in wijk.

    In: wijk object en aantal clusters.
    uit: lijst."""
    wijk_nummer = wijk.wijk
    pad = helpers.data_pad(wijk_nummer, 'houses')
    df_coords = pd.read_csv(pad, usecols=['x', 'y'])
    df_output = pd.read_csv(pad, usecols=['maxoutput'])
    df_gecombineerd = pd.read_csv(pad)
    cluster_outputs = [9999, 9999]

    # Itereer totdat maximum van cluster_outputs kleiner of gelijk is aan 1800
    while not max(cluster_outputs) <= 1800:
        km = KMeans(n_clusters=k, n_init='auto')
        cluster_id = km.fit_predict(df_coords)
        gefilterde_output = []
        gefilterd_gecombineerd = []

        # Iteratieve clustering tot gewenste maximale output-waarde bereikt is
        for i in range(k):
            gefilterde_output.append(df_output[cluster_id == i])
            gefilterd_gecombineerd.append(df_gecombineerd[cluster_id == i])
        centroids = km.cluster_centers_
        cluster_outputs = []
        cluster_cents = []

        # Bereken output voor elke gefilterde cluster en append cluster_outputs
        for i in range(k):
            cluster_outputs.append(sum(gefilterde_output[i]["maxoutput"]))
            cluster_cents.append(
                f'{round(centroids[i][0])}, {round(centroids[i][1])}')

        batterijen = kies_batterij(cluster_outputs)
        csv_writer.Write_csv(f'Huizen&Batterijen/k_means/batterij_{k}.csv') \
            .batterij(batterijen, cluster_cents)

    wijk.laad_batterijen(
        helpers.data_pad(wijk_nummer, k, kmeans=True), 5000)
    return gefilterd_gecombineerd


def kmeans_alg(wijk: object, k=5) -> object:
    """ Voert het K-means clustering algoritme uit op een wijkobject.

    In: wijk object en k(standaard 5).
    Uit: wijk object."""
    wijk_buffer = copy.deepcopy(wijk)
    gefilterde_huizen = gebruik_clusters(wijk_buffer, k)
    wijk_nummer = wijk_buffer.wijk

    # Schrijf de geclusterde huizen naar CSV-bestanden
    for i in range(k):
        csv_writer.Write_csv(
            f'Huizen&Batterijen/k_means/batterij_{k}_cluster_{i}.csv').huizen(
            gefilterde_huizen[i])

    # Laad huizen in het wijkobject voor elk cluster
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


def kies_batterij(outputs: list[float]) -> list[int]:
    """Kiest de batterijcapaciteiten op basis van de gegeven outputs.

    In: lijst van floats.
    Uit: lijst van integers"""
    batterijen = []
    bat_cat = [450, 900, 1800]

    # Selecteer batterijcapaciteiten op basis van outputwaarden
    for i in range(len(outputs)):
        for j in range(len(bat_cat)):
            if outputs[i] > bat_cat[j]:
                continue
            batterijen.append(bat_cat[j])
            break
    return batterijen
