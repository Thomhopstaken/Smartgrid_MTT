import csv


class Write_csv:

    def __init__(self, bestand: str) -> None:
        self.bestand = bestand

    def batterij(self, batterijen: list[object],
                 centroids: list[list[float]]) -> None:
        with open(self.bestand, 'w', newline='') as b:
            schrijver = csv.writer(b)
            veld = ["positie", "capaciteit"]
            schrijver.writerow(veld)
            for i in range(len(batterijen)):
                schrijver.writerow([centroids[i], batterijen[i]])

    def huizen(self, huizen: list[object]) -> None:
        with open(self.bestand, 'w', newline='') as b:
            schrijver = csv.writer(b)
            veld = ["x", "y", "maxoutput"]
            schrijver.writerow(veld)
            for ind in huizen.index:
                schrijver.writerow(
                    [huizen['x'][ind], huizen['y'][ind],
                     huizen['maxoutput'][ind]])

    def maak_kosten(self) -> None:
        with open(self.bestand, 'w', newline='') as b:
            schrijver = csv.writer(b)
            veld = ["kosten"]
            schrijver.writerow(veld)

    def append_kosten(self, kosten: int) -> None:
        with open(self.bestand, 'a', newline='') as b:
            schrijver = csv.writer(b)
            veld = [kosten]
            schrijver.writerow(veld)
