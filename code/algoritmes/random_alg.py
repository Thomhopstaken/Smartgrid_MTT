import copy
from .kmeans import gebruik_clusters
import random


def random_alg(wijk) -> object:
    """Voert het random algoritme uit op een wijkobject.

    In: wijk object.
    Uit: wijk object."""
    random.shuffle(wijk.batterijen)
    random.shuffle(wijk.losse_huizen)
    wijk_buffer = copy.deepcopy(wijk)
    gebruik_clusters(wijk_buffer, 5)
    
    # Verbind losse huizen met batterijen als er nog losse huizen zijn.
    while len(wijk_buffer.losse_huizen) > 0:
        loop_start = len(wijk_buffer.losse_huizen)
        
        # Verbind losse huizen met beschikbare batterijen.
        for batterij in wijk_buffer.batterijen:
            for huis in wijk_buffer.losse_huizen:
                if huis.kan_aansluiten(batterij):
                    wijk_buffer.leg_route(batterij, huis)
        loop_einde = len(wijk_buffer.losse_huizen)
        
        # Controleer of er nog losse huizen zijn om aan te sluiten.
        if loop_start == loop_einde:
            return random_alg(wijk)
    return wijk_buffer
