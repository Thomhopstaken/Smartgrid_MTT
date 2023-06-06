from batterijen import Batterijen
from district import District
from huizen import Huizen

class Smartgrid:
    pass


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