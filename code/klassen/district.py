from .batterijen import Batterijen
from .huizen import Huizen
from typing import TextIO
import json
import os


class District:
    def __init__(self, district: int, id: int) -> None:
        """Laad een wijk in aan de hand van opgegeven getal.

        In: wijknummer."""
        self.id = id
        self.districtnummer = district
        self.batterijen = []
        self.losse_huizen = []
        self.gelinkte_huizen = []

        self.laad_batterijen(self.data_pad(district, 'batteries'))
        self.laad_huizen(self.data_pad(district, 'houses'))

        for huis in self.losse_huizen:
            huis.bereken_afstand(self.batterijen)

    def laad_batterijen(self, bestand: str) -> None:
        """Neemt data van bestand en maakt daarmee batterijobjecten.
        deze worden ongebracht in batterijlijst.

        In: CSV bestand"""

        # neemt file eindigend op batteries.csv als input.
        with open(bestand, 'r') as b:
            teller = len(b.readlines())
        with open(bestand, 'r') as b:
            for i in range(0, teller):
                data = self.data_inladen(b)
                # voeg batterij object aan batterij-lijst toe.
                if data[0].isnumeric():
                    self.batterijen.append(
                        Batterijen(i, int(data[0]), int(data[1]),
                                   float(data[2])))

    def laad_huizen(self, bestand: str) -> None:
        """Neemt data van bestand en maakt daarna huisobjecten.
        Deze worden ondergebracht in huislijst.

        In: CSV bestand"""

        # neemt file eindigend op houses.csv als input. 
        with open(bestand, 'r') as b:
            teller = len(b.readlines())
        with open(bestand, 'r') as b:
            for i in range(0, teller):
                data = self.data_inladen(b)
                # voeg batterij object aan huizen-lijst toe.
                if data[0].isnumeric():
                    self.losse_huizen.append(
                        Huizen(i, int(data[0]), int(data[1]), float(data[2])))

    def data_inladen(self, b: TextIO):
        """Neemt bestandlijn en converteert het naar een lijst.

        In: CSV bestand.
        Uit: lijst met 3 variabelen."""

        line = b.readline()
        line = line.replace("\n", '')
        line = line.replace('\"', '')

        return line.split(",")

    def data_pad(self, district, item) -> str:
        """Vind het juist bestandspad naar opgevraagde bestand.

        In: bestaandsnaam
        Uit: pad naar opgevraagde bestand."""

        cwd = os.getcwd()
        sep = os.sep
        pad = f'{sep}Huizen&Batterijen{sep}district_{district}{sep}district-{district}_{item}.csv'
        return cwd + os.path.normpath(pad)

    # def link_huis(self, id):
    #     """Link een huis aan een batterij, verwijder het huis uit losse_huizen en
    #     en voeg deze toe aan gelinkte_huizen.
    #
    #     In: Huis_id"""
    #
    #     for huis in self.losse_huizen:
    #         if huis.huis_id == id:
    #             self.losse_huizen.remove(huis)
    #             self.gelinkte_huizen.append(huis)
    #             huis.aangesloten = True
    #             break

    # def delink_huis(self, id):
    #     for huis in self.gelinkte_huizen:
    #         if huis.huis_id == id:
    #             self.gelinkte_huizen.remove(huis)
    #             self.losse_huizen.append(huis)
    #             huis.aangesloten = False
    #             continue

    # def vind_los_huis(self, id):
    #     """Returnt een ongekoppeld huis."""
    #     for huis in self.losse_huizen:
    #         if huis.huis_id == id:
    #             return huis

    def creer_connectie(self, batterij, huis):
        huis.aangesloten = batterij
        if huis in self.losse_huizen:
            self.losse_huizen.remove(huis)
            self.gelinkte_huizen.append(huis)
        batterij.update_verbruik(huis.maxoutput)
        batterij.gelinkte_huizen.append(huis)

    def leg_kabel_route(self, batterij, huis):
        cursor_x, cursor_y = huis.x_as, huis.y_as
        while cursor_x < batterij.x_as:
            if ((cursor_x), (cursor_y)) not in batterij.gelegde_kabels:
                huis.leg_kabel((cursor_x), (cursor_y))
                batterij.kabel_toevoegen(((cursor_x), (cursor_y)))
            cursor_x += 1
        while cursor_x > batterij.x_as:
            if ((cursor_x), (cursor_y)) not in batterij.gelegde_kabels:
                huis.leg_kabel((cursor_x), (cursor_y))
                batterij.kabel_toevoegen(((cursor_x), (cursor_y)))
            cursor_x -= 1
        while cursor_y < batterij.y_as:
            if ((cursor_x), (cursor_y)) not in batterij.gelegde_kabels:
                huis.leg_kabel((cursor_x), (cursor_y))
                batterij.kabel_toevoegen(((cursor_x), (cursor_y)))
            cursor_y += 1
        while cursor_y > batterij.y_as:
            if ((cursor_x), (cursor_y)) not in batterij.gelegde_kabels:
                huis.leg_kabel((cursor_x), (cursor_y))
                batterij.kabel_toevoegen(((cursor_x), (cursor_y)))
            cursor_y -= 1
        self.creer_connectie(batterij, huis)

    def kosten_berekening(self):
        prijskaartje = 0
        # Kost batterijen
        prijskaartje += (len(self.batterijen)) * 5000

        for batterij in self.batterijen:
            prijskaartje += (len(batterij.gelegde_kabels)) * 9

        return prijskaartje

    def jsonify(self, wijk_nummer):
        json_dict = []
        district = {"district": int(wijk_nummer), "costs-shared": self.kosten_berekening()}
        json_dict.append(district)
        batterij_data = {}
        for batterij in self.batterijen:
            lokatie_bat = f"{batterij.x_as},{batterij.y_as}"
            capaciteit = batterij.capaciteit
            huizen = []
            for huis in batterij.gelinkte_huizen:
                huis_data = {}
                lokatie_huis = f"{huis.x_as},{huis.y_as}"
                output = huis.maxoutput
                kabels = []
                for i in range(len(huis.kabels)):
                    kabels.append(f"{huis.kabels[i][0]},{huis.kabels[i][1]}")
                huis_data["location"] = lokatie_huis
                huis_data["output"] = output
                huis_data["cables"] = kabels
                huizen.append(huis_data)
            batterij_data["location"] = lokatie_bat
            batterij_data["capacity"] = capaciteit
            batterij_data["houses"] = huizen
            json_dict.append(batterij_data)
            batterij_data = {}
        with open("output.json", "w") as outfile:
            json.dump(json_dict, outfile)