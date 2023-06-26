import copy
import random
import copy
from .kmeans import gebruik_clusters

def greedy_alg(wijk) -> None:
    """Greedy algoritme om huizen aan te sluiten op batterijen in een wijk."""
    wijk_buffer = copy.deepcopy(wijk)
    gebruik_clusters(wijk_buffer, 5)
    counter = 0

    # # Bereken afstand
    # afstanden = wijk_buffer.bereken_afstand()

    # # Leg route wanneer mogelijk
    # for batterij, huis, _ in afstanden:
    #     if huis.kan_aansluiten(batterij):
    #         wijk_buffer.leg_route(batterij, huis)
    #         counter += 1

    # # Teruggaan en herverdelen
    # while len(wijk_buffer.losse_huizen) > 0:
    #     #print(len(wijk_buffer.losse_huizen))
    #     willekeurige_batterij = random.choice(wijk_buffer.batterijen)
    #     willekeurig_huis = random.choice(willekeurige_batterij.gelinkte_huizen)
    #     willekeurige_batterij.ontkoppel_huis(willekeurig_huis, wijk_buffer)
    #     willekeurig_huis.verwijder_kabels()
    #     #print("ontkoppeld")
        
    #     # Leg route wanneer mogelijk
    #     for huis in wijk.losse_huizen:
    #         for batterij in wijk.batterijen:
    #             if huis.kan_aansluiten(batterij):
    #                 wijk.leg_route(batterij, huis)
    #                 print("route")

    #                 counter += 1
    # print(f"losse huizen: {len(wijk.losse_huizen)}")
    # print(f"dichtstbijzijnde batterij: {huis.dichtstbijzijnde_batterij()}")


    #Geshuffelde nested lijst
    geshuffelde_afstanden = wijk_buffer.shuffle_afstanden()

    #print(geshuffelde_afstanden)
    for inner_lijst in geshuffelde_afstanden:
        for batterij, huis, _ in inner_lijst:
            if huis.kan_aansluiten(batterij):
                wijk_buffer.leg_route(batterij, huis)
                counter += 1

    # Teruggaan en herverdelen
    while len(wijk_buffer.losse_huizen) > 0:
        willekeurige_batterij = random.choice(wijk_buffer.batterijen)
        willekeurig_huis = random.choice(willekeurige_batterij.gelinkte_huizen)
        willekeurige_batterij.ontkoppel_huis(willekeurig_huis, wijk_buffer)
        willekeurig_huis.verwijder_kabels()
        for inner_lijst in geshuffelde_afstanden:
            for batterij, huis, _ in inner_lijst:
                if huis.kan_aansluiten(batterij):
                    wijk_buffer.leg_route(batterij, huis)
                    counter += 1

    # for batterij in wijk_buffer.batterijen:
    #     print(batterij.resterende_capaciteit)

    #print(counter)
    return wijk_buffer

