class Batterijen:

    def __init__(self, i, x, y, capaciteit) -> None:
        """Neemt gegevens van batterijen uit district en slaat het op in batterij object."""
        self.batterij_id = i
        self.x_as = x
        self.y_as = y
        self.capaciteit = capaciteit
        self.gebruik = 0
        self.gelinkte_huizen = []
        self.afstand_huizen = []
        
        #to do: lijst van dicts maken met huis_id: huis object en afstand: afstande. 
    
    def afstand_berekenen(self, huizen) -> None:
        """Berekent afstand van batterijen tot huizen."""
        # itereer over ongekoppelde huizen, voeg deze toe aan dictionary en geef afstand tot batterij als waarde mee
        for huis in huizen:
            afstand = abs(huis.x_as - self.x_as) + abs(huis.y_as - self.y_as)
            self.afstand_huizen.append({'huis': huis.huis_id, 'afstand': afstand})
        self.afstand_huizen.sort(key=lambda x: x['afstand'], reverse=True)


    def closest_house(self):
        distance = self.afstand_huizen
        return min(distance, key=distance.get)

    def update_usage(self, output):
        self.resterende_capaciteit -= output
