from .batterijen import Batterijen
from .huizen import Huizen
from typing import TextIO
import json
import os
import random


class District:
    def __init__(self, district: int, id: int, laad_huis=True, laad_batterij=True) -> None:
        """Laad een wijk in aan de hand van opgegeven getal.

        In: wijknummer."""
        self.id = id
        self.districtnummer = district
        self.batterijen = []
        self.losse_huizen = []
        self.gelinkte_huizen = []
        self.afstanden_batterij_huis = []
    
        if laad_huis:
            self.laad_huizen(data_pad(district, 'houses'))

        if laad_batterij:
            self.laad_batterijen(data_pad(district, 'batteries'))

        for huis in self.losse_huizen:
            huis.bereken_afstand(self.batterijen)

    def laad_batterijen(self, bestand: str, prijs:int=5000) -> None:
        """Neemt data van bestand en maakt daarmee batterijobjecten.
        deze worden ongebracht in batterijlijst.

        In: CSV bestand"""

        # neemt file eindigend op batteries.csv als input.
        with open(bestand, 'r') as b:
            teller = len(b.readlines())
        with open(bestand, 'r') as b:
            for i in range(0, teller):
                data = data_inladen(b)
                # voeg batterij object aan batterij-lijst toe.
                if data[0].isnumeric():
                    self.batterijen.append(
                        Batterijen(i, int(data[0]), int(data[1]),
                                   float(data[2]), prijs))


    def laad_huizen(self, bestand: str) -> None:
        """Neemt data van bestand en maakt daarna huisobjecten.
        Deze worden ondergebracht in huislijst.

        In: CSV bestand"""

        # neemt file eindigend op houses.csv als input. 
        with open(bestand, 'r') as b:
            teller = len(b.readlines())
        with open(bestand, 'r') as b:
            for i in range(0, teller):
                data = data_inladen(b)
                # voeg batterij object aan huizen-lijst toe.
                if data[0].isnumeric():
                    self.losse_huizen.append(
                        Huizen(i, int(data[0]), int(data[1]), float(data[2])))

    def bereken_afstand(self):
        for batterij in self.batterijen:
            for huis in self.losse_huizen:
                afstand = abs(batterij.x_as - huis.x_as) + abs(batterij.y_as - huis.y_as)
                self.afstanden_batterij_huis.append((batterij, huis, afstand))
                self.afstanden_batterij_huis = sorted(self.afstanden_batterij_huis, key=lambda x: x[2])
        return(self.afstanden_batterij_huis)
        # print(f"AFSTAND HUIZEN: {self.afstanden_batterij_huis}")
        # print(len(self.afstanden_batterij_huis))


    def leg_route(self, batterij, huis):
        cursor_x, cursor_y = huis.x_as, huis.y_as
        target = [batterij.x_as, batterij.y_as]
        for kabel in batterij.gelegde_kabels:
            if (abs(cursor_x - kabel[0]) + abs(cursor_y - kabel[1])) < (abs(cursor_x - target[0]) + abs(cursor_y - target[1])):
                target = [kabel[0], kabel[1]]
        while cursor_x < target[0]:
            if ((cursor_x), (cursor_y))  in batterij.gelegde_kabels:
                self.creer_connectie(batterij, huis)
                return
            huis.leg_kabel((cursor_x), (cursor_y))
            batterij.kabel_toevoegen(((cursor_x), (cursor_y)))
            cursor_x += 1
        while cursor_x > target[0]:
            if ((cursor_x), (cursor_y)) in batterij.gelegde_kabels:
                self.creer_connectie(batterij, huis)
                return
            huis.leg_kabel((cursor_x), (cursor_y))
            batterij.kabel_toevoegen(((cursor_x), (cursor_y)))
            cursor_x -= 1
        while cursor_y < target[1]:
            if ((cursor_x), (cursor_y)) in batterij.gelegde_kabels:
                self.creer_connectie(batterij, huis)
                return
            huis.leg_kabel((cursor_x), (cursor_y))
            batterij.kabel_toevoegen(((cursor_x), (cursor_y)))
            cursor_y += 1
        while cursor_y > target[1]:
            if ((cursor_x), (cursor_y)) in batterij.gelegde_kabels:
                self.creer_connectie(batterij, huis)
                return
            huis.leg_kabel((cursor_x), (cursor_y))
            batterij.kabel_toevoegen(((cursor_x), (cursor_y)))
            cursor_y -= 1
        huis.leg_kabel((cursor_x), (cursor_y))
        self.creer_connectie(batterij, huis)



    def creer_connectie(self, batterij, huis):
        huis.aangesloten = batterij
        if huis in self.losse_huizen:
            self.losse_huizen.remove(huis)
            self.gelinkte_huizen.append(huis)
        batterij.update_verbruik(huis.maxoutput)
        batterij.gelinkte_huizen.append(huis)


    def kosten_berekening(self):
        prijskaartje = 0
        # Kosten batterijen
        for batterij in self.batterijen:
            prijskaartje += batterij.prijs
        len_kabels = 0
        for batterij in self.batterijen:
            len_kabels += len(batterij.gelegde_kabels)
        prijskaartje += len_kabels * 9
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
        with open("figures/output.json", "w") as outfile:
            json.dump(json_dict, outfile)

    def hc_verwissel_huizen(self):
        huis_x, huis_y, batterij_x, batterij_y = self.hc_kies_willekeurige_huizen()
        if self.check_capaciteit(huis_x, huis_y, batterij_x, batterij_y):
            self.hc_kabels_verleggen(huis_x, huis_y, batterij_x, batterij_y)
    
    
    def hc_kies_willekeurige_huizen(self):

        huizen_gevonden = False

        while not huizen_gevonden:
            x = self.gelinkte_huizen[random.randint(0, 149)]
            y = self.gelinkte_huizen[random.randint(0, 149)]
            if x.aangesloten != y.aangesloten:
                huis_x, huis_y = x, y
                batterij_x, batterij_y = x.aangesloten, y.aangesloten
                huizen_gevonden = True
        return huis_x, huis_y, batterij_x, batterij_y

