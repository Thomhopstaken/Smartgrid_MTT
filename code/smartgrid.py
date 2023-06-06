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
    print(wijk.huizen)
    # haal bestanden op.
    
    
    
    #draai op het nieuwe district de laad_batterijen def. 

    #draai op het nieuwe district de laad_huizen def. 

