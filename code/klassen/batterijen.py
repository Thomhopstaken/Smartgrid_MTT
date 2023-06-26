class Batterijen:

    def __init__(self, i, x, y,
                 capaciteit: int, prijs: int) -> None:
        """Neemt gegevens van batterijen uit district en
        slaat het op in batterij object.

        In: wijknummer, x-as, y-as, capaciteit en prijs."""
        self.batterij_id = i
        self.x_as = x
        self.y_as = y

        self.prijs = prijs
        self.capaciteit = capaciteit
        self.resterende_capaciteit = capaciteit

        self.gelinkte_huizen: list[object] = []
        self.gelegde_kabels: list[tuple[int, int]] = []

    def ontkoppel_huis(self, huis: object, wijk: object) -> None:
        """Ontkoppelt een huis object.

        In: Huis object en wijk object."""
        self.gelinkte_huizen.remove(huis)
        wijk.gelinkte_huizen.remove(huis)

        wijk.losse_huizen.append(huis)
        self.update_verbruik(huis.maxoutput, ontkoppeling=True)
        huis.aangesloten = False

    def update_verbruik(self, output: int, ontkoppeling: bool = False) -> None:
        """Update de resterende capaciteit van de batterij
        na het aansluiten van een huis.

        In: maxoutput en ontkoppeling."""
        if ontkoppeling:
            self.resterende_capaciteit += output
        else:
            self.resterende_capaciteit -= output

    def kabel_toevoegen(self, kabel: tuple[int, int]) -> None:
        """Voegt een kabel toe aan batterij.

        In: kabel coördinaten."""
        self.gelegde_kabels.append(kabel)

    def herbereken_capaciteit(self) -> None:
        """berekent de capaciteit na verwisseling van huizen."""
        totale_output = sum(huis.maxoutput for huis in self.gelinkte_huizen)
        self.resterende_capaciteit = self.capaciteit - totale_output

    def kabels_verwijderen(self) -> None:
        """Verwijdert kabels van een batterij object."""
        self.gelegde_kabels = []
