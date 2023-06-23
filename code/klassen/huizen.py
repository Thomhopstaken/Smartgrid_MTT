

class Huizen:

    def __init__(self, i, x, y, maxoutput) -> None:
        """Neemt gegevens van Huizen uit district
        en slaat ze op in een Huizen object."""
        self.huis_id = i
        self.x_as = x
        self.y_as = y
        self.maxoutput = maxoutput
        self.kabels: list[tuple[int, int]] = []
        self.afstand_batterijen: dict[object, int] = {}
        self.aangesloten = False

    def bereken_afstand(self, batterijen) -> None:
        """berekent de afstand tussen huis en alle batterijen."""
        for batterij in batterijen:
            afstand = abs(batterij.x_as - self.x_as) + abs(batterij.y_as
                                                           - self.y_as)
            self.afstand_batterijen[batterij] = afstand
        self.afstand_batterijen = dict(sorted(self.afstand_batterijen.items(),
                                              key=lambda item: item[1]))

    def dichtstbijzijnde_batterij(self):
        """Geeft kortste afstand vanaf een huis."""
        if self.afstand_batterijen:
            return min(self.afstand_batterijen, key=self.afstand_batterijen.get)
        else:
            return None


    def leg_kabel(self, x, y) -> None:
        """Voegt kabels toe in self.kabels."""
        self.kabels.append((x, y))

    def kan_aansluiten(self, batterij) -> bool:
        """Controleert of een huis kan worden aangesloten op een batterij."""
        if not self.aangesloten:
            if batterij.resterende_capaciteit - self.maxoutput >= 0:
                return True
            else:
                return False
        else:
            return False

    def verwijder_kabels(self) -> None:
        """verwijderd alle kabels in kabels."""
        self.kabels = []
