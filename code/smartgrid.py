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
        for house in district.huizen:
            self.grid[(50 - house.y_as)][house.x_as] = colored('H', 'blue')

    def add_batteries(self, district):
        for battery in district.batterijen:
            self.grid[(50 - battery.y_as)][battery.x_as] = colored('B', 'red')


    pass
    # to do: algo keuze maken huis naar batterij

    # to do: huizen aan batterij verbinden.

    # to do: kabels leggen.



if __name__ == "__main__":
    
    # vraag om district.
    wijknummer = input('Wijk 1, 2 of 3: ')
    
    # maak een district aan. 
    wijk = District(wijknummer)

    print('huizen')
    for huis in wijk.huizen:
        print(huis.x_as, huis.y_as, huis.maxoutput)
    
    print('Batterijen')
    for batterij in wijk.batterijen:
        print(batterij.x_as, batterij.y_as, batterij.capaciteit)

    grid = Smartgrid()
    grid.add_houses(wijk)
    grid.add_batteries(wijk)
    grid.print_grid()

