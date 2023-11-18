# Grafos
## Que es?
Un grafo son diagramas que tiene 2 componentes, puntos y lineas, los puntos son los nodos/vertices, y las lineas son las aristas.

## Conceptos basicos

### Grafo simple
Un grafo G son un conjunto V de Vertices y un conjunto E de aristas tal que cada arista e ∈ E se asocia con un par no ordenado de vertices.
G=(V{V1,V2,V3},E{(V1,V2), (V2,V3)})

### Arista
Tenemos una arista e=(v,w), si v y w estan conectados por una arista son incidentes, y como son incidentes son adyacentes porque son vertices vecinos.

### Camino

### Grafos dirigidos
El grafo dirigido o digrafo a diferencia del grafo simple tiene la variante de que cada arista tiene uan direccion especifica, indicando la direccion

V es un conjunto de vertices o nodos tal como en los simples
E es el conjunto de aristas, donde cada arista tiene el par ordenado (v,w) pero indica la relacion entre el vertice v hacia el vertice W.

En los grafos dirigidos tenemos:
- Arista dirigida
- Vertice inicial y final: Tiene vertice inicial y final ya que comienza en uno y va dirigido hacia otro que es donde termina la arista.
- Grado de entrada y salida

### Grafo Ponderado
El grafo ponderado es un grafo con pesos, osea tenemos el grafo G=(V,E) que tiene asignada una funcion w: E -> R(reales)

- Cada Arista en el grafo tiene un peso asignado representado por la funcion w
- La notacion w(i,j) se utiliza para denotar el peso de la arista que va de i a j.

#### Longitud de un camion
La longitud de un camion del grafo ponderado es la suma de los pesos de las aristas que componen ese camino

## Grafos especiales

### Grafo Completo
El grafo completo con n vertices, notado como Kn, es un grafo simple con n vertices, y hay exactamente una arista por cada par distinto de vertices.
Ej: K4 es un grafo completo con 4 vertices y 3 aristas.

### Grafo bipartito
El grafo G=(V,E) es bipartito si se pueden dividir sus vertices en dos conjuntos disjuntos v1,v2 de manera que la union de ambos conjuntos sea igual al conjunto de vertices total, la interseccion sea vacia y cada arista en E conecta un vertice en V1 con uno en V2.
Osea:
1. V1 ∩ V2 = ∅
2. V1 u V2 = V
3. Cada arista en E es indicente a un vertice en V1 y otro en V2




## Mas grafos

### Grafo convexo
Es un grafo donde 