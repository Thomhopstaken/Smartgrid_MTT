
def greedy_alg(wijk) -> None:
    print("greedy")
    """Greedy algoritme om huizen aan te sluiten op batterijen in een wijk."""
    counter = 0
    stop_counter = 0

    # for batterij in wijk.batterijen:
    #     afstanden = batterij.bereken_afstand(wijk.losse_huizen)
    # print(afstanden)
    
    afstanden = wijk.bereken_afstand()
    #print(afstanden)

    #while len(wijk.losse_huizen): 
    # Combinatie: batterij, huis, afstand
    for combinatie in afstanden:
        batterij, huis, afstand = combinatie
        print(batterij, huis, afstand)
        if huis.kan_aansluiten(batterij):
            print("kan aansluiten")
            counter += 1
            wijk.leg_route(batterij, huis)

    if len(wijk.losse_huizen) != 0:
        #print(f"OUTPUT: {wijk.losse_huizen[0].maxoutput}")
        batterij_met_max_capaciteit = max(wijk.batterijen, key=lambda x: x.resterende_capaciteit)
        resterende_huis = wijk.losse_huizen[0]
        #print(f'MAX BATTERIJ: {batterij_met_max_capaciteit.resterende_capaciteit}')
        for combinatie in afstanden:
            batterij, huis, afstand = combinatie
            if resterende_huis.kan_aansluiten(batterij):
                wijk.leg_route(batterij_met_max_capaciteit, huis)
                counter += 1
            
    print(counter)

    for batterij in wijk.batterijen:
        print(batterij.resterende_capaciteit)

    #         #print(huis)
    #         if huis.kan_aansluiten(batterij):
    #             print("kan aansluiten")
    #             wijk.leg_route(batterij, huis)
    #             counter += 1
    #             stop_counter = 0
    #         else:
    #             print("kan niet aansluiten")
    #             stop_counter += 1
    #             if counter >= 148 and stop_counter == 5:
    #                 return False
    #     if stop_counter == 5:
    #         print('run failed!')
    #         return False
    # print('Run Succesvol!')
    # return True
                
