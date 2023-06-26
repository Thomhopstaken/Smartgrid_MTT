from code.algoritmes import random_alg, greedy, kmeans
from code.algoritmes import hill_climbing
from code.klassen import district
from code.visualisatie import smartgrid
from code.helpers import experiment, helpers
from code.visualisatie import grafiek
import os


if __name__ == "__main__":

    wijk_kiezen = input('Kies wijk 1, 2 of 3: ')
    wijk = district.Wijk(wijk_kiezen, wijk_kiezen)
    algoritme_kiezen = input('Kies uit algoritme (R)andom, (G)reedy, (K)Means, (H)ill: ')
    aantal_runs = int(input('Geef aantal runs: '))
    algoritme_kiezen = algoritme_kiezen[0].upper() + algoritme_kiezen[1:]
    
    if algoritme_kiezen == 'R' or algoritme_kiezen == "Random":
        experiment.run_experiment("Random", wijk_kiezen, aantal_runs)            
    elif algoritme_kiezen == 'G' or algoritme_kiezen == "Greedy":
        experiment.run_experiment("Greedy", wijk_kiezen, aantal_runs)
    elif algoritme_kiezen == 'H' or algoritme_kiezen == "Hill":
        experiment.run_experiment("Hill", wijk_kiezen, aantal_runs)
    elif algoritme_kiezen == 'K' or algoritme_kiezen == "KMeans":
        experiment.run_experiment("KMeans", wijk_kiezen, aantal_runs)
    elif algoritme_kiezen == 'Test':
        cwd = os.getcwd()
        grafiek.hill_climber_grafiek(f'{cwd}/Huizen&Batterijen/experiment/Hill_Climb_Run_Hill_experiment.csv')
    else: 
        print('Invalid Argument')