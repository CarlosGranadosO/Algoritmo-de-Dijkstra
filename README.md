# Algoritmo de Dijkstra

Este proyecto implementa el algoritmo de Dijkstra para encontrar las distancias más cortas desde un nodo inicial a todos los demás nodos en un grafo no dirigido y ponderado.

## Descripción

El algoritmo de Dijkstra es un algoritmo clásico para la búsqueda de caminos más cortos en grafos ponderados y no dirigidos. Se utiliza principalmente para encontrar la ruta más corta desde un nodo inicial a todos los otros nodos del grafo, siempre que los pesos de las aristas no sean negativos.

## Características

- Inicialización de las distancias de todos los nodos a infinito, excepto el nodo inicial.
- Uso de una lista de no visitados para llevar el control de los nodos que aún no han sido procesados.
- Selección del nodo no visitado con la menor distancia conocida.
- Actualización de las distancias de los nodos vecinos si se encuentra un camino más corto.
- Iteración del proceso hasta que todos los nodos hayan sido visitados o que los nodos restantes sean inalcanzables.

## Instalación

1. Clona este repositorio en tu máquina local:

    ```bash
    git clone https://github.com/CarlosGranadosO/Algoritmo-de-Dijkstra.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd algDij
    ```

## Uso

1. Ajusta el grafo y el nodo inicial en el script `algDij.py` según tus necesidades: en este ejemplo se usa un grafo y el inicio el el [0,0]

    ```python
    grafo = [
        [0, 7, 9, 0, 0, 14],
        [7, 0, 10, 15, 0, 0],
        [9, 10, 0, 11, 0, 2],
        [0, 15, 11, 0, 6, 0],
        [0, 0, 0, 6, 0, 9],
        [14, 0, 2, 0, 9, 0]
    ]

    inicio = 0
    ```

2. Ejecuta el algoritmo:

    ```bash
    python algDij.py
    ```

3. Observa la salida de las distancias mínimas desde el nodo inicial a todos los otros nodos en la consola.



