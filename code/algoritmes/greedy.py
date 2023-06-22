import random

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
    lijst_lijsten = []
        
    for i in range(0, len(afstanden), 10):
        sublijst = afstanden[i:i+10]
        random.shuffle(sublijst)
        lijst_lijsten.append(sublijst)
        #print(len(lijst_lijsten))
    #print(lijst_lijsten)

    while len(wijk.losse_huizen): 
        for inner_lijst in lijst_lijsten:
            for tuple in inner_lijst:
                batterij, huis, afstand = tuple
                if huis.kan_aansluiten(batterij):
                    print("kan aansluiten")
                    counter += 1
                    wijk.leg_route(batterij, huis)
        print(counter)

    # if len(wijk.losse_huizen) != 0:
    #     #print(f"OUTPUT: {wijk.losse_huizen[0].maxoutput}")
    #     batterij_maxcap = max(wijk.batterijen, key=lambda x: x.resterende_capaciteit)
    #     resterende_huis = wijk.losse_huizen[0]
    #     #print(f'MAX BATTERIJ: {batterij_met_max_capaciteit.resterende_capaciteit}')
    #     verschil = abs(batterij_maxcap.resterende_capaciteit - resterende_huis.maxoutput)
    #     print(f"verschil: {verschil}")
    #     print(f"resterende capaciteit: {batterij_maxcap.resterende_capaciteit}")
        
    #     te_ontkoppelen_huis = None
    #     for combinatie in afstanden:
    #         print(combinatie)
    #         batterij, huis, afstand = combinatie
    #         print(f"HUIS {huis}")
    #         if huis.maxoutput >= verschil and huis.maxoutput <= batterij_maxcap.resterende_capaciteit:
    #             te_ontkoppelen_huis = huis
    #     print(f"ontkoppel huis: {te_ontkoppelen_huis}")
    #     wijk.ontkoppel_huis(te_ontkoppelen_huis)
        
    #     if resterende_huis.kan_aansluiten(batterij):
    #         wijk.leg_route(batterij_maxcap, huis)
    #         counter += 1
            
    #print(counter)

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
                
