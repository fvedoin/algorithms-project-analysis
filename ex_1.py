# busca em largura  
from utils import neighbors

def breadthSearch(centrals, exchangeOrders, start, goal):
    infinity = float('inf')  # 1
    centralsNumber = len(centrals) # 1

    # 3n - Configurando todos os blocos #
    c = [False] * centralsNumber # n
    d = [infinity] * centralsNumber # n
    a = ['null'] * centralsNumber # n

    # 2 - Configurando o vértice de origem #
    c[start] = True # 1
    d[start] = 0 # 1

    # 2 - Preparando a fila de visitas #
    q = [] #1
    q.append(start) #1

    # Propagação das visitas #
    while(len(q) > 0): # n (pior caso)
        u = q.pop(0)
        for v in neighbors(u, exchangeOrders): #5m
            if c[v] == False:
                c[v] = True
                d[v] = d[u] + 1
                a[v] = u
                q.append(v)
    vertex = goal # 1
    path = [] # 1
    path.append(goal) # 1
    while(a[vertex] != 'null'): # 2n
        vertex = a[vertex]
        path.append(vertex)
    return path[::-1]  # 1


verticesNumber = 5
# Monta um grafo C = {0, 1, 2, 3, 4}
C = [i for i in range(verticesNumber)]
# Array de arestas no formato [origem, destino]
L = [[0, 1], [0, 2], [1, 3], [3, 4], [2, 4]]
path = breadthSearch(C, L, 0, 4)
if len(path) == 1:
    print("Não há caminho")
else:
    print("O menor caminho é:", path)