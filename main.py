from code.algoritmes import random_alg, greedy, kmeans
from code.algoritmes import hill_climbing
from code.klassen import district
from code.visualisatie import smartgrid
from code.visualisatie import grafiek


def run_printer(x):
    print(f'run: {x + 1}', end='\r', flush=True)

def gemiddelde_berekenen(data):
    return int(sum(data)/len(data))


if __name__ == "__main__":

    wijk_kiezen = input('Kies wijk 1, 2 of 3: ')
    algoritme_kiezen = input('Kies uit algoritme (R)andom, (G)reedy, (K)Means, (H)ill: ')

    algoritme_kiezen = algoritme_kiezen[0].upper() + algoritme_kiezen[1:]

    run_succesvol = False
    succesvolle_runs = 0
    mislukte_runs = 0
    goedkoopste_run = ''
    goedkoopste_kosten = 9999999
    duurste_kosten = 0
    

    if algoritme_kiezen == 'R' or algoritme_kiezen == "Random":
        aantal_runs = int(input('geef aantal runs: '))
        bestandsnaam = f'figures/data_random/kosten_wijk:_{wijk_kiezen}_|runs:_{aantal_runs}.csv'
        grafiek.schrijf_csv_kosten(bestandsnaam)
        for x in range (0, aantal_runs):
            wijk = district.District(wijk_kiezen, x)
            run_succesvol = random_alg.random_alg(wijk)
            run_printer(x)
            if run_succesvol:
                kosten_wijk = wijk.kosten_berekening()
                grafiek.data_schrijven(bestandsnaam, kosten_wijk)
                if kosten_wijk < goedkoopste_kosten:
                    goedkoopste_kosten = kosten_wijk
                    goedkoopste_run = wijk
                if kosten_wijk > duurste_kosten:
                    duurste_kosten = kosten_wijk
                succesvolle_runs += 1
            else: 
                mislukte_runs += 1
        data = grafiek.data_inlezen(bestandsnaam)        
        gemiddelde_prijs = gemiddelde_berekenen(data)
        grafiek.grafiek_maken(data, wijk_kiezen, aantal_runs)
                
    elif algoritme_kiezen == 'G' or algoritme_kiezen == "Greedy":
        aantal_runs = 1
        wijk = district.District(wijk_kiezen, aantal_runs)
        run = greedy.greedy_alg(wijk)
        succesvolle_runs[wijk] = wijk.kosten_berekening()
    
    elif algoritme_kiezen == 'H' or algoritme_kiezen == "Hill":
        aantal_runs = 1
        while not run_succesvol: 
            wijk = district.District(wijk_kiezen, aantal_runs)
            run_succesvol = random_alg.random_alg(wijk)
        kosten_randomrun = wijk.kosten_berekening()
        print(f'kosten random:      {kosten_randomrun}')
        hill_climbing.hill_climbing_alg(wijk)
        print(f'hill climbing kosten: {wijk.kosten_berekening()}')
        

    elif algoritme_kiezen == 'K' or algoritme_kiezen == "KMeans":

        run = kmeans.kmeans_alg(wijk_kiezen, n_runs=20)

        run[0][0].jsonify(wijk_kiezen)
        smartgrid.visualise(run[0][1], run[0][0], k_means=True, k=run[0][1])
        print(run[1])
        print(run[2])

    else: 
        print('Invalid Argument')
    
    # if succesvolle_runs > 0:
    #     #goedkoopste_run = min(succesvolle_runs, key= lambda x: succesvolle_runs[x])
    #     #gemiddelde_prijs = int(sum(succesvolle_runs.values()) / succesvolle_runs)
    #     #duurste_run = max(succesvolle_runs, key= lambda x: succesvolle_runs[x])
        
    #     print('')
    #     print('Resultaten: ')
    #     print(f'Succesvolle runs:   {succesvolle_runs}')
    #     print(f'Mislukte runs:      {mislukte_runs}')
    #     print(f'Goedkoopste run:    {goedkoopste_run.id} | {goedkoopste_kosten}')
    #     print(f'Gemiddelde:         {gemiddelde_prijs}')
    #     print(f'Duurste run:        {duurste_kosten}')
        
    #     smartgrid.visualise(wijk_kiezen, goedkoopste_run)
    #     goedkoopste_run.jsonify(wijk_kiezen)
        
    # else:
    #     print('Geen succesvolle runs!')


    