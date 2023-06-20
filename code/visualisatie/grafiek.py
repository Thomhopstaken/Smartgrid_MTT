import csv
import numpy as np
import matplotlib.pyplot as plt

def schrijf_csv_kosten(bestandsnaam):
    with open(bestandsnaam, 'w', newline='') as bestand:
        schrijver = csv.writer(bestand)
        veld = ["Kosten:"]
        schrijver.writerow(veld)

def data_schrijven(bestandsnaam, kosten):
    with open(bestandsnaam, 'a', newline='') as bestand:
        schrijver = csv.writer(bestand)
        veld = [kosten]
        schrijver.writerow(veld)


def data_inlezen(bestandsnaam):
    data = []
    
    with open(bestandsnaam, 'r',) as bestand:
        lezer = csv.reader(bestand)
        
        for rij in lezer:
            for waarde in rij:
                if waarde != 'Kosten:':
                    data.append(float(waarde))
    return data


def grafiek_maken(data, wijk_kiezen, aantal_runs):
    gemiddelde = np.mean(data)
    standaard_af = np.std(data)
    
    x = np.linspace(min(data), max(data), 100)
    y = (1 / (standaard_af * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - gemiddelde) / standaard_af) ** 2)
    
    plt.plot(x, y)
    plt.hist(data, bins=20, density=True, alpha=0.5)
    plt.title(f'Wijk {wijk_kiezen}')
    
    plt.savefig(f'figures/data_random/grafiek_wijk:_{wijk_kiezen}|runs:_{aantal_runs}')