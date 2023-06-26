import csv


class Write_csv:

    def __init__(self, bestand: str) -> None:
        """Initialiseert een nieuw CSV-schrijverobject
        met het opgegeven bestand."""
        self.bestand = bestand

    def batterij(self, batterijen: list[object],
                 centroids: list[list[float]]) -> None:
        """Schrijft de batterijgegevens naar het CSV-bestand.

        in: lijst met batterijen en lijst met centroids."""
        with open(self.bestand, 'w', newline='') as b:
            schrijver = csv.writer(b)
            veld = ["positie", "capaciteit"]
            schrijver.writerow(veld)

            # Schrijf de gegevens van elke batterij naar het CSV-bestand.
            for i in range(len(batterijen)):
                schrijver.writerow([centroids[i], batterijen[i]])

    def huizen(self, huizen: list[object]) -> None:
        """Schrijft de huisgegevens naar het CSV-bestand.

        In: Een lijst van huisobjecten."""
        with open(self.bestand, 'w', newline='') as b:
            schrijver = csv.writer(b)
            veld = ["x", "y", "maxoutput"]
            schrijver.writerow(veld)

            # Schrijf de gegevens van elk huis naar het CSV-bestand.
            for ind in huizen.index:
                schrijver.writerow(
                    [huizen['x'][ind], huizen['y'][ind],
                     huizen['maxoutput'][ind]])

    def maak_kosten(self) -> None:
        """Maakt een nieuw CSV-bestand voor het opslaan van kostengegevens."""
        with open(self.bestand, 'w', newline='') as b:
            schrijver = csv.writer(b)
            veld = ["kosten"]
            schrijver.writerow(veld)

    def append_kosten(self, kosten: int) -> None:
        """Voegt een nieuwe kostengegevensrij toe aan het CSV-bestand.

        iN: De kostenwaarde die moet worden toegevoegd."""
        with open(self.bestand, 'a', newline='') as b:
            schrijver = csv.writer(b)
            veld = [kosten]
            schrijver.writerow(veld)
