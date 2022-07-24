# função que filtra as centrals conectadas
def neighbors(vertex, edges):
    result = filter(lambda x: x[0] == vertex, edges)
    return list(map(lambda x: x[1], result))