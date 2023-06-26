import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def histogram(data, wijk_kiezen, aantal_runs):
    """Maakt een histogram en plot de normale verdeling van de gegeven dataset.

    In: data, wijknummer en aantal runs."""
    gemiddelde = np.mean(data)
    standaard_af = np.std(data)

    x = np.linspace(min(data), max(data), 100)
    y = (1 / (standaard_af * np.sqrt(2 * np.pi))) * np.exp(
        -0.5 * ((x - gemiddelde) / standaard_af) ** 2)

    plt.plot(x, y)
    plt.hist(data, bins=20, density=True, alpha=0.5)
    plt.title(f'Wijk {wijk_kiezen}')

    plt.savefig(
        f'figures/data_random/grafiek_wijk_{wijk_kiezen}_runs:_{aantal_runs}')


def hill_climber_grafiek(bestand):
    """Maakt een grafiek van de kostenveranderingen
    tijdens de uitvoering van de Hill Climber.

    In: bestand met kostendata."""
    data = pd.read_csv(bestand)
    data['iteratie'] = range(1, len(data) + 1)

    plt.plot(data['iteratie'], data['kosten'])

    plt.title('Hill Climber')
    plt.ylabel('Kosten')
    plt.xlabel('Iteraties')

    plt.savefig('figures/grafiek_hillclimber')
