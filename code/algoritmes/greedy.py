import random

def greedy_alg(wijk) -> None:
    print("greedy")
    """Greedy algoritme om huizen aan te sluiten op batterijen in een wijk."""

    counter = 0
    stop_counter = 0
    
    afstanden = wijk.bereken_afstand()
    #print(afstanden)
    lijst_lijsten = []
        
    for i in range(0, len(afstanden), 3):
        sublijst = afstanden[i:i+3]
        random.shuffle(sublijst)
        lijst_lijsten.append(sublijst)
    print(len(lijst_lijsten))
    print(lijst_lijsten)

    #while len(wijk.losse_huizen): 
    for inner_lijst in lijst_lijsten:
        for tuple in inner_lijst:
            batterij, huis, afstand = tuple
            if huis.kan_aansluiten(batterij):
                #print("kan aansluiten")
                counter += 1
                wijk.leg_route(batterij, huis)

    if len(wijk.losse_huizen) == 1:
        #wijk.ontkoppel_huis(huis)
        for huis in wijk.losse_huizen:
            print(huis)
            print(huis.maxoutput)

    for batterij in wijk.batterijen:
        print(batterij.resterende_capaciteit)

    print(counter)
    return wijk

