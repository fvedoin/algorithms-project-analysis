from utils import neighbors

def findArgMin(d, c):
    dMin = 999
    argMin = 0
    for i, _ in enumerate(d):
        if c[i] == False:
            if d[i] < dMin:
                dMin = d[i]
                argMin = i
    return argMin

def distanceToCost(w, p, gasPrice, autonomy):
    parsedW = []
    for costPerVertex in w:
        amount = {}
        for costPerEdge in costPerVertex:
            amount[costPerEdge] = gasPrice * costPerVertex[costPerEdge] / autonomy + p[costPerEdge]
        parsedW.append(amount)
    return parsedW


def hasNextFalseNode(nodesNumber, c):
    for n in range(nodesNumber):
        if c[n] == False:
            return n
    return 'STOP'

# custo total: (n+m)log2(n)
def dijkstra(v, w, p, gasPrice, autonomy, origin, destiny):

    w = distanceToCost(w, p, gasPrice, autonomy)
    infinity = float('inf') # 1
    vertexNumber = len(v) # 1

    # 3n - Configurando todos os blocos #
    d = [infinity] * vertexNumber
    a = ['null'] * vertexNumber
    c = [False] * vertexNumber

    d[origin] = 0 # n
    while(hasNextFalseNode(vertexNumber, c) != 'STOP'):
        # log2(n)
        u = findArgMin(d, c)
        c[u] = True
        for i in v[u]: # m
            if c[i] == False:
                if d[i] > d[u] + w[u][i]:
                    d[i] = d[u] + w[u][i] # log2(n)
                    a[i] = u
    idx = destiny
    path = []
    path.append(destiny)
    while(a[idx] != 'null'):
        idx = a[idx]
        path.append(idx)
    return path[::-1], d[destiny]

# Vértices
V = [0, 1, 2, 3]
# Array de arestas no formato [origem, destino]
A = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 3]]
# Estrutura as arestas
V = list(map(lambda x: neighbors(x, A), V))
# Pesos das arestas de cada posição
W = [{1: 1, 2: 2}, {2: 2, 3: 10}, {3: 3}]

result = dijkstra(V, W, p=[5, 5, 5, 5], gasPrice=1, autonomy=1, origin=0, destiny=3)

if(result[1] == float('inf')):
	print("Não há caminho")
else:
	print('O menor caminho é:', result[0])
	print('O custo total é:', result[1])
