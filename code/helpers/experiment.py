from code.algoritmes import random_alg, kmeans, greedy, hill_climbing
from code.helpers import csv_writer, helpers
from code.visualisatie import smartgrid
import pandas as pd
import os
from tqdm import tqdm


def run_experiment(algoritme: str, wijk: int, runs=1) -> None:
    """Run een experiment op basis van wijk en algoritme>

    In: algoritme naam en wijknummer."""
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
        if run.kosten_berekening() < df['kosten'].min() or not os.path.isfile(helpers.data_pad(wijk.wijk, algoritme, experiment=True)):
            print(f"Nieuw goedkoopst run: {df['kosten'].min()}")
            run.jsonify(run.wijk, algoritme)
            smartgrid.visualisatie(algoritme, run.wijk)
