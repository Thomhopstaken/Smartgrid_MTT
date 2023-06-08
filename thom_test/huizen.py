class Huizen:

    def __init__(self, i, x, y, maxoutput) -> None:
        """Neemt gegevens van Huizen uit district en slaat ze op in een Huizen object."""
        self.huis_id = i
        self.x_as = x
        self.y_as = y
        self.maxoutput = maxoutput
        self.kabels = []
        self.linked = False

    def lay_cable(self, x, y) -> None:
        """Maakt connecties tussen batterijen en huizen."""
        self.kabels.append((x, y))

    