import random

def random_alg(wijk) -> bool:
    """Willekeurig algoritme om huizen aan te sluiten op batterijen in een wijk."""
    random.shuffle(wijk.losse_huizen)
    counter = 0
    stop_counter = 0
    while len(wijk.losse_huizen) > 0:
        for batterij in wijk.batterijen:
            for huis in wijk.losse_huizen:
                if huis.kan_huis_aansluiten_op_batterij(batterij):
                    counter += 1
                    stop_counter = 0
                    wijk.link_huis(huis.huis_id)
                    wijk.leg_kabel_route(batterij, huis)
                    #print(f"{counter}: yes")
                else:
                    stop_counter += 1
                    #print(f'{counter}: error on house {huis.huis_id}')
                    #print(f'capaciteit batterij: {batterij.batterij_id}: {batterij.resterende_capaciteit}')
                    #print(f'stop counter: {stop_counter}')
                    if counter >= 148 and stop_counter == 5:
                        return False

            if stop_counter == 5:
                #print('run failed!')
                return False
    #print('Run Succesvol!')
    return True
'''
                else:
                    if counter == 149 and batterij.resterende_capaciteit < huis.maxoutput:
                    #     stop_counter += 1
                        print(f'{counter}: error on house {huis.huis_id}')
                    #print(f'cordinates; {huis.x_as}|{huis.y_as}')
                    #print(f'output: {huis.maxoutput}')
                        print(f'capaciteit batterij: {batterij.batterij_id}: {batterij.resterende_capaciteit}')
                        try:
                            random_huis = random.choice(wijk.gelinkte_huizen)
                            wijk.delink_huis(random_huis.huis_id)
                            random_huis.verwijder_kabels()
                            batterij.delink_output(random_huis)
                            counter = 148
                            print("Delinked: ", random_huis.huis_id)
                        except IndexError:
                            print("Index Error")

        if stop_counter == 5:
            print('run failed!')

'''