def hc_kabels_verleggen(self, huis_x, huis_y, batterij_x, batterij_y):
    """legt kabels tussen huis_x en batterij_y en huis_y en batterij_x"""
    huis_x.verwijder_kabels()
    huis_y.verwijder_kabels()
    self.leg_route(batterij_x, huis_y)
    self.leg_route(batterij_y, huis_x)

    index_x = batterij_x.gelinkte_huizen.index(huis_x)
    index_y = batterij_y.gelinkte_huizen.index(huis_y)
    batterij_x.gelinkte_huizen.append(
        batterij_y.gelinkte_huizen.pop(index_y))
    batterij_y.gelinkte_huizen.append(
        batterij_x.gelinkte_huizen.pop(index_x))

    batterij_x.overbodige_kabels_verwijderen()
    batterij_y.overbodige_kabels_verwijderen()
    
    def check_capaciteit(self, huis_x, huis_y, batterij_x, batterij_y):
        """checkt of wissel huis_x en huis_y haalbaar is ivm capaciteit. """
        nieuwe_cap_bat_x = batterij_x.resterende_capaciteit + huis_x.maxoutput
        nieuwe_cap_bat_y = batterij_y.resterende_capaciteit + huis_y.maxoutput
        # Nieuw cap - maxoutput zal bijna nooit allebei >= 0 zijn omdat de resterende capaciteiten
        # zo dichtbij 0 zijn. Als je bijvoorbeeld twee blokken van 5 huizen gebruikt in plaats van twee
        # willekeurige huizen gebruikt, is de kans aanzienelijk groter dat je de huizen kan wisselen
        if nieuwe_cap_bat_x - huis_y.maxoutput >= 0 and nieuwe_cap_bat_y - huis_x.maxoutput >= 0:
            return True
        else: 
            return False
        

def data_inladen(b: TextIO):
    """Neemt bestandlijn en converteert het naar een lijst.

    In: CSV bestand.
    Uit: lijst met 3 variabelen."""

    line = b.readline()
    line = line.replace("\n", '')
    line = line.replace('\"', '')

    return line.split(",")


def data_pad(district, item, item2=None, kmeans=False,
             huizen=False) -> str:
    """Vind het juist bestandspad naar opgevraagde bestand.

    In: bestaandsnaam
    Uit: pad naar opgevraagde bestand."""

    cwd = os.getcwd()
    sep = os.sep
    if kmeans == True:
        pad = f'{sep}Huizen&Batterijen{sep}k_means{sep}batterij_{item}.csv'
        return cwd + os.path.normpath(pad)

    if huizen == True:
        pad = f'{sep}Huizen&Batterijen{sep}k_means{sep}batterij_{item}_cluster_{item2}.csv'
        return cwd + os.path.normpath(pad)

    pad = f'{sep}Huizen&Batterijen{sep}district_{district}{sep}district-{district}_{item}.csv'
    return cwd + os.path.normpath(pad)



