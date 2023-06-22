import csv
class Write_csv:

    def __init__(self, bestand):
        self.bestand = bestand

    def batterij(self, batterijen, centroids):
        with open(self.bestand, 'w', newline='') as b:
            writer = csv.writer(b)
            veld = ["positie", "capaciteit"]
            writer.writerow(veld)
            for i in range(len(batterijen)):
                writer.writerow([centroids[i], batterijen[i]])

    def huizen(self, huizen):
        with open(self.bestand, 'w', newline='') as b:
            writer = csv.writer(b)
            veld = ["x", "y", "maxoutput"]
            writer.writerow(veld)
            for ind in huizen.index:
                writer.writerow(
                    [huizen['x'][ind], huizen['y'][ind], huizen['maxoutput'][ind]])

    def maak_kosten(self):
        with open(self.bestand, 'w', newline='') as b:
            schrijver = csv.writer(b)
            veld = ["kosten"]
            schrijver.writerow(veld)

    def append_kosten(self, kosten):
        with open(self.bestand, 'a', newline='') as b:
            schrijver = csv.writer(b)
            veld = [kosten]
            schrijver.writerow(veld)