import copy
from .kmeans import gebruik_clusters
import random


def greedy_alg(wijk) -> object:
    """Greedy algoritme om huizen aan te sluiten op batterijen in een wijk."""
    wijk_buffer = copy.deepcopy(wijk)
    gebruik_clusters(wijk_buffer, 5)
    counter = 0

    # Geshuffelde nested lijst
    geshuffelde_afstanden = wijk_buffer.shuffle_afstanden()

    # Print(geshuffelde_afstanden)
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
    return wijk_buffer
