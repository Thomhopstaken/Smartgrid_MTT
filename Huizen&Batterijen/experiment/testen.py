import pandas as pd
import numpy as np
from scipy.stats import f_oneway, kruskal


def stat_test(wijknummer, test):
    kmeans = pd.read_csv(f'KMeans_{wijknummer}_experiment.csv')['kosten']
    greedy = pd.read_csv(f'Greedy_{wijknummer}_experiment.csv')['kosten']
    random = pd.read_csv(f'Random_{wijknummer}_experiment.csv')['kosten']
    hillclimb = pd.read_csv(f'Hill_{wijknummer}_experiment.csv')['kosten']
    q3, q1 = np.percentile(hillclimb, [75, 25])
    print(len(hillclimb))
    iqr = q3 - q1
    print(iqr)
    if test == 'ANOVA':
        print(f'One-Way ANOVA: {f_oneway(kmeans, greedy, random, hillclimb)}')
    if test == 'Kruskal':
        print(f'Kruskal-Wallis: {kruskal(kmeans, greedy, random, hillclimb)}')

if __name__ == '__main__':
    stat_test(1, 'Kruskal')