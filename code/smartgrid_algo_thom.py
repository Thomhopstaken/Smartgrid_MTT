from batterijen import Batterijen
from district import District
from huizen import Huizen
from termcolor import colored

class Smartgrid:

    def __init__(self):
        self.grid = self.create_grid()

    def create_grid(self):
        rows, cols = (51, 51)
        arr = [["_" for _ in range(cols)] for _ in range(rows)]
        return arr

    def print_grid(self):
        for row in self.grid:
            print(*row)
    def add_houses(self, district):
        for house in district.losse_huizen:
            self.grid[(50 - house.y_as)][house.x_as] = colored('H', 'blue')

    def add_batteries(self, district):
        for battery in district.batterijen:
            self.grid[(50 - battery.y_as)][battery.x_as] = colored('B', 'red')

    def add_cable(self, y, x):
        try:
            self.grid[y][x] += 1
        except TypeError:
            self.grid[y][x] = 1

    def huizen_verdelen(self, wijk):
        for batterij in wijk.batterijen:
            for huis in batterij.afstand_huizen:
                if huis in wijk.losse_huizen:
                    if batterij.huidig_verbruik + huis.maxoutput <= batterij.capaciteit:
                        batterij.gelinkte_huizen.append(huis)
                        batterij.huidig_verbruik += huis.maxoutput 
                        huis.afstand_batterij = batterij.afstand_huizen[huis]
                        wijk.huizen_gelinkt(huis)
                    else:
                        continue
                else:
                    continue
        
                    


if __name__ == "__main__":
    
    # vraag om district.
    wijknummer = input('Wijk 1, 2 of 3: ')
    
    # maak een district aan. 
    wijk = District(wijknummer)

    # print('huizen')
    # for huis in wijk.losse_huizen:
    #     print(huis.x_as, huis.y_as, huis.maxoutput)
    #
    # print('Batterijen')
    # for batterij in wijk.batterijen:
    #     print(batterij.x_as, batterij.y_as, batterij.capaciteit)
    #
    grid = Smartgrid()
    grid.add_houses(wijk)
    grid.add_batteries(wijk)
    grid.huizen_verdelen(wijk)
    # grid.add_cable(0, 0)
    # grid.add_cable(0, 0)
    # grid.add_cable(0, 0)
    # grid.print_grid()

    # print(wijk.batterijen[0].afstand_huizen)
    # print(wijk.batterijen[0].x_as)
    # print(wijk.batterijen[0].y_as)

    
    for batterij in wijk.batterijen:
        print(F'Batterij {batterij.batterij_id} gebruik: {batterij.huidig_verbruik}')
        print(f'gelinkte huizen:')
        for huis in batterij.gelinkte_huizen:
            print(f' {huis.huis_id}|', end='')
        print('')
            
        