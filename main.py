from code.algoritmes import random
from code.klassen import district
from code.visualisatie import smartgrid


if __name__ == "__main__":

    wijknummer = input('Wijk 1, 2 of 3: ')
    # maak een district aan.
    
    
    counter = 0
    succesvolle_run = False
    while succesvolle_run == False:
        wijk = district.District(wijknummer)
        succesvolle_run = random.random_alg(wijk)
        counter += 1
        print(counter)
        

    smartgrid.visualise(wijknummer, wijk)