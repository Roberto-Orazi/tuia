# Grafos
## Que es?
Un grafo son diagramas que tiene 2 componentes, puntos y lineas, los puntos son los nodos/vertices, y las lineas son las
aristas.

## Conceptos basicos

### Grafo simple
Un grafo G son un conjunto V de Vertices y un conjunto E de aristas tal que cada arista e ∈ E se asocia con un par no
ordenado de vertices. G=(V{V1,V2,V3},E{(V1,V2), (V2,V3)})

### Arista
Tenemos una arista e=(v,w), si v y w estan conectados por una arista son incidentes, y como son incidentes son
adyacentes porque son vertices vecinos.

### Camino

### Grafos dirigidos
El grafo dirigido o digrafo a diferencia del grafo simple tiene la variante de que cada arista tiene uan direccion
especifica, indicando la direccion

V es un conjunto de vertices o nodos tal como en los simples E es el conjunto de aristas, donde cada arista tiene el par
ordenado (v,w) pero indica la relacion entre el vertice v hacia el vertice W.

En los grafos dirigidos tenemos:
- Arista dirigida
- Vertice inicial y final: Tiene vertice inicial y final ya que comienza en uno y va dirigido hacia otro que es donde
  termina la arista.
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
Ej: K4 es un grafo completo con 4 vertices y 6 aristas.
para calcular esto es (n*(n-1))/2

### Grafo bipartito
El grafo G=(V,E) es bipartito si se pueden dividir sus vertices en dos conjuntos disjuntos v1,v2 de manera que la union
de ambos conjuntos sea igual al conjunto de vertices total, la interseccion sea vacia y cada arista en E conecta un
vertice en V1 con uno en V2. Osea:
1. V1 ∩ V2 = ∅
2. V1 u V2 = V
3. Cada arista en E es indicente a un vertice en V1 y otro en V2




## Mas grafos

### Grafo conexo
Es un grafo donde siempre hay un camino entre cualquier par de vertices. Los grafos no conexos consisten en varias
partes llamadas componentes conexas. La cantidad de componentes conexas se denota como k(G)

### SubGrafo
Un grafo G'=(V',E') es sub grafo de G=(V,E) si cumple con ciertas condiciones, incluyendo que sus vertices y aristas son
un subconjunto de los de G.

### Subgrafo complementario
El subgrafo complementario de un vertice V en un grafo G denotado por G - v elimina el vertice v y sus aristas
incidentes.

### Grado de un vertice
El grado es el numero de aristas incidentes en v

### Teorema del grado
En un grafo no dirigido o multigrafo la suma de los grados de todos los vertices es igual a 2 veces el numero de aristas. Lo que implica que la cantidad de vertices con grado impar debe ser par.


## Representacion de grafos
### Matriz de adyacencia
La matriz de adyacencia se construye de una matriz nxn que serian los vertices por los vertices y ponemos un uno o cero
dependiendo si son adyacentes o no

### Matriz de incidencia
La matriz de incidencia se construye con una matrix mxn en el cual m son los vertices y n las aristas. Con la matriz de
incidencia luego sabemos el grado de el vertice ya que si sumamos todas sus incidencias logramos el grado.


## Algoritmo de dijkstra
El algoritmo de dijkstra tiene el objetivo de encotnrar el camino mas corto entre dos vertices dados en un grafo
ponderado y conexo.

Si o si tiene que ser un grafo ponderado o conexo y que los pesos de las aristas sean siempre positivos.

1. Inicializar las distancias: D(a)=0 y para cada vertice v≠a inicializa D(v)=∞ a = al vertice de origen.
2. Inicializa el conjunto T como el conjunto de todos los vertices.
3. Selecciona un vertice v en T tal que D(v) sea minimo
4. Quita v de T
5. Para cada vertice t en T adyacente a v, actualizar la etiqueta D(t)=min{D(t),D(v)+w(v,t)}
6. si z ∈ T, repite desde el paso 3, sino terminamos. Y D(z) es la longitud de la ruta mas corta de a a z

## Arboles

Los arboles son un tipo especial de grafo. Un arbol es un grafo simple que satisface la propiedad de que para cualquier
par de vertices v y w en el arbol, existe un unico camion unico de v a w.

Se pueden clasificar los arboles en arboles con raiz y arboles libres. Un arbol con raiz tiene un nodo especial
designado como la raiz.

Propiedades:
- Un grafo conexo y sin ciclos es un arbol.
- Un grafo conexo con n vertices y n-1 aristas es un arbol
- Un grafo con n vertices y n-1 aristas, sin ciclos es un arbol.

### Arboles de expansion
Un arbol de expansion de un grafo es un subgrafo que cumple con:
1. Es un subgrafo de G
2. Es un arbol
3. Contiene todos los vertices de G.

Un arbol de expansion para un grafo existe si y solo si el grafo es conexo.

### Arbol de expansion minima
Un arbol de expansion minima de un grafo con esos pesos es un arbol de expansion cuyo peso total es minimo.

El algoritmo de prim es un metodo para encontrar un arbol de expansion minima. Inicia con un vertice Y, en cada paso,
agrega la arista de peso minimo que conecta un vertice en el arbol con uno fuera de el, hasta que todos los vertices
estan incluidos.

Se usan para conectar vertices de manera eficiente y minimizando el peso total.

# Notas para hacer grafos
Son circuito euleriano si:
- Si todos los vertices son pares
- Si hay dos vertices con grado impar y empieza en uno de los impares y termina en el otro

## Circuito euleriano
Un grafo es euleriano si y solo si es conexo y todos sus vertices tienen grado par.
Empieza y termina en un punto especifico.

## Camino euleriano
Un grafo admite un camino euleriano(NO CIRCUITO) si y solo si es conexo y todos sus vertices tienen grado par salvo dos de grado impar.
Si existe el camino empieza y termina en uno de los 2 vertices de grado impar.
osea empieza en uno y termina en el otro

## Formula ejercicio 9
si tengo
25 x 5 = 2E
E = 125/2 = 62.5
como no es entero par no es posible
