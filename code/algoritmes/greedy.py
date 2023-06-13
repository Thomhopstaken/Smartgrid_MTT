def greedy_alg(wijk) -> None:
    """Greedy algoritme om huizen aan te sluiten op batterijen in een wijk."""
    counter = 0
    stop_counter = 0
    while len(wijk.losse_huizen) > 0:
        for huis in wijk.losse_huizen:
            for batterij in huis.afstand_batterijen:
                if huis.kan_huis_aansluiten_op_batterij(batterij):
                    batterij.update_verbruik(huis.maxoutput)
                    wijk.link_huis(huis.huis_id)
                    wijk.leg_kabel_route(batterij, huis)
                
                else:
                    stop_counter += 1
                    print(f'{counter}: error on house {huis.huis_id}')
                    print(f'capaciteit batterij: {batterij.batterij_id}: {batterij.resterende_capaciteit}')
                    print(f'stop counter: {stop_counter}')
                    if counter >= 148 and stop_counter == 5:
                        return False

            if stop_counter == 5:
                #print('run failed!')
                return False

                    
                    