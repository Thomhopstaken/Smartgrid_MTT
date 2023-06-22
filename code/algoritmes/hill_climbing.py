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
        
        while self.counter < 100:
            nieuwe_wijk = copy.deepcopy(self.oude_wijk)
            nieuwe_wijk.hc_verwissel_huizen()
        
        print(self.kosten)    
        
            # self.check_uitkomst(nieuwe_wijk)
            # if self.counter == 100:
            #     print(self.kosten)
            #     nieuwe_wijk = copy.deepcopy(self.oude_wijk)
            #     nieuwe_wijk.hc_verwissel_alle_huizen()
            #     self.counter = 0
            #     print(self.kosten)
