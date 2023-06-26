import os
import pandas as pd
from scipy.stats import shapiro

cwd = os.getcwd()
sep = os.sep

bestand = f'gecombineerd.csv'
df = pd.read_csv(bestand)
shapiro(df['kmeans'])