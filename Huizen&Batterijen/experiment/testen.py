import os
import pandas as pd
from scipy.stats import f_oneway, kruskal

cwd = os.getcwd()
sep = os.sep

bestand = f'gecombineerd.csv'
df = pd.read_csv(bestand)
kmeans = df['kmeans'].dropna()
greedy = df['greedy'].dropna()
random = df['random'].dropna()
hillclimb = df['hillclimber'].dropna()

print(f'One-Way ANOVA: {f_oneway(kmeans, greedy, random, hillclimb)}')
print(f'Kruskal-Wallis: {kruskal(kmeans, greedy, random, hillclimb)}')
