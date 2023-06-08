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
        if self.grid[y][x] == colored('H', 'blue') or self.grid[y][x] == colored('B', 'red'):
            return
        try:
            self.grid[y][x] += 1
        except TypeError:
            self.grid[y][x] = 1

    def make_connection(self, battery, house):
        house.linked = True
        battery.update_usage(house.maxoutput)
        battery.gelinkte_huizen.append(house)

    def route_cable(self, battery, house):
        cursor_x, cursor_y = battery.x_as, battery.y_as
        while cursor_x < house.x_as:
            house.lay_cable((cursor_x), (cursor_y))
            self.add_cable((50 - cursor_y), (cursor_x + 1))
            cursor_x += 1
        while cursor_x > house.x_as:
            house.lay_cable((cursor_x), (cursor_y))
            self.add_cable((50 - cursor_y), (cursor_x - 1))
            cursor_x -= 1
        while cursor_y < house.y_as:
            house.lay_cable((cursor_x), (cursor_y))
            self.add_cable((50 - cursor_y - 1), (cursor_x))
            cursor_y += 1
        while cursor_y > house.y_as:
            house.lay_cable((cursor_x), (cursor_y))
            self.add_cable((50 - cursor_y + 1), (cursor_x))
            cursor_y -= 1
        house.lay_cable((cursor_x), (cursor_y))
        self.make_connection(battery, house)
    

    # to do: algo keuze maken huis naar batterij

    # to do: huizen aan batterij verbinden.

    # to do: kabels leggen.

def huis_checker(huis, batterij):
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

    # print(wijk.batterijen[0].x_as)
    # print(wijk.batterijen[0].y_as)

    # print(wijk.batterijen[0].closest_house().x_as)
    # print(wijk.batterijen[0].closest_house().y_as)

    while len(wijk.losse_huizen) > 0:
        for batterij in wijk.batterijen:
            for huis in wijk.losse_huizen:
                if huis_checker(huis, batterij):
                    #batterij.gebruik += huis.maxoutput
                    wijk.huis_linken(huis.huis_id)
                    grid.route_cable(batterij, huis)
 
    grid.print_grid()
    for batterij in wijk.batterijen:
        print(F'Batterij {batterij.batterij_id} gebruik: {batterij.resterende_capaciteit}')
        print(f'gelinkte huizen:')
        print(f'{len(batterij.gelinkte_huizen)}')
        #for huis in batterij.gelinkte_huizen:
        #    print(f' {huis.huis_id}|', end='')
            
        