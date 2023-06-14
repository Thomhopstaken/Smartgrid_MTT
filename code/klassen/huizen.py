class Huizen:

    def __init__(self, i, x, y, maxoutput) -> None:
        """Neemt gegevens van Huizen uit district en slaat ze op in een Huizen object."""
        
        self.huis_id = i
        self.x_as = x
        self.y_as = y
        self.maxoutput = maxoutput
        self.kabels = []
        self.afstand_batterijen = {}
        self.aangesloten = False
    
    def bereken_afstand(self, batterijen):
        for batterij in batterijen:
            afstand = abs(batterij.x_as - self.x_as) + abs(batterij.y_as - self.y_as)
            self.afstand_batterijen[batterij] = afstand
        self.afstand_batterijen = dict(sorted(self.afstand_batterijen.items(), key=lambda item:item[1]))

    def leg_kabel(self, x, y) -> None:
        """Voegt kabels toe in self.kabels."""
        
        self.kabels.append((x, y))
        # print(f"kabels: {self.kabels}")

    def kan_huis_aansluiten_op_batterij(self, batterij) -> bool:
        """Controleert of een huis kan worden aangesloten op een batterij."""
        
        if not self.aangesloten:
            if batterij.resterende_capaciteit - self.maxoutput >= 0:
                return True
            else:
                return False
        else:
            return False

    def verwijder_kabels(self) -> None:
         self.kabels = []