import pandas as pd
from scipy.stats import f_oneway, kruskal


def stat_test(wijknummer, test):
    """Berekent statische gegevens over experiment data.

    In: Wijknummer en type test."""
    kmeans = pd.read_csv(f'KMeans_{wijknummer}_experiment.csv')['kosten']
    greedy = pd.read_csv(f'Greedy_{wijknummer}_experiment.csv')['kosten']
    random = pd.read_csv(f'Random_{wijknummer}_experiment.csv')['kosten']
    hillclimb = pd.read_csv(f'Hill_{wijknummer}_experiment.csv')['kosten']

    if test == 'ANOVA':
        print(f'One-Way ANOVA: {f_oneway(kmeans, greedy, random, hillclimb)}')
    if test == 'Kruskal':
        print(f'Kruskal-Wallis: {kruskal(kmeans, greedy, random, hillclimb)}')

if __name__ == '__main__':
    stat_test(1, 'Kruskal')