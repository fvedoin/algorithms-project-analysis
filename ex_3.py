import numpy as np

def knapsack(trucksCapacity, itemsWeight, itemsProfit):
    # Matriz de memorização
    M = np.zeros((len(itemsWeight) + 1, trucksCapacity[0] + 1, trucksCapacity[1] + 1))
    x, y, z = 0, 0, 0
    includedItems = []
    for i in range(1, len(itemsWeight) + 1):
        for c_1 in range(trucksCapacity[0] + 1):
            for c_2 in range(trucksCapacity[1] + 1):
                x = M[i - 1, c_1, c_2]
                if c_1 >= itemsWeight[i - 1]:
                    includedItems.append(i-1)
                    y = M[i - 1, c_1 - itemsWeight[i - 1], c_2] + itemsProfit[i - 1]
                if c_2 >= itemsWeight[i - 1]:
                    includedItems.append(i-1)
                    z = M[i - 1, c_1, c_2 - itemsWeight[i - 1]] + itemsProfit[i - 1]
                M[i, c_1, c_2] = max(x, max(y, z))
                y, z = 0, 0

    notIncludedItems = [i for i in range(len(itemsWeight)) if i not in includedItems]
    lostProfit = np.sum(itemsProfit) - M[-1, -1, -1]
    return [notIncludedItems, lostProfit]

# 2 caminhões com capacidades de carga 15 e 7
trucksCapacity = [15, 7]
itemsWeight = [20, 2, 3, 4]
itemsProfit = [5, 1, 1, 10]
result = knapsack(trucksCapacity, itemsWeight, itemsProfit)
print('Os items que não foram entregues são:', result[0])
print('O lucro perdido na entrega foi:', result[1])
