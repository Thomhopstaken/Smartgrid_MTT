def kan_huizen_verwisselen(afstand_huis_x_bat_x, afstand_huis_x_bat_y, afstand_huis_y_bat_x, 
                           afstand_huis_y_bat_y, huis_x, huis_y, batterij_x, batterij_y):
    if afstand_huis_x_bat_x > afstand_huis_y_bat_x and afstand_huis_y_bat_y > afstand_huis_x_bat_y:
        nieuwe_cap_bat_x = batterij_x.resterende_capaciteit + huis_x.maxoutput
        nieuwe_cap_bat_y = batterij_y.resterende_capaciteit + huis_y.maxoutput
        if nieuwe_cap_bat_x - huis_y.maxoutput >= 0 and nieuwe_cap_bat_y - huis_x.maxoutput >= 0:
            return True
        else: return False
    else:
        return False

def hill_climbing_alg(wijk) -> None:
    counter = 1
    while counter != 0:
        counter = 0
        for i in range(len(wijk.batterijen)): 
            batterij_x = wijk.batterijen[i]
            for x in range(len(wijk.batterijen)):
                if i != x:
                    batterij_y = wijk.batterijen[x]
                else:
                    continue 
                for j in range(len(batterij_x.gelinkte_huizen)):
                    huis_x = wijk.batterijen[i].gelinkte_huizen[j]
                    for y in range(len(batterij_y.gelinkte_huizen)):
                        huis_y = wijk.batterijen[x].gelinkte_huizen[y]
                        afstand_huis_x_bat_x = huis_x.afstand_batterijen[batterij_x]
                        afstand_huis_x_bat_y = huis_x.afstand_batterijen[batterij_y]
                        afstand_huis_y_bat_x = huis_y.afstand_batterijen[batterij_x]
                        afstand_huis_y_bat_y = huis_y.afstand_batterijen[batterij_y]
                        if kan_huizen_verwisselen(afstand_huis_x_bat_x, afstand_huis_x_bat_y, afstand_huis_y_bat_x, afstand_huis_y_bat_y, huis_x, huis_y, batterij_x, batterij_y):
                            huis_x.verwijder_kabels()
                            huis_y.verwijder_kabels()
                            wijk.leg_kabel_route(batterij_x, huis_y)    
                            wijk.leg_kabel_route(batterij_y, huis_x)
                            counter += 1                   
    for batterij in wijk.batterijen:
        batterij.overbodige_kabels_verwijderen()
                    
                
        
    
    
    
    

        


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