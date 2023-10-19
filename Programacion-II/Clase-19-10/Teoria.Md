# Grafos
Los grafos son diagramas con dos componentes:
1. Puntos
    Se les llama vertices o nodos
2. Lineas
    Se les llama aristas

## Definicion matematica de un grafo No dirigido
Un grafo G (solo grafo se refiere a grafo no dirigido o grafo simple), consiste en un conjunto de vertices y un conjunto E de aristas. tal que cada arista e pertenece a E y se asocia con un par no ordenado de vertices.
### Incidencia
Si la arista e esta asociada con los vertices v y w se escribe e=(v,w).
Entonces se dice que una arista e=(v,w) en un grafo es incidente sobre v y w.
### Adyacencia
A su vez los vertices v y w son incidentes sobre e, que son adyacentes o vecinos entre ellos.

En el caso de tener un grafo G con vertices V y aristas E, se escribe G=(V,E).
Los conjuntos E y V tienen que ser finitos, y que V no sea vacio.

## Camino de un grafo
Un camino en un grafo es la sucesion de vertices (v0,v1,v2,...,vn-1) y aristas (l0,l1,l2,...,ln-1) tales que li=(vi,vi+1) para todo i e {0,1,...,n}

La longitud del camino se determina por la cantidad de aristas que recorre, en este caso n.

## Grafo dirigido
Consiste en un conjunto V de vertices y un conjunto E de aristas tal que cada arista e pertentece a E, y se asocia con un par ordenado de vertices.
(v,w) y (w,v)  representan cosas distintas.

## Multigrafo
Sea V un conjunto finito no vacio, decimos que G =(V,E) es un multigrafo si para algunos vertices existen dos o mas aristas en E que conectan los mismos vertices.

Los multigrafos dirigidos se hacen de la misma forma solo que agregando direccion a las aristas.

## Subgrafo
Sea G=(V,E) un grafo, G'=(V',E') es un subgrafo de G si se cumple:
- V' es subconjunto de V
- E' es subconjunto de E
- Para toda arista e que esta en E', si e incide en los vertices v y w, entonces v,w pertenece a V'


# FALTA MAS CONCEPTOS SOBRE GRAFOS.

