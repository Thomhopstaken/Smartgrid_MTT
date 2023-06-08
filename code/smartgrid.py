from batterijen import Batterijen
from district import District
from huizen import Huizen
from termcolor import colored


class Smartgrid:
    def __init__(self):
        """Initialiseert het Smartgrid-object."""
        self.grid = self.create_grid()

    def create_grid(self):
        """Maakt een 2D-array voor het grid en vult het met lege cellen."""
        rows, cols = (51, 51)
        arr = [["_" for _ in range(cols)] for _ in range(rows)]
        return arr

    def print_grid(self):
        """Print het Smartgrid."""
        for row in self.grid:
            print(*row)

    def add_houses(self, district):
        """Voegt huizen toe aan het Smartgrid."""
        for house in district.losse_huizen:
            self.grid[(50 - house.y_as)][house.x_as] = colored('H', 'blue')

    def add_batteries(self, district):
        """Voegt batterijen toe aan het Smartgrid."""
        for battery in district.batterijen:
            self.grid[(50 - battery.y_as)][battery.x_as] = colored('B', 'red')

    def add_cable(self, y, x):
        """Voegt een kabel toe aan het Smartgrid op de opgegeven positie."""
        if self.grid[y][x] == colored('H', 'blue') or self.grid[y][x] == colored('B', 'red'):
            return
        try:
            self.grid[y][x] += 1
        except TypeError:
            self.grid[y][x] = 1

    def route_cable(self, wijk, batterij, huis):
        """Bepaalt de route van de kabel tussen een batterij en een huis."""
        cursor_x, cursor_y = batterij.x_as, batterij.y_as
        while cursor_x < huis.x_as:
            huis.lay_cable((cursor_x), (cursor_y))
            self.add_cable((50 - cursor_y), (cursor_x + 1))
            cursor_x += 1
        while cursor_x > huis.x_as:
            huis.lay_cable((cursor_x), (cursor_y))
            self.add_cable((50 - cursor_y), (cursor_x - 1))
            cursor_x -= 1
        while cursor_y < huis.y_as:
            huis.lay_cable((cursor_x), (cursor_y))
            self.add_cable((50 - cursor_y - 1), (cursor_x))
            cursor_y += 1
        while cursor_y > huis.y_as:
            huis.lay_cable((cursor_x), (cursor_y))
            self.add_cable((50 - cursor_y + 1), (cursor_x))
            cursor_y -= 1
        huis.lay_cable((cursor_x), (cursor_y))
        wijk.creer_connectie(batterij, huis)

def huis_checker(huis, batterij):
    """Controleert of een huis kan worden aangesloten op een batterij."""
    if not huis.linked:
        if batterij.resterende_capaciteit - huis.maxoutput >= 0:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    
    # vraag om district.
    wijknummer = input('Wijk 1, 2 of 3: ')
    #algoritme_keuze = input('Kies 1 (greedy algoritme) of 2 (random algoritme)')
    
    # maak een district aan. 
    wijk = District(wijknummer)
    grid = Smartgrid()
    grid.add_houses(wijk)
    grid.add_batteries(wijk)
    
    while len(wijk.losse_huizen) > 0:
        for batterij in wijk.batterijen:
            for huis in wijk.losse_huizen:
                if huis_checker(huis, batterij):
                    #batterij.gebruik += huis.maxoutput
                    wijk.huis_linken(huis.huis_id)
                    grid.route_cable(wijk, batterij, huis)
 
    grid.print_grid()
    for batterij in wijk.batterijen:
        print(F'Batterij {batterij.batterij_id} gebruik: {batterij.resterende_capaciteit}')
        print(f'gelinkte huizen:')
        print(f'{len(batterij.gelinkte_huizen)}')
        #for huis in batterij.gelinkte_huizen:
        #    print(f' {huis.huis_id}|', end='')