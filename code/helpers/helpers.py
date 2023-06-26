import os
from code.klassen import district


def data_pad(wijk: int, item, item2=None, kmeans=False,
             huizen=False, experiment=False, json=False) -> str:
    """Vind het juist bestandspad naar opgevraagde bestand.

    In: bestaandsnaam
    Uit: pad naar opgevraagde bestand."""

    cwd = os.getcwd()
    sep = os.sep
    if kmeans:
        pad = f'{sep}Huizen&Batterijen{sep}k_means{sep}batterij_{item}.csv'
        return cwd + os.path.normpath(pad)

    if huizen:
        pad = f'{sep}Huizen&Batterijen{sep}k_means{sep}batterij_{item}_cluster_{item2}.csv'
        return cwd + os.path.normpath(pad)

    if experiment:
        pad = f'{sep}Huizen&Batterijen{sep}experiment{sep}{item}_{wijk}_experiment.csv'
        return cwd + os.path.normpath(pad)

    if json:
        pad = f'{sep}figures{sep}smartgrid_{wijk}_{item}_output.json'
        return cwd + os.path.normpath(pad)

    pad = f'{sep}Huizen&Batterijen{sep}district_{wijk}{sep}district-{wijk}_{item}.csv'
    return cwd + os.path.normpath(pad)


def wijk_lader(algoritme: str, wijk: int) -> object:
    """Runt het opgrvraagde algoritme.

    In: wijknummer en naam algoritme.
    Uit: """
    algoritmes = {'Random': district.Wijk(wijk, algoritme, True, False),
                  'Greedy': district.Wijk(wijk, algoritme, True, False),
                  'Hill': district.Wijk(wijk, algoritme, True, False),
                  'KMeans': district.Wijk(wijk, algoritme, False, False)}
    return algoritmes[algoritme]
