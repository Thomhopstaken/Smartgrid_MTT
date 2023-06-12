import random

def random_alg(wijk) -> None:
    """Willekeurig algoritme om huizen aan te sluiten op batterijen in een wijk."""

    counter = 0
    stop_counter = 0
    while len(wijk.losse_huizen) > 0:
        for batterij in wijk.batterijen:
            for huis in wijk.losse_huizen:
                if huis.kan_huis_aansluiten_op_batterij(batterij):
                    counter += 1
                    wijk.link_huis(huis.huis_id)
                    wijk.leg_kabel_route(batterij, huis)
                    #print(f"{counter}: yes")
                else:
                    if counter == 149 and batterij.resterende_capaciteit < huis.maxoutput:
                        stop_counter += 1
                    #print(f'{counter}: error on house {huis.huis_id}')
                    #print(f'capaciteit batterij: {batterij.batterij_id}: {batterij.resterende_capaciteit}')
        if stop_counter == 5:
            print('run failed!')
            return False
    print('Run Succesvol!')    
    return True