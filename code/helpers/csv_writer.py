import csv
class Write_csv:

    def __init__(self, bestand):
        self.bestand = bestand

    def batterij(self, batterijen, centroids):
        with open(self.bestand, 'w', newline='') as file:
            writer = csv.writer(file)
            field = ["positie", "capaciteit"]
            writer.writerow(field)
            for i in range(len(batterijen)):
                writer.writerow([centroids[i], batterijen[i]])

    def huizen(self, huizen):
        with open(self.bestand, 'w', newline='') as file:
            writer = csv.writer(file)
            field = ["x", "y", "maxoutput"]
            writer.writerow(field)
            for ind in huizen.index:
                writer.writerow(
                    [huizen['x'][ind], huizen['y'][ind], huizen['maxoutput'][ind]])

