class Batterijen:

    def __init__(self, i, x, y, capaciteit) -> None:
        """Neemt gegevens van batterijen uit district en slaat het op in batterij object."""
        self.batterij_id = i
        self.x_as = x
        self.y_as = y
        self.capaciteit = capaciteit
        self.resterende_capaciteit = capaciteit
        self.gelinkte_huizen = []
        self.afstand_huizen = {}
    
    def afstand_berekenen(self, huizen) -> None:
        """Berekent afstand van batterijen tot huizen."""
        # itereer over ongekoppelde huizen, voeg deze toe aan dictionary en geef afstand tot batterij als waarde mee
        for huis in huizen:
            afstand = abs(huis.x_as - self.x_as) + abs(huis.y_as - self.y_as)
            self.afstand_huizen[huis] = afstand
            self.afstand_huizen = dict(sorted(self.afstand_huizen.items(), key=lambda x: x[1]))
            # print(f"afstand huizen: {self.afstand_huizen}")

    def closest_house(self):
        distance = self.afstand_huizen
        return min(distance, key=distance.get)

    def update_usage(self, output):
        self.resterende_capaciteit -= output
