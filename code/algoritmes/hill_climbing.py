import copy

class Hill_climber:
    
    def __init__(self, wijk) -> None:
        
        self.oude_wijk = copy.deepcopy(wijk)
        self.kosten = wijk.kosten_berekening()
        self.nieuwe_wijk = copy.deepcopy(wijk)
        
        self.counter = 0
        self.aanpassingen = 0
                
    def check_uitkomst(self):
        
        nieuwe_kosten = self.nieuwe_wijk.kosten_berekening()
        oude_kosten = self.kosten
        
        if nieuwe_kosten < oude_kosten:
            self.oude_wijk = self.nieuwe_wijk
            self.kosten = nieuwe_kosten
            self.counter = 0
            self.aanpassingen += 1
            self.nieuwe_wijk = copy.deepcopy(self.oude_wijk)
        else: 
            self.counter += 1
            
    
    def draai_hillclimber(self):
        
        while self.counter < 100:
            if self.nieuwe_wijk.hillclimber_wissel():
                self.check_uitkomst()
            else:
                continue
            
        print(self.kosten)
        