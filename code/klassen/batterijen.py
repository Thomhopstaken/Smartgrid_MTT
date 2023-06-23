class Batterijen:

    def __init__(self, i: int, x: int, y: int,
                 capaciteit: int, prijs: int) -> None:
        """Neemt gegevens van batterijen uit district en
        slaat het op in batterij object."""
        self.batterij_id = i
        self.x_as = x
        self.y_as = y
        self.prijs = prijs
        self.capaciteit = capaciteit
        self.resterende_capaciteit = capaciteit
        self.gelinkte_huizen: list[object] = []
        self.gelegde_kabels: list[tuple[int, int]] = []

    def ontkoppel_huis(self, huis, wijk):
        """Ontkoppelt een willekeurig huis."""
        #huis = random.choice(self.gelinkte_huizen)
        self.gelinkte_huizen.remove(huis)
        wijk.gelinkte_huizen.remove(huis)
        wijk.losse_huizen.append(huis)
        self.update_verbruik(huis.maxoutput, ontkoppeling=True)
        huis.aangesloten = False

    def update_verbruik(self, output, ontkoppeling=False) -> None:
        """Update de resterende capaciteit van de batterij
        na het aansluiten van een huis."""
        if ontkoppeling:
            self.resterende_capaciteit += output
        else:
            self.resterende_capaciteit -= output

    def kabel_toevoegen(self, kabel) -> None:
        """Voegt een kabel toe aan batterij."""
        self.gelegde_kabels.append(kabel)

    def overbodige_kabels_verwijderen(self) -> None:
        """verwijderd kabels die niet naar een huis leiden."""
        huis_kabels = set()
        for huis in self.gelinkte_huizen:
            for kabel in huis.kabels:
                huis_kabels.add(kabel)
        overbodige_kabels = [kabel for kabel in self.gelegde_kabels
                             if kabel not in huis_kabels]
        self.gelegde_kabels = [kabel for kabel in self.gelegde_kabels
                               if kabel not in overbodige_kabels]

    def herbereken_capaciteit(self) -> None:
        """berekend de capaciteit na verwisseling van huizen."""
        totale_output = sum(huis.maxoutput for huis in self.gelinkte_huizen)
        self.resterende_capaciteit = self.capaciteit - totale_output
