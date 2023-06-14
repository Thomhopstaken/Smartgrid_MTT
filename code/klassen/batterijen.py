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
        self.gelegde_kabels = []

    # def delink_output(self, huis):
    #     self.resterende_capaciteit -= huis.maxoutput
    #     nieuwe_lijst = set(self.gelinkte_huizen) - set(huis)
    #     self.gelinkte_huizen = list(nieuwe_lijst)

    def bereken_afstand(self, huizen) -> None:
        """Berekent afstand van batterijen tot huizen."""

        # itereer over ongekoppelde huizen, voeg deze toe aan dictionary en geef afstand tot batterij als waarde mee
        for huis in huizen:
            afstand = abs(huis.x_as - self.x_as) + abs(huis.y_as - self.y_as)
            self.afstand_huizen[huis.huis_id] = afstand
            self.afstand_huizen = dict(sorted(self.afstand_huizen.items(), key=lambda item:item[1]))
            print(f"AFSTAND HUIZEN: {self.afstand_huizen}")
     

    def dichtstbijzijnde_huis(self) -> int:
        """Neemt het dichtstbijzijnde huis vanaf een batterij."""

        afstand = self.afstand_huizen
        return min(afstand, key=afstand.get)
    
    def update_verbruik(self, output) -> None:
        """Update de resterende capaciteit van de batterij na het aansluiten van een huis."""

        self.resterende_capaciteit -= output

    def kabel_toevoegen(self, kabel):
        self.gelegde_kabels.append(kabel)
        
    def overbodige_kabels_verwijderen(self):
        huis_kabels = set()
        for huis in self.gelinkte_huizen:
            for kabel in huis.kabels:
                huis_kabels.add(kabel)
        overbodige_kabels = [kabel for kabel in self.gelegde_kabels if kabel not in huis_kabels]
        self.gelegde_kabels = [kabel for kabel in self.gelegde_kabels if kabel not in overbodige_kabels]
                