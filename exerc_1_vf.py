# função que filtra as centrals conectadas
def neighbors(central, exchangeOrders):
    result = filter(lambda x: x[0] == central, exchangeOrders)
    return list(map(lambda x: x[1], result))

# busca em largura  
def find_path_minimun_central(centrals, exchangeOrders, start, goal):
    infinity = float('inf')  # 1
    n_centrals = len(centrals) # 1

    # 3n - Configurando todos os blocos #
    c = [False for i in range(n_centrals)] # n
    d = [infinity for i in range(n_centrals)] # n
    a = ['null' for i in range(n_centrals)] # n

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
    idx = goal # 1
    path = [] # 1
    path.append(goal) # 1
    while(a[idx] != 'null'): # 2n
        idx = a[idx]
        path.append(idx)
    return path[::-1]  # 1


if __name__ == '__main__':
    verticesNumber = 5
    # Monta um grafo C = {0, 1, 2, 3, 4}
    C = [i for i in range(verticesNumber)]
    L = [[0, 1], [0, 2], [1, 3], [3, 4], [2, 4]]
    path = find_path_minimun_central(C, L, 0, 4)
    if len(path) == 1:
        print("Não há caminho")
    else:
        print("O caminho é:", path)