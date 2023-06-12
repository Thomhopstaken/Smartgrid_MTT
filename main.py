from code.algoritmes import random
from code.klassen import district
from code.visualisatie import smartgrid


if __name__ == "__main__":

    wijknummer = input('Wijk 1, 2 of 3: ')
    colors = ['b', 'y', 'r', 'c', 'm']
    # maak een district aan.
    wijk = district.District(wijknummer)

    random.random_alg(wijk)

    smartgrid.visualise(wijknummer, wijk)