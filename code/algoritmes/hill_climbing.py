import copy
from code.helpers import csv_writer, helpers
from .random_alg import random_alg


class Hill_climber:

    def __init__(self, wijk: object) -> None:
        """ Initialiseert een Hill_climber object met een wijk.

        In: wijk object."""
        self.oude_wijk = wijk
        self.kosten = wijk.kosten_berekening()
        self.nieuwe_wijk = wijk

        self.counter = 0

    def check_uitkomst(self) -> None:
        """Controleert of de nieuwe kosten lager zijn dan de oude kosten.
        True? vervang oude wijk met nieuwe wijk.
        False? counter wordt verhoogd."""
        nieuwe_kosten = self.nieuwe_wijk.kosten_berekening()
        oude_kosten = self.kosten

        # Controleer of de nieuwe kosten lager zijn dan de oude kosten.
        if nieuwe_kosten < oude_kosten:
            self.oude_wijk = self.nieuwe_wijk
            self.kosten = nieuwe_kosten
            self.counter = 0
            self.nieuwe_wijk = copy.deepcopy(self.oude_wijk)
        else:
            self.counter += 1

    def draai_hillclimber(self) -> object:
        """ Voert de hillclimber uit op de wijk.

        Uit: Wijk object."""
        bestand = helpers.data_pad(self.oude_wijk.id, "Hill_Climb_Run",
                                   experiment=True)
        csv_writer.Write_csv(bestand).maak_kosten()

        # Voer de hillclimber uit zolang de counter kleiner is dan 150.
        while self.counter < 150:
            csv_writer.Write_csv(bestand).append_kosten(self.kosten)
            if self.nieuwe_wijk.willekeurige_huizen_wisselen():
                self.check_uitkomst()

        return self.oude_wijk


def hillclimber_alg(wijk: object) -> object:
    """Voert het hillclimber algoritme uit op een wijk.

    in: wijk object.
    Uit: wijk object."""
    wijk_kopie = copy.deepcopy(wijk)
    random_wijk = random_alg(wijk_kopie)
    hillclimber = Hill_climber(random_wijk)
    nieuw_wijk = hillclimber.draai_hillclimber()
    return nieuw_wijk
