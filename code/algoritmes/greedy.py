
def greedy_alg(wijk) -> None:
    print("greedy")
    """Greedy algoritme om huizen aan te sluiten op batterijen in een wijk."""
    counter = 0
    stop_counter = 0

    for batterij in wijk.batterijen:
        afstanden = batterij.bereken_afstand(wijk.losse_huizen)
    #print(afstanden)

    huis_en_afstand = list(afstanden.items())
    #print(huizen)
    
    while len(wijk.losse_huizen) > 0:
        for batterij in wijk.batterijen:
            for huizen in huis_en_afstand:
                if huizen[0].kan_aansluiten(batterij):
                    wijk.leg_route(batterij, huizen[0])
                    counter += 1
                    stop_counter = 0
                else:
                    stop_counter += 1
                    if counter >= 148 and stop_counter == 5:
                        return False
            if stop_counter == 5:
                print('run failed!')
                return False
        print('Run Succesvol!')
        return True
                    
