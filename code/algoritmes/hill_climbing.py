# def kan_huizen_verwisselen_1(afstand_huis_x_bat_x, afstand_huis_x_bat_y, afstand_huis_y_bat_x, 
#                            afstand_huis_y_bat_y, huis_x, huis_y, batterij_x, batterij_y):
#     if afstand_huis_x_bat_x > afstand_huis_y_bat_xand afstand_huis_y_bat_y > afstand_huis_x_bat_y:
#         nieuwe_cap_bat_x = batterij_x.resterende_capaciteit + huis_x.maxoutput
#         nieuwe_cap_bat_y = batterij_y.resterende_capaciteit + huis_y.maxoutput
#         if nieuwe_cap_bat_x - huis_y.maxoutput >= 0 and nieuwe_cap_bat_y - huis_x.maxoutput >= 0:
#             return True
#         else: return False
#     else:
#         return False

# def kan_huizen_verwisselen_2(afstand_huis_x_bat_x, afstand_huis_x_bat_y, afstand_huis_y_bat_x, 
#                            afstand_huis_y_bat_y, huis_x, huis_y, batterij_x, batterij_y):
#     if afstand_huis_x_bat_x > afstand_huis_y_bat_x and afstand_huis_y_bat_y > afstand_huis_x_bat_y:
#         nieuwe_cap_bat_x = batterij_x.resterende_capaciteit + huis_x.maxoutput
#         nieuwe_cap_bat_y = batterij_y.resterende_capaciteit + huis_y.maxoutput
#         if nieuwe_cap_bat_x - huis_y.maxoutput >= 0 and nieuwe_cap_bat_y - huis_x.maxoutput >= 0:
#             return True
#         else: return False
#     else:
#         return False

def vind_batterij_y(huis_x, batterij_x):
    """zoekt de batterij die het dichtste bij huis_x ligt"""
    kortste_afstand = huis_x.afstand_batterijen[batterij_x]
    batterij_y = batterij_x
    for batterij, afstand in huis_x.afstand_batterijen.items():
        if afstand < kortste_afstand:
            batterij_y = batterij
    return batterij_y

def kan_wisselen(huis_x, batterij_x, batterij_y):
    """checkt of er een huis gevonden kan worden dat verder ligt van batterij_y.
        zo ja, checkt of de nieuwe capaciteit staat kan bestaan"""
    huis_y_gevonden = vind_huis_y(huis_x, batterij_y)
    if huis_y_gevonden[0]:
        huis_y = huis_y_gevonden[1]
        if check_capaciteit(huis_x, huis_y, batterij_x, batterij_y):
            return True, huis_y
        else:
            return False, huis_y
    else:
        return False, huis_y_gevonden[1]

def vind_huis_y(huis_x, batterij_y):
    """zoekt bij batterij_y een huis dat verder ligt dan huis_x"""
    afstand_huis_x = huis_x.afstand_batterijen[batterij_y]
    huis_y = None
    for huis in batterij_y.gelinkte_huizen:
        afstand = huis.afstand_batterijen[batterij_y]
        if afstand > afstand_huis_x:
            huis_y = huis
            return True, huis_y
    else:
        return False, huis_y

def check_capaciteit(huis_x, huis_y, batterij_x, batterij_y):
    """checkt of wissel huis_x en huis_y haalbaar is ivm capaciteit. """
    nieuwe_cap_bat_x = batterij_x.resterende_capaciteit + huis_x.maxoutput
    nieuwe_cap_bat_y = batterij_y.resterende_capaciteit + huis_y.maxoutput
    if nieuwe_cap_bat_x - huis_y.maxoutput >= 0 and nieuwe_cap_bat_y - huis_x.maxoutput >= 0:
        return True
    else: 
        return False

def kabels_verleggen(wijk, huis_x, huis_y, batterij_x, batterij_y):
    """legt kabels tussen huis_x en batterij_y en huis_y en batterij_x"""
    huis_x.verwijder_kabels()
    huis_y.verwijder_kabels()
    wijk.leg_route(batterij_x, huis_y)    
    wijk.leg_route(batterij_y, huis_x)
    
    index_x = batterij_x.gelinkte_huizen.index(huis_x)
    index_y = batterij_y.gelinkte_huizen.index(huis_y)
    batterij_x.gelinkte_huizen.append(batterij_y.gelinkte_huizen.pop(index_y))
    batterij_y.gelinkte_huizen.append(batterij_x.gelinkte_huizen.pop(index_x))



def hill_climbing_alg(wijk) -> None:
    teller = 0
    counter = 1
    while counter != 0:
        counter = 0
        teller += 1
        for i in range(len(wijk.batterijen)): 
            batterij_x = wijk.batterijen[i]
            for huis_x in batterij_x.gelinkte_huizen:
                batterij_y = vind_batterij_y(huis_x, batterij_x)
                if batterij_y == batterij_x:
                    continue
                else:
                    wissel = kan_wisselen(huis_x, batterij_x, batterij_y)
                    if not wissel[0]:
                        continue
                    else:
                        kabels_verleggen(wijk, huis_x, wissel[1], batterij_x, batterij_y)
                        counter += 1
        print(counter)
            # for x in range(len(wijk.batterijen)):
            #     if i != x:
            #         batterij_y = wijk.batterijen[x]
            #     else:
            #         continue 
            #     for j in range(len(batterij_x.gelinkte_huizen)):
            #         huis_x = wijk.batterijen[i].gelinkte_huizen[j]
            #         for y in range(len(batterij_y.gelinkte_huizen)):
            #             huis_y = wijk.batterijen[x].gelinkte_huizen[y]
            #             afstand_huis_x_bat_x = huis_x.afstand_batterijen[batterij_x]
            #             afstand_huis_x_bat_y = huis_x.afstand_batterijen[batterij_y]
            #             afstand_huis_y_bat_x = huis_y.afstand_batterijen[batterij_x]
            #             afstand_huis_y_bat_y = huis_y.afstand_batterijen[batterij_y]
            #             if kan_huizen_verwisselen_1(afstand_huis_x_bat_x, afstand_huis_x_bat_y, afstand_huis_y_bat_x, 
            #                                       afstand_huis_y_bat_y, huis_x, huis_y, batterij_x, batterij_y):
            #                 huis_x.verwijder_kabels()
            #                 huis_y.verwijder_kabels()
            #                 wijk.leg_kabel_route(batterij_x, huis_y)    
            #                 wijk.leg_kabel_route(batterij_y, huis_x)
            #                 counter += 1                   
    for batterij in wijk.batterijen:
        batterij.overbodige_kabels_verwijderen()
        #print(f'{batterij.batterij_id} : {batterij.gelegde_kabels}')
    print(teller)             
                
# idee:

""" run een random algoritme totdat het een succesvolle run geeft. 
    verwissel vervolgens huizen tussen batterijen om kost efficienter te maken. 
    potentiele wisselstaten: 
        - verwissel huis 1 van batterij 1 met huis 2 van batterij 2 
        als beide huizen efficienter zijn bij andere batterij. 
        - verwissel huis 1 van batterij 1 met huis 2 van batterij 2 
        als huis 1 efficienter is bij batterij 2.
    potientele eind staten:
        - runnen totdat elk huis niet meer efficient verplaatst kan worden. 
        - runnen totdat elk huis 1 keer verplaatst is. """