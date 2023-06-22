import copy
import random

class Hill_climber:
    
    def __init__(self, wijk) -> None:
        
        self.oude_wijk = copy.deepcopy(wijk)
        self.kosten = wijk.kosten_berekening()
        
        self.counter = 0
        self.aanpassingen = 0
                
    def check_uitkomst(self, nieuwe_wijk):
        
        nieuwe_kosten = nieuwe_wijk.kosten_berekening()
        oude_kosten = self.kosten
        
        if nieuwe_kosten < oude_kosten:
            self.oude_wijk = nieuwe_wijk
            self.kosten = nieuwe_kosten
            self.counter = 0
            self.aanpassingen += 1
        else: 
            self.counter += 1
            
    
    def draai_hillclimber(self):
        
        while self.counter <= 1000:
            nieuwe_wijk = copy.deepcopy(self.oude_wijk)
            nieuwe_wijk.hc_verwissel_huizen()
            
            self.check_uitkomst(nieuwe_wijk)
            

# def vind_batterij_y(huis_x, batterij_x):
#     """zoekt de batterij die het dichtste bij huis_x ligt"""
#     kortste_afstand = huis_x.afstand_batterijen[batterij_x]
#     batterij_y = batterij_x
#     for batterij, afstand in huis_x.afstand_batterijen.items():
#         if afstand < kortste_afstand:
#             batterij_y = batterij
#     return batterij_y

# def kan_wisselen(huis_x, batterij_x, batterij_y):
#     """checkt of er een huis gevonden kan worden dat verder ligt van batterij_y.
#         zo ja, checkt of de nieuwe capaciteit staat kan bestaan"""
#     huis_y_gevonden = vind_huis_y(huis_x, batterij_y)
#     if huis_y_gevonden[0]:
#         huis_y = huis_y_gevonden[1]
#         if check_capaciteit(huis_x, huis_y, batterij_x, batterij_y):
#             return True, huis_y
#         else:
#             return False, huis_y
#     else:
#         return False, huis_y_gevonden[1]

# def vind_huis_y(huis_x, batterij_y):
#     """zoekt bij batterij_y een huis dat verder ligt dan huis_x"""
#     afstand_huis_x = huis_x.afstand_batterijen[batterij_y]
#     huis_y = None
#     for huis in batterij_y.gelinkte_huizen:
#         afstand = huis.afstand_batterijen[batterij_y]
#         if afstand > afstand_huis_x:
#             huis_y = huis
#             return True, huis_y
#     else:
#         return False, huis_y





# def hill_climbing_alg(wijk) -> None:
#     teller = 0
#     counter = 1
#     while counter != 0:
#         counter = 0
#         teller += 1
#         for i in range(len(wijk.batterijen)): 
#             batterij_x = wijk.batterijen[i]
#             for huis_x in batterij_x.gelinkte_huizen:
#                 batterij_y = vind_batterij_y(huis_x, batterij_x)
#                 if batterij_y == batterij_x:
#                     continue
#                 else:
#                     wissel = kan_wisselen(huis_x, batterij_x, batterij_y)
#                     if not wissel[0]:
#                         continue
#                     else:
#                         kabels_verleggen(wijk, huis_x, wissel[1], batterij_x, batterij_y)
#                         counter += 1
#         print(counter)
#             #                 counter += 1                   
      
                
        
    
    
    
    
