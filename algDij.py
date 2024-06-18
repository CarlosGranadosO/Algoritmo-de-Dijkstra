def dijkstra (grafo, inicio):
    #numero de nodos del grafo
    n=len(grafo)

    #distancias inicializadas a inf
    distancias=[float('inf')]*n 
    distancias[inicio]=0

    #conjunto de nodos no visitaos
    noVisitados=set(range(n))

    while noVisitados:
        #seleccionar el nodo no visitado mas cernao
        nodoActual=min(noVisitados, key=lambda nodo: distancias[nodo])
        #si la ditancia min es inf los nodos restantes no son alcanzables
        if distancias[nodoActual]== float('inf'):
            break
        #elminar el nodo actual de los no visitados
        noVisitados.remove(nodoActual)

        #actualizar las distancias de los vecinos al nodo actual
        for vecino, peso in enumerate(grafo[nodoActual]):
            if peso>0:
                nuevaDistancia=distancias[nodoActual]+peso
                if nuevaDistancia < distancias[vecino]:
                    distancias[vecino] = nuevaDistancia
    return distancias

#main
grafo = [
    [0, 7, 9, 0, 0, 14],
    [7, 0, 10, 15, 0, 0],
    [9, 10, 0, 11, 0, 2],
    [0, 15, 11, 0, 6, 0],
    [0, 0, 0, 6, 0, 9],
    [14, 0, 2, 0, 9, 0]
]
inicio=0
distancias=dijkstra(grafo,inicio)
print(f"Distancias desde el nodo {inicio}: {distancias}")
