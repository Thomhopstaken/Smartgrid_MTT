from code.klassen import district
import os


def data_pad(wijk: int, item: str, item2=None, kmeans=False,
             huizen=False, experiment=False, json=False) -> str:
    """Vind het juist bestandspad naar opgevraagde bestand.

    In: bestaandsnaam
    Uit: pad naar opgevraagde bestand."""
    cwd = os.getcwd()
    sep = os.sep

    # Retourneer het volledige pad voor k-means batterijgegevens.
    if kmeans:
        pad = f'{sep}Huizen&Batterijen{sep}k_means{sep}batterij_{item}.csv'
        return cwd + os.path.normpath(pad)

    # Retourneer het volledige pad voor k-means batterijgegevens per cluster.
    if huizen:
        pad = (f'{sep}Huizen&Batterijen{sep}k_means'
               f'{sep}batterij_{item}_cluster_{item2}.csv')
        return cwd + os.path.normpath(pad)

    # Retourneer het volledige pad voor experimentele gegevens van de wijk.
    if experiment:
        pad = (f'{sep}Huizen&Batterijen{sep}experiment'
               f'{sep}{item}_{wijk}_experiment.csv')
        return cwd + os.path.normpath(pad)

    # Retourneer het volledige pad voor JSON-uitvoer van het smart grid.
    if json:
        pad = f'{sep}figuren{sep}smartgrid_{wijk}_{item}_output.json'
        return cwd + os.path.normpath(pad)

    pad = (f'{sep}Huizen&Batterijen{sep}district_'
           f'{wijk}{sep}district-{wijk}_{item}.csv')
    return cwd + os.path.normpath(pad)


def wijk_lader(algoritme: str, wijk: int) -> object:
    """Runt het opgrvraagde algoritme.

    In: wijknummer en naam algoritme.
    Uit: wijk object."""
    algoritmes = {'Random': district.Wijk(wijk, algoritme, True, False),
                  'Greedy': district.Wijk(wijk, algoritme, True, True),
                  'Hill': district.Wijk(wijk, algoritme, True, False),
                  'KMeans': district.Wijk(wijk, algoritme, False, False)}
    return algoritmes[algoritme]
