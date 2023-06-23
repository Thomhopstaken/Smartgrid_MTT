from code.algoritmes import random_alg, greedy, kmeans
from code.algoritmes import hill_climbing
from code.klassen import district
from code.visualisatie import smartgrid
from code.helpers import experiment, helpers


def run_printer(x):
    print(f'run: {x + 1}', end='\r', flush=True)

def gemiddelde_berekenen(data):
    return int(sum(data)/len(data))


if __name__ == "__main__":

    wijk_kiezen = input('Kies wijk 1, 2 of 3: ')
    wijk = district.Wijk(wijk_kiezen, wijk_kiezen)
    algoritme_kiezen = input('Kies uit algoritme (R)andom, (G)reedy, (K)Means, (H)ill: ')

    algoritme_kiezen = algoritme_kiezen[0].upper() + algoritme_kiezen[1:]

    run_succesvol = False
    succesvolle_runs = 0
    mislukte_runs = 0
    goedkoopste_run = ''
    goedkoopste_kosten = 9999999
    duurste_kosten = 0
    

    if algoritme_kiezen == 'R' or algoritme_kiezen == "Random":
        # wijk = helpers.wijk_lader("Random", wijk_kiezen)
        # kmeans.gebruik_clusters(wijk, 5)
        # for _ in range(5):
        # run = random_alg.random_alg(wijk)
        # run.jsonify(wijk_kiezen, "Random")
        # for batterij in run.batterijen:
        #     for huis in batterij.gelinkte_huizen:
        #         print(huis.kabels)

        # run.jsonify(wijk_kiezen, "Random")
        # smartgrid.visualise("Random", wijk_kiezen)
        experiment.run_experiment("Random", wijk_kiezen, 5)


        # aantal_runs = int(input('geef aantal runs: '))


        # bestandsnaam = helpers.data_pad(wijk_nummer, algoritme, experiment=True))
        # grafiek.schrijf_csv_kosten(bestandsnaam)
        # for x in range (0, aantal_runs):
        #     wijk = district.Wijk(wijk_kiezen, x)
        #     run_succesvol = random_alg.random_alg(wijk)
        #     run_printer(x)
        #     if run_succesvol:
        #         kosten_wijk = wijk.kosten_berekening()
        #         grafiek.data_schrijven(bestandsnaam, kosten_wijk)
        #         if kosten_wijk < goedkoopste_kosten:
        #             goedkoopste_kosten = kosten_wijk
        #             goedkoopste_run = wijk
        #         if kosten_wijk > duurste_kosten:
        #             duurste_kosten = kosten_wijk
        #         succesvolle_runs += 1
        #     else:
        #         mislukte_runs += 1
        # data = grafiek.data_inlezen(bestandsnaam)
        # gemiddelde_prijs = gemiddelde_berekenen(data)
        # grafiek.grafiek_maken(data, wijk_kiezen, aantal_runs)
                
    elif algoritme_kiezen == 'G' or algoritme_kiezen == "Greedy":
        experiment.run_experiment("Greedy", wijk_kiezen, 5)
        # aantal_runs = 1
        # wijk = district.Wijk(wijk_kiezen, aantal_runs)
        # run = greedy.greedy_alg(wijk)
        # succesvolle_runs[wijk] = wijk.kosten_berekening()
        # run.jsonify(wijk_kiezen)
        # smartgrid.visualise("Greedy")
        # print(wijk.kosten_berekening())

    elif algoritme_kiezen == 'H' or algoritme_kiezen == "Hill":
        # aantal_runs = 10
        # runs = 0
        # while runs <= aantal_runs:
        # wijk = helpers.wijk_lader("Hill", wijk_kiezen)
        # wijk = random_alg.random_alg(wijk)
        #     kosten_randomrun = wijk.kosten_berekening()
        #     print(f'kosten random:      {kosten_randomrun}')
        # hillclimber = hill_climbing.Hill_climber(wijk)
        # wijk = hillclimber.draai_hillclimber()
        # print(wijk.kosten_berekening())
        # run = hill_climbing.hillclimber_alg(wijk)
        # print(run.kosten_berekening())
        #     print(hillclimber.aanpassingen)
        #     runs += 1
        experiment.run_experiment("Hill", wijk_kiezen, 5)

    

    elif algoritme_kiezen == 'K' or algoritme_kiezen == "KMeans":
        # wijk = helpers.wijk_lader("KMeans", wijk_kiezen)
        experiment.run_experiment("KMeans", wijk_kiezen, 5)
        # for _ in range(5):
        #     run = kmeans.kmeans_alg(wijk)
        #     print(run.kosten_berekening())
        # run.jsonify(wijk_kiezen, "KMeans")
        # smartgrid.visualise("KMeans", wijk_kiezen)

    else: 
        print('Invalid Argument')
    
    if succesvolle_runs > 0:
        # goedkoopste_run = min(succesvolle_runs, key= lambda x: succesvolle_runs[x])
        # gemiddelde_prijs = int(sum(succesvolle_runs.values()) / succesvolle_runs)
        # duurste_run = max(succesvolle_runs, key= lambda x: succesvolle_runs[x])

        print('')
        print('Resultaten: ')
        print(f'Succesvolle runs:   {succesvolle_runs}')
        print(f'Mislukte runs:      {mislukte_runs}')
        print(f'Goedkoopste run:    {goedkoopste_run.id} | {goedkoopste_kosten}')
        print(f'Gemiddelde:         {gemiddelde_prijs}')
        print(f'Duurste run:        {duurste_kosten}')

        smartgrid.visualise(wijk_kiezen, goedkoopste_run)
        goedkoopste_run.jsonify(wijk_kiezen)

    else:
        print('Geen succesvolle runs!')


    