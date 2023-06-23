import random
import copy

def greedy_alg(wijk) -> None:

    wijk_kopie = copy.deepcopy(wijk)

    # print("greedy")
    """Greedy algoritme om huizen aan te sluiten op batterijen in een wijk."""
    counter = 0
    
    # Bereken afstand
    afstanden = wijk_kopie.bereken_afstand()

    for batterij, huis, _ in afstanden:
        if huis.kan_aansluiten(batterij):
            wijk_kopie.leg_route(batterij, huis)
            counter += 1

    # Teruggaan en herverdelen
    while len(wijk_kopie.losse_huizen) > 0:
        #print(len(wijk_kopie.losse_huizen))
        willekeurige_batterij = random.choice(wijk_kopie.batterijen)
        willekeurig_huis = random.choice(willekeurige_batterij.gelinkte_huizen)
        willekeurige_batterij.ontkoppel_huis(willekeurig_huis, wijk_kopie)
        #print("ontkoppeld")
        
        # Leg route wanneer mogelijk
        for huis in wijk_kopie.losse_huizen[:]:
            for batterij in wijk_kopie.batterijen:
                if huis.kan_aansluiten(batterij):
                    wijk_kopie.leg_route(batterij, huis)
                    counter += 1
        # print(f"losse huizen: {len(wijk_kopie.losse_huizen)}")
        # print(f"dichtstbijzijnde batterij: {huis.dichtstbijzijnde_batterij()}")


    # # Geshuffelde nested lijst
    # geshuffelde_afstanden = wijk_kopie.shuffle_afstanden()

    # print(geshuffelde_afstanden)
    # for inner_lijst in geshuffelde_afstanden:
    #     for tuple in inner_lijst:
    #         batterij, huis, afstand = tuple
    #         if huis.kan_aansluiten(batterij):
    #             #print("kan aansluiten")
    #             wijk_kopie.leg_route(batterij, huis)
    #              counter += 1


    # #Teruggaan en herverdelen
    # while len(wijk_kopie.losse_huizen) > 0:
    #     for inner_lijst in geshuffelde_afstanden:
    #         huis = random.choice()
    #         for tuple in inner_lijst:
    #             batterij, huis, afstand = tuple
    #             wijk_kopie.ontkoppel_huis(huis)
    #             if huis.kan_aansluiten(batterij):
    #                 wijk_kopie.leg_route(batterij, huis)
    #                 counter += 1


    # for batterij in wijk_kopie.batterijen:
        # print(batterij.resterende_capaciteit)

    # print(counter)
    return wijk_kopie

