from batterijen import Batterijen
from huizen import Huizen
from typing import TextIO


class District:

    def __init__(self, district) -> None:
        
        self.districtnummer = district
        self.batterijen = []
        self.huizen = [] 
        
        #self.laad_batterijen(f"Smartgrid_MTT/data/Huizen&Batterijen/district_{self.districtnummer}/district-{self.districtnummer}_batteries.csv")
        self.laad_huizen(f"data/Huizen&Batterijen/district_{self.districtnummer}/district-{self.districtnummer}_houses.csv")
    
    def laad_batterijen(self, bestand):
    # neemt file eindigend op batteries.csv als input. 
        with open(bestand, 'r') as b:
            teller = len(b.readlines())
        with open(bestand, 'r') as b:
            for x in range(1, teller):
                data = self.data_inladen(b)
        # voeg batterij object aan batterij-lijst toe.
                self.batterijen.append(Batterijen(data[0],data[1],data[2]))

    def laad_huizen(self, bestand):
    # neemt file eindigend op houses.csv als input. 
        with open(bestand, 'r') as b:
            teller = len(b.readlines())
        with open(bestand, 'r') as b:
            for x in range(1, teller):
                data = self.data_inladen(b)
        # voeg batterij object aan huizen-lijst toe.
                self.batterijen.append(Huizen(data[0],data[1],data[2]))

    def data_inladen(self, b: TextIO) -> list[str]:
        """take fileline and load it as list.

        Post: list of strings is returned"""

        line = b.readline()
        line = line.replace("\n", '')
        return line.split("\t")
    