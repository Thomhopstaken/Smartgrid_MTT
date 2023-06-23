from .batterijen import Batterijen
from .huizen import Huizen
from typing import TextIO
from code.helpers import helpers
import json
import random


class Wijk:
    def __init__(self, district: str, id: str, laad_huis=True, laad_batterij=True) -> None:
        """Laad een wijk in aan de hand van opgegeven getal.

        In: wijknummer."""
        self.id = id
        self.wijk = district
        self.districtnummer = district
        self.batterijen: list[Batterijen] = []
        self.losse_huizen: list[Huizen] = []
        self.gelinkte_huizen: list[Huizen] = []
        self.afstanden_batterij_huis: list[tuple[Batterijen, Huizen, int]] = []
        self.geshuffelde_afstanden: list[tuple[Batterijen, Huizen, int]] = []

    
        if laad_huis:
            self.laad_huizen(helpers.data_pad(district, 'houses'))

        if laad_batterij:
            self.laad_batterijen(helpers.data_pad(district, 'batteries'))

        for huis in self.losse_huizen:
            huis.bereken_afstand(self.batterijen)

    def ontkoppel_huis(self, huis: Huizen) -> None:
        self.gelinkte_huizen.remove(huis)
        self.losse_huizen.append(huis)
        huis.aangesloten = False

    def laad_batterijen(self, bestand: str, prijs:int=5000) -> None:
        """Neemt data van bestand en maakt daarmee batterijobjecten.
        deze worden ongebracht in batterijlijst.

        In: CSV bestand"""

        # neemt file eindigend op batteries.csv als input.
        with open(bestand, 'r') as b:
            teller = len(b.readlines())
        with open(bestand, 'r') as b:
            for i in range(0, teller):
                data = parse_csv(b)
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
                data = parse_csv(b)
                # voeg batterij object aan huizen-lijst toe.
                if data[0].isnumeric():
                    self.losse_huizen.append(
                        Huizen(i, int(data[0]), int(data[1]), float(data[2])))

    def bereken_afstand(self) -> list[tuple[Batterijen, Huizen, int]]:
        for batterij in self.batterijen:
            for huis in self.losse_huizen:
                afstand = abs(batterij.x_as - huis.x_as) + abs(batterij.y_as - huis.y_as)
                self.afstanden_batterij_huis.append((batterij, huis, afstand))
        self.afstanden_batterij_huis = sorted(self.afstanden_batterij_huis, key=lambda x: x[2])
        return(self.afstanden_batterij_huis)
    

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


    def creer_connectie(self, batterij: Batterijen, huis: Huizen) -> None:
        huis.aangesloten = batterij
        if huis in self.losse_huizen:
            self.losse_huizen.remove(huis)
            self.gelinkte_huizen.append(huis)
        batterij.update_verbruik(huis.maxoutput)
        batterij.gelinkte_huizen.append(huis)


    def kosten_berekening(self) -> int:
        """Berekent de prijs van alle batterijen en kabels in wijk."""
        prijskaartje = 0
        # Kosten batterijen
        for batterij in self.batterijen:
            prijskaartje += batterij.prijs
        len_kabels = 0
        for batterij in self.batterijen:
            len_kabels += len(batterij.gelegde_kabels)
        prijskaartje += len_kabels * 9
        return prijskaartje

    def herleg_alle_kabels(self):
        for huis in self.gelinkte_huizen:
            huis.verwijder_kabels()
        for huis in self.gelinkte_huizen:
            self.leg_route(huis.aangesloten, huis)

    def jsonify(self, wijk_nummer: int, algoritme: str) -> None:
        """Print de informatie van de wijk naar een json bestand
        
        In: wijknummer, algoritme naam."""
        json_dict = []
        district = {"district": int(wijk_nummer), "costs-shared": self.kosten_berekening()}
        json_dict.append(district)
        batterij_data = {}
        for batterij in self.batterijen:
            locatie_bat = f"{batterij.x_as},{batterij.y_as}"
            capaciteit = batterij.capaciteit
            huizen = []
            for huis in batterij.gelinkte_huizen:
                huis_data = {}
                locatie_huis = f"{huis.x_as},{huis.y_as}"
                output = huis.maxoutput
                kabels = []
                for i in range(len(huis.kabels)):
                    kabels.append(f"{huis.kabels[i][0]},{huis.kabels[i][1]}")
                huis_data["location"] = locatie_huis
                huis_data["output"] = output
                huis_data["cables"] = kabels
                huizen.append(huis_data)
            batterij_data["location"] = locatie_bat
            batterij_data["capacity"] = capaciteit
            batterij_data["houses"] = huizen
            json_dict.append(batterij_data)
            batterij_data = {}
        with open(f"figures/{algoritme}_{wijk_nummer}_output.json", "w") as outfile:
            json.dump(json_dict, outfile)

    def hill_climber(self) -> bool:
        """Checkt of 3 huizen van de ene batterij gewisseld
        kunnen worden met 3 huizen van een andere batterij.

        Uit: True als huizen verwisselt kunnen worden. Anders False."""
        batterij_x, batterij_y = self.hc_kies_willekeurige_batterijen()
        huizen_x = self.hc_kies_willekeurige_huizen(batterij_x)
        huizen_y = self.hc_kies_willekeurige_huizen(batterij_y)

        if self.hc_check_capaciteit(huizen_x, huizen_y, batterij_x, batterij_y):
            self.hc_wissel_huizen(huizen_x, huizen_y, batterij_x, batterij_y)
            return True
        else:
            return False

    def hc_wissel_huizen(self, huizen_x: list[Huizen], huizen_y: list[Huizen], 
                         batterij_x: Batterijen, batterij_y: Batterijen) -> None:
        """Wissel 3 huizen van de ene batterij met 3 huizen van een andere batterij.

        In: 2 lijsten met drie huis objecten, 2 batterij objecten."""
        for x in range(len(huizen_x)):
            self.hc_kabels_verleggen(huizen_x[x], batterij_y, batterij_x)
            self.hc_kabels_verleggen(huizen_y[x], batterij_x, batterij_y)
        batterij_x.herbereken_capaciteit()
        batterij_y.herbereken_capaciteit()     
             
    def hc_kies_willekeurige_huizen(self, batterij: Batterijen) -> list[Huizen]:
        """Kiest drie willekeurige huizen uit de lijst.
        van gelinkte huizen aan de aangegeven batterij.
        
        In: batterij object
        uit: lijst met 3 huis objecten."""
        huizen = random.sample(batterij.gelinkte_huizen, k=3)    
        return huizen
    
    def hc_kies_willekeurige_batterijen(self) -> list[Batterijen]:
        """Kiest twee willekeurige batterijen uit batterijen.

        Uit: 2 batterij objecten."""
        batterijen = random.sample(self.batterijen, k=2)
        return batterijen

    def hc_kabels_verleggen(self, huis: Huizen, nieuwe_batterij: Batterijen, 
                            oude_batterij: Batterijen) -> None:
        """legt kabels tussen huis naar nieuwe batterij en verwijderd de oude kabels.

        In: 1 huis object en 2 batterij objecten."""
        oude_batterij.gelinkte_huizen.remove(huis)
        huis.verwijder_kabels()
        self.leg_route(nieuwe_batterij, huis)
        oude_batterij.overbodige_kabels_verwijderen()
    
    def hc_check_capaciteit(self, huizen_x: list[Huizen], huizen_y: list[Huizen],
                            batterij_x: Batterijen, batterij_y: Batterijen) -> bool:
        """checkt of wissel huis_x en huis_y haalbaar is ivm capaciteit.

        In: 2 lijsten met 3 huis objecten, 2 batterij objecten.
        Uit: als nieuwe cap - nieuwe output >= 0 dan True, anders False"""
        huizen_x_output = sum(huis.maxoutput for huis in huizen_x)
        huizen_y_output = sum(huis.maxoutput for huis in huizen_y)
        nieuwe_cap_bat_x = batterij_x.resterende_capaciteit + huizen_x_output
        nieuwe_cap_bat_y = batterij_y.resterende_capaciteit + huizen_y_output

        if nieuwe_cap_bat_x - huizen_y_output >= 0 and nieuwe_cap_bat_y - huizen_x_output >= 0:
            return True
        else: 
            return False


def parse_csv(b: TextIO) -> list:
    """Neemt bestandlijn en converteert het naar een lijst.

    In: CSV bestand.
    Uit: lijst met 3 variabelen."""

    line = b.readline()
    line = line.replace("\n", '')
    line = line.replace('\"', '')

    return line.split(",")






