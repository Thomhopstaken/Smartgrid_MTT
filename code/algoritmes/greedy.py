
def greedy_alg(wijk) -> None:
    """Greedy algoritme om huizen aan te sluiten op batterijen in een wijk."""
    counter = 0
    stop_counter = 0

    #while len(wijk.losse_huizen) > 0:
    for batterij in wijk.batterijen:
        for huis in batterij.afstand_huizen:
            print(f"HUIS: {huis}")

            if huis.kan_huis_aansluiten_op_batterij(batterij):
                wijk.leg_kabel_route(batterij, huis)
                print(counter)
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

                    
