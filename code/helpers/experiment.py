from code.algoritmes import random_alg, kmeans, greedy, hill_climbing
from code.helpers import csv_writer, helpers
from code.visualisatie import smartgrid
from scipy.stats import f_oneway, kruskal
import pandas as pd
import os
from tqdm import tqdm


def run_experiment(algoritme: str, wijk: int, runs=1) -> None:
    """Run een experiment op basis van wijk en algoritme

    In: algoritme naam, wijknummer en runs(standaard 1)."""
    wijk = helpers.wijk_lader(algoritme, wijk)
    bestand = helpers.data_pad(wijk.wijk, algoritme, experiment=True)

    # Controleer of het bestand bestaat en lees het in een DataFrame
    try:
        df = pd.read_csv(bestand)

    # Als het bestand niet bestaat, maak nieuw bestand.
    except FileNotFoundError:
        csv_writer.Write_csv(bestand).maak_kosten()
        df = pd.read_csv(bestand)

    algoritmes = {'Random': random_alg.random_alg,
                  'Greedy': greedy.greedy_alg,
                  'Hill': hill_climbing.hillclimber_alg,
                  'KMeans': kmeans.kmeans_alg}

    # Voer het gekozen algoritme uit voor het opgegeven aantal runs
    for _ in tqdm(range(runs)):
        df = pd.read_csv(bestand)
        run = algoritmes[algoritme](wijk)
        csv_writer.Write_csv(bestand).append_kosten(run.kosten_berekening())

        # Controleer of run goedkoper is dan de vorige beste run
        # en/of het experimentele bestand bestaat
        if run.kosten_berekening() < df['kosten'].min() or not os.path.isfile(
                helpers.data_pad(wijk.wijk, algoritme, experiment=True)):
            print(f"Nieuw goedkoopst run: {df['kosten'].min()}")
            run.jsonify(run.wijk, algoritme)
            smartgrid.visualisatie(algoritme, run.wijk)


def stat_test(wijknummer, test) -> None:
    """Run een hypothese test op basis van wijk

        In: wijknummer en test"""
    cwd = os.getcwd()
    sep = os.sep
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

    if test == 'ANOVA':
        print(f'One-Way ANOVA: {f_oneway(kmeans, greedy, random, hillclimb)}')
    if test == 'Kruskal':
        print(f'Kruskal-Wallis: {kruskal(kmeans, greedy, random, hillclimb)}')
