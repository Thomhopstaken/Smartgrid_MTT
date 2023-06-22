import copy
import random

def random_alg(wijk):
    """Willekeurig algoritme om huizen aan te sluiten op batterijen in een wijk."""
    random.shuffle(wijk.batterijen)
    random.shuffle(wijk.losse_huizen)
    wijk_buffer = copy.deepcopy(wijk)
    while len(wijk_buffer.losse_huizen) > 0:
        loop_start = len(wijk_buffer.losse_huizen)
        for batterij in wijk_buffer.batterijen:
            for huis in wijk_buffer.losse_huizen:
                if huis.kan_aansluiten(batterij):
                    wijk_buffer.leg_route(batterij, huis)

        loop_einde = len(wijk_buffer.losse_huizen)
        if loop_start == loop_einde:
            return random_alg(wijk)
    return wijk_buffer