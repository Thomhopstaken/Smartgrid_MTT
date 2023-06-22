import os
from code.klassen import district


def data_pad(district, item, item2=None, kmeans=False,
             huizen=False, experiment=False, json=False) -> str:
    """Vind het juist bestandspad naar opgevraagde bestand.

    In: bestaandsnaam
    Uit: pad naar opgevraagde bestand."""

    cwd = os.getcwd()
    sep = os.sep
    if kmeans == True:
        pad = f'{sep}Huizen&Batterijen{sep}k_means{sep}batterij_{item}.csv'
        return cwd + os.path.normpath(pad)

    if huizen == True:
        pad = f'{sep}Huizen&Batterijen{sep}k_means{sep}batterij_{item}_cluster_{item2}.csv'
        return cwd + os.path.normpath(pad)

    if experiment == True:
        pad = f'{sep}Huizen&Batterijen{sep}experiment{sep}{item}_{district}_experiment.csv'
        return cwd + os.path.normpath(pad)

    if json == True:
        pad = f'{sep}figures{sep}smartgrid_{district}_{item}_output.json'
        return cwd + os.path.normpath(pad)

    pad = f'{sep}Huizen&Batterijen{sep}district_{district}{sep}district-{district}_{item}.csv'
    return cwd + os.path.normpath(pad)


def wijk_lader(algoritme, wijk):
    algoritmes = {'Random': district.District(wijk, algoritme, True, True),
                  'KMeans': district.District(wijk, algoritme, False, False)}
    return algoritmes[algoritme]
