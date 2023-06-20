
def greedy_alg(wijk) -> None:
    # print("greedy")
    """Greedy algoritme om huizen aan te sluiten op batterijen in een wijk."""
    counter = 0
    stop_counter = 0

    # for batterij in wijk.batterijen:
    #     afstanden = batterij.bereken_afstand(wijk.losse_huizen)
    # print(afstanden)
    
    afstanden = wijk.bereken_afstand()
    print(afstanden)

    #while wijk.losse_huizen:
    #print(len(wijk.losse_huizen))
    for combinatie in afstanden:
        print(combinatie[1])
        if combinatie[1].kan_aansluiten(combinatie[0]):
            print("kan aansluiten")
            counter += 1
        
            wijk.leg_route(combinatie[0], combinatie[1])
    #print(f"OUTPUT: {wijk.losse_huizen[0].maxoutput}")
    return wijk
    # print(counter)

    # for batterij in wijk.batterijen:
    #     print(batterij.resterende_capaciteit)

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
                
