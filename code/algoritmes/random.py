import random

def random_alg(wijk) -> None:
    """Willekeurig algoritme om huizen aan te sluiten op batterijen in een wijk."""

    counter = 0
    while len(wijk.losse_huizen) > 0:
        for batterij in wijk.batterijen:
            for huis in wijk.losse_huizen:
                if huis.kan_huis_aansluiten_op_batterij(batterij):
                    counter += 1
                    wijk.link_huis(huis.huis_id)
                    wijk.leg_kabel_route(batterij, huis)
                    print(f"{counter}: yes")
                else:
                    print(f'{counter}: error on house {huis.huis_id}')
                    #print(f'cordinates; {huis.x_as}|{huis.y_as}')
                    #print(f'output: {huis.maxoutput}')
                    print(f'capaciteit batterij: {batterij.batterij_id}: {batterij.resterende_capaciteit}')
                    