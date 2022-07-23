def find_arg_min(d, c):
    d_min = 999
    arg_min = 0
    for i, _ in enumerate(d):
        if c[i] == False:
            if d[i] < d_min:
                d_min = d[i]
                arg_min = i
    return arg_min


def convert_distance_to_cost(w, p, price, autonomy):
    w_processed = []
    for i in w:
        data = {}
        for k in i:
            data[k] = price*i[k]/autonomy + p[k]
        w_processed.append(data)
    return w_processed


def get_next_false_node(n_nodes, c):
    for n in range(n_nodes):
        if c[n] == False:
            return n
    return 'STOP'

# custo total: (n+m)log2(n)
def minimize_travel_cost(v, w, p, price, autonomy, origin, destiny):

    w = convert_distance_to_cost(w, p, price, autonomy)
    infinity = float('inf') # 1
    n_centrals = len(v) # 1

    # 3n - Configurando todos os blocos #
    d = [infinity for i in range(n_centrals)]
    a = ['null' for i in range(n_centrals)]
    c = [False for i in range(n_centrals)]

    d[origin] = 0 # n
    while(get_next_false_node(n_centrals, c) != 'STOP'):
        # log2(n)
        u = find_arg_min(d, c)
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


if __name__ == "__main__":
    V = [[1, 2], [2, 3], [3], []]
    W = [{1: 1, 2: 2}, {2: 2, 3: 10}, {3: 3}]
    print(minimize_travel_cost(V, W, p=[5, 5, 5, 5], price=5,
                               autonomy=10, origin=0, destiny=3))
