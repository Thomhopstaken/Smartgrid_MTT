def greedy_alg(wijk) -> None:
    """Greedy algoritme om huizen aan te sluiten op batterijen in een wijk."""
    
    while len(wijk.losse_huizen) > 0:
        for batterij in wijk.batterijen:
            for huis in wijk.losse_huizen:
                if huis.kan_huis_aansluiten_op_batterij(batterij):
                    wijk.link_huis(huis.huis_id)
                    wijk.route_cable(batterij, huis)