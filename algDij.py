def dijkstra (grafo, inicio):
    #numero de nodos del grafo
    n=len(grafo) #n sera la cantidad de nodos que tenemos en nuestro grafo 

    #aqui definimos todas las distancias como infinitas "inicialmente todos los nodos son inalcanzables desde la poscicion ini"
    distancias=[float('inf')]*n  #al multiplicar con n tenemos las distancias del len del grafo
    distancias[inicio]=0#se define 0 porque la distancia de cualquier nodo(en este caso inicio) a si mismo siempre es 0 

    #conjunto de nodos no visitaos
    noVisitados=set(range(n)) #generamos una secuencia de 0 til n-1 para enumerar los nodos no visitados , set para hacerlos un conjunto

    while noVisitados:
        #seleccionar el nodo no visitado mas cernao
        nodoActual=min(noVisitados, key=lambda nodo: distancias[nodo])     #gracias a lamda sacamos la distancia min de los nodos no visitados 
                                                                           #y devolvemos el lugar del nodo
        if distancias[nodoActual]== float('inf'):#si la ditancia min es inf los nodos restantes no son alcanzables
            break                                #se termina el ciclo
        #else elminamos el nodo actual de los no visitados ya que ya lo visitamos
        noVisitados.remove(nodoActual)

        #actualizar las distancias de los vecinos al nodo actual
        for vecino, peso in enumerate(grafo[nodoActual]):
            if peso>0:#s
                nuevaDistancia=distancias[nodoActual]+peso
                if nuevaDistancia < distancias[vecino]:#esto se hace para que dado el caso que el vecino de un peso mayor no se sustituya como nueva distancia
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
