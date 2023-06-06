class Batterijen:

    def __init__(self, x, y, capaciteit) -> None:
        """Neemt gegevens van batterijen uit district en slaat het op in batterij object."""

        self.x_as = x
        self.y_as = y
        self.capaciteit = capaciteit