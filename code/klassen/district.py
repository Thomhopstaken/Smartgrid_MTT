from .batterijen import Batterijen
from code.helpers import helpers
from .huizen import Huizen
import json
import random
from typing import TextIO


class Wijk:
    def __init__(self, district: str, id: str, laad_huis: bool = True,
                 laad_batterij: bool = True) -> None:
        """Laad een wijk in aan de hand van opgegeven getal.

        In: wijknummer, run-nummer."""
        self.id = id
        self.wijk = district
        self.districtnummer = district

        self.batterijen: list[Batterijen] = []
        self.losse_huizen: list[Huizen] = []
        self.gelinkte_huizen: list[Huizen] = []

        self.afstanden_batterij_huis: list[tuple[Batterijen, Huizen, int]] = []
        self.geshuffelde_afstanden: list[tuple[Batterijen, Huizen, int]] = []

        # Laad de huizen in als laad_huis True is
        if laad_huis:
            self.laad_huizen(helpers.data_pad(district, 'houses'))

        # Laad de batterijen in als laad_batterij True is
        if laad_batterij:
            self.laad_batterijen(helpers.data_pad(district, 'batteries'))

        # Bereken de afstanden tussen huizen en batterijen
        for huis in self.losse_huizen:
            huis.bereken_afstand(self.batterijen)

    def ontkoppel_huis(self, huis: Huizen) -> None:
        """Ontkoppelt een huis object.

        In: huis object."""
        self.gelinkte_huizen.remove(huis)
        self.losse_huizen.append(huis)
        huis.aangesloten = False

    def laad_batterijen(self, bestand: str, prijs: int = 1800) -> None:
        """Neemt data van bestand en maakt daarmee batterij objecten.
        deze worden ongebracht in batterijlijst.

        In: CSV bestandpad, prijs(standaard 1800)."""

        # neemt file eindigend op batteries.csv als input
        with open(bestand, 'r') as b:
            teller = len(b.readlines())

        # neemt file eindigend op batteries.csv als input.
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

        In: CSV bestandpad."""

        # neemt file eindigend op houses.csv als input.
        with open(bestand, 'r') as b:
            teller = len(b.readlines())

        # neemt file eindigend op batteries.csv als input.
        with open(bestand, 'r') as b:
            for i in range(0, teller):
                data = parse_csv(b)

                # voeg batterij object aan huizen-lijst toe.
                if data[0].isnumeric():
                    self.losse_huizen.append(
                        Huizen(i, int(data[0]), int(data[1]), float(data[2])))

    def bereken_afstand(self) -> list[tuple[Batterijen, Huizen, int]]:
        """Berekent de afstand van huizen tot batterijen
        en sorteert van klein naar groot.

        Uit: lijst met tuple bestaande uit een batterij object,
        een huis object en afstand tussen huizen en batterijen."""
        for batterij in self.batterijen:
            for huis in self.losse_huizen:
                afstand = abs(batterij.x_as - huis.x_as) + abs(
                    batterij.y_as - huis.y_as)
                self.afstanden_batterij_huis.append((batterij, huis, afstand))
        self.afstanden_batterij_huis = sorted(self.afstanden_batterij_huis,
                                              key=lambda x: x[2])
        return (self.afstanden_batterij_huis)

    def shuffle_afstanden(self) -> list[list[tuple[object, int]]]:
        """Maakt sublijsten aan in afstanden_batterij_huis en shuffled.

        Uit: maakt een lijst aan met
        geshuffelde afstanden_batterij_huis lijst."""
        self.bereken_afstand()
        for i in range(0, len(self.afstanden_batterij_huis), 3):
            sublijst = self.afstanden_batterij_huis[i:i + 3]
            random.shuffle(sublijst)
            self.geshuffelde_afstanden.append(sublijst)
        return self.geshuffelde_afstanden

    def leg_route(self, batterij: Batterijen, huis: Huizen) -> None:
        """Legt een route voor het leggen van een kabel
        van een huis naar een batterij.

        In: batterij object en huis object."""
        cursor_x, cursor_y = huis.x_as, huis.y_as
        target = [batterij.x_as, batterij.y_as]

        # Bepaal het doel als het dichtstbijzijnde
        # punt waar al een kabel is gelegd
        for kabel in batterij.gelegde_kabels:
            if (abs(cursor_x - kabel[0]) + abs(cursor_y - kabel[1])) < (
                    abs(cursor_x - target[0]) + abs(cursor_y - target[1])):
                target = [kabel[0], kabel[1]]

        # Leg de kabel in stappen totdat het doel is bereikt
        while cursor_x < target[0]:
            if ((cursor_x), (cursor_y)) in batterij.gelegde_kabels:
                self.creer_connectie(batterij, huis)
                return
            huis.leg_kabel((cursor_x), (cursor_y))
            batterij.kabel_toevoegen(((cursor_x), (cursor_y)))
            cursor_x += 1

        # Ga naar links totdat het doel is bereikt in de x-richting.
        while cursor_x > target[0]:
            if ((cursor_x), (cursor_y)) in batterij.gelegde_kabels:
                self.creer_connectie(batterij, huis)
                return
            huis.leg_kabel((cursor_x), (cursor_y))
            batterij.kabel_toevoegen(((cursor_x), (cursor_y)))
            cursor_x -= 1

        # Ga naar boven totdat het doel is bereikt in de y-richting
        while cursor_y < target[1]:
            if ((cursor_x), (cursor_y)) in batterij.gelegde_kabels:
                self.creer_connectie(batterij, huis)
                return
            huis.leg_kabel((cursor_x), (cursor_y))
            batterij.kabel_toevoegen(((cursor_x), (cursor_y)))
            cursor_y += 1

        # Ga naar beneden totdat het doel is bereikt in de y-richting
        while cursor_y > target[1]:
            if ((cursor_x), (cursor_y)) in batterij.gelegde_kabels:
                self.creer_connectie(batterij, huis)
                return
            huis.leg_kabel((cursor_x), (cursor_y))
            batterij.kabel_toevoegen(((cursor_x), (cursor_y)))
            cursor_y -= 1

        # Leg de kabel op het doel
        huis.leg_kabel((cursor_x), (cursor_y))
        self.creer_connectie(batterij, huis)

    def creer_connectie(self, batterij: Batterijen, huis: Huizen) -> None:
        """Creëert een verbinding tussen een batterij en een huis.

        In: batterij object en huis object."""
        huis.aangesloten = batterij

        # Verplaats het huis van losse_huizen naar gelinkte_huizen
        if huis in self.losse_huizen:
            self.losse_huizen.remove(huis)
            self.gelinkte_huizen.append(huis)
        batterij.update_verbruik(huis.maxoutput)

        # Voeg het huis toe aan gelinkte_huizen van de batterij
        # als deze er niet in zit.
        if huis not in batterij.gelinkte_huizen:
            batterij.gelinkte_huizen.append(huis)

    def kosten_berekening(self) -> int:
        """Berekent de prijs van alle batterijen en kabels in wijk.

        Uit: prijskaartje"""
        prijskaartje = 0

        # Kosten van batterijen berekenen
        for batterij in self.batterijen:
            prijskaartje += batterij.prijs
        len_kabels = 0
        for batterij in self.batterijen:
            len_kabels += len(batterij.gelegde_kabels)
        prijskaartje += len_kabels * 9
        return prijskaartje

    def herleg_alle_kabels(self) -> None:
        """Herlegt kabels tussen batterijen en huizen."""
        for batterij in self.batterijen:
            batterij.kabels_verwijderen()
            batterij.resterende_capaciteit = batterij.capaciteit
        for huis in self.gelinkte_huizen:
            huis.verwijder_kabels()
        for huis in self.gelinkte_huizen:
            self.leg_route(huis.aangesloten, huis)

    def jsonify(self, wijk_nummer: int, algoritme: str) -> None:
        """Print de informatie van de wijk naar een json bestand

        In: wijknummer, algoritme naam."""
        json_dict = []
        district = {"district": int(wijk_nummer),
                    "costs-shared": self.kosten_berekening()}
        json_dict.append(district)
        batterij_data = {}

        # Loop over de batterijen om de informatie op te slaan
        for batterij in self.batterijen:
            locatie_bat = f"{batterij.x_as},{batterij.y_as}"
            capaciteit = batterij.capaciteit
            huizen = []

            # Loop over gelinkte huizen van de batterij en sla info op
            for huis in batterij.gelinkte_huizen:
                huis_data = {}
                locatie_huis = f"{huis.x_as},{huis.y_as}"
                output = huis.maxoutput
                kabels = []

                # Loop over de kabels van het huis om coördinaten op te slaan
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

        # Schrijf de JSON-data naar het bestand
        with open(f"figuren/{algoritme}_{wijk_nummer}_output.json",
                  "w") as outfile:
            json.dump(json_dict, outfile)

    def willekeurige_huizen_wisselen(self) -> bool:
        """Checkt of 3 huizen van de ene batterij gewisseld
        kunnen worden met 3 huizen van een andere batterij.

        Uit: True als huizen verwisselt kunnen worden. Anders False."""
        batterij_x, batterij_y = self.kies_willekeurige_batterijen()
        huizen_x = self.kies_willekeurige_huizen(batterij_x)
        huizen_y = self.kies_willekeurige_huizen(batterij_y)

        # Controleer of de huizen kunnen worden
        # verwisseld door capaciteit te controleren.
        if self.check_capaciteit(huizen_x, huizen_y, batterij_x,
                                 batterij_y):
            self.wissel_huizen(huizen_x, huizen_y, batterij_x, batterij_y)
            return True
        else:
            return False

    def wissel_huizen(self, huizen_x: list[Huizen], huizen_y: list[Huizen],
                      batterij_x: Batterijen, batterij_y: Batterijen) -> None:
        """
        Wissel 3 huizen van de ene batterij met 3 huizen
        van een andere batterij.

        In: 2 lijsten met drie huis objecten, 2 batterij objecten.
        """
        for x in range(len(huizen_x)):
            self.kabels_verleggen(huizen_x[x], batterij_y, batterij_x)
            self.kabels_verleggen(huizen_y[x], batterij_x, batterij_y)
        self.herleg_alle_kabels()

    def kies_willekeurige_huizen(self,
                                 batterij: Batterijen) -> list[Huizen]:
        """Kiest drie willekeurige huizen uit de lijst.
        van gelinkte huizen aan de aangegeven batterij.

        In: batterij object
        uit: lijst met 3 huis objecten."""
        huizen = random.sample(batterij.gelinkte_huizen, k=3)
        return huizen

    def kies_willekeurige_batterijen(self) -> list[Batterijen]:
        """Kiest twee willekeurige batterijen uit batterijen.

        Uit: 2 batterij objecten."""
        batterijen = random.sample(self.batterijen, k=2)
        return batterijen

    def kabels_verleggen(self, huis: Huizen, nieuwe_batterij: Batterijen,
                         oude_batterij: Batterijen) -> None:
        """legt kabels tussen huis naar nieuwe batterij
        en verwijderd de oude kabels.

        In: 1 huis object en 2 batterij objecten."""
        oude_batterij.gelinkte_huizen.remove(huis)
        self.leg_route(nieuwe_batterij, huis)

    def check_capaciteit(self, huizen_x: list[Huizen],
                         huizen_y: list[Huizen], batterij_x: Batterijen,
                         batterij_y: Batterijen) -> bool:
        """checkt of wissel huis_x en huis_y haalbaar is ivm capaciteit.

        In: 2 lijsten met 3 huis objecten, 2 batterij objecten.
        Uit: als nieuwe cap - nieuwe output >= 0 dan True, anders False"""
        huizen_x_output = sum(huis.maxoutput for huis in huizen_x)
        huizen_y_output = sum(huis.maxoutput for huis in huizen_y)
        nieuwe_cap_bat_x = batterij_x.resterende_capaciteit + huizen_x_output
        nieuwe_cap_bat_y = batterij_y.resterende_capaciteit + huizen_y_output

        # Controleer of de nieuwe capaciteit - nieuwe output >= 0
        if nieuwe_cap_bat_x - huizen_y_output >= 0 and \
                nieuwe_cap_bat_y - huizen_x_output >= 0:
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
