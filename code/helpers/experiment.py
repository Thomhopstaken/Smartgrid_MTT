from tqdm import tqdm

import pandas as pd
from code.visualisatie import smartgrid
from code.helpers import csv_writer, helpers
from code.algoritmes import random_alg, kmeans, greedy, hill_climbing
import os

def run_experiment(algoritme, wijk, runs=1):
    wijk = helpers.wijk_lader(algoritme, wijk)

    bestand = helpers.data_pad(wijk.wijk, algoritme, experiment=True)

    try:
        df = pd.read_csv(bestand)

    except FileNotFoundError:
        csv_writer.Write_csv(bestand).maak_kosten()
        df = pd.read_csv(bestand)

    algoritmes = {'Random': random_alg.random_alg,
                  'Greedy': greedy.greedy_alg,
                  'Hill': hill_climbing.hillclimber_alg,
                  'KMeans': kmeans.kmeans_alg}

    for _ in tqdm(range(runs)):
        df = pd.read_csv(bestand)
        run = algoritmes[algoritme](wijk)
        # print(run)
        # print(run.kosten_berekening())
        csv_writer.Write_csv(bestand).append_kosten(run.kosten_berekening())
        if run.kosten_berekening() < df['kosten'].min() or not os.path.isfile(helpers.data_pad(wijk.wijk, algoritme)):
            print(df['kosten'].min())
            run.jsonify(run.wijk, algoritme)
            smartgrid.visualise(algoritme, run.wijk)


