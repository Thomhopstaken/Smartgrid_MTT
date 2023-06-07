class Batterijen:

    def __init__(self, x, y, capaciteit) -> None:
        """Neemt gegevens van batterijen uit district en slaat het op in batterij object."""
        self.x_as = x
        self.y_as = y
        self.capaciteit = capaciteit
        self.huidig_gebruik = 0
        self.gelinkte_huizen = []
        self.afstand_huizen = {}
    
    def afstand_berekenen(self, huizen) -> None:
        """Berekent afstand van batterijen tot huizen."""
        # itereer over ongekoppelde huizen, voeg deze toe aan dictionary en geef afstand tot batterij als waarde mee
        for huis in huizen:
            afstand = abs((huis.x_as + huis.y_as) - (self.x_as + self.y_as))
            self.afstand_huizen[huis] = afstand
            self.afstand_huizen = dict(sorted(self.afstand_huizen.items(), key=lambda x: x[1]))
            print(f"afstand huizen: {self.afstand_huizen}")
