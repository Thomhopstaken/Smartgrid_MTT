import random

def greedy_alg(wijk) -> None:
    print("greedy")
    """Greedy algoritme om huizen aan te sluiten op batterijen in een wijk."""

    counter = 0
    
    # Enkele lijst
    afstanden = wijk.bereken_afstand()

    for batterij, huis, _ in afstanden:
        if huis.kan_aansluiten(batterij):
            wijk.leg_route(batterij, huis)
            counter += 1

    while len(wijk.losse_huizen) > 0:
        # Teruggaan en herverdelen
        #print(len(wijk.losse_huizen))
        willekeurige_batterij = random.choice(wijk.batterijen)
        willekeurig_huis = random.choice(willekeurige_batterij.gelinkte_huizen)
        willekeurige_batterij.ontkoppel_huis(willekeurig_huis, wijk)
        #print("ontkoppeld")
        #print(len(wijk.losse_huizen))
        
        # for batterij, huis, _ in afstanden:
        #     if huis.kan_aansluiten(batterij):
        #         wijk.leg_route(batterij, huis)
        
        for huis in wijk.losse_huizen[:]:
            for batterij in wijk.batterijen:
                if huis.kan_aansluiten(batterij):
                    wijk.leg_route(batterij, huis)
                    counter += 1
                    #break
        print(f"losse huizen: {len(wijk.losse_huizen)}")
        print(f"dichtstbijzijnde batterij: {huis.dichtstbijzijnde_batterij()}")


    # # Geshuffelde nested lijst
    # geshuffelde_afstanden = wijk.shuffle_afstanden()

    # print(geshuffelde_afstanden)
    # for inner_lijst in geshuffelde_afstanden:
    #     for tuple in inner_lijst:
    #         batterij, huis, afstand = tuple
    #         if huis.kan_aansluiten(batterij):
    #             #print("kan aansluiten")
    #             wijk.leg_route(batterij, huis)
#                 counter += 1


    # #Teruggaan en herverdelen
    # while len(wijk.losse_huizen) > 0:
    #     for inner_lijst in geshuffelde_afstanden:
    #         huis = random.choice()
    #         for tuple in inner_lijst:
    #             batterij, huis, afstand = tuple
    #             wijk.ontkoppel_huis(huis)
    #             if huis.kan_aansluiten(batterij):
    #                 wijk.leg_route(batterij, huis)
    #                 counter += 1



    # Info
    for batterij in wijk.batterijen:
        print(batterij.resterende_capaciteit)

    print(counter)
    return wijk

