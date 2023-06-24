import random

def greedy_alg(wijk) -> None:
    """Greedy algoritme om huizen aan te sluiten op batterijen in een wijk."""
    counter = 0

    # Bereken afstand
    afstanden = wijk.bereken_afstand()

    # Leg route wanneer mogelijk
    for batterij, huis, _ in afstanden:
        if huis.kan_aansluiten(batterij):
            wijk.leg_route(batterij, huis)
            counter += 1

    # Teruggaan en herverdelen
    while len(wijk.losse_huizen) > 0:
        #print(len(wijk.losse_huizen))
        willekeurige_batterij = random.choice(wijk.batterijen)
        willekeurig_huis = random.choice(willekeurige_batterij.gelinkte_huizen)
        willekeurige_batterij.ontkoppel_huis(willekeurig_huis, wijk)
        willekeurig_huis.verwijder_kabels()
        #print("ontkoppeld")
        
        # Leg route wanneer mogelijk
        for huis in wijk.losse_huizen:
            for batterij in wijk.batterijen:
                if huis.kan_aansluiten(batterij):
                    wijk.leg_route(batterij, huis)
                    print("route")

                    counter += 1
    print(f"losse huizen: {len(wijk.losse_huizen)}")
    print(f"dichtstbijzijnde batterij: {huis.dichtstbijzijnde_batterij()}")


    # # Geshuffelde nested lijst
    # geshuffelde_afstanden = wijk.shuffle_afstanden()

    # #print(geshuffelde_afstanden)
    # for inner_lijst in geshuffelde_afstanden:
    #         batterij, huis, _ = tuple
    #         if huis.kan_aansluiten(batterij):
    #             wijk.leg_route(batterij, huis)
    #             counter += 1

    # # Teruggaan en herverdelen
    # while len(wijk.losse_huizen) > 0:
    #     willekeurige_batterij = random.choice(wijk.batterijen)
    #     willekeurig_huis = random.choice(willekeurige_batterij.gelinkte_huizen)
    #     willekeurige_batterij.ontkoppel_huis(willekeurig_huis, wijk)
    #     willekeurig_huis.verwijder_kabel()
    #     for inner_lijst in geshuffelde_afstanden:
    #         for batterij, huis, _ in inner_lijst:
    #             wijk.ontkoppel_huis(huis)
    #             if huis.kan_aansluiten(batterij):
    #                 wijk.leg_route(batterij, huis)
    #                 counter += 1

    for batterij in wijk.batterijen:
        print(batterij.resterende_capaciteit)

    print(counter)
    return wijk

