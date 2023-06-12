from code.klassen.district import District
from termcolor import colored


class Smartgrid:

    def __init__(self):
        """Initialiseert het Smartgrid-object."""
        self.grid = self.create_grid()

    def initialiseer_grid(self):
        """Initialiseert een 2D-array voor het grid en vult het met lege cellen."""
        rij, kolom = (51, 51)
        arr = [["_" for _ in range(kolom)] for _ in range(rij)]
        return arr

    def print_grid(self):
        """Print het Smartgrid."""
        for rij in self.grid:
            print(*rij)

    def huizen_toevoegen(self, district):
        """Voegt huizen toe aan het Smartgrid."""
        for huis in district.losse_huizen:
            self.grid[(50 - huis.y_as)][huis.x_as] = colored('H', 'blue')

    def batterijen_toevoegen(self, district):
        """Voegt batterijen toe aan het Smartgrid."""
        for batterij in district.batterijen:
            self.grid[(50 - batterij.y_as)][batterij.x_as] = colored('B', 'red')

    def kabel_toevoegen(self, y, x):
        """Geeft kleur aan huis en batterij in grid."""
        if self.grid[y][x] == colored('H', 'blue') or self.grid[y][x] == colored('B', 'red'):
            return
        try:
            self.grid[y][x] += 1
        except TypeError:
            self.grid[y][x] = 1

    def leg_kabel_route(self, wijk, batterij, huis):
        """Bepaalt de route van de kabel tussen een batterij en een huis."""
        cursor_x, cursor_y = batterij.x_as, batterij.y_as
        while cursor_x < huis.x_as:
            huis.leg_kabel((cursor_x), (cursor_y))
            self.kabel_toevoegen((50 - cursor_y), (cursor_x + 1))
            cursor_x += 1
        while cursor_x > huis.x_as:
            huis.leg_kabel((cursor_x), (cursor_y))
            self.kabel_toevoegen((50 - cursor_y), (cursor_x - 1))
            cursor_x -= 1
        while cursor_y < huis.y_as:
            huis.leg_kabel((cursor_x), (cursor_y))
            self.kabel_toevoegen((50 - cursor_y - 1), (cursor_x))
            cursor_y += 1
        while cursor_y > huis.y_as:
            huis.leg_kabel((cursor_x), (cursor_y))
            self.kabel_toevoegen((50 - cursor_y + 1), (cursor_x))
            cursor_y -= 1
        huis.leg_kabel((cursor_x), (cursor_y))
        wijk.creer_connectie(batterij, huis)




if __name__ == "__main__":
    # vraag om district.
    wijknummer = input('Wijk 1, 2 of 3: ')
    if wijknummer not in ["1", "2", "3"]:
        print("Ongeldig wijknummer.")
    else:
        wijknummer = int(wijknummer)
        # maak een district aan
        wijk = District(wijknummer)
        # maak een smartgrid aan
        grid = Smartgrid()
    
    grid.huizen_bijvoegen(wijk)
    grid.batterijen_bijvoegen(wijk)

    algoritme_keuze = input('Kies (g)reedy algoritme of (r)andom algoritme: ')
    
    if algoritme_keuze == "r":
        while len(wijk.losse_huizen) > 0:
            for batterij in wijk.batterijen:
                for huis in wijk.losse_huizen:
                    if huis.kan_huis_aansluiten_op_batterij(batterij):
                        # batterij.gebruik += huis.maxoutput
                        wijk.link_huis(huis.huis_id)
                        grid.leg_kabel_route(wijk, batterij, huis)
    
    elif algoritme_keuze == "g":
        while len(wijk.losse_huizen) > 0:
            for batterij in wijk.batterijen:
                for huis in wijk.losse_huizen:
                    if kan_huis_aansluiten_op_batterij(huis, batterij):
                        wijk.link_huis(huis.huis_id)
                        grid.leg_kabel_route(wijk, batterij, huis)
    else:
        print("Ongeldig algoritme keuze.")
    
    
    grid.print_grid()

    for batterij in wijk.batterijen:
        print(F'Batterij {batterij.batterij_id} gebruik: {batterij.resterende_capaciteit}')
        print(f'gelinkte huizen:')
        print(f'{len(batterij.gelinkte_huizen)}')
        #for huis in batterij.gelinkte_huizen:
        #    print(f' {huis.huis_id}|', end='')