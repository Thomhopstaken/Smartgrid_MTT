from batterijen import Batterijen
from huizen import Huizen
from typing import TextIO
import os


class District:

    def __init__(self, district) -> None:
        
        self.districtnummer = district
        self.batterijen = []
        self.huizen = [] 
        
        self.laad_batterijen(f"{self.bestand_vinden('batteries')}")
        self.laad_huizen(f"{self.bestand_vinden('houses')}")
    
    def laad_batterijen(self, bestand):
        """Neemt data van bestand en maakt daarmee batterijobjecten.
        deze worden ongebracht in batterijlijst."""
        
    # neemt file eindigend op batteries.csv als input. 
        with open(bestand, 'r') as b:
            teller = len(b.readlines())
        with open(bestand, 'r') as b:
            for x in range(0, teller):
                data = self.data_inladen(b)
        # voeg batterij object aan batterij-lijst toe.
                if data[0].isnumeric():
                    self.batterijen.append(Batterijen(int(data[0]), int(data[1]), float(data[2])))

    def laad_huizen(self, bestand):
        """Neemt data van bestand en maakt daarna huisobjecten.
        deze worden ondergebracht in huislijst."""    
        
        # neemt file eindigend op houses.csv als input. 
        with open(bestand, 'r') as b:
            teller = len(b.readlines())
        with open(bestand, 'r') as b:
            for x in range(0, teller):
                data = self.data_inladen(b)
        # voeg batterij object aan huizen-lijst toe.
                if data[0].isnumeric():
                    self.huizen.append(Huizen(int(data[0]), int(data[1]), float(data[2])))

    def data_inladen(self, b: TextIO) -> list[str]:
        """Neemt bestandlijn en maakt er een lijst van."""
        line = b.readline()
        line = line.replace("\n", '')
        line = line.replace('\"','')
        return line.split(",")
    
    def bestand_vinden(self, naam):
        """Zoekt juiste bestandpad voor opgevraagde naam."""
        hoofdfolder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        district_map = os.path.join(hoofdfolder, 'Huizen&Batterijen', f'district_{self.districtnummer}')
        bestandnaam = f'district-{self.districtnummer}_{naam}.csv'
        return os.path.join(district_map, bestandnaam)
    